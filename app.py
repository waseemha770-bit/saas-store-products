from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import database

app = Flask(__name__)
app.secret_key = 'tajergo_super_secure_key_2026'

@app.route('/')
def home(): return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug):
    user = database.get_user_by_slug(slug)
    if not user: return "المتجر غير موجود أو تم إيقافه", 404
    settings = database.get_settings(user.get('id'))
    products = database.get_products(user.get('id'))
    return render_template('store.html', user=user, settings=settings, products=products)

# API لاستقبال الطلبات من السلة الذكية
@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user: return jsonify({"error": "Store not found"}), 404
    
    data = request.json
    settings = database.get_settings(user.get('id'))
    order_id = database.create_order(user.get('id'), data['name'], data['phone'], data['cart'], data['total'])
    
    # تجهيز رسالة الواتساب المنسقة
    msg = f"مرحباً، طلب جديد من المتجر 🛒\nرقم الطلب: {order_id}\nالاسم: {data['name']}\nالهاتف: {data['phone']}\n\nالمنتجات:\n"
    for item in data['cart']: msg += f"- {item['name']} (x{item['qty']})\n"
    msg += f"\nالإجمالي: {data['total']} {settings.get('currency', 'ريال')}"
    
    whatsapp_url = f"https://wa.me/{settings.get('whatsapp', '')}?text={msg}"
    return jsonify({"whatsapp_url": whatsapp_url})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = database.authenticate_user(request.form.get('slug'), request.form.get('pass'))
        if user:
            session['user_id'] = user.get('id')
            session['store_slug'] = user.get('store_slug')
            return redirect(url_for('dashboard'))
        flash("بيانات الدخول خاطئة أو المتجر موقوف", "danger")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_product':
            database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock'))
            flash("تم إضافة المنتج للمخزون!", "success")
        elif action == 'save_settings':
            settings_data = {'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'), 'whatsapp': request.form.get('whatsapp'), 'currency': request.form.get('currency'), 'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'), 'header_size': request.form.get('header_size')}
            database.update_settings(session['user_id'], settings_data)
            flash("تم تحديث إعدادات المتجر", "success")
        return redirect(url_for('dashboard'))
        
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    orders = database.get_orders(session['user_id'])
    return render_template('dashboard.html', products=products, settings=settings, orders=orders, store_slug=session['store_slug'])

# --- نظام الإدارة العليا (Super Admin) ---
@app.route('/system-admin', methods=['GET', 'POST'])
def system_admin():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            if request.form.get('password') == 'waseem2026': session['super_admin'] = True
            else: flash("كلمة المرور غير صحيحة", "danger")
        elif 'super_admin' in session:
            if action == 'add_merchant':
                if database.create_new_merchant(request.form.get('name'), request.form.get('slug'), request.form.get('password')):
                    flash(f"تم إنشاء المتجر: {request.form.get('slug')}", "success")
                else: flash("رابط المتجر محجوز مسبقاً", "danger")
            elif action == 'toggle_status':
                database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
                flash("تم تحديث حالة المتجر", "warning")
            elif action == 'delete_merchant':
                database.delete_user(request.form.get('user_id'))
                flash("تم حذف المتجر وبياناته نهائياً", "danger")
        return redirect(url_for('system_admin'))
        
    if not session.get('super_admin'): return render_template('system_admin.html', logged_in=False)
    merchants = database.get_all_users()
    return render_template('system_admin.html', logged_in=True, merchants=merchants)

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__': app.run(debug=True)

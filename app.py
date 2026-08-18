from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import database
import os

app = Flask(__name__)
# استخدام المتغير السري من Vercel، مع توفير مفتاح احتياطي لمنع انهيار النظام نهائياً
app.secret_key = os.environ.get('SECRET_KEY', 'tajergo_super_secure_key_2026')

@app.route('/')
def home(): return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug):
    user = database.get_user_by_slug(slug)
    if not user: return "المتجر غير موجود أو تم إيقافه", 404
    settings = database.get_settings(user.get('id'))
    products = database.get_products(user.get('id'))
    return render_template('store.html', user=user, settings=settings, products=products)

@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user: return jsonify({"error": "Store not found"}), 404
    data = request.json
    settings = database.get_settings(user.get('id'))
    order_id = database.create_order(user.get('id'), data['name'], data['phone'], data['cart'], data['total'])
    
    msg = f"مرحباً، طلب جديد 🛒\nرقم الطلب: {order_id}\nالاسم: {data['name']}\nالهاتف: {data['phone']}\n\nالمنتجات:\n"
    for item in data['cart']: msg += f"- {item['name']} (الكمية: {item['qty']})\n"
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
    is_super_admin = (session['store_slug'] == 'admin-store')

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_product':
            database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock'))
            flash("تم إضافة المنتج بنجاح!", "success")
        elif action == 'save_settings':
            settings_data = {'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'), 'whatsapp': request.form.get('whatsapp'), 'currency': request.form.get('currency'), 'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'), 'header_size': request.form.get('header_size')}
            database.update_settings(session['user_id'], settings_data)
            flash("تم تحديث إعدادات المتجر", "success")
        elif action == 'add_merchant' and is_super_admin:
            if database.create_new_merchant(request.form.get('name'), request.form.get('slug'), request.form.get('password')): flash(f"تم إنشاء المتجر: {request.form.get('slug')}", "success")
            else: flash("رابط المتجر محجوز مسبقاً", "danger")
        elif action == 'toggle_status' and is_super_admin:
            database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
            flash("تم تحديث حالة المتجر", "warning")
        elif action == 'delete_merchant' and is_super_admin:
            database.delete_user(request.form.get('user_id'))
            flash("تم حذف المتجر نهائياً", "danger")
        return redirect(url_for('dashboard'))
        
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    orders = database.get_orders(session['user_id'])
    merchants = database.get_all_users() if is_super_admin else []
    
    return render_template('dashboard.html', products=products, settings=settings, orders=orders, merchants=merchants, store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__': app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response
import database, os, urllib.parse, io, csv

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'tajergo_super_secure_key_2026'
MAIN_DOMAIN = "saas-store-products.vercel.app"

@app.before_request
def handle_custom_domains():
    host = request.host.lower()
    excluded_paths = ['/login', '/logout', '/dashboard', '/api/', '/export']
    if MAIN_DOMAIN not in host and not any(request.path.startswith(p) for p in excluded_paths) and host not in ['127.0.0.1:5000', 'localhost:5000']:
        merchant_settings = database.settings_col.find_one({"custom_domain": host})
        if merchant_settings:
            user = database.users_col.find_one({"id": merchant_settings['u_id']})
            if user and user.get('active') == 'TRUE': return view_store_logic(user['store_slug'])
            return "المتجر متوقف أو محذوف.", 403
        return "هذا النطاق غير مسجل في منصتنا.", 404

def view_store_logic(slug):
    user = database.get_user_by_slug(slug)
    if not user: return "المتجر غير موجود أو تم إيقافه", 404
    return render_template('store.html', user=user, settings=database.get_settings(user.get('id')), products=database.get_products(user.get('id')))

@app.route('/')
def home(): return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug): return view_store_logic(slug)

@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user: return jsonify({"error": "Store not found"}), 404
    data = request.json; settings = database.get_settings(user.get('id'))
    address = data.get('address', 'غير مسجل'); payment = data.get('payment', 'غير مسجل')
    order_id = database.create_order(user.get('id'), data['name'], data['phone'], address, payment, data['cart'], data['total'])
    msg = f"مرحباً، لدي طلب جديد 🛒\n\n🧾 *رقم الطلب:* {order_id}\n👤 *الاسم:* {data['name']}\n📞 *الهاتف:* {data['phone']}\n📍 *العنوان:* {address}\n💳 *الدفع:* {payment}\n\n🛍️ *المنتجات:*\n"
    for item in data['cart']: msg += f"▪️ {item['name']} (الكمية: {item['qty']})\n"
    msg += f"\n💰 *الإجمالي:* {data['total']} {settings.get('currency', 'ريال')}\n\n*(الرجاء إرفاق صورة إشعار الحوالة هنا إذا كان الدفع مسبقاً)*"
    return jsonify({"whatsapp_url": f"https://wa.me/{settings.get('whatsapp', '')}?text={urllib.parse.quote(msg)}"})

@app.route('/export/orders')
def export_orders():
    if 'user_id' not in session: return redirect(url_for('login'))
    orders = database.get_orders(session['user_id']); output = io.StringIO(); writer = csv.writer(output)
    writer.writerow(['رقم الطلب', 'التاريخ', 'العميل', 'الهاتف', 'العنوان', 'طريقة الدفع', 'المنتجات', 'الإجمالي', 'حالة الطلب'])
    for o in orders:
        items_str = " | ".join([f"{i['name']} (x{i['qty']})" for i in o.get('cart_items', [])])
        writer.writerow([o['order_id'], o['date'].strftime('%Y-%m-%d %H:%M'), o['customer_name'], o['customer_phone'], o.get('customer_address', ''), o.get('payment_info', ''), items_str, o['total'], o.get('status', 'جديد 🟡')])
    return Response(output.getvalue().encode('utf-8-sig'), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=TajerGo_Orders_Report.csv"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = database.authenticate_user(request.form.get('slug'), request.form.get('pass'))
        if user: session['user_id'] = user.get('id'); session['store_slug'] = user.get('store_slug'); return redirect(url_for('dashboard'))
        flash("بيانات الدخول خاطئة أو المتجر موقوف", "danger")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    is_super_admin = (session['store_slug'] == 'admin-store')
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_product': database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة بنجاح!", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id'), session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل بنجاح!", "success")
        elif action == 'delete_product': database.delete_product(request.form.get('product_id'), session['user_id']); flash("تم الحذف بنجاح", "danger")
        elif action == 'update_order_status': database.orders_col.update_one({"order_id": request.form.get('order_id'), "store_id": session['user_id']}, {"$set": {"status": request.form.get('new_status')}}); flash("تم تحديث الحالة", "success")
        elif action == 'change_password':
            old_p, new_p, confirm_p = request.form.get('old_password', ''), request.form.get('new_password', ''), request.form.get('confirm_password', '')
            if not old_p or not new_p: flash("املأ جميع حقول كلمة المرور", "danger")
            elif new_p != confirm_p: flash("كلمة المرور غير متطابقة", "danger")
            else: flash("تم تغيير كلمة المرور بنجاح" if database.change_user_password(session['user_id'], old_p, new_p) else "كلمة المرور الحالية خاطئة", "success" if database.change_user_password(session['user_id'], old_p, new_p) else "danger")
        elif action == 'save_settings':
            database.update_settings(session['user_id'], {
                'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'),
                'whatsapp': request.form.get('whatsapp'), 'currency': request.form.get('currency'),
                'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'),
                'header_size': request.form.get('header_size'), 'facebook': request.form.get('facebook'),
                'instagram': request.form.get('instagram'), 'tiktok': request.form.get('tiktok'),
                'custom_domain': request.form.get('custom_domain', '').replace('https://', '').replace('http://', '').strip('/'),
                'logo_url': request.form.get('logo_url', '').strip(),
                'img_provider': request.form.get('img_provider', 'imgbb'),
                'img_api_key': request.form.get('img_api_key', '').strip(),
                'cloudinary_name': request.form.get('cloudinary_name', '').strip(),
                'cloudinary_preset': request.form.get('cloudinary_preset', '').strip()
            })
            flash("تم حفظ الإعدادات بنجاح", "success")
        elif action == 'add_merchant' and is_super_admin:
            if database.create_new_merchant(request.form.get('name'), request.form.get('slug'), request.form.get('password')): flash("تم إنشاء المتجر بنجاح", "success")
            else: flash("رابط المتجر محجوز", "danger")
        elif action == 'toggle_status' and is_super_admin: database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
        elif action == 'delete_merchant' and is_super_admin: database.delete_user(request.form.get('user_id'))
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    total_rev = sum(float(str(o['total']).replace(',','').strip()) for o in orders if o.get('status') == 'تم التوصيل 🟢')
    status_counts = {"جديد 🟡": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders: status_counts[o.get('status', 'جديد 🟡')] += 1
    return render_template('dashboard.html', products=database.get_products(session['user_id']), settings=database.get_settings(session['user_id']), orders=orders, stats={"total_orders": len(orders), "total_revenue": total_rev, "status_counts": status_counts}, merchants=(database.get_all_users() if is_super_admin else []), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
if __name__ == '__main__': app.run(debug=True)

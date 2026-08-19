from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort
import database, os, urllib.parse, io, csv, json, urllib.request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'tajergo_super_secure_key_2026'
MAIN_DOMAIN = "saas-store-products.vercel.app"

# دالة ذكية لتجاوز حظر الصور (CDN Proxy) وعرض شعار المنصة
@app.context_processor
def inject_global_vars():
    admin = database.users_col.find_one({"store_slug": "admin-store"})
    logo = "https://via.placeholder.com/150/0d6efd/ffffff?text=TajerGo"
    if admin:
        sett = database.settings_col.find_one({"u_id": admin['id']})
        if sett and sett.get('platform_logo'): logo = sett.get('platform_logo')
    
    # دالة بروكسي فك الحظر وتسريع الصور
    def proxy_img(url):
        if not url: return "https://via.placeholder.com/400x300?text=بدون+صورة"
        if url.startswith('http'): return f"https://wsrv.nl/?url={urllib.parse.quote(url)}"
        return url
        
    return dict(platform_logo=logo, proxy_img=proxy_img)

@app.before_request
def handle_custom_domains():
    host = request.host.lower()
    excluded_paths = ['/login', '/logout', '/dashboard', '/api/', '/export', '/manifest', '/sw.js']
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
    products = database.get_products(user.get('id'))
    for p in products:
        p['rating'] = round(p.get('ratings_sum', 0) / p.get('ratings_count', 1), 1) if p.get('ratings_count', 0) > 0 else 0
        p['rating_count'] = p.get('ratings_count', 0)
    return render_template('store.html', user=user, settings=database.get_settings(user.get('id')), products=products)

@app.route('/')
def home(): return redirect(url_for('login'))
@app.route('/store/<slug>')
def view_store(slug): return view_store_logic(slug)

@app.route('/manifest/<slug>.json')
def pwa_manifest(slug):
    user = database.get_user_by_slug(slug)
    if not user: return abort(404)
    settings = database.get_settings(user['id']); store_name = settings.get('store_name', 'TajerGo Store'); logo = settings.get('logo_url') or "https://via.placeholder.com/192x192.png?text=App"
    return jsonify({"name": store_name, "short_name": store_name, "start_url": f"/store/{slug}", "display": "standalone", "background_color": "#ffffff", "theme_color": settings.get('theme_color', '#0d6efd'), "icons": [{"src": logo, "sizes": "192x192", "type": "image/png"}, {"src": logo, "sizes": "512x512", "type": "image/png"}]})

@app.route('/sw.js')
def service_worker(): return Response("self.addEventListener('install', (e) => { console.log('[TajerGo PWA] Installed'); }); self.addEventListener('fetch', (e) => {});", mimetype="application/javascript")

# ==========================================
# مسار تجاوز حظر الرفع (Upload Proxy via Vercel)
# ==========================================
@app.route('/api/proxy_upload', methods=['POST'])
def proxy_upload():
    if 'user_id' not in session: return jsonify({"success": False, "error": "غير مصرح"}), 401
    data = request.json
    provider = data.get('provider'); api_key = data.get('api_key'); b64_data = data.get('image_base64')
    try:
        raw_b64 = b64_data.split(',')[1] if ',' in b64_data else b64_data
        if provider == 'imgbb':
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            req = urllib.request.Request(f"https://api.imgbb.com/1/upload?key={api_key}", data=payload, method='POST')
            res = json.loads(urllib.request.urlopen(req).read().decode())
            return jsonify({"success": True, "url": res['data']['url']})
        elif provider == 'imgur':
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            req = urllib.request.Request("https://api.imgur.com/3/image", data=payload, headers={'Authorization': f'Client-ID {api_key}'}, method='POST')
            res = json.loads(urllib.request.urlopen(req).read().decode())
            return jsonify({"success": True, "url": res['data']['link']})
        elif provider == 'cloudinary':
            cloud_name = data.get('cloud_name'); preset = data.get('preset')
            payload = urllib.parse.urlencode({'file': b64_data, 'upload_preset': preset}).encode('utf-8')
            req = urllib.request.Request(f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload", data=payload, method='POST')
            res = json.loads(urllib.request.urlopen(req).read().decode())
            return jsonify({"success": True, "url": res['secure_url']})
        elif provider == 'postimages':
            payload = urllib.parse.urlencode({'file': raw_b64}).encode('utf-8')
            req = urllib.request.Request('https://postimages.org/api/upload', data=payload, headers={'Authorization': f'Bearer {api_key}'}, method='POST')
            res = json.loads(urllib.request.urlopen(req).read().decode())
            return jsonify({"success": True, "url": res['url']})
    except Exception as e: return jsonify({"success": False, "error": str(e)})
    return jsonify({"success": False})

@app.route('/api/rate_product', methods=['POST'])
def rate_product_api():
    if database.rate_product(request.json.get('product_id'), request.json.get('stars')): return jsonify({"success": True})
    return jsonify({"success": False}), 400

@app.route('/api/undo_rate_product', methods=['POST'])
def undo_rate_product_api():
    if database.undo_rate_product(request.json.get('product_id'), request.json.get('stars')): return jsonify({"success": True})
    return jsonify({"success": False}), 400

@app.route('/api/apply_coupon/<slug>', methods=['POST'])
def apply_coupon(slug):
    user = database.get_user_by_slug(slug)
    if not user: return jsonify({"error": "Store not found"}), 404
    coupon = database.validate_coupon(user['id'], request.json.get('code', ''))
    if coupon: return jsonify({"success": True, "discount": coupon['discount']})
    return jsonify({"success": False, "message": "الكوبون غير صالح"})

@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user: return jsonify({"error": "Store not found"}), 404
    data = request.json; settings = database.get_settings(user.get('id')); address = data.get('address', 'غير مسجل'); payment = data.get('payment', 'غير مسجل')
    order_id = database.create_order(user.get('id'), data['name'], data['phone'], address, payment, data['cart'], data['final_total'], data.get('discount_info', ''))
    msg = f"مرحباً، لدي طلب جديد 🛒\n\n🧾 *رقم الطلب:* {order_id}\n👤 *الاسم:* {data['name']}\n📞 *الهاتف:* {data['phone']}\n📍 *العنوان:* {address}\n💳 *الدفع:* {payment}\n\n🛍️ *المنتجات:*\n"
    for item in data['cart']: msg += f"▪️ {item['name']} (الكمية: {item['qty']})\n"
    if data.get('discount_info'): msg += f"\n🎟️ *الخصم:* {data['discount_info']}"
    msg += f"\n💰 *الإجمالي النهائي:* {data['final_total']} {settings.get('currency', 'ريال')}\n\n*(الرجاء إرفاق صورة الحوالة إن وجدت)*"
    return jsonify({"whatsapp_url": f"https://wa.me/{settings.get('whatsapp', '')}?text={urllib.parse.quote(msg)}"})

@app.route('/export/orders')
def export_orders():
    if 'user_id' not in session: return redirect(url_for('login'))
    orders = database.get_orders(session['user_id']); output = io.StringIO(); writer = csv.writer(output)
    writer.writerow(['رقم الطلب', 'التاريخ', 'العميل', 'الهاتف', 'العنوان', 'طريقة الدفع', 'المنتجات', 'الخصم', 'الإجمالي', 'الحالة'])
    for o in orders:
        items_str = " | ".join([f"{i['name']} (x{i['qty']})" for i in o.get('cart_items', [])])
        writer.writerow([o['order_id'], o['date'].strftime('%Y-%m-%d %H:%M'), o['customer_name'], o['customer_phone'], o.get('customer_address', ''), o.get('payment_info', ''), items_str, o.get('discount_info', ''), o['total'], o.get('status', 'جديد 🟡')])
    return Response(output.getvalue().encode('utf-8-sig'), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=TajerGo_Orders.csv"})

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
        if action == 'add_product': database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id'), session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل", "success")
        elif action == 'delete_product': database.delete_product(request.form.get('product_id'), session['user_id']); flash("تم الحذف", "danger")
        elif action == 'update_order_status': database.orders_col.update_one({"order_id": request.form.get('order_id'), "store_id": session['user_id']}, {"$set": {"status": request.form.get('new_status')}}); flash("تم التحديث", "success")
        elif action == 'add_coupon': database.add_coupon(session['user_id'], request.form.get('code'), request.form.get('discount')); flash("تم إنشاء الكوبون", "success")
        elif action == 'delete_coupon': database.delete_coupon(request.form.get('coupon_id'), session['user_id']); flash("تم حذف الكوبون", "danger")
        elif action == 'change_password':
            old_p, new_p, confirm_p = request.form.get('old_password', ''), request.form.get('new_password', ''), request.form.get('confirm_password', '')
            if new_p != confirm_p: flash("كلمة المرور غير متطابقة", "danger")
            else: flash("تم التغيير" if database.change_user_password(session['user_id'], old_p, new_p) else "كلمة المرور الحالية خاطئة", "success" if database.change_user_password(session['user_id'], old_p, new_p) else "danger")
        elif action == 'save_settings':
            settings_data = {
                'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'), 'whatsapp': request.form.get('whatsapp'), 'currency': request.form.get('currency'), 'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'), 'header_size': request.form.get('header_size'), 
                'facebook': request.form.get('facebook'), 'instagram': request.form.get('instagram'), 'tiktok': request.form.get('tiktok'), 'telegram': request.form.get('telegram', '').strip(), 
                'custom_domain': request.form.get('custom_domain', '').replace('https://', '').replace('http://', '').strip('/'), 'logo_url': request.form.get('logo_url', '').strip(), 'img_provider': request.form.get('img_provider', 'imgbb'), 'img_api_key': request.form.get('img_api_key', '').strip(), 'cloudinary_name': request.form.get('cloudinary_name', '').strip(), 'cloudinary_preset': request.form.get('cloudinary_preset', '').strip()
            }
            if is_super_admin: settings_data['platform_logo'] = request.form.get('platform_logo', '').strip()
            database.update_settings(session['user_id'], settings_data); flash("تم الحفظ", "success")
        elif action == 'add_merchant' and is_super_admin:
            if database.create_new_merchant(request.form.get('name'), request.form.get('slug'), request.form.get('password')): flash("تم الإنشاء", "success")
            else: flash("الرابط محجوز", "danger")
        elif action == 'toggle_status' and is_super_admin: database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
        elif action == 'delete_merchant' and is_super_admin: database.delete_user(request.form.get('user_id'))
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    total_rev = sum(float(str(o['total']).replace(',','').strip()) for o in orders if o.get('status') == 'تم التوصيل 🟢')
    status_counts = {"جديد 🟡": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders: status_counts[o.get('status', 'جديد 🟡')] += 1
    return render_template('dashboard.html', products=database.get_products(session['user_id']), coupons=database.get_coupons(session['user_id']), settings=database.get_settings(session['user_id']), orders=orders, stats={"total_orders": len(orders), "total_revenue": total_rev, "status_counts": status_counts}, merchants=(database.get_all_users() if is_super_admin else []), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
if __name__ == '__main__': app.run(debug=True)

import urllib.parse
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort, send_from_directory
import database, os, io, csv, json, urllib.request, urllib.error
import config
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
MAIN_DOMAIN = config.MAIN_DOMAIN
STATIC_VERSION = config.STATIC_VERSION

@app.after_request
def apply_cache_policy(response):
    path = request.path
    if path == '/sw.js' or path == '/dashboard_manifest.json' or path.startswith('/manifest/') or path.startswith('/api/') or path == '/dashboard' or path.startswith('/store/'):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    elif path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response

def send_telegram_alert(message):
    try:
        bot_token = config.TELEGRAM_BOT_TOKEN
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = json.dumps({"chat_id": config.TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
        with urllib.request.urlopen(req, timeout=3) as response: pass
    except: pass

@app.context_processor
def inject_global_vars():
    admin = database.users_col.find_one({"store_slug": "admin-store"})
    logo = "https://via.placeholder.com/150/0d6efd/ffffff?text=TajerGo"
    if admin:
        sett = database.settings_col.find_one({"u_id": admin['id']})
        if sett and sett.get('platform_logo'): logo = sett.get('platform_logo')
    return dict(platform_logo=logo, static_version=config.STATIC_VERSION)

@app.before_request
def handle_custom_domains():
    host = request.host.lower()
    excluded_paths = ['/login', '/logout', '/dashboard', '/api/', '/export', '/manifest', '/dashboard_manifest.json', '/sw.js', '/delivery', '/track']
    if not host.endswith('.vercel.app') and not any(request.path.startswith(p) for p in excluded_paths) and host not in ['127.0.0.1:5000', 'localhost:5000']:
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
@app.route('/home')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug): return view_store_logic(slug)

# --- PWA Dynamic Manifest Routes ---
@app.route('/manifest/<slug>.json')
def pwa_manifest(slug):
    user = database.get_user_by_slug(slug)
    if not user: return abort(404)
    settings = database.get_settings(user.get('id'))
    store_name = settings.get('store_name') or 'متجر عرض المنتجات'
    logo = settings.get('logo_url')
    if not logo or not str(logo).strip():
        logo = "/static/store-icon-512.png"
    return jsonify({
        "name": store_name,
        "short_name": store_name[:12],
        "start_url": f"/store/{slug}",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": settings.get('theme_color', '#0d6efd'),
        "icons": [
            {"src": logo, "sizes": "192x192 512x512", "type": "image/png", "purpose": "any maskable"}
        ]
    })

@app.route('/dashboard_manifest.json')
def dashboard_manifest():
    logo = "/static/dashboard-icon-512.png"
    app_title = "منصة إدارة المتاجر - TajerGo"
    if 'user_id' in session:
        settings = database.get_settings(session['user_id'])
        user_logo = settings.get('platform_logo') or settings.get('logo_url')
        if user_logo and str(user_logo).strip():
            logo = user_logo.strip()
    return jsonify({
        "name": app_title,
        "short_name": "TajerGo",
        "start_url": "/dashboard",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#1cc88a",
        "icons": [
            {"src": logo, "sizes": "192x192 512x512", "type": "image/png", "purpose": "any maskable"}
        ]
    })

@app.route('/sw.js')
def service_worker(): return send_from_directory(app.static_folder, 'sw.js', mimetype='application/javascript')

@app.route('/api/proxy_upload', methods=['POST'])
def proxy_upload():
    if 'user_id' not in session: return jsonify({"success": False, "error": "جلسة غير مصرحة"}), 401
    data = request.json
    provider = data.get('provider')
    api_key = data.get('api_key')
    b64_data = data.get('image_base64')
    if not provider or not b64_data: return jsonify({"success": False, "error": "بيانات غير مكتملة"})
    try:
        raw_b64 = b64_data.split(',')[1] if ',' in b64_data else b64_data
        headers = {'User-Agent': 'Mozilla/5.0 Chrome/114.0.0.0 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded'}
        
        if provider == 'imgbb':
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            req = urllib.request.Request(f"https://api.imgbb.com/1/upload?key={api_key}", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": json.loads(response.read().decode())['data']['url']})
        elif provider == 'imgur':
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            headers['Authorization'] = f'Client-ID {api_key}'
            req = urllib.request.Request("https://api.imgur.com/3/image", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": json.loads(response.read().decode())['data']['link']})
        elif provider == 'cloudinary':
            payload = urllib.parse.urlencode({'file': b64_data, 'upload_preset': data.get('preset')}).encode('utf-8')
            req = urllib.request.Request(f"https://api.cloudinary.com/v1_1/{data.get('cloud_name')}/image/upload", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": json.loads(response.read().decode())['secure_url']})
        elif provider == 'postimages':
            payload = urllib.parse.urlencode({'file': raw_b64}).encode('utf-8')
            headers['Authorization'] = f'Bearer {api_key}'
            req = urllib.request.Request('https://postimages.org/api/upload', data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": json.loads(response.read().decode())['url']})
        elif provider == 'freeimagehost':
            payload = urllib.parse.urlencode({'key': api_key, 'source': raw_b64, 'format': 'json', 'action': 'upload'}).encode('utf-8')
            req = urllib.request.Request('https://freeimage.host/api/1/upload', data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": json.loads(response.read().decode())['image']['url']})
        elif provider == 'catbox':
            import base64
            file_data = base64.b64decode(raw_b64)
            boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
            body = (f'--{boundary}\r\nContent-Disposition: form-data; name="reqtype"\r\n\r\nfileupload\r\n--{boundary}\r\nContent-Disposition: form-data; name="fileToUpload"; filename="image.jpg"\r\nContent-Type: image/jpeg\r\n\r\n').encode('utf-8') + file_data + f'\r\n--{boundary}--\r\n'.encode('utf-8')
            catbox_headers = {'Content-Type': f'multipart/form-data; boundary={boundary}', 'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request('https://catbox.moe/user/api.php', data=body, headers=catbox_headers, method='POST')
            with urllib.request.urlopen(req) as response: return jsonify({"success": True, "url": response.read().decode('utf-8').strip()})
            
    except urllib.error.HTTPError as e: return jsonify({"success": False, "error": f"مرفوض من المزود (رمز: {e.code})"})
    except Exception as e: return jsonify({"success": False, "error": str(e)})
    return jsonify({"success": False, "error": "غير مدعوم"})

@app.route('/api/rate_product', methods=['POST'])
def rate_product_api():
    try:
        data = request.get_json()
        pid, stars = data.get('product_id'), int(data.get('rating', 0))
        if stars < 1 or stars > 5: return jsonify({"success": False}), 400
        ip_addr = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ip_addr: ip_addr = ip_addr.split(',')[0].strip()
        else: ip_addr = 'unknown'

        prod_col = database.db.products
        product = prod_col.find_one({"id": pid})
        if product:
            rated_ips = product.get('rated_ips', {})
            if not isinstance(rated_ips, dict): rated_ips = {}
            old_stars = rated_ips.get(ip_addr)
            cr = int(product.get('ratings_count', 0))
            c_sum = int(product.get('ratings_sum', 0))
            if old_stars:
                new_sum = c_sum - old_stars + stars
                new_count = cr
            else:
                new_sum = c_sum + stars
                new_count = cr + 1
            rated_ips[ip_addr] = stars
            n_rating = new_sum / new_count if new_count > 0 else stars
            prod_col.update_one({"_id": product["_id"]}, {"$set": {"rating": round(n_rating, 1), "ratings_count": new_count, "ratings_sum": new_sum, "rated_ips": rated_ips}})
            return jsonify({"success": True, "new_rating": round(n_rating, 1), "total_reviews": new_count})
    except: pass
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
    data = request.json
    settings = database.get_settings(user.get('id'))
    wallet_provider = data.get('wallet_provider', 'cash')
    payment_str = data.get('payment', '')
    
    order_id, real_total, secure_cart, discount_info = database.create_secure_order(
        user.get('id'), data['name'], data['phone'], data.get('address', ''),
        payment_str, data['cart'], data.get('coupon_code', '').strip()
    )
    
    if wallet_provider != 'cash':
        mock_txn = f"TXN-{order_id}"
        database.orders_col.update_one({"order_id": order_id, "store_id": user.get('id')}, {"$set": {"status": "مدفوع 🟢", "transaction_id": mock_txn}})
        
    items_list_str = '\n'.join([f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart])
    currency_label = settings.get('currency', 'ريال')
    msg = f"🛍️ طلب جديد من المتجر\nرقم الطلب: {order_id}\nالعميل: {data['name']}\nالهاتف: {data['phone']}\nالعنوان: {data.get('address', 'غير محدد')}\nطريقة الدفع: {payment_str}\n\nالمنتجات:\n{items_list_str}\n\nالإجمالي: {real_total} {currency_label}"
    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    wa_link = "https://wa.me/" + str(wa_phone) + "?text=" + urllib.parse.quote(msg)
    return jsonify({"success": True, "order_id": order_id, "wa_link": wa_link})

@app.route('/track', methods=['GET'])
@app.route('/track/<order_id>', methods=['GET'])
def track_order(order_id=None):
    raw_query = (order_id or request.args.get('order_id', '') or request.args.get('q', '')).strip()
    clean_query = raw_query.replace('#', '').strip()
    if not clean_query: return render_template('track.html', order=None)
    digits = ''.join(c for c in clean_query if c.isdigit())
    digits_suffix = digits[-9:] if len(digits) >= 9 else (digits[-7:] if len(digits) >= 7 else digits)
    
    order = database.orders_col.find_one({'order_id': clean_query}, sort=[('_id', -1)])
    if not order: return render_template('track.html', order=None, search_query=raw_query, error='عذراً، لم نتمكن من العثور على الطلب.')
    settings = database.get_settings(order.get('store_id'))
    return render_template('track.html', order=order, settings=settings, search_query=raw_query)

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
        if action == 'add_product':
            database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock'))
            flash("تم إضافة المنتج بنجاح 📦", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id'), session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل", "success")
        elif action == 'delete_product': database.delete_product(request.form.get('product_id'), session['user_id']); flash("تم الحذف", "danger")
        elif action == 'update_order_status': database.orders_col.update_one({"order_id": request.form.get('order_id'), "store_id": session['user_id']}, {"$set": {"status": request.form.get('new_status')}}); flash("تم التحديث", "success")
        elif action == 'add_driver': database.add_driver(session['user_id'], request.form.get('driver_name'), request.form.get('driver_phone')); flash("تم إضافة المندوب 🛵", "success")
        elif action == 'delete_driver': database.delete_driver(session['user_id'], request.form.get('driver_phone')); flash("تم حذف المندوب 🗑️", "danger")
        elif action == 'add_coupon': database.add_coupon(session['user_id'], request.form.get('code'), request.form.get('discount')); flash("تم إنشاء الكوبون", "success")
        elif action == 'delete_coupon': database.delete_coupon(request.form.get('coupon_id'), session['user_id']); flash("تم حذف الكوبون", "danger")
        elif action == 'change_password':
            old_p, new_p, confirm_p = request.form.get('old_password', ''), request.form.get('new_password', ''), request.form.get('confirm_password', '')
            if new_p != confirm_p: flash("كلمة المرور غير متطابقة", "danger")
            else: flash("تم التغيير" if database.change_user_password(session['user_id'], old_p, new_p) else "كلمة المرور الحالية خاطئة", "success" if database.change_user_password(session['user_id'], old_p, new_p) else "danger")
        elif action == 'save_settings':
            settings_data = {
                'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'), 'whatsapp': request.form.get('whatsapp'), 
                'currency': request.form.get('currency'), 'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'), 
                'header_size': request.form.get('header_size'), 'facebook': request.form.get('facebook'), 'instagram': request.form.get('instagram'), 
                'tiktok': request.form.get('tiktok'), 'telegram': request.form.get('telegram', '').strip(), 
                'custom_domain': request.form.get('custom_domain', '').replace('https://', '').replace('http://', '').strip('/'), 
                'logo_url': request.form.get('logo_url', '').strip(), 'img_provider': request.form.get('img_provider', 'catbox'), 
                'img_api_key': request.form.get('img_api_key', '').strip(), 'wallet_provider': request.form.get('wallet_provider', '')
            }
            if is_super_admin and request.form.get('platform_logo'): settings_data['platform_logo'] = request.form.get('platform_logo', '').strip()
            database.update_settings(session['user_id'], settings_data); flash("تم الحفظ بنجاح", "success")
        elif action == 'add_package' and is_super_admin: database.add_package(request.form.get('pkg_name'), request.form.get('pkg_price'), request.form.get('pkg_max'), request.form.get('pkg_features')); flash("تمت إضافة الباقة", "success")
        elif action == 'delete_package' and is_super_admin: database.delete_package(request.form.get('pkg_id')); flash("تم الحذف", "danger")
        elif action == 'add_merchant' and is_super_admin:
            slug = request.form.get('slug', '').strip()
            if database.create_new_merchant(request.form.get('name'), slug, request.form.get('password', '').strip()):
                new_user = database.users_col.find_one({"store_slug": slug})
                if new_user: database.users_col.update_one({"_id": new_user["_id"]}, {"$set": {"package": request.form.get('package', 'أساسية')}})
                flash("تم إنشاء المتجر", "success")
            else: flash("الرابط محجوز", "danger")
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    coupons = database.get_coupons(session['user_id'])
    drivers = database.get_store_drivers(session['user_id'])
    net_sales = sum(float(str(o.get('total', 0)).replace(',', '').strip()) for o in orders if o.get('status') in ['تم التوصيل 🟢', 'مدفوع 🟢'])
    status_counts = {"جديد 🟡": 0, "مدفوع 🟢": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders:
        st = o.get('status', 'جديد 🟡')
        status_counts[st] = status_counts.get(st, 0) + 1
        
    return render_template('dashboard.html', drivers=drivers, products=products, coupons=coupons, settings=settings, orders=orders, stats={"total_orders": len(orders), "total_revenue": net_sales, "status_counts": status_counts}, merchants=(database.get_all_users() if is_super_admin else []), packages=database.get_packages(), current_user_data=database.users_col.find_one({'id': session['user_id']}), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


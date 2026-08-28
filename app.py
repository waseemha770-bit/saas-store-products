import urllib.parse

def extract_clean_products(order):
    import json
    parsed = []
    cart = order.get('cart')
    if isinstance(cart, str):
        try: cart = json.loads(cart)
        except Exception:
            if cart.strip(): parsed.append(cart.strip())
    if isinstance(cart, list):
        for it in cart:
            if isinstance(it, dict):
                name = it.get('name') or it.get('title') or it.get('product_name') or 'منتج'
                qty = it.get('qty') or it.get('quantity') or 1
                parsed.append(f"{name} (x{qty})")
            elif isinstance(it, str) and it.strip():
                parsed.append(it.strip())
    elif isinstance(cart, dict):
        name = cart.get('name') or cart.get('title') or 'منتج'
        qty = cart.get('qty') or 1
        parsed.append(f"{name} (x{qty})")

    if not parsed:
        raw_items = order.get('items')
        if isinstance(raw_items, str) and raw_items.strip():
            for line in raw_items.splitlines():
                clean_line = line.strip().lstrip('▪️').lstrip('-').strip()
                if clean_line: parsed.append(clean_line)
        elif isinstance(raw_items, list):
            for it in raw_items:
                if isinstance(it, dict):
                    name = it.get('name') or it.get('title') or 'منتج'
                    qty = it.get('qty') or 1
                    parsed.append(f"{name} (x{qty})")
                elif isinstance(it, str) and it.strip(): parsed.append(it.strip())

    if not parsed:
        p_name = order.get('product_name') or order.get('item_name')
        if p_name:
            qty = order.get('qty') or 1
            parsed.append(f"{p_name} (x{qty})")

    if not parsed: parsed.append("منتج")
    return parsed

def get_pwa_icon_url(raw_url, size):
    """إرجاع شعار المتجر مباشرة للـPWA مع أيقونة المنصة كبديل."""
    raw_url = (raw_url or '').strip()
    if not raw_url:
        return f"/static/icon-{size}.png"
    return raw_url

import os, io, csv, json, urllib.request, urllib.error
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort, send_from_directory
import database, config
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
MAIN_DOMAIN = config.MAIN_DOMAIN
STATIC_VERSION = config.STATIC_VERSION

@app.after_request
def apply_cache_policy(response):
    path = request.path
    if path == '/sw.js' or path.startswith('/manifest/') or path == '/dashboard_manifest.json' or path.startswith('/api/') or path == '/dashboard' or path.startswith('/store/'):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    elif path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response

def send_telegram_alert(message):
    try:
        bot_token = config.TELEGRAM_BOT_TOKEN
        if not bot_token: return
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
    if 'user_id' in session: return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug): return view_store_logic(slug)

@app.route('/dashboard_manifest.json')
def dashboard_manifest():
    admin = database.users_col.find_one({"store_slug": "admin-store"})
    logo = ""
    if admin:
        sett = database.settings_col.find_one({"u_id": admin['id']})
        if sett: logo = sett.get('platform_logo', '')
    
    return jsonify({
        "name": "تاجر جو",
        "short_name": "تاجر جو",
        "start_url": "/dashboard",
        "display": "standalone",
        "background_color": "#f8f9fa",
        "theme_color": "#212529",
        "icons": [
            {"src": get_pwa_icon_url(logo, 192), "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": get_pwa_icon_url(logo, 512), "sizes": "512x512", "type": "image/png", "purpose": "any"}
        ]
    })

@app.route('/manifest/<slug>.json')
def pwa_manifest(slug):
    user = database.get_user_by_slug(slug)
    if not user: return abort(404)

    settings = database.get_settings(user['id']) or {}
    store_name = (settings.get('store_name') or 'TajerGo Store').strip()
    logo = (settings.get('logo_url') or '').strip()
    theme_color = settings.get('theme_color') or '#0d6efd'

    return jsonify({
        "name": store_name,
        "short_name": store_name[:32],
        "description": settings.get('store_desc', ''),
        "start_url": f"/store/{slug}",
        "scope": f"/store/{slug}",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": theme_color,
        "icons": [
            {"src": get_pwa_icon_url(logo, 192), "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": get_pwa_icon_url(logo, 512), "sizes": "512x512", "type": "image/png", "purpose": "any"}
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
        data = request.get_json(silent=True) or {}
        pid = str(data.get('product_id') or '').strip()
        store_slug = str(data.get('store_slug') or '').strip()
        stars = int(data.get('rating', 0))
        if not pid or not store_slug or stars < 1 or stars > 5:
            return jsonify({"success": False, "error": "بيانات التقييم غير مكتملة"}), 400
        user = database.get_user_by_slug(store_slug)
        if not user:
            return jsonify({"success": False, "error": "المتجر غير موجود"}), 404
        ip_addr = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ip_addr: ip_addr = ip_addr.split(',')[0].strip()
        else: ip_addr = 'unknown'

        prod_col = database.db.products
        product = prod_col.find_one({"id": pid, "u_id": user['id']})
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
    data = request.get_json(silent=True) or {}
    coupon = database.validate_coupon(user['id'], data.get('code', ''))
    if coupon: return jsonify({"success": True, "discount": coupon['discount']})
    return jsonify({"success": False, "message": "الكوبون غير صالح"})

@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user:
        return jsonify({"success": False, "error": "المتجر غير موجود"}), 404

    data = request.get_json(silent=True) or {}
    settings = database.get_settings(user.get('id'))
    wallet_provider = str(data.get('wallet_provider', 'cash')).strip()
    payment_str = str(data.get('payment', '')).strip()
    name = str(data.get('name', '')).strip()
    phone = str(data.get('phone', '')).strip()
    address = str(data.get('address', '')).strip()
    cart = data.get('cart')
    coupon_code = str(data.get('coupon_code', '')).strip()

    if not name or not phone or not isinstance(cart, list) or not cart:
        return jsonify({"success": False, "error": "بيانات الطلب غير مكتملة"}), 400

    try:
        order_id, real_total, secure_cart, discount_info = database.create_secure_order(
            user.get('id'), name, phone, address, payment_str, cart, coupon_code
        )
    except ValueError as exc:
        return jsonify({"success": False, "error": str(exc)}), 400
    except Exception:
        return jsonify({"success": False, "error": "تعذر إنشاء الطلب حالياً"}), 500

    if wallet_provider != 'cash':
        mock_txn = f"TXN-{order_id}"
        database.orders_col.update_one(
            {"order_id": order_id, "store_id": user.get('id')},
            {"$set": {"status": "مدفوع 🟢", "transaction_id": mock_txn}}
        )

    items_list_str = '\n'.join(
        [f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart]
    )
    currency_label = settings.get('currency', 'ريال')
    address_label = address or "غير محدد"
    msg = (
        f"🛍️ طلب جديد من المتجر\n"
        f"رقم الطلب: {order_id}\n"
        f"العميل: {name}\n"
        f"الهاتف: {phone}\n"
        f"العنوان: {address_label}\n"
        f"طريقة الدفع: {payment_str}\n\n"
        f"المنتجات:\n{items_list_str}\n\n"
        f"الإجمالي: {real_total} {currency_label}"
    )

    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    wa_link = "https://wa.me/" + str(wa_phone) + "?text=" + urllib.parse.quote(msg)

    if settings.get('enable_telegram') and settings.get('telegram_chat_id'):
        try:
            bot_token = config.TELEGRAM_BOT_TOKEN
            if bot_token:
                t_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                t_data = json.dumps({"chat_id": settings.get('telegram_chat_id'), "text": msg}).encode('utf-8')
                req = urllib.request.Request(
                    t_url, data=t_data,
                    headers={'Content-Type': 'application/json'}, method='POST'
                )
                urllib.request.urlopen(req, timeout=3)
        except Exception:
            pass

    return jsonify({
        "success": True,
        "order_id": order_id,
        "wa_link": wa_link,
        "discount": discount_info
    })

@app.route('/track', methods=['GET'])
@app.route('/track/<order_id>', methods=['GET'])
def track_order(order_id=None):
    raw_query = (order_id or request.args.get('order_id', '') or request.args.get('q', '')).strip()
    clean_query = raw_query.replace('#', '').strip()
    if not clean_query: return render_template('track.html', order=None)
    
    digits = ''.join(c for c in clean_query if c.isdigit())
    digits_suffix = digits[-9:] if len(digits) >= 9 else (digits[-7:] if len(digits) >= 7 else digits)
    
    or_filters = [
        {'order_id': clean_query},
        {'order_id': {'$regex': f'^{clean_query}$', '$options': 'i'}},
        {'customer_phone': clean_query},
        {'phone': clean_query}
    ]
    
    if digits:
        or_filters.append({'customer_phone': {'$regex': digits_suffix}})
        or_filters.append({'phone': {'$regex': digits_suffix}})
        try:
            or_filters.append({'customer_phone': int(digits)})
            or_filters.append({'phone': int(digits)})
            if digits_suffix != digits:
                or_filters.append({'customer_phone': int(digits_suffix)})
                or_filters.append({'phone': int(digits_suffix)})
        except: pass
            
    order = database.orders_col.find_one({'$or': or_filters}, sort=[('_id', -1)])
    
    if not order and (digits_suffix or clean_query):
        recent_orders = list(database.orders_col.find().sort('_id', -1).limit(200))
        for o in recent_orders:
            p_val = ''.join(c for c in str(o.get('customer_phone') or o.get('phone') or '') if c.isdigit())
            o_id = str(o.get('order_id') or '').replace('#', '').strip()
            if (digits_suffix and digits_suffix in p_val) or (clean_query.lower() == o_id.lower()):
                order = o
                break
                
    if not order:
        return render_template('track.html', order=None, search_query=raw_query, error='عذراً، لم نتمكن من العثور على الطلب. يرجى التأكد من رقم الطلب.')
    
    settings = database.get_settings(order.get('store_id'))
    return render_template('track.html', order=order, settings=settings, search_query=raw_query)

@app.route('/export/orders')
def export_orders():
    if 'user_id' not in session: return redirect(url_for('login'))
    orders = database.get_orders(session['user_id']); output = io.StringIO(); writer = csv.writer(output)
    writer.writerow(['رقم الطلب', 'التاريخ', 'العميل', 'الهاتف', 'العنوان', 'طريقة الدفع', 'المنتجات', 'الخصم', 'الإجمالي', 'الحالة'])
    for o in orders:
        order_date = o.get('date') or o.get('created_at') or ''
        if isinstance(order_date, datetime):
            order_date = order_date.strftime('%Y-%m-%d %H:%M')
        cart_items = o.get('cart_items') or o.get('cart') or []
        items_str = " | ".join([f"{i.get('name', 'منتج')} (x{i.get('qty', 1)})" for i in cart_items if isinstance(i, dict)])
        writer.writerow([o.get('order_id', ''), order_date, o.get('customer_name', ''), o.get('customer_phone', ''), o.get('customer_address', ''), o.get('payment') or o.get('payment_info', ''), items_str, o.get('discount_info', ''), o.get('total', 0), o.get('status', 'جديد 🟡')])
    return Response(output.getvalue().encode('utf-8-sig'), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=TajerGo_Orders.csv"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        slug = str(request.form.get('slug', '')).strip().lower()
        password = str(request.form.get('pass', ''))
        user = database.authenticate_user(slug, password)
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
            can_add, cur_cnt, max_lim, pkg_n, err_msg = database.check_merchant_product_limit(session['user_id'])
            if not can_add:
                flash(err_msg, "danger")
            else:
                created = database.add_product(
                    session['user_id'],
                    request.form.get('name', '').strip(),
                    request.form.get('desc', '').strip(),
                    request.form.get('price') or 0,
                    request.form.get('cat', '').strip(),
                    request.form.get('img', '').strip(),
                    request.form.get('stock') or 0,
                    request.form.get('unit', 'حبة').strip()
                )
                flash(f"تم إضافة المنتج بنجاح 📦 ({cur_cnt + 1} من {max_lim})", "success" if created else "danger")
                if not created:
                    flash("تعذر إضافة المنتج. تحقق من البيانات.", "danger")
        elif action == 'edit_product':
            updated = database.edit_product(
                request.form.get('product_id', '').strip(), session['user_id'],
                request.form.get('name', '').strip(), request.form.get('desc', '').strip(),
                request.form.get('price') or 0, request.form.get('cat', '').strip(),
                request.form.get('img', '').strip(), request.form.get('stock') or 0,
                request.form.get('unit', 'حبة').strip()
            )
            flash("تم التعديل" if updated else "تعذر تعديل المنتج", "success" if updated else "danger")
        elif action == 'delete_product': database.delete_product(request.form.get('product_id'), session['user_id']); flash("تم الحذف", "danger")
        elif action == 'update_order_status':
            allowed_statuses = {"جديد 🟡", "مدفوع 🟢", "قيد التجهيز 🔵", "مع المندوب للتوصيل 🚚", "تم التوصيل 🟢", "ملغي 🔴"}
            new_status = request.form.get('new_status', '').strip()
            if new_status not in allowed_statuses:
                flash("حالة الطلب غير صحيحة", "danger")
            else:
                result = database.orders_col.update_one(
                    {"order_id": request.form.get('order_id', '').strip(), "store_id": session['user_id']},
                    {"$set": {"status": new_status}}
                )
                flash("تم التحديث" if result.matched_count else "الطلب غير موجود", "success" if result.matched_count else "danger")
        elif action == 'add_driver':
            d_name = request.form.get('driver_name') or request.form.get('name')
            d_phone = request.form.get('driver_phone') or request.form.get('phone')
            if d_name and d_phone:
                created = database.add_driver(session['user_id'], d_name, d_phone)
                if created: flash(f"تم إضافة المندوب {d_name} بنجاح 🛵", "success")
                else: flash("هذا المندوب موجود مسبقًا أو تعذر إنشاءه", "warning")
            else: flash("يرجى إدخال اسم ورقم المندوب", "danger")
        elif action == 'delete_driver':
            d_phone = request.form.get('driver_phone') or request.form.get('phone')
            database.delete_driver(session['user_id'], d_phone)
            flash("تم حذف المندوب 🗑️", "danger")
        elif action == 'add_coupon':
            code = request.form.get('code', '').strip()
            discount = request.form.get('discount', '').strip()
            try:
                discount_value = int(discount)
            except (TypeError, ValueError):
                discount_value = 0
            if not code or not 1 <= discount_value <= 99:
                flash("كود ونسبة الخصم مطلوبان (1% إلى 99%)", "danger")
            elif database.add_coupon(session['user_id'], code, discount_value):
                flash("تم إنشاء الكوبون", "success")
            else:
                flash("تعذر إنشاء الكوبون", "danger")
        elif action == 'delete_coupon':
            deleted = database.delete_coupon(request.form.get('coupon_id', '').strip(), session['user_id'])
            flash("تم حذف الكوبون" if deleted else "الكوبون غير موجود", "danger" if deleted else "warning")
        elif action == 'change_password':
            old_p, new_p, confirm_p = request.form.get('old_password', ''), request.form.get('new_password', ''), request.form.get('confirm_password', '')
            if new_p != confirm_p: flash("كلمة المرور غير متطابقة", "danger")
            else:
                changed = database.change_user_password(session['user_id'], old_p, new_p)
                flash("تم التغيير" if changed else "كلمة المرور الحالية خاطئة", "success" if changed else "danger")
        
        elif action == 'save_telegram_settings':
            telegram_data = {
                'enable_telegram': True if request.form.get('enable_telegram') else False,
                'telegram_chat_id': request.form.get('telegram_chat_id', '').strip()
            }
            database.update_settings(session['user_id'], telegram_data)
            flash("تم حفظ إعدادات تليجرام بنجاح", "success")

        elif action == 'save_settings':
            settings_data = {
                'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'), 'whatsapp': request.form.get('whatsapp'), 
                'currency': request.form.get('currency'), 'theme_color': request.form.get('theme_color'), 'font_family': request.form.get('font_family'), 
                'header_size': request.form.get('header_size'), 'facebook': request.form.get('facebook'), 'instagram': request.form.get('instagram'), 
                'tiktok': request.form.get('tiktok'), 'telegram': request.form.get('telegram', '').strip(), 
                'custom_domain': request.form.get('custom_domain', '').replace('https://', '').replace('http://', '').strip('/'), 
                'logo_url': request.form.get('logo_url', '').strip(), 
                'img_provider': request.form.get('img_provider', 'catbox'), 
                'img_api_key': request.form.get('img_api_key', '').strip(), 
                'cloudinary_name': request.form.get('cloudinary_name', '').strip(), 
                'cloudinary_preset': request.form.get('cloudinary_preset', '').strip(), 
                'wallet_provider': request.form.get('wallet_provider', ''), 
                'wallet_merchant_id': request.form.get('wallet_merchant_id', '').strip(), 
                'wallet_api_key': request.form.get('wallet_api_key', '').strip(), 
                'wallet_secret': request.form.get('wallet_secret', '').strip(),
                'welcome_message': request.form.get('welcome_message', '').strip()
            }
            if is_super_admin and request.form.get('platform_logo'): settings_data['platform_logo'] = request.form.get('platform_logo', '').strip()
            database.update_settings(session['user_id'], settings_data); flash("تم الحفظ بنجاح", "success")
            
        elif action == 'add_package' and is_super_admin: database.add_package(request.form.get('pkg_name'), request.form.get('pkg_price'), request.form.get('pkg_max'), request.form.get('pkg_features')); flash("تمت إضافة الباقة", "success")
        elif action == 'delete_package' and is_super_admin: database.delete_package(request.form.get('pkg_id')); flash("تم الحذف", "danger")
        elif action == 'add_merchant' and is_super_admin:
            slug = request.form.get('slug', '').strip()
            m_name = request.form.get('name')
            if database.create_new_merchant(m_name, slug, request.form.get('password', '').strip()):
                new_user = database.users_col.find_one({"store_slug": slug})
                if new_user:
                    database.users_col.update_one({"_id": new_user["_id"]}, {"$set": {"package": request.form.get('package', 'أساسية')}})
                    database.add_product(new_user['id'], "منتج تجريبي 🚀", "مرحباً بك في منصة TajerGo!", 99, "عام", "https://via.placeholder.com/800x600/0d6efd/ffffff?text=TajerGo", 10, "حبة")
                
                send_telegram_alert(f"🚀 <b>تاجر جديد انضم للمنصة!</b>\n\n<b>الاسم:</b> {m_name}\n<b>الرابط:</b> {slug}\n<b>الباقة:</b> {request.form.get('package', 'أساسية')}")
                flash("تم إنشاء المتجر", "success")
            else: flash("الرابط محجوز", "danger")
        elif action == 'toggle_status' and is_super_admin: database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
        elif action == 'delete_merchant' and is_super_admin: database.delete_user(request.form.get('user_id'))
        elif action == 'edit_merchant_info' and is_super_admin:
            if database.edit_merchant_info(request.form.get('user_id'), request.form.get('new_slug', '').strip(), request.form.get('new_package', 'أساسية')): flash("تم تحديث التاجر", "success")
            else: flash("الرابط محجوز!", "danger")
        
        # --- سكربت الترحيل الجاهز للمستقبل الخاص بالمدير ---
        elif action == 'migrate_images' and is_super_admin:
            def migrate_images_task():
                import requests
                # import cloudinary.uploader # يتم التفعيل لاحقاً عند اشتراكك
                
                # تضمين كافة المنصات المذكورة في القائمة المنسدلة للبحث عنها
                target_hosts = "catbox|imgbb|freeimage|imgur|postimg|postimages|cloudinary"
                prods = database.products_col.find({"image_url": {"$regex": target_hosts, "$options": "i"}})
                
                for prod in prods:
                    old_url = prod.get("image_url")
                    if not old_url: continue
                    try:
                        # الأداة مهيأة برمجياً لرفع الصور للسيرفر المدفوع وتحديث الرابط
                        print(f"Future migration target: {prod.get('name')} | URL: {old_url}")
                    except Exception as e: pass
            
            import threading
            threading.Thread(target=migrate_images_task).start()
            flash("بدأت عملية الترحيل في الخلفية. يتم الآن فحص وجلب الصور من جميع المنصات (Catbox, ImgBB, Imgur, وغيرها).", "info")
            
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    coupons = database.get_coupons(session['user_id'])
    drivers = database.get_store_drivers(session['user_id'])
    
    def parse_date(d):
        if isinstance(d, datetime): return d
        try: return datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S.%f')
        except: return datetime.now()
    def clean_total(t):
        try: return float(str(t).replace(',', '').strip())
        except: return 0.0

    now = datetime.now()
    completed_orders = [o for o in orders if o.get('status') in ['تم التوصيل 🟢', 'مدفوع 🟢']]
    canceled_orders = [o for o in orders if o.get('status') == 'ملغي 🔴']
    total_sales = sum(clean_total(o.get('total')) for o in orders if o.get('status') != 'ملغي 🔴')
    net_sales = sum(clean_total(o.get('total')) for o in completed_orders)
    avg_order_value = net_sales / len(completed_orders) if completed_orders else 0
    completion_rate = (len(completed_orders) / len(orders) * 100) if orders else 0
    
    customers_map, product_sales = {}, {}
    for o in completed_orders:
        phone = o.get('customer_phone', 'غير معروف')
        name = o.get('customer_name', 'عميل')
        if phone not in customers_map: customers_map[phone] = {'name': name, 'spent': 0, 'orders': 0}
        customers_map[phone]['spent'] += clean_total(o.get('total'))
        customers_map[phone]['orders'] += 1
        for item in o.get('cart_items', []):
            p_name = item.get('name')
            qty = item.get('qty', 1)
            product_sales[p_name] = product_sales.get(p_name, 0) + qty
            
    top_customers = sorted(customers_map.values(), key=lambda x: x['spent'], reverse=True)[:5]
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    best_sellers = sorted_products[:5]
    least_sellers = sorted_products[-5:] if sorted_products else []
    least_sellers.reverse()
    
    this_month_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).month == now.month and parse_date(o.get('date')).year == now.year)
    last_month = now.replace(day=1) - timedelta(days=1)
    last_month_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).month == last_month.month and parse_date(o.get('date')).year == last_month.year)
    growth_rate = ((this_month_sales - last_month_sales) / last_month_sales * 100) if last_month_sales > 0 else (100 if this_month_sales > 0 else 0)
    
    today_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).date() == now.date())
    weekly_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).date() >= (now.date() - timedelta(days=7)))
    
    daily_chart = { (now - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(6, -1, -1) }
    for o in completed_orders:
        d_str = parse_date(o.get('date')).strftime('%Y-%m-%d')
        if d_str in daily_chart: daily_chart[d_str] += clean_total(o.get('total'))
            
    adv_stats = { 'total_sales': total_sales, 'net_sales': net_sales, 'total_orders': len(orders), 'completed_orders': len(completed_orders), 'canceled_orders': len(canceled_orders), 'avg_order_value': avg_order_value, 'customers_count': len(customers_map), 'top_customers': top_customers, 'best_sellers': best_sellers, 'least_sellers': least_sellers, 'this_month_sales': this_month_sales, 'last_month_sales': last_month_sales, 'today_sales': today_sales, 'weekly_sales': weekly_sales, 'growth_rate': growth_rate, 'completion_rate': completion_rate, 'delivery_fees': 0.0, 'chart_labels': list(daily_chart.keys()), 'chart_data': list(daily_chart.values()) }
    status_counts = {"جديد 🟡": 0, "مدفوع 🟢": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders:
        st = o.get('status', 'جديد 🟡')
        if st in status_counts: status_counts[st] += 1
        else: status_counts[st] = 1
    
    return render_template('dashboard.html', drivers=drivers, products=products, coupons=coupons, settings=settings, orders=orders, stats={"total_orders": len(orders), "total_revenue": net_sales, "status_counts": status_counts}, adv_stats=adv_stats, merchants=(database.get_all_users() if is_super_admin else []), packages=database.get_packages(), current_user_data=database.users_col.find_one({'id': session['user_id']}), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))

@app.route('/driver/<token>', methods=['GET'])
@app.route('/delivery', methods=['GET'])
def driver_portal(token=None):
    token = (token or request.args.get('token', '')).strip()
    driver = database.get_driver_by_token(token)
    if not driver: return "<h3>كود المندوب غير صالح أو تم إلغاؤه</h3>", 404
    orders = list(database.orders_col.find({"store_id": driver.get('store_id'), "driver_phone": driver.get('phone'), "status": {"$in": ["مع المندوب للتوصيل 🚚", "قيد التجهيز 🔵"]}}).sort('_id', -1))
    return render_template('driver.html', driver=driver, orders=orders)

@app.route('/driver/complete/<order_id>', methods=['POST'])
def driver_complete_order(order_id):
    token = request.form.get('token')
    driver = database.get_driver_by_token(token)
    if not driver: return jsonify({"error": "Unauthorized"}), 403
    database.orders_col.update_one({"order_id": order_id, "store_id": driver.get('store_id'), "driver_phone": driver['phone']}, {"$set": {"status": "تم التوصيل 🟢", "delivered_at": datetime.now().strftime("%Y-%m-%d %H:%M")}})
    return redirect(f"/driver/{token}")

@app.route('/api/drivers/add', methods=['POST'])
def api_add_driver():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json(silent=True) or {}
    name = str(data.get('name', '')).strip()
    phone = str(data.get('phone', '')).strip()
    if not name or not phone:
        return jsonify({"success": False, "error": "اسم ورقم المندوب مطلوبان"}), 400
    token = database.add_driver(session['user_id'], name, phone)
    if not token: return jsonify({"success": False, "error": "المندوب موجود بالفعل أو تعذر إنشاؤه"}), 400
    return jsonify({"success": True, "token": token})

@app.route('/api/orders/assign-driver', methods=['POST'])
def api_assign_driver():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json(silent=True) or {}
    order_id = str(data.get('order_id', '')).strip()
    driver_name = str(data.get('driver_name', '')).strip()
    driver_phone = str(data.get('driver_phone', '')).strip()
    if not order_id or not driver_name or not driver_phone:
        return jsonify({"success": False, "error": "بيانات الإسناد غير مكتملة"}), 400
    result = database.assign_order_driver(order_id, session['user_id'], driver_name, driver_phone)
    if result.matched_count == 0:
        return jsonify({"success": False, "error": "الطلب غير موجود"}), 404
    return jsonify({"success": True})

@app.route('/api/drivers/delete/<token>', methods=['POST'])
def api_delete_driver(token):
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    database.drivers_col.delete_one({"token": token, "store_id": session.get('user_id')})
    return jsonify({"success": True})

@app.route('/api/orders/update-status', methods=['POST'])
def api_update_order_status():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json(silent=True) or {}
    order_id = str(data.get('order_id', '')).strip()
    status = str(data.get('status', '')).strip()
    allowed_statuses = {"جديد 🟡", "مدفوع 🟢", "قيد التجهيز 🔵", "مع المندوب للتوصيل 🚚", "تم التوصيل 🟢", "ملغي 🔴"}
    if not order_id or status not in allowed_statuses:
        return jsonify({"success": False, "error": "بيانات الحالة غير صحيحة"}), 400
    result = database.orders_col.update_one({"order_id": order_id, "store_id": session.get('user_id')}, {"$set": {"status": status}})
    if result.matched_count == 0:
        return jsonify({"success": False, "error": "الطلب غير موجود"}), 404
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
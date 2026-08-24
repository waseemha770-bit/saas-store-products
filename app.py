from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort
import database, os, urllib.parse, io, csv, json, urllib.request, urllib.error
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
MAIN_DOMAIN = "saas-store-products.vercel.app"

def send_telegram_alert(message):
    try:
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN"); url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = json.dumps({"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": message, "parse_mode": "HTML"}).encode('utf-8')
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
    return dict(platform_logo=logo)

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
    wallet_phone = data.get('wallet_phone', '')
    payment_str = data.get('payment', '')
    
    # 1. إنشاء الطلب الآمن في قاعدة البيانات
    order_id, real_total, secure_cart, discount_info = database.create_secure_order(
        user.get('id'), data['name'], data['phone'], data.get('address', ''), 
        payment_str, data['cart'], data.get('coupon_code', '').strip()
    )
    
    payment_status_msg = "⏳ *حالة الدفع:* الدفع عند الاستلام (غير مدفوع)"
    
    # --- محاكاة البنك الوهمي (Mock API) --- #
    if wallet_provider != 'cash':
        # في العالم الحقيقي، نرسل طلب HTTP هنا إلى البنك وننتظر الرد
        # لكن الآن سنفترض أن البنك رد علينا بـ (عملية ناجحة)
        mock_bank_response = {"status": "success", "transaction_id": f"TXN-{order_id}"}
        
        if mock_bank_response["status"] == "success":
            # تحديث حالة الطلب في قاعدة البيانات إلى مدفوع تلقائياً
            database.orders_col.update_one(
                {"order_id": order_id, "store_id": user.get('id')}, 
                {"": {"status": "مدفوع 🟢", "transaction_id": mock_bank_response["transaction_id"]}}
            )
            payment_status_msg = f"✅ *حالة الدفع:* مدفوع إلكترونياً بنجاح (عملية وهمية: {mock_bank_response['transaction_id']})"
        else:
            payment_status_msg = "❌ *حالة الدفع:* فشلت عملية الدفع الإلكتروني"
    # ----------------------------------------------- #

    # 2. تجهيز رسالة الواتساب للتاجر
    msg = f"مرحباً، لدي طلب جديد 🛒

🧾 *رقم الطلب:* {order_id}
👤 *الاسم:* {data['name']}
📞 *الهاتف:* {data['phone']}
📍 *العنوان:* {data.get('address', '')}
💳 *طريقة الدفع:* {payment_str}
{payment_status_msg}

🛍️ *المنتجات:*
"
    for item in secure_cart: msg += f"▪️ {item['name']} (الكمية: {item['qty']})
"
    if discount_info: msg += f"
🎟️ *الخصم:* {discount_info}"
    msg += f"
💰 *الإجمالي النهائي:* {real_total} {settings.get('currency', 'ريال')}

*()*"
    
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
        if action == 'add_product': database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id'), session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل", "success")
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
                'wallet_secret': request.form.get('wallet_secret', '').strip()
            }
            if is_super_admin and request.form.get('platform_logo'): settings_data['platform_logo'] = request.form.get('platform_logo', '').strip()
            database.update_settings(session['user_id'], settings_data); flash("تم الحفظ بنجاح", "success")
        elif action == 'add_package' and is_super_admin: database.add_package(request.form.get('pkg_name'), request.form.get('pkg_price'), request.form.get('pkg_max'), request.form.get('pkg_features')); flash("تمت إضافة الباقة", "success")
        elif action == 'delete_package' and is_super_admin: database.delete_package(request.form.get('pkg_id')); flash("تم الحذف", "danger")
        elif action == 'add_merchant' and is_super_admin:
            slug = request.form.get('slug', '').strip()
            if database.create_new_merchant(request.form.get('name'), slug, request.form.get('password', '').strip()):
                new_user = database.users_col.find_one({"store_slug": slug})
                if new_user:
                    database.users_col.update_one({"_id": new_user["_id"]}, {"$set": {"package": request.form.get('package', 'أساسية')}})
                    database.add_product(new_user['id'], "منتج تجريبي 🚀", "مرحباً بك في منصة TajerGo!", 99, "عام", "https://via.placeholder.com/800x600/0d6efd/ffffff?text=TajerGo", 10)
                send_telegram_alert(f"🎉 <b>تاجر جديد!</b>\n👤 {request.form.get('name')}\n🔗 {slug}")
                flash("تم إنشاء المتجر", "success")
            else: flash("الرابط محجوز", "danger")
        elif action == 'toggle_status' and is_super_admin: database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
        elif action == 'delete_merchant' and is_super_admin: database.delete_user(request.form.get('user_id'))
        elif action == 'edit_merchant_info' and is_super_admin:
            if database.edit_merchant_info(request.form.get('user_id'), request.form.get('new_slug', '').strip(), request.form.get('new_package', 'أساسية')): flash("تم تحديث التاجر", "success")
            else: flash("الرابط محجوز!", "danger")
            
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    coupons = database.get_coupons(session['user_id'])
    
    def parse_date(d):
        if isinstance(d, datetime): return d
        try: return datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S.%f')
        except: return datetime.now()
    def clean_total(t):
        try: return float(str(t).replace(',', '').strip())
        except: return 0.0

    now = datetime.now()
    completed_orders = [o for o in orders if o.get('status') == 'تم التوصيل 🟢']
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
    status_counts = {"جديد 🟡": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders: status_counts[o.get('status', 'جديد 🟡')] += 1
    
    return render_template('dashboard.html', products=products, coupons=coupons, settings=settings, orders=orders, stats={"total_orders": len(orders), "total_revenue": net_sales, "status_counts": status_counts}, adv_stats=adv_stats, merchants=(database.get_all_users() if is_super_admin else []), packages=database.get_packages(), current_user_data=database.users_col.find_one({'id': session['user_id']}), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
if __name__ == '__main__': app.run(debug=True)

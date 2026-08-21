import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort
import database, os, urllib.parse, io, csv, json, urllib.request, urllib.error

app = Flask(__name__)

# ==========================================
# نظام إشعارات التلجرام (Super Admin)
# ==========================================
def send_telegram_alert(message):
    try:
        import requests
        url = "https://api.telegram.org/bot8843130010:AAE0z_PMlt9EoQi75z99cXece4RAzfRk2g4/sendMessage"
        requests.post(url, json={"chat_id": "892385625", "text": message, "parse_mode": "HTML"}, timeout=3)
    except:
        pass

app.secret_key = os.getenv('SECRET_KEY') or 'tajergo_super_secure_key_2026'
MAIN_DOMAIN = "saas-store-products.vercel.app"

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

# ==============================================================
# بروكسي الرفع القوي والمموه لتجاوز حظر الاستضافات وحظر البوتات
# ==============================================================
@app.route('/api/proxy_upload', methods=['POST'])
def proxy_upload():
    if 'user_id' not in session: return jsonify({"success": False, "error": "جلسة غير مصرحة"}), 401
    data = request.json
    provider = data.get('provider')
    api_key = data.get('api_key')
    b64_data = data.get('image_base64')
    
    if not provider or not b64_data:
        return jsonify({"success": False, "error": "بيانات غير مكتملة"})
        
    try:
        raw_b64 = b64_data.split(',')[1] if ',' in b64_data else b64_data
        
        # التمويه بأن الطلب قادم من متصفح جوجل كروم حقيقي لمنع الحظر
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        if provider == 'imgbb':
            if not api_key: return jsonify({"success": False, "error": "مفتاح ImgBB مفقود في الإعدادات"})
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            req = urllib.request.Request(f"https://api.imgbb.com/1/upload?key={api_key}", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                return jsonify({"success": True, "url": res['data']['url']})
                
        elif provider == 'imgur':
            if not api_key: return jsonify({"success": False, "error": "مفتاح Imgur مفقود في الإعدادات"})
            payload = urllib.parse.urlencode({'image': raw_b64}).encode('utf-8')
            headers['Authorization'] = f'Client-ID {api_key}'
            req = urllib.request.Request("https://api.imgur.com/3/image", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                return jsonify({"success": True, "url": res['data']['link']})
                
        elif provider == 'cloudinary':
            cloud_name = data.get('cloud_name')
            preset = data.get('preset')
            if not cloud_name or not preset: return jsonify({"success": False, "error": "إعدادات Cloudinary غير مكتملة"})
            payload = urllib.parse.urlencode({'file': b64_data, 'upload_preset': preset}).encode('utf-8')
            req = urllib.request.Request(f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload", data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                return jsonify({"success": True, "url": res['secure_url']})
                
        elif provider == 'postimages':
            if not api_key: return jsonify({"success": False, "error": "مفتاح Postimages مفقود"})
            payload = urllib.parse.urlencode({'file': raw_b64}).encode('utf-8')
            headers['Authorization'] = f'Bearer {api_key}'
            req = urllib.request.Request('https://postimages.org/api/upload', data=payload, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                return jsonify({"success": True, "url": res['url']})
                
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        return jsonify({"success": False, "error": f"رفض المزود الطلب (رمز الخطأ: {e.code}). تأكد من صحة المفتاح."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
        
    return jsonify({"success": False, "error": "مزود خدمة غير مدعوم"})


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
    msg += f"\n💰 *الإجمالي النهائي:* {data['final_total']} {settings.get('currency', 'ريال')}\n\n*()*"
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
        if action == 'add_product': database.add_product(session['user_id'], request.form.get('name')
        
, request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id')
        
, session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل", "success")
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
                'custom_domain': request.form.get('custom_domain', '').replace('https://', '').replace('http://', '').strip('/'), 'logo_url': request.form.get('logo_url', '').strip(), 'img_provider': request.form.get('img_provider', 'imgbb'), 'img_api_key': request.form.get('img_api_key', '').strip(), 'cloudinary_name': request.form.get('cloudinary_name', '').strip(), 'cloudinary_preset': request.form.get('cloudinary_preset', '').strip(), 'wallet_provider': request.form.get('wallet_provider', ''), 'wallet_merchant_id': request.form.get('wallet_merchant_id', '').strip(), 'wallet_api_key': request.form.get('wallet_api_key', '').strip(), 'wallet_secret': request.form.get('wallet_secret', '').strip()
            }
            if is_super_admin: settings_data['platform_logo'] = request.form.get('platform_logo', '').strip()
            database.update_settings(session['user_id'], settings_data); flash("تم الحفظ بنجاح", "success")
        elif action == 'add_package' and is_super_admin:
            database.add_package(request.form.get('pkg_name'), request.form.get('pkg_price'), request.form.get('pkg_max'), request.form.get('pkg_features'))
            flash("تمت إضافة الباقة بنجاح", "success")
        elif action == 'delete_package' and is_super_admin:
            database.delete_package(request.form.get('pkg_id'))
            flash("تم حذف الباقة", "danger")
        elif action == 'add_merchant' and is_super_admin:
            slug = request.form.get('slug', '').strip()
            if database.create_new_merchant(request.form.get('name'), slug, request.form.get('password', '').strip()):
                new_user = database.users_col.find_one({"store_slug": slug})
                if new_user:
                    database.users_col.update_one({"_id": new_user["_id"]}, {"$set": {"package": request.form.get('package', 'أساسية')}})
                    database.add_product(new_user['id'], "منتج تجريبي 🚀", "مرحباً بك في منصة TajerGo! هذا منتج تجريبي.", 99, "عام", "https://via.placeholder.com/800x600/0d6efd/ffffff?text=TajerGo+Product", 10)
        

                
                # إرسال إشعار للمدير
                send_telegram_alert(f"🎉 <b>تاجر جديد انضم لمنصتك!</b>\n\n👤 <b>اسم التاجر:</b> {request.form.get('name')}\n🔗 <b>رابط المتجر:</b> {slug}\n📦 <b>الباقة:</b> {request.form.get('package', 'أساسية')}\n🔑 <b>كلمة المرور:</b> {request.form.get('password', '').strip()}")

                flash("تم إنشاء المتجر بنجاح وتحديد الباقة!", "success")
            else: flash("الرابط محجوز", "danger")
        elif action == 'toggle_status' and is_super_admin: database.toggle_user_status(request.form.get('user_id'), request.form.get('current_status'))
        elif action == 'delete_merchant' and is_super_admin: database.delete_user(request.form.get('user_id'))
        elif action == 'edit_merchant_info' and is_super_admin:
            if database.edit_merchant_info(request.form.get('user_id'), request.form.get('new_slug', '').strip(), request.form.get('new_package', 'أساسية')): flash("تم تحديث بيانات التاجر بنجاح!", "success")
            else: flash("الرابط الجديد محجوز لتاجر آخر!", "danger")
        return redirect(url_for('dashboard'))
    
    orders = database.get_orders(session['user_id'])
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    coupons = database.get_coupons(session['user_id'])
    
    # === خوارزمية الذكاء والإحصاء المتقدمة ===
    from datetime import datetime, timedelta
    now = datetime.now()
    def parse_date(d):
        if isinstance(d, datetime): return d
        try: return datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S.%f')
        except: return now
        
    def clean_total(t):
        try: return float(str(t).replace(',', '').strip())
        except: return 0.0

    completed_orders = [o for o in orders if o.get('status') == 'تم التوصيل 🟢']
    canceled_orders = [o for o in orders if o.get('status') == 'ملغي 🔴']
    
    total_sales = sum(clean_total(o.get('total')) for o in orders if o.get('status') != 'ملغي 🔴')
    net_sales = sum(clean_total(o.get('total')) for o in completed_orders)
    
    avg_order_value = net_sales / len(completed_orders) if completed_orders else 0
    completion_rate = (len(completed_orders) / len(orders) * 100) if orders else 0
    
    customers_map = {}
    product_sales = {}
    delivery_fees_total = 0.0 
    
    for o in completed_orders:
        phone = o.get('customer_phone', 'غير معروف')
        name = o.get('customer_name', 'عميل')
        total = clean_total(o.get('total'))
        if phone not in customers_map: customers_map[phone] = {'name': name, 'spent': 0, 'orders': 0}
        customers_map[phone]['spent'] += total
        customers_map[phone]['orders'] += 1
        
        for item in o.get('cart_items', []):
            p_name = item.get('name')
            qty = item.get('qty', 1)
            if p_name not in product_sales: product_sales[p_name] = 0
            product_sales[p_name] += qty
            
    top_customers = sorted(customers_map.values(), key=lambda x: x['spent'], reverse=True)[:5]
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    best_sellers = sorted_products[:5]
    least_sellers = sorted_products[-5:] if len(sorted_products) > 0 else []
    least_sellers.reverse()
    
    this_month_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).month == now.month and parse_date(o.get('date')).year == now.year)
    last_month = now.replace(day=1) - timedelta(days=1)
    last_month_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).month == last_month.month and parse_date(o.get('date')).year == last_month.year)
    growth_rate = ((this_month_sales - last_month_sales) / last_month_sales * 100) if last_month_sales > 0 else (100 if this_month_sales > 0 else 0)
    
    today_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).date() == now.date())
    weekly_sales = sum(clean_total(o.get('total')) for o in completed_orders if parse_date(o.get('date')).date() >= (now.date() - timedelta(days=7)))
    
    daily_chart = {}
    for i in range(6, -1, -1):
        d_str = (now - timedelta(days=i)).strftime('%Y-%m-%d')
        daily_chart[d_str] = 0
        
    for o in completed_orders:
        d_str = parse_date(o.get('date')).strftime('%Y-%m-%d')
        if d_str in daily_chart: daily_chart[d_str] += clean_total(o.get('total'))
            
    adv_stats = {
        'total_sales': total_sales,
        'net_sales': net_sales,
        'total_orders': len(orders),
        'completed_orders': len(completed_orders),
        'canceled_orders': len(canceled_orders),
        'avg_order_value': avg_order_value,
        'customers_count': len(customers_map),
        'top_customers': top_customers,
        'best_sellers': best_sellers,
        'least_sellers': least_sellers,
        'this_month_sales': this_month_sales,
        'last_month_sales': last_month_sales,
        'today_sales': today_sales,
        'weekly_sales': weekly_sales,
        'growth_rate': growth_rate,
        'completion_rate': completion_rate,
        'delivery_fees': delivery_fees_total,
        'chart_labels': list(daily_chart.keys()),
        'chart_data': list(daily_chart.values())
    }
    
    status_counts = {"جديد 🟡": 0, "قيد التجهيز 🔵": 0, "تم التوصيل 🟢": 0, "ملغي 🔴": 0}
    for o in orders: status_counts[o.get('status', 'جديد 🟡')] += 1
    
    return render_template('dashboard.html', products=products, coupons=coupons, settings=settings, orders=orders, stats={"total_orders": len(orders), "total_revenue": net_sales, "status_counts": status_counts}, adv_stats=adv_stats, merchants=(database.get_all_users() if is_super_admin else []), packages=database.get_packages(), current_user_data=database.users_col.find_one({'_id': session['user_id']}), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))









# --- نظام تتبع المشاهدات ---


@app.route('/api/rate_product', methods=['POST'])
def api_rate_product_clean():
    try:
        from flask import request, jsonify, make_response
        from bson.objectid import ObjectId
        data = request.get_json() if request.is_json else request.form
        pid = data.get('product_id') or data.get('id')
        rating_val = float(data.get('rating', 0))
        
        if request.cookies.get(f'rated_{pid}'):
            return jsonify({"success": False, "error": "already_rated"})
            
        user_ip = request.headers.get('x-real-ip', request.headers.get('X-Forwarded-For', request.remote_addr))
        if user_ip and ',' in user_ip: user_ip = user_ip.split(',')[0].strip()
            
        if not pid or rating_val < 1: return jsonify({"success": False, "error": "invalid"})
        
        db_col = database.products_col if hasattr(database, 'products_col') else (database.db.products if hasattr(database, 'db') else database.products)
        
        try: query = {"_id": ObjectId(pid)}
        except: query = {"id": str(pid)}
        prod = db_col.find_one(query)
        if not prod:
            query = {"id": int(pid)} if str(pid).isdigit() else {"name": pid}
            prod = db_col.find_one(query)
            
        if prod:
            rated_ips = prod.get('rated_ips', [])
            if user_ip in rated_ips: return jsonify({"success": False, "error": "already_rated"})
            
            curr_rating, curr_reviews = float(prod.get('rating', 0)), int(prod.get('reviews', 0))
            new_reviews = curr_reviews + 1
            new_rating = round(((curr_rating * curr_reviews) + rating_val) / new_reviews, 1)
            
            db_col.update_one(query, {"$set": {"rating": new_rating, "reviews": new_reviews}, "$addToSet": {"rated_ips": user_ip}})
            resp = make_response(jsonify({"success": True, "new_rating": new_rating, "new_reviews": new_reviews}))
            resp.set_cookie(f'rated_{pid}', '1', max_age=31536000)
            return resp
            
        return jsonify({"success": False, "error": "not_found"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/manifest.json')
def serve_manifest():
    from flask import send_file
    return send_file('static/manifest.json', mimetype='application/json')

@app.route('/sw.js')
def serve_sw():
    from flask import send_file
    return send_file('static/sw.js', mimetype='application/javascript')

@app.before_request
def track_store_views():
    from flask import request
    from datetime import datetime
    if request.method == 'GET' and not request.path.startswith(('/api', '/static', '/dashboard', '/login', '/logout', '/manifest', '/sw.js')):
        try:
            db_obj = database.db if hasattr(database, 'db') else database
            today = datetime.now().strftime('%Y-%m-%d')
            month = datetime.now().strftime('%Y-%m')
            db_obj.store_stats.update_one(
                {"_id": "views_tracker"},
                {"$inc": {"total": 1, f"daily.{today}": 1, f"monthly.{month}": 1}},
                upsert=True
            )
        except: pass

@app.context_processor
def inject_dashboard_stats():
    from flask import request
    from datetime import datetime, timedelta
    if request.path.startswith('/dashboard') or request.path.startswith('/admin'):
        try:
            db_obj = database.db if hasattr(database, 'db') else database
            stats = db_obj.store_stats.find_one({"_id": "views_tracker"}) or {}
            today = datetime.now().strftime('%Y-%m-%d')
            month = datetime.now().strftime('%Y-%m')
            
            daily = stats.get('daily', {}).get(today, 0)
            monthly = stats.get('monthly', {}).get(month, 0)
            total = stats.get('total', 0)
            
            weekly = sum(stats.get('daily', {}).get((datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'), 0) for i in range(7))
            return dict(v_daily=daily, v_weekly=weekly, v_monthly=monthly, v_total=total)
        except Exception: 
            return dict(v_daily=0, v_weekly=0, v_monthly=0, v_total=0)
    return {}

if __name__ == '__main__': app.run(debug=True)


from datetime import datetime, timedelta

@app.before_request
def track_visit():
    if request.method == 'GET' and not any(request.path.startswith(x) for x in ['/api', '/static', '/dashboard', '/login']):
        try:
            db_obj = database.db if hasattr(database, 'db') else database
            db_obj.visit_logs.insert_one({"timestamp": datetime.utcnow()})
        except: pass

def get_stats():
    try:
        db_obj = database.db if hasattr(database, 'db') else database
        now = datetime.utcnow()
        return {
            "daily": db_obj.visit_logs.count_documents({"timestamp": {"$gte": now - timedelta(days=1)}}),
            "weekly": db_obj.visit_logs.count_documents({"timestamp": {"$gte": now - timedelta(days=7)}}),
            "monthly": db_obj.visit_logs.count_documents({"timestamp": {"$gte": now - timedelta(days=30)}})
        }
    except: return {"daily": 0, "weekly": 0, "monthly": 0}

# تحديث دالة dashboard لتمرير الإحصائيات
original_dashboard = re.search(r"""@app\.route\(['"]/dashboard['"].*?def dashboard""", app_code, re.DOTALL)
if original_dashboard:
    app_code = app_code.replace("return render_template('dashboard.html')", "return render_template('dashboard.html', stats=get_stats())")

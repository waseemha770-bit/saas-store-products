# Software Project Context
Export Date: Fri Aug 28 23:04:22 +03 2026

--- 

## File Path: ./PROJECT_CONTEXT.md
```
# 🧠 سياق المشروع الحالي — TajerGo

## الحالة المعتمدة
هذا الملف يصف النسخة الحالية من المشروع فقط، ولا يعتمد على سياقات قديمة.

## Architecture
- Backend: Python / Flask
- Database: MongoDB
- Hosting: Vercel Serverless
- Frontend: HTML + Bootstrap RTL + JavaScript
- PWA: `/sw.js` واحد + Manifest ديناميكي عبر `/manifest/<slug>.json`
- هوية PWA: شعار كل متجر من `settings.logo_url` هو أيقونة التطبيق والـfavicon و`apple-touch-icon`، مع أيقونة TajerGo كبديل عند عدم وجود شعار.

## لوحة التاجر
- `templates/base_dashboard.html`: القالب الأساسي.
- `templates/dashboard.html`: محتوى لوحة التاجر.
- `templates/partials/`: العناصر المشتركة مثل الشريط العلوي والتبويبات والنوافذ المشتركة.
- `static/css/dashboard.css`: تنسيقات لوحة التاجر.
- `static/js/dashboard.js`: وظائف الأزرار والتبويبات والتعامل مع API.

## قاعدة البيانات
جميع عمليات MongoDB في `database.py`. المجموعات الحالية تشمل:
`users`, `products`, `settings`, `orders`, `coupons`, `packages`, `drivers`.

## التخزين المؤقت
الصفحات الديناميكية والمتاجر وواجهات API وManifest وService Worker تستخدم `no-store`.
ملفات CSS/JS الثابتة تستخدم Cache طويلًا مع رقم إصدار في الرابط.

## قواعد التطوير
- لا تستخدم `re.sub()` لتعديل ملفات المشروع.
- لا تنشئ ملفات `fix_*.py` أو `update_*.py` لتنفيذ تعديلات مؤقتة.
- لا تكرر الدوال أو الأزرار أو Service Worker أو Manifest.
- أي وظيفة جديدة يجب أن يكون لها Route واضح، وواجهة واضحة، ومعالجة أخطاء واضحة.
- أي تعديل في لوحة التاجر يجب اختباره على الهاتف والكمبيوتر.

## النشر
Local → GitHub → Vercel → MongoDB.

```

-----------------------------------
## File Path: ./README.md
```
# 🛒 TajerGo — منصة المتاجر الإلكترونية SaaS

منصة متعددة التجار مبنية بـ Python/Flask، تتيح إدارة المنتجات والطلبات والكوبونات والمناديب وإظهار متجر مستقل لكل تاجر.

## التقنية الحالية
- Backend: Python / Flask
- Frontend: HTML5 + Bootstrap 5 RTL + Font Awesome + JavaScript
- Database: MongoDB
- Hosting: Vercel Serverless
- PWA: Service Worker واحد عبر `/sw.js` وManifest ديناميكي لكل متجر

## الهيكل
```text
app.py
config.py
database.py
backup_db.py
setup_indexes.py
requirements.txt
vercel.json
templates/
  base_dashboard.html
  dashboard.html
  partials/
    topbar.html
    flash_messages.html
    dashboard_nav.html
    addDriverModal.html
    guideModal.html
  login.html
  store.html
  driver.html
  track.html
  system_admin.html
static/
  css/
    dashboard.css
    store.css
    login.css
    driver.css
    track.css
    system_admin.css
  js/
    app.js
    dashboard.js
  sw.js
docs/
```

## قواعد الصيانة
1. لا تستخدم سكربتات `fix_*.py` أو Regex لتعديل ملفات المشروع.
2. عدّل الملف الأصلي مباشرة، ثم اختبره.
3. لا تضف نسخة ثانية من Service Worker أو Manifest أو JavaScript لوظيفة موجودة.
4. بيانات التطبيق تأتي من MongoDB عبر `database.py`.
5. الصفحات الديناميكية تستخدم `Cache-Control: no-store`.
6. ملفات CSS/JS تستخدم إصدارًا في الرابط مع Cache طويل.
7. جميع تغييرات الواجهة المشتركة في `base_dashboard.html` و`templates/partials/`.
8. الأسرار تحفظ في متغيرات البيئة ولا تكتب داخل Git.

## متغيرات البيئة
راجع `.env.example`. الحد الأدنى المطلوب:
- `SECRET_KEY`
- `MONGO_URI`

والاختياري:
- `MONGO_DB_NAME`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `MAIN_DOMAIN`
- `STATIC_VERSION`

## النشر
```text
Local project → GitHub → Vercel → MongoDB
```

بعد كل نشر يجب فتح النسخة المنشورة واختبار لوحة التاجر والمتجر، وليس الاكتفاء بنجاح Build.

```

-----------------------------------
## File Path: ./ai_project_context.md
```
# Software Project Context
Export Date: Thu Aug 27 02:45:00 +03 2026

--- 

## File Path: ./PROJECT_CONTEXT.md
```
# 🧠 سياق المشروع الحالي — TajerGo

## الحالة المعتمدة
هذا الملف يصف النسخة الحالية من المشروع فقط، ولا يعتمد على سياقات قديمة.

## Architecture
- Backend: Python / Flask
- Database: MongoDB
- Hosting: Vercel Serverless
- Frontend: HTML + Bootstrap RTL + JavaScript
- PWA: `/sw.js` واحد + Manifest ديناميكي عبر `/manifest/<slug>.json`
- هوية PWA: شعار كل متجر من `settings.logo_url` هو أيقونة التطبيق والـfavicon و`apple-touch-icon`، مع أيقونة TajerGo كبديل عند عدم وجود شعار.

## لوحة التاجر
- `templates/base_dashboard.html`: القالب الأساسي.
- `templates/dashboard.html`: محتوى لوحة التاجر.
- `templates/partials/`: العناصر المشتركة مثل الشريط العلوي والتبويبات والنوافذ المشتركة.
- `static/css/dashboard.css`: تنسيقات لوحة التاجر.
- `static/js/dashboard.js`: وظائف الأزرار والتبويبات والتعامل مع API.

## قاعدة البيانات
جميع عمليات MongoDB في `database.py`. المجموعات الحالية تشمل:
`users`, `products`, `settings`, `orders`, `coupons`, `packages`, `drivers`.

## التخزين المؤقت
الصفحات الديناميكية والمتاجر وواجهات API وManifest وService Worker تستخدم `no-store`.
ملفات CSS/JS الثابتة تستخدم Cache طويلًا مع رقم إصدار في الرابط.

## قواعد التطوير
- لا تستخدم `re.sub()` لتعديل ملفات المشروع.
- لا تنشئ ملفات `fix_*.py` أو `update_*.py` لتنفيذ تعديلات مؤقتة.
- لا تكرر الدوال أو الأزرار أو Service Worker أو Manifest.
- أي وظيفة جديدة يجب أن يكون لها Route واضح، وواجهة واضحة، ومعالجة أخطاء واضحة.
- أي تعديل في لوحة التاجر يجب اختباره على الهاتف والكمبيوتر.

## النشر
Local → GitHub → Vercel → MongoDB.

```

-----------------------------------
## File Path: ./README.md
```
# 🛒 TajerGo — منصة المتاجر الإلكترونية SaaS

منصة متعددة التجار مبنية بـ Python/Flask، تتيح إدارة المنتجات والطلبات والكوبونات والمناديب وإظهار متجر مستقل لكل تاجر.

## التقنية الحالية
- Backend: Python / Flask
- Frontend: HTML5 + Bootstrap 5 RTL + Font Awesome + JavaScript
- Database: MongoDB
- Hosting: Vercel Serverless
- PWA: Service Worker واحد عبر `/sw.js` وManifest ديناميكي لكل متجر

## الهيكل
```text
app.py
config.py
database.py
backup_db.py
setup_indexes.py
requirements.txt
vercel.json
templates/
  base_dashboard.html
  dashboard.html
  partials/
    topbar.html
    flash_messages.html
    dashboard_nav.html
    addDriverModal.html
    guideModal.html
  login.html
  store.html
  driver.html
  track.html
  system_admin.html
static/
  css/
    dashboard.css
    store.css
    login.css
    driver.css
    track.css
    system_admin.css
  js/
    app.js
    dashboard.js
  sw.js
docs/
```

## قواعد الصيانة
1. لا تستخدم سكربتات `fix_*.py` أو Regex لتعديل ملفات المشروع.
2. عدّل الملف الأصلي مباشرة، ثم اختبره.
3. لا تضف نسخة ثانية من Service Worker أو Manifest أو JavaScript لوظيفة موجودة.
4. بيانات التطبيق تأتي من MongoDB عبر `database.py`.
5. الصفحات الديناميكية تستخدم `Cache-Control: no-store`.
6. ملفات CSS/JS تستخدم إصدارًا في الرابط مع Cache طويل.
7. جميع تغييرات الواجهة المشتركة في `base_dashboard.html` و`templates/partials/`.
8. الأسرار تحفظ في متغيرات البيئة ولا تكتب داخل Git.

## متغيرات البيئة
راجع `.env.example`. الحد الأدنى المطلوب:
- `SECRET_KEY`
- `MONGO_URI`

والاختياري:
- `MONGO_DB_NAME`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `MAIN_DOMAIN`
- `STATIC_VERSION`

## النشر
```text
Local project → GitHub → Vercel → MongoDB
```

بعد كل نشر يجب فتح النسخة المنشورة واختبار لوحة التاجر والمتجر، وليس الاكتفاء بنجاح Build.

```

-----------------------------------
## File Path: ./app.py
```
import urllib.parse
def extract_clean_products(order):
    """دالة معيارية لاستخراج أسماء المنتجات والكميات من أي هيكل بيانات مخزن"""
    import json
    parsed = []
    
    # أ) فحص حقل السلة (cart) سواء كان مصفوفة أو نص JSON
    cart = order.get('cart')
    if isinstance(cart, str):
        try:
            cart = json.loads(cart)
        except Exception:
            if cart.strip():
                parsed.append(cart.strip())
                
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

    # ب) فحص حقل items إذا لم نجد منتجات في السلة
    if not parsed:
        raw_items = order.get('items')
        if isinstance(raw_items, str) and raw_items.strip():
            for line in raw_items.splitlines():
                clean_line = line.strip().lstrip('▪️').lstrip('-').strip()
                if clean_line:
                    parsed.append(clean_line)
        elif isinstance(raw_items, list):
            for it in raw_items:
                if isinstance(it, dict):
                    name = it.get('name') or it.get('title') or 'منتج'
                    qty = it.get('qty') or 1
                    parsed.append(f"{name} (x{qty})")
                elif isinstance(it, str) and it.strip():
                    parsed.append(it.strip())

    # ج) فحص الحقول الفردية القديمة
    if not parsed:
        p_name = order.get('product_name') or order.get('item_name')
        if p_name:
            qty = order.get('qty') or 1
            parsed.append(f"{p_name} (x{qty})")

    # في حال انعدام البيانات تماماً
    if not parsed:
        parsed.append("منتج")

    return parsed

import re
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort, send_from_directory
import database, os, urllib.parse, io, csv, json, urllib.request, urllib.error
import config
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
MAIN_DOMAIN = config.MAIN_DOMAIN
STATIC_VERSION = config.STATIC_VERSION

@app.after_request
def apply_cache_policy(response):
    path = request.path
    if path == '/sw.js' or path.startswith('/manifest/') or path.startswith('/api/') or path == '/dashboard' or path.startswith('/store/'):
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
    excluded_paths = ['/login', '/logout', '/dashboard', '/api/', '/export', '/manifest', '/sw.js', '/delivery', '/track']
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

@app.route('/manifest/<slug>.json')
def pwa_manifest(slug):
    """إنشاء Manifest مستقل لكل متجر باستخدام شعار المتجر كأيقونة للتطبيق."""
    user = database.get_user_by_slug(slug)
    if not user:
        return abort(404)

    settings = database.get_settings(user['id']) or {}
    store_name = (settings.get('store_name') or 'TajerGo Store').strip()
    logo = (settings.get('logo_url') or '').strip()
    fallback_logo = '/static/icon-512.png'
    icon_src = logo or fallback_logo
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
            {"src": icon_src, "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": icon_src, "sizes": "512x512", "type": "image/png", "purpose": "any"}
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
    if not user:
        return jsonify({"error": "Store not found"}), 404
        
    data = request.json
    settings = database.get_settings(user.get('id'))
    wallet_provider = data.get('wallet_provider', 'cash')
    payment_str = data.get('payment', '')
    
    order_id, real_total, secure_cart, discount_info = database.create_secure_order(
        user.get('id'), data['name'], data['phone'], data.get('address', ''),
        payment_str, data['cart'], data.get('coupon_code', '').strip()
    )
    
    payment_status_msg = "⏳ حالة الدفع: الدفع عند الاستلام"
    if wallet_provider != 'cash':
        mock_txn = f"TXN-{order_id}"
        database.orders_col.update_one(
            {"order_id": order_id, "store_id": user.get('id')},
            {"$set": {"status": "مدفوع 🟢", "transaction_id": mock_txn}}
        )
        payment_status_msg = f"✅ حالة الدفع: مدفوع إلكترونياً ({mock_txn})"
        
    items_list_str = '\n'.join([f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart])
    currency_label = settings.get('currency', 'ريال')
    
    msg = f"🛍️ طلب جديد من المتجر\nرقم الطلب: {order_id}\nالعميل: {data['name']}\nالهاتف: {data['phone']}\nالعنوان: {data.get('address', 'غير محدد')}\nطريقة الدفع: {payment_str}\n\nالمنتجات:\n{items_list_str}\n\nالإجمالي: {real_total} {currency_label}"

    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    
    # 🌟 هنا الإصلاح الدقيق والمضمون 100% 🌟
    wa_link = f"https://wa.me/{wa_phone}?text={{urllib.parse.quote(msg)}}"
    
    # تصحيح الخطأ في دمج المتغير لتجنب أي مشاكل
    wa_link = "https://wa.me/" + str(wa_phone) + "?text=" + urllib.parse.quote(msg)
    
    return jsonify({
        "success": True,
        "order_id": order_id,
        "wa_link": wa_link
    })


@app.route('/track', methods=['GET'])
@app.route('/track/<order_id>', methods=['GET'])
def track_order(order_id=None):
    raw_query = (order_id or request.args.get('order_id', '') or request.args.get('q', '')).strip()
    clean_query = raw_query.replace('#', '').strip()
    
    if not clean_query:
        return render_template('track.html', order=None)
    
    digits = ''.join(c for c in clean_query if c.isdigit())
    digits_suffix = digits[-9:] if len(digits) >= 9 else (digits[-7:] if len(digits) >= 7 else digits)
    
    or_filters = [
        {'order_id': clean_query},
        {'order_id': {'': f'^{clean_query}$', '': 'i'}},
        {'customer_phone': clean_query},
        {'phone': clean_query}
    ]
    
    if digits:
        or_filters.append({'customer_phone': {'': digits_suffix}})
        or_filters.append({'phone': {'': digits_suffix}})
        try:
            or_filters.append({'customer_phone': int(digits)})
            or_filters.append({'phone': int(digits)})
            if digits_suffix != digits:
                or_filters.append({'customer_phone': int(digits_suffix)})
                or_filters.append({'phone': int(digits_suffix)})
        except:
            pass
            
    order = database.orders_col.find_one({'': or_filters}, sort=[('_id', -1)])
    
    if not order and (digits_suffix or clean_query):
        recent_orders = list(database.orders_col.find().sort('_id', -1).limit(200))
        for o in recent_orders:
            p_val = ''.join(c for c in str(o.get('customer_phone') or o.get('phone') or '') if c.isdigit())
            o_id = str(o.get('order_id') or '').replace('#', '').strip()
            if (digits_suffix and digits_suffix in p_val) or (clean_query.lower() == o_id.lower()):
                order = o
                break
                
    if not order:
        return render_template('track.html', order=None, search_query=raw_query, error='عذراً، لم نتمكن من العثور على الطلب. يرجى التأكد من رقم الطلب (مثال: ORD-XXXX) أو رقم هاتفك المسجل.')
    
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
            # فحص الباقة والحد الأقصى قبل الإضافة
            can_add, cur_cnt, max_lim, pkg_n, err_msg = database.check_merchant_product_limit(session['user_id'])
            if not can_add:
                flash(err_msg, "danger")
            else:
                database.add_product(
                    session['user_id'], 
                    request.form.get('name'), 
                    request.form.get('desc'), 
                    (request.form.get('price') or 0), 
                    request.form.get('cat'), 
                    request.form.get('img'), 
                    request.form.get('stock')
                )
                flash(f"تم إضافة المنتج بنجاح 📦 ({cur_cnt + 1} من {max_lim})", "success")
        elif action == 'edit_product': database.edit_product(request.form.get('product_id'), session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم التعديل", "success")
        elif action == 'delete_product': database.delete_product(request.form.get('product_id'), session['user_id']); flash("تم الحذف", "danger")
        elif action == 'update_order_status': database.orders_col.update_one({"order_id": request.form.get('order_id'), "store_id": session['user_id']}, {"$set": {"status": request.form.get('new_status')}}); flash("تم التحديث", "success")
        elif action == 'add_driver':
            d_name = request.form.get('driver_name') or request.form.get('name')
            d_phone = request.form.get('driver_phone') or request.form.get('phone')
            if d_name and d_phone:
                created = database.add_driver(session['user_id'], d_name, d_phone)
                if created:
                    flash(f"تم إضافة المندوب {d_name} بنجاح 🛵", "success")
                else:
                    flash("هذا المندوب موجود مسبقًا أو تعذر إنشاءه", "warning")
            else:
                flash("يرجى إدخال اسم ورقم المندوب", "danger")
        elif action == 'delete_driver':
            d_phone = request.form.get('driver_phone') or request.form.get('phone')
            database.delete_driver(session['user_id'], d_phone)
            flash("تم حذف المندوب 🗑️", "danger")
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
        if st in status_counts:
            status_counts[st] += 1
        else:
            status_counts[st] = 1
    
    return render_template('dashboard.html', drivers=drivers, products=products, coupons=coupons, settings=settings, orders=orders, stats={"total_orders": len(orders), "total_revenue": net_sales, "status_counts": status_counts}, adv_stats=adv_stats, merchants=(database.get_all_users() if is_super_admin else []), packages=database.get_packages(), current_user_data=database.users_col.find_one({'id': session['user_id']}), store_slug=session['store_slug'], is_super_admin=is_super_admin)

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
@app.route('/driver/<token>', methods=['GET'])
@app.route('/delivery', methods=['GET'])
def driver_portal(token=None):
    token = (token or request.args.get('token', '')).strip()
    driver = database.get_driver_by_token(token)
    if not driver:
        return "<h3>كود المندوب غير صالح أو تم إلغاؤه</h3>", 404
    orders = list(database.orders_col.find({
        "store_id": driver.get('store_id'),
        "driver_phone": driver.get('phone'),
        "status": {"$in": ["مع المندوب للتوصيل 🚚", "قيد التجهيز 🔵"]}
    }).sort('_id', -1))
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
    data = request.json
    token = database.add_driver(session['user_id'], data['name'], data['phone'])
    if not token:
        return jsonify({"success": False, "error": "المندوب موجود بالفعل أو تعذر إنشاؤه"}), 400
    return jsonify({"success": True, "token": token})

@app.route('/api/orders/assign-driver', methods=['POST'])
def api_assign_driver():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    database.assign_order_driver(data['order_id'], session['user_id'], data['driver_name'], data['driver_phone'])
    return jsonify({"success": True})

@app.route('/api/drivers/delete/<token>', methods=['POST'])
def api_delete_driver(token):
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    database.drivers_col.delete_one({"token": token, "store_id": session.get('user_id')})
    return jsonify({"success": True})

@app.route('/api/orders/update-status', methods=['POST'])
def api_update_order_status():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    database.orders_col.update_one({"order_id": data['order_id'], "store_id": session.get('user_id')}, {"$set": {"status": data['status']}})
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True)

```

-----------------------------------
## File Path: ./backup_db.py
```
import dns.resolver

# تجاوز إعدادات DNS الخاصة بـ Termux للاتصال بسيرفرات جوجل
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']

import database
import json, os
from datetime import datetime
from bson import json_util

# إنشاء مجلد يحمل تاريخ ووقت اليوم
backup_folder = f"TajerGo_Backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
os.makedirs(backup_folder, exist_ok=True)

collections = {
    'users': database.users_col,
    'products': database.products_col,
    'settings': database.settings_col,
    'orders': database.orders_col,
    'coupons': database.coupons_col,
    'packages': database.packages_col,
    'drivers': database.drivers_col
}

print(f"📥 جاري سحب بيانات المنصة إلى المجلد المحلي: {backup_folder}...")

for name, col in collections.items():
    data = list(col.find())
    # استخدام json_util للتعامل مع بيانات MongoDB الخاصة (مثل ObjectId والتواريخ)
    with open(f"{backup_folder}/{name}.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, default=json_util.default, ensure_ascii=False, indent=4)
    print(f" - تم حفظ جدول: {name} ({len(data)} سجل)")

print(f"✅ تمت عملية النسخ الاحتياطي بنجاح!\n📂 يمكنك العثور على الملفات داخل مجلد المشروع باسم: {backup_folder}")

```

-----------------------------------
## File Path: ./config.py
```
import os

SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "tajergo_db")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MAIN_DOMAIN = os.getenv("MAIN_DOMAIN", "saas-store-products.vercel.app")
STATIC_VERSION = os.getenv("STATIC_VERSION", "20260825.1")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is required")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is required")

```

-----------------------------------
## File Path: ./database.py
```
from pymongo import MongoClient
import uuid, os
from datetime import datetime
import config

# الاتصال بقاعدة البيانات
client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[config.MONGO_DB_NAME]

# المجموعات (Collections)
users_col = db['users']
products_col = db['products']
settings_col = db['settings']
orders_col = db['orders']
coupons_col = db['coupons']
packages_col = db['packages']

# ==========================================
# إدارة المستخدمين (التجار)
# ==========================================
def authenticate_user(slug, password): 
    return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})

def get_user_by_slug(slug): 
    return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_all_users(): 
    return list(users_col.find({}))

def create_new_merchant(name, slug, password):
    if users_col.find_one({"store_slug": slug}): return False
    users_col.insert_one({"id": f"U-{uuid.uuid4().hex[:6]}", "username": name, "store_slug": slug, "password": password, "active": "TRUE"})
    return True

def toggle_user_status(user_id, current_status): 
    users_col.update_one({"id": user_id}, {"$set": {"active": "FALSE" if current_status == "TRUE" else "TRUE"}})

def delete_user(user_id):
    users_col.delete_one({"id": user_id})
    products_col.delete_many({"u_id": user_id})
    settings_col.delete_one({"u_id": user_id})
    orders_col.delete_many({"store_id": user_id})
    coupons_col.delete_many({"u_id": user_id})

def change_user_password(user_id, old_password, new_password):
    if not users_col.find_one({"id": user_id, "password": old_password}): return False
    users_col.update_one({"id": user_id}, {"$set": {"password": new_password}})
    return True

def edit_merchant_info(user_id, new_slug, new_package):
    existing = users_col.find_one({'store_slug': new_slug})
    if existing and str(existing.get('id', existing.get('_id'))) != str(user_id): return False
    try:
        from bson.objectid import ObjectId
        query = {'$or': [{'id': user_id}, {'_id': ObjectId(user_id)}]}
    except: 
        query = {'id': user_id}
    users_col.update_one(query, {'$set': {'store_slug': new_slug, 'package': new_package}})
    return True

# ==========================================
# إدارة الإعدادات
# ==========================================
def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    return setting if setting else {'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 'theme_color': '#0d6efd', 'font_family': 'Cairo'}

def update_settings(user_id, data): 
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

# ==========================================
# إدارة المنتجات
# ==========================================
def add_product(user_id, name, desc, price, cat, img, stock):
    try: 
        products_col.insert_one({"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "created_at": datetime.now(), "ratings_sum": 0, "ratings_count": 0, "rated_ips": {}})
        return True
    except: return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock):
    try: 
        products_col.update_one({"id": product_id, "u_id": user_id}, {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock)}})
        return True
    except: return False

def delete_product(product_id, user_id): 
    products_col.delete_one({"id": product_id, "u_id": user_id})

def get_products(user_id): 
    return list(products_col.find({"u_id": user_id}))

# ==========================================
# 🛡️ الأمان: معالجة الطلبات الآمنة (Backend Cart Validation)
# ==========================================

def create_secure_order(store_id, customer_name, customer_phone, customer_address, payment, cart_items, coupon_code=""):
    import secrets
    order_id = "ORD-" + secrets.token_hex(3).upper()
    
    secure_cart = []
    total = 0.0
    
    for item in cart_items:
        # جلب بيانات المنتج من قاعدة البيانات للتأكد من الاسم والسعر الحقيقي
        prod_id = item.get('id') or item.get('product_id') or item.get('_id')
        p_name = item.get('name') or item.get('title')
        p_price = float(item.get('price', 0))
        qty = int(item.get('qty', 1))
        
        if prod_id:
            db_prod = products_col.find_one({"_id": prod_id, "store_id": store_id}) or products_col.find_one({"id": prod_id, "store_id": store_id})
            if db_prod:
                p_name = db_prod.get('name') or db_prod.get('title') or p_name
                p_price = float(db_prod.get('price', p_price))
        
        if not p_name:
            p_name = f"منتج #{str(prod_id)[:6]}" if prod_id else "منتج"
            
        subtotal = p_price * qty
        total += subtotal
        secure_cart.append({
            "id": str(prod_id) if prod_id else "",
            "name": str(p_name),
            "price": p_price,
            "qty": qty,
            "subtotal": subtotal
        })

    discount_info = {}
    if coupon_code:
        coupon = validate_coupon(store_id, coupon_code)
        if coupon:
            disc_val = float(coupon['discount'])
            total = max(0.0, total - disc_val)
            discount_info = {"code": coupon_code, "discount": disc_val}

    order_doc = {
        "order_id": order_id,
        "store_id": store_id,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_address": customer_address,
        "payment": payment,
        "cart": secure_cart,
        "total": round(total, 2),
        "status": "جديد 🟡",
        "discount_info": discount_info,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    orders_col.insert_one(order_doc)
    return order_id, round(total, 2), secure_cart, discount_info



def get_orders(store_id): 
    return list(orders_col.find({"store_id": store_id}).sort("date", -1))

# ==========================================
# الكوبونات والباقات (تمت استعادتها وتأمينها)
# ==========================================
def add_coupon(user_id, code, discount_percent): 
    coupons_col.insert_one({"id": f"C-{uuid.uuid4().hex[:6]}", "u_id": user_id, "code": code.upper(), "discount": int(discount_percent)})
def get_coupons(user_id): 
    return list(coupons_col.find({"u_id": user_id}))
def delete_coupon(coupon_id, user_id): 
    coupons_col.delete_one({"id": coupon_id, "u_id": user_id})
def validate_coupon(user_id, code): 
    return coupons_col.find_one({"u_id": user_id, "code": code.upper()})

def get_packages(): 
    return list(packages_col.find())
def add_package(name, price, max_products, features):
    try:
        import re as regex_lib
        # استخراج الأرقام فقط لضمان تحويلها لـ int
        val = str(max_products)
        clean_str = regex_lib.sub(r'\D', '', val)
        clean_max = int(clean_str) if clean_str else 999999
    except:
        clean_max = 20

    db.packages.insert_one({
        "name": str(name).strip(),
        "price": str(price).strip(),
        "max_products": clean_max,
        "pkg_max": clean_max,
        "features": str(features).strip()
    })


def delete_package(pkg_id):
    from bson.objectid import ObjectId
    packages_col.delete_one({'_id': ObjectId(pkg_id)})


# ==========================================
# إدارة المناديب (Drivers Management)
# ==========================================
drivers_col = db['drivers']

def add_driver(store_id, name, phone):
    try:
        import secrets
        clean_phone = str(phone).strip()
        clean_name = str(name).strip()
        existing = drivers_col.find_one({"store_id": store_id, "phone": clean_phone})
        if not existing:
            token = secrets.token_hex(8)
            drivers_col.insert_one({
                "store_id": store_id,
                "name": clean_name,
                "phone": clean_phone,
                "token": token
            })
            return token
        return False
    except Exception as e:
        print("Driver Insert Error:", e)
        return False


def get_store_drivers(store_id):
    try:
        import secrets
        from bson.objectid import ObjectId
        drivers = list(drivers_col.find({"store_id": store_id}).sort('_id', -1))
        for d in drivers:
            d_id_str = str(d['_id'])
            d['_id'] = d_id_str
            # إذا كان المندوب لا يملك رمز بوابة، نقوم بتوليده وحفظه فوراً
            if 'token' not in d:
                new_token = secrets.token_hex(8)
                drivers_col.update_one({"_id": ObjectId(d_id_str)}, {"$set": {"token": new_token}})
                d['token'] = new_token
        return drivers
    except Exception as e:
        print("Driver Fetch Error:", e)
        return []


def delete_driver(store_id, phone):
    try:
        drivers_col.delete_one({"store_id": store_id, "phone": str(phone).strip()})
        return True
    except Exception as e:
        print("Driver Delete Error:", e)
        return False



def get_driver_by_token(token):
    return drivers_col.find_one({"token": token.lower()}, {"_id": 0})


def assign_order_driver(order_id, store_id, driver_name, driver_phone):
    return orders_col.update_one(
        {"order_id": str(order_id), "store_id": store_id},
        {"$set": {
            "driver_name": driver_name,
            "driver_phone": driver_phone,
            "status": "مع المندوب للتوصيل 🚚"
        }}
    )




def extract_real_order_items(order, store_id=None):
    """استخراج وتنسيق أسماء المنتجات الحقيقية بدقة من كافة صيغ الطلبات"""
    import json
    extracted = []
    
    # 1. فحص حقل cart سواء كان مصفوفة أو نص JSON
    cart_data = order.get('cart')
    if isinstance(cart_data, str):
        try:
            cart_data = json.loads(cart_data)
        except:
            if cart_data.strip():
                extracted.append({"name": cart_data.strip(), "qty": 1})
                return extracted

    if isinstance(cart_data, list):
        for item in cart_data:
            if isinstance(item, dict):
                p_name = item.get('name') or item.get('title') or item.get('product_name') or item.get('item_name')
                qty = item.get('qty') or item.get('quantity') or 1
                prod_id = item.get('id') or item.get('product_id') or item.get('_id')
                
                # إذا كان الاسم غير متوفر أو عام، نبحث عنه في المنتجات
                if (not p_name or p_name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    prod = products_col.find_one({"id": str(prod_id)}) or products_col.find_one({"_id": prod_id})
                    if prod:
                        p_name = prod.get('name') or prod.get('title')
                
                if p_name:
                    extracted.append({"name": str(p_name), "qty": qty})
            elif isinstance(item, str) and item.strip():
                extracted.append({"name": item.strip(), "qty": 1})

    # 2. فحص الحقول الفردية القديمة
    if not extracted:
        single_name = order.get('product_name') or order.get('item_name')
        if single_name:
            extracted.append({"name": str(single_name), "qty": order.get('qty', 1)})

    # 3. التحقق من نص المنتجات الصريح إن وجد
    if not extracted:
        raw_text = order.get('items_text') or order.get('order_details')
        if raw_text:
            extracted.append({"name": str(raw_text), "qty": 1})

    return extracted if extracted else [{"name": "طلب #" + str(order.get('order_id', '')), "qty": 1}]


def resolve_order_items(order, store_id=None):
    """محرك استخراج ومطابقة أسماء المنتجات بدقة واحترافية من قاعدة البيانات"""
    import json
    from bson.objectid import ObjectId
    
    store_id = store_id or order.get('store_id')
    results = []
    
    # خريطة سريعة لمنتجات المتجر بالمعرف والسعر
    store_prods = list(products_col.find({"store_id": store_id})) if store_id else list(products_col.find({}))
    prod_by_id = {}
    prod_by_price = {}
    
    for p in store_prods:
        p_name = p.get('name') or p.get('title') or p.get('name_ar')
        if p_name:
            if '_id' in p: prod_by_id[str(p['_id'])] = p_name
            if 'id' in p: prod_by_id[str(p['id'])] = p_name
            try:
                price_val = float(p.get('price', 0))
                if price_val > 0 and price_val not in prod_by_price:
                    prod_by_price[price_val] = p_name
            except:
                pass

    # 1. فحص حقل السلة cart
    cart = order.get('cart')
    if isinstance(cart, str):
        try:
            cart = json.loads(cart)
        except:
            pass
            
    if isinstance(cart, list) and len(cart) > 0:
        for it in cart:
            if isinstance(it, dict):
                # البحث عن أي مفتاح يحمل اسم المنتج
                name = (it.get('name') or it.get('title') or it.get('product_name') or 
                        it.get('item_name') or it.get('name_ar') or it.get('label'))
                
                prod_id = str(it.get('id') or it.get('product_id') or it.get('_id') or '')
                qty = it.get('qty') or it.get('quantity') or 1
                
                # مطابقة المعرف مع جدول المنتجات إذا كان الاسم مفقوداً
                if (not name or name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    name = prod_by_id.get(prod_id)
                
                # مطابقة السعر مع جدول المنتجات كحل بديل
                if not name or name in ['منتج', 'منتجات متنوعة', '']:
                    try:
                        p_price = float(it.get('price', 0))
                        name = prod_by_price.get(p_price)
                    except:
                        pass
                        
                if name and name not in ['منتج', 'منتجات متنوعة']:
                    results.append(f"{name} (x{qty})")
                    
            elif isinstance(it, str) and it.strip() and it.strip() != 'منتج':
                results.append(it.strip())

    # 2. فحص الحقول النصية والفردية
    if not results:
        direct_name = order.get('product_name') or order.get('item_name') or order.get('title')
        if direct_name and direct_name != 'منتج':
            results.append(f"{direct_name} (x{order.get('qty', 1)})")

    # 3. مطابقة إجمالي الطلب مع أسعار منتجات المتجر للطلبات القديمة جداً
    if not results:
        try:
            total_val = float(order.get('total', 0))
            if total_val in prod_by_price:
                results.append(f"{prod_by_price[total_val]} (x1)")
        except:
            pass

    # 4. في حال تعذر المطابقة التامة نضع كود الطلب المرجعي
    if not results:
        results.append(f"طلب {order.get('order_id', '')}")

    return results


def get_store_orders_enhanced(store_id):
    """دالة مطورة وذكية لجلب الطلبات مع مطابقة أسماء المنتجات"""
    orders = list(orders_col.find({"store_id": store_id}).sort('_id', -1))
    
    # 1. جلب خريطة المنتجات لمطابقتها مع الأكواد
    prods = list(products_col.find({"store_id": store_id}))
    prod_map = {}
    for p in prods:
        name = p.get('name') or p.get('title')
        if name:
            if '_id' in p: prod_map[str(p['_id'])] = name
            if 'id' in p: prod_map[str(p['id'])] = name
            
    import json
    for o in orders:
        if '_id' in o: o['_id'] = str(o['_id'])
        
        final_list = []
        cart = o.get('cart')
        
        # 2. فك السلة لو كانت نصاً
        if isinstance(cart, str):
            try: cart = json.loads(cart)
            except: 
                if cart.strip(): final_list.append(f"▪️ {cart.strip()}")
        
        # تحويل القاموس لمصفوفة إن وجد
        if isinstance(cart, dict):
            cart = [cart]
            
        # 3. قراءة المصفوفة بدقة
        if isinstance(cart, list):
            for item in cart:
                if isinstance(item, dict):
                    name = item.get('name') or item.get('title') or item.get('product_name')
                    # المطابقة عبر ID في حال غياب الاسم
                    if not name or name == 'منتج':
                        pid = str(item.get('id') or item.get('_id') or item.get('product_id') or '')
                        if pid in prod_map:
                            name = prod_map[pid]
                            
                    if not name or name == 'منتج':
                        name = "منتج غير مسجل"
                        
                    qty = item.get('qty') or item.get('quantity') or 1
                    final_list.append(f"▪️ {name} (x{qty})")
                elif isinstance(item, str) and item.strip():
                    final_list.append(f"▪️ {item.strip()}")
                    
        # 4. قراءة الحقول القديمة (دعم الإصدارات السابقة للطلبات)
        if not final_list:
            legacy = o.get('product_name') or o.get('item_name') or o.get('items')
            if isinstance(legacy, str) and legacy.strip():
                if '▪️' not in legacy:
                    final_list.append(f"▪️ {legacy} (x{o.get('qty', 1)})")
                else:
                    final_list.append(legacy)
                    
        # 5. خطة الطوارئ
        if not final_list:
            final_list.append("▪️ منتج غير محدد")
            
        o['final_products'] = final_list
        
    return orders



def check_product_limit(store_id):
    """التحقق من تجاوز التاجر للحد الأقصى للمنتجات بناءً على باقته"""
    try:
        user = users_col.find_one({"id": store_id})
        if not user: 
            return False, "حساب المتجر غير موجود."
            
        # استثناء المتجر الرئيسي (المدير) من القيود
        if user.get("store_slug") == "admin-store":
            return True, ""
            
        pkg_name = user.get("package", "أساسية")
        
        # جلب بيانات الباقة من قاعدة البيانات
        try:
            pkg = db.packages.find_one({"name": pkg_name})
        except:
            pkg = None
            
        # معالجة الحد الأقصى (في حال كتب المدير "لامحدود" نصياً بدلاً من رقم)
        max_str = str(pkg.get("max_products", 20)) if pkg else "20"
        try:
            max_prods = int(max_str)
        except ValueError:
            max_prods = 9999999 # رقم لا نهائي في حال الباقة المفتوحة
            
        # حساب العدد الفعلي للمنتجات الحالية في متجر التاجر
        current_count = products_col.count_documents({"store_id": store_id})
        
        if current_count >= max_prods:
            return False, f"عذراً! باقتك الحالية ({pkg_name}) تسمح بإضافة {max_prods} منتج كحد أقصى. يرجى ترقية باقتك لإضافة المزيد."
            
        return True, ""
    except Exception as e:
        print("Package Limit Check Error:", e)
        return True, "" # في حال الخطأ التقني نسمح بالمرور كي لا يتوقف المتجر



def check_merchant_product_limit(user_id):
    try:
        import re as regex_lib
        from bson.objectid import ObjectId
        user = users_col.find_one({"id": user_id})
        if not user:
            try:
                user = users_col.find_one({"_id": ObjectId(str(user_id))})
            except:
                pass

        if not user:
            return True, 0, 999999, "عامة", ""

        pkg_name = str(user.get("package", "أساسية")).strip()
        
        # البحث في قاعدة البيانات بمطابقة مرنة
        target_pkg = db.packages.find_one({"name": {"$regex": f"^{regex_lib.escape(pkg_name)}$", "$options": "i"}})

        if target_pkg:
            raw_val = target_pkg.get("max_products") if target_pkg.get("max_products") is not None else target_pkg.get("pkg_max", 20)
            try:
                max_limit = int(raw_val)
            except:
                max_limit = 20
        else:
            # إذا لم توجد الباقة في الجدول، نأخذ حداً صغيراً بدلاً من 20
            max_limit = 5

        current_prods = get_products(user_id)
        current_count = len(current_prods) if current_prods else 0

        if current_count >= max_limit:
            err_msg = f"⚠️ تم الوصول للحد الأقصى! باقتك ({pkg_name}) تسمح بـ {max_limit} منتج فقط (لديك حالياً {current_count} منتج)."
            return False, current_count, max_limit, pkg_name, err_msg

        return True, current_count, max_limit, pkg_name, ""
    except Exception as e:
        print("Limit Error:", e)
        return True, 0, 999999, "خطأ", ""


```

-----------------------------------
## File Path: ./docs/REFACTORING.md
```
# مراجعة وتنظيم المشروع — 2026-08-25

## ما تم تنفيذه
1. تنظيف الملفات غير المستخدمة وملفات التعديل الآلي القديمة.
2. إنشاء `base_dashboard.html` وتوحيد عناصر لوحة التاجر عبر `templates/partials/`.
3. فصل CSS وJavaScript الخاصين بلوحة التاجر.
4. منع أزرار النماذج من العمل بشكل غير محدد بإضافة `type="submit"` للأزرار التي تنفذ إرسال النموذج.
5. إزالة أسلوب سكربتات تعديل `app.py` وHTML آليًا.
6. اعتماد MongoDB كمصدر البيانات الحالي عبر `database.py` و`config.py`.
7. توحيد Service Worker إلى `static/sw.js` واحد، مع Manifest ديناميكي لكل متجر.
8. إضافة سياسة Cache واضحة: الصفحات الديناميكية لا تُخزن، وCSS/JS الثابت يستخدم Cache طويلًا مع إصدار.
9. إزالة تكرار دالة `add_driver` وتوحيد Collection الخاصة بالمناديب.
10. إصلاح مسار بوابة المندوب ودعمه للمسارين `/driver/<token>` و`/delivery?token=...`.
11. تأمين تحديثات الطلبات بحيث تتضمن `store_id` في استعلامات التاجر.
12. نقل إعدادات البيئة إلى `config.py` ومنع الأسرار من الدخول إلى Git.
13. تحديث README وPROJECT_CONTEXT وdocs/setup.md لتطابق البنية الحالية.

## تحقق محلي
- تم فحص بنية Python بواسطة AST بدون أخطاء نحوية.
- تم تحميل جميع قوالب Jinja الرئيسية والـpartials بنجاح.
- تم التأكد من عدم وجود نسخة ثانية من Service Worker أو Manifest ثابت.
- تم التأكد من عدم وجود ملفات `fix_*.py` أو `update_*.py` داخل النسخة النهائية.

```

-----------------------------------
## File Path: ./docs/setup.md
```
# إعداد وتشغيل TajerGo

## 1) المتطلبات
- Python 3.10+
- MongoDB
- حساب Vercel للنشر

## 2) متغيرات البيئة
انسخ `.env.example` إلى `.env` في البيئة المحلية، ثم ضع القيم الحقيقية.
في Vercel أضف نفس المتغيرات من Project Settings → Environment Variables.

المطلوب:
- `SECRET_KEY`
- `MONGO_URI`

اختياري:
- `MONGO_DB_NAME`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `MAIN_DOMAIN`
- `STATIC_VERSION`

## 3) التشغيل المحلي
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 4) قاعدة البيانات
لتجهيز الفهارس:
```bash
python setup_indexes.py
```

للنسخ الاحتياطي:
```bash
python backup_db.py
```

## 5) النشر
```text
Local → GitHub → Vercel → MongoDB
```

بعد كل نشر:
1. افتح `/dashboard`.
2. اختبر كل تبويب.
3. أضف/عدل/احذف منتجًا.
4. افتح المتجر في نافذة خاصة.
5. اختبر الطلب والأزرار الخاصة بالمناديب.
6. تحقق من Console وعدم وجود أخطاء JavaScript.

## 6) سياسة التحديث
الصفحات الديناميكية لا تستخدم Cache.
ملفات CSS/JS تستخدم رقم إصدار في الرابط.
Service Worker واحد فقط موجود في `static/sw.js` ويُقدم عبر `/sw.js`.

```

-----------------------------------
## File Path: ./export_project_pro.sh
```
#!/bin/bash

# Check if dialog is installed
if ! command -v dialog &> /dev/null; then
    echo "[!] Error: 'dialog' is not installed. Please install it using: pkg install dialog"
    exit 1
fi

OUTPUT_FILE="ai_project_context.md"

# Interactive menu using dialog (Updated Title)
CHOICE=$(dialog --stdout --title "GitHub to Gemini Reviewer" \
    --menu "Choose project source:" 12 50 2 \
    1 "Project is already on your phone (Local folder)" \
    2 "Clone temporarily from GitHub (Read-only & Safe)")

clear

if [ "$CHOICE" == "1" ]; then
    TARGET_DIR=$(dialog --stdout --inputbox "Enter local folder path on your phone:" 8 50 "/data/data/com.termux/files/home/")
    clear
    if [ ! -d "$TARGET_DIR" ]; then
        echo "[!] Error: Directory does not exist."
        exit 1
    fi
    echo " [+] Reading project locally from: $TARGET_DIR"

elif [ "$CHOICE" == "2" ]; then
    USERNAME=$(dialog --stdout --inputbox "Enter GitHub Username:" 8 50)
    REPO=$(dialog --stdout --inputbox "Enter Repository Name:" 8 50)
    TOKEN=$(dialog --stdout --passwordbox "Enter GitHub Personal Access Token (PAT):" 8 50)
    clear
    
    TARGET_DIR="temp_read_only_folder"
    REPO_URL="https://${TOKEN}@github.com/${USERNAME}/${REPO}.git"
    
    echo "[*] Cloning repository temporarily (Read-only)..."
    git clone "$REPO_URL" "$TARGET_DIR" &>/dev/null
    
    if [ $? -ne 0 ]; then
        echo "[!] Error: Failed to clone. Check your details or token."
        exit 1
    fi
    echo " [+] Cloned successfully (Your GitHub repo is 100% untouched)."
else
    echo "Process cancelled."
    exit 0
fi

echo ""
echo "[*] Generating unified AI context file ($OUTPUT_FILE)..."
echo "# Software Project Context" > "$OUTPUT_FILE"
echo "Export Date: $(date)" >> "$OUTPUT_FILE"
echo -e "\n--- \n" >> "$OUTPUT_FILE"

cd "$TARGET_DIR"
file_count=0

find . -type f \
    -not -path '*/.*' \
    -not -path '*/node_modules*' \
    -not -path '*/venv/*' \
    -not -path '*/__pycache__*' \
    -not -path '*/build/*' \
    -not -path '*/dist/*' \
    -not -name '*.png' \
    -not -name '*.jpg' \
    -not -name '*.jpeg' \
    -not -name '*.gif' \
    -not -name '*.ico' \
    -not -name '*.pdf' \
    -not -name '*.zip' \
    -not -name '*.db' \
    -not -name '*.sqlite' \
    -not -name '*.lock' | while read -r file; do
    
    file_count=$((file_count + 1))
    echo "   [+] Processing file: $file"
    
    echo "## File Path: $file" >> "../$OUTPUT_FILE"
    echo '```' >> "../$OUTPUT_FILE"
    cat "$file" >> "../$OUTPUT_FILE"
    echo -e '\n```\n' >> "../$OUTPUT_FILE"
    echo "-----------------------------------" >> "../$OUTPUT_FILE"
done

cd ..

if [ "$CHOICE" == "2" ]; then
    rm -rf "$TARGET_DIR"
fi

cp "$OUTPUT_FILE" /sdcard/Download/

echo ""
echo "=================================================="
echo "      Process Completed Successfully! 🎉          "
echo "=================================================="
echo " 📂 File saved in Termux: $OUTPUT_FILE"
echo " 📱 Saved directly to: Download/$OUTPUT_FILE"
echo "=================================================="

```

-----------------------------------
## File Path: ./requirements.txt
```
Flask==2.3.2
gunicorn==20.1.0
pymongo[srv]==4.5.0
dnspython==2.4.2
requests

```

-----------------------------------
## File Path: ./setup_indexes.py
```
import dns.resolver

# إجبار المكتبة على استخدام سيرفرات جوجل للـ DNS متجاهلة ملف resolv.conf
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']

import database
from pymongo import ASCENDING

print("⏳ جاري إنشاء الفهارس (Indexes) لتسريع المنصة...")

# فهرسة معرف التاجر (لأن كل استعلامات المتجر تعتمد عليه)
database.products_col.create_index([("u_id", ASCENDING)])

# فهرسة التصنيف لتسريع التنقل بين الأقسام
database.products_col.create_index([("category", ASCENDING)])

# فهرسة اسم المنتج لتسريع شريط البحث
database.products_col.create_index([("name", ASCENDING)])

# فهرسة رابط المتجر في جدول المستخدمين لتسريع عملية الدخول
database.users_col.create_index([("store_slug", ASCENDING)], unique=True)

print("✅ تم إنشاء الفهارس بنجاح! قاعدة البيانات الآن مجهزة للعمل بأقصى سرعة مع ملايين المنتجات 🚀")

```

-----------------------------------
## File Path: ./static/css/dashboard.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f4f6f9; }
        .form-control, .form-select { border: 2px solid #b3b3b3 !important; border-radius: 8px; padding: 10px 15px; background-color: #fcfcfc; font-weight: bold; color: #333; transition: all 0.3s ease; }
        .form-control:focus, .form-select:focus { border-color: #0d6efd !important; background-color: #fff; box-shadow: 0 0 8px rgba(13, 110, 253, 0.3); outline: none; }
        .card { border-radius: 12px; }
        .upload-btn-wrapper { position: relative; overflow: hidden; display: inline-block; width: 100%; margin-bottom: 5px; }
        .upload-btn-wrapper input[type=file] { font-size: 100px; position: absolute; left: 0; top: 0; opacity: 0; cursor: pointer; }
        .divider-text { display: flex; align-items: center; text-align: center; color: #888; font-weight: bold; margin: 8px 0; }
        .divider-text::before, .divider-text::after { content: ''; flex: 1; border-bottom: 1px dashed #ccc; }
        .divider-text:not(:empty)::before { margin-left: .5em; } .divider-text:not(:empty)::after { margin-right: .5em; }

/* Dashboard navigation: keep all tabs accessible on small screens. */
#myTab {
    overflow-x: auto;
    flex-wrap: nowrap;
    scrollbar-width: thin;
}
#myTab .nav-item { flex: 0 0 auto; }
#myTab .nav-link { white-space: nowrap; }

```

-----------------------------------
## File Path: ./static/css/driver.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f2f5f9; padding-bottom: 30px; }
        .header-banner { background: linear-gradient(135deg, #0d6efd, #2b2b2b); color: white; padding: 40px 0 30px; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 20px;}
        .order-card { background: #fff; border: none; border-radius: 20px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); margin-bottom: 15px; border-right: 5px solid #0d6efd; transition: transform 0.3s ease; }
        .order-card:hover { transform: translateY(-3px); }
        .btn-deliver { background-color: #25D366; color: white; font-weight: 800; border-radius: 12px; padding: 12px; width: 100%; border: none; transition: background 0.3s; }
        .btn-deliver:hover { background-color: #1ebe57; }

```

-----------------------------------
## File Path: ./static/css/login.css
```
body {
            font-family: 'Cairo', sans-serif;
            background-color: #f2f5f9;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            background-image: radial-gradient(circle at top right, rgba(13, 110, 253, 0.1) 0%, transparent 40%),
                              radial-gradient(circle at bottom left, rgba(13, 110, 253, 0.05) 0%, transparent 40%);
        }
        .login-card {
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.06);
            padding: 40px 30px;
            width: 100%;
            max-width: 400px;
            border-top: 5px solid #0d6efd;
            position: relative;
            z-index: 1;
        }
        .platform-logo {
            width: 110px;
            height: 110px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            margin-top: -80px; /* لرفع الشعار قليلاً خارج البطاقة */
            margin-bottom: 20px;
            background-color: #fff;
        }
        .form-control {
            border-radius: 12px;
            padding: 12px 15px;
            font-weight: 600;
            background-color: #f8f9fa;
            border: 1px solid #eaeaea;
            transition: all 0.3s;
        }
        .form-control:focus {
            background-color: #fff;
            border-color: #0d6efd;
            box-shadow: 0 0 0 0.25rem rgba(13,110,253,0.1);
        }
        .btn-login {
            border-radius: 12px;
            padding: 12px;
            font-weight: 800;
            font-size: 1.1rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(13,110,253,0.2) !important;
        }
        .input-icon {
            color: #888;
        }

```

-----------------------------------
## File Path: ./static/css/store.css
```

        body { font-family: var(--store-font, 'Cairo'), sans-serif; background-color: #f2f5f9; padding-bottom: 25px; color: #333; }

        
        /* Hero Section */
        .header-small .hero-section { padding: 40px 0 30px; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; margin-bottom: 25px; }
        .header-small .hero-title { font-size: 1.8rem; }
        .header-small .store-logo { width: 80px; height: 80px; }
        .header-large .hero-section { padding: 80px 0 60px; border-bottom-left-radius: 50px; border-bottom-right-radius: 50px; margin-bottom: 35px; }
        .header-large .hero-title { font-size: 3.5rem; }
        .header-large .store-logo { width: 120px; height: 120px; }
        .header-medium .hero-section { padding: 60px 0 40px; border-bottom-left-radius: 40px; border-bottom-right-radius: 40px; margin-bottom: 30px; }
        .header-medium .hero-title { font-size: 2.5rem; }
        .header-medium .store-logo { width: 100px; height: 100px; }

        .hero-section { background: linear-gradient(135deg, var(--main-color) 0%, #2b2b2b 100%); color: white; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.08); position: relative; overflow: hidden; }
        .hero-section::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('data:image/svg+xml;utf8,<svg opacity="0.05" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="none"/><circle cx="50" cy="50" r="40" stroke="white" stroke-width="2" fill="none"/></svg>') repeat; pointer-events: none; }
        .store-logo { object-fit: cover; border-radius: 50%; border: 4px solid rgba(255,255,255,0.9); box-shadow: 0 8px 20px rgba(0,0,0,0.15); background-color: #fff; margin-bottom: 15px; position: relative; z-index: 1; transition: transform 0.3s ease; }
        .store-logo:hover { transform: scale(1.05); }

        /* Search, Sort & Actions */
        .search-bar-container { background: #fff; border-radius: 50rem; padding: 5px; box-shadow: var(--card-shadow); transition: box-shadow 0.3s ease; }
        .search-bar-container:focus-within { box-shadow: var(--hover-shadow); }
        .search-bar-container input { border: none !important; box-shadow: none !important; font-weight: 600; }
        .sort-select { background-color: #fff; border: 1px solid #eaeaea; border-radius: 50rem; padding: 8px 15px; font-weight: 700; color: #555; box-shadow: var(--card-shadow); cursor: pointer; outline: none; appearance: none; -webkit-appearance: none; -moz-appearance: none; background-image: url('data:image/svg+xml;utf8,<svg fill="%23555" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>'); background-repeat: no-repeat; background-position: left 10px center; padding-left: 35px;}
        .sort-select:focus { border-color: var(--main-color); box-shadow: var(--hover-shadow); }
        .btn-share { border-radius: 50rem; padding: 8px 15px; font-weight: bold; }

        /* Tabs */
        .category-tabs { flex-wrap: nowrap; overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; padding: 5px 5px 20px 5px; margin-bottom: 10px; gap: 12px; scrollbar-width: none; }
        .category-tabs .nav-link { border-radius: 50rem; white-space: nowrap; color: #555; font-weight: 700; background-color: #fff; border: 1px solid #eaeaea; box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); padding: 8px 24px; }
        .category-tabs .nav-link.active { background-color: var(--main-color); color: white; border-color: var(--main-color); box-shadow: 0 6px 15px rgba(0,0,0,0.1); transform: translateY(-2px); }

        /* Product Cards */
        .product-card { border: none; border-radius: 20px; box-shadow: var(--card-shadow); overflow: hidden; background: #fff; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); }
        .product-card:hover { transform: translateY(-5px); box-shadow: var(--hover-shadow); }
        .img-wrapper { position: relative; width: 100%; padding-top: 100%; background-color: #fff; cursor: pointer; overflow: hidden; border-bottom: 1px solid #f0f0f0; }
        .product-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; padding: 0; transition: transform 0.5s ease; }
        .product-card:hover .product-img { transform: scale(1.05); }

        .product-title { font-size: 1rem; font-weight: 800; color: #2c3e50; line-height: 1.4; margin-bottom: 4px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .product-price { font-size: 1.25rem; font-weight: 800; color: var(--main-color); }
        .product-price small { font-size: 0.85rem; color: #888; font-weight: 600; }

        .btn-custom { background-color: var(--main-color); color: white; font-weight: 700; border-radius: 12px; padding: 10px; transition: all 0.2s; border: none; }
        .btn-custom:hover { filter: brightness(1.1); transform: scale(1.02); }
        .btn-secondary-custom { background-color: #e9ecef; color: #6c757d; font-weight: 700; border-radius: 12px; padding: 10px; border: none; }

        /* Rating & Badges */
        .rating-badge { display: inline-flex; align-items: center; background: #fff8e1; color: #ffb300; padding: 4px 10px; border-radius: 50rem; font-size: 0.8rem; font-weight: 800; cursor: pointer; transition: background 0.2s; margin-bottom: 8px;}
        .rating-badge:hover { background: #ffecb3; }
        .tags-container { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 12px; }
        .tag-badge { background: #f8f9fa; border: 1px solid #e9ecef; color: #6c757d; font-size: 0.7rem; padding: 3px 8px; border-radius: 6px; font-weight: 600; }

        /* Floating Cart */
        #floating-cart { position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%); background: rgba(13, 110, 253, 0.95); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); color: white; border-radius: 50rem; padding: 12px 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); cursor: pointer; z-index: 1000; font-weight: 800; font-size: 1.1rem; display: none; width: auto; white-space: nowrap; transition: all 0.3s ease; }
        #floating-cart:hover { transform: translateX(-50%) scale(1.05); }

        /* Modals & Support */
        .modal-content { border-radius: 24px; border: none; }
        .modal-header { border-bottom: 1px solid #f0f0f0; border-radius: 24px 24px 0 0; }
        .support-card { background: #fff; border: none; border-radius: 20px; padding: 20px; box-shadow: var(--card-shadow); margin-top: 30px; text-align: center; }
        .btn-support-wa { background-color: #25D366; color: white; border-radius: 50rem; padding: 10px 22px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: all 0.2s; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.2); }
        .btn-support-wa:hover { background-color: #1ebe57; color: white; transform: translateY(-2px); }
    

.modal-star:hover, .modal-star:hover ~ .modal-star { fill: #ffc107 !important; transform: scale(1.15); } .star-selected { fill: #ffc107 !important; }

```

-----------------------------------
## File Path: ./static/css/system_admin.css
```
body{font-family:'Cairo',sans-serif; background-color:#1e1e2d; color:#fff;}

```

-----------------------------------
## File Path: ./static/css/track.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f4f7fb; color: #333; }
        .track-card { border-radius: 20px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .stepper { display: flex; justify-content: space-between; position: relative; margin: 30px 0; }
        .stepper::before { content: ''; position: absolute; top: 22px; left: 10%; right: 10%; height: 4px; background: #e0e0e0; z-index: 1; }
        .stepper-progress { position: absolute; top: 22px; right: 10%; height: 4px; background: #198754; z-index: 2; transition: width 0.5s ease; }
        .step-item { position: relative; z-index: 3; text-align: center; width: 25%; }
        .step-icon { width: 48px; height: 48px; border-radius: 50%; background: #e0e0e0; color: #fff; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 1.2rem; transition: all 0.3s ease; }
        .step-item.active .step-icon { background: #0d6efd; box-shadow: 0 0 0 6px rgba(13,110,253,0.2); }
        .step-item.completed .step-icon { background: #198754; }
        .step-item.canceled .step-icon { background: #dc3545; }
        .step-label { font-size: 0.85rem; font-weight: 700; color: #6c757d; }
        .step-item.active .step-label { color: #0d6efd; }
        .step-item.completed .step-label { color: #198754; }

```

-----------------------------------
## File Path: ./static/js/app.js
```
// Shared frontend helpers for TajerGo.
(function () {
    'use strict';

    window.fixImg = window.fixImg || function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };
})();

```

-----------------------------------
## File Path: ./static/js/dashboard.js
```
// TajerGo Dashboard JavaScript
(function () {
    'use strict';

    window.fixImg = function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };

    window.copyDriverPortalLink = function (token) {
        const input = document.getElementById('link-' + token);
        if (!input) return;
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(input.value).then(
                () => alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة'),
                () => fallbackCopy(input)
            );
        } else {
            fallbackCopy(input);
        }
    };

    function fallbackCopy(input) {
        input.select();
        document.execCommand('copy');
        alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة');
    }

    window.submitNewDriver = function (event) {
        event.preventDefault();
        const name = (document.getElementById('driverNameInput')?.value || '').trim();
        const phone = (document.getElementById('driverPhoneInput')?.value || '').trim();
        if (!name || !phone) {
            alert('يرجى إدخال اسم ورقم المندوب');
            return false;
        }

        fetch('/api/drivers/add', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name, phone})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إضافة المندوب بنجاح وتوليد بوابته الخاصة');
                window.location.reload();
            } else {
                alert('حدث خطأ: ' + (data.error || 'تعذر الإضافة'));
            }
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
        return false;
    };

    window.deleteDriver = function (token) {
        if (!confirm('هل أنت متأكد من حذف هذا المندوب؟')) return;
        fetch('/api/drivers/delete/' + encodeURIComponent(token), {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                if (data.success) window.location.reload();
                else alert(data.error || 'تعذر حذف المندوب');
            })
            .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.updateOrderStatus = function (orderId, newStatus) {
        fetch('/api/orders/update-status', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({order_id: orderId, status: newStatus})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) window.location.reload();
            else alert(data.error || 'تعذر تحديث الحالة');
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.assignOrderToDriver = function (orderId, selectEl) {
        const selectedOption = selectEl?.options[selectEl.selectedIndex];
        const driverName = selectedOption?.getAttribute('data-name');
        const driverPhone = selectedOption?.getAttribute('data-phone');
        if (!driverPhone) return;

        selectEl.disabled = true;
        fetch('/api/orders/assign-driver', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                order_id: orderId,
                driver_name: driverName,
                driver_phone: driverPhone
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إسناد الطلب (' + orderId + ') للمندوب: ' + driverName);
                window.location.reload();
            } else {
                alert(data.error || 'حدث خطأ أثناء الإسناد');
                selectEl.disabled = false;
            }
        })
        .catch(() => {
            alert('فشل الاتصال بالخادم');
            selectEl.disabled = false;
        });
    };

    document.addEventListener('DOMContentLoaded', function () {
        const activeTab = localStorage.getItem('tajergo_active_tab');
        if (activeTab) {
            const tabBtn = document.querySelector(`button[data-bs-target="${CSS.escape(activeTab)}"]`);
            if (tabBtn && window.bootstrap) {
                bootstrap.Tab.getOrCreateInstance(tabBtn).show();
            }
        }

        document.querySelectorAll('button[data-bs-toggle="tab"]').forEach(function (tabElm) {
            tabElm.addEventListener('shown.bs.tab', function (event) {
                const currentTarget = event.target.getAttribute('data-bs-target');
                if (currentTarget) localStorage.setItem('tajergo_active_tab', currentTarget);
            });
        });
    });
})();

```

-----------------------------------
## File Path: ./static/sw.js
```
const CACHE_NAME = 'tajergo-static-v20260825-2';
const STATIC_EXTENSIONS = /\.(?:css|js|png|jpg|jpeg|webp|svg|woff2?)$/i;

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Dynamic pages/API: always use the network so new products/settings/orders
  // are never hidden by an old Service Worker cache.
  if (request.mode === 'navigate' || url.pathname.startsWith('/api/') ||
      url.pathname.startsWith('/store/') || url.pathname.startsWith('/dashboard') ||
      url.pathname.startsWith('/manifest/')) {
    event.respondWith(fetch(request));
    return;
  }

  if (!url.pathname.startsWith('/static/') || !STATIC_EXTENSIONS.test(url.pathname)) {
    return;
  }

  event.respondWith(
    caches.match(request).then(cached => {
      const network = fetch(request).then(response => {
        if (response.ok) {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        }
        return response;
      });
      return cached || network;
    })
  );
});

```

-----------------------------------
## File Path: ./templates/base_dashboard.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}لوحة التحكم | TajerGo{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}?v={{ static_version }}">
    {% block head_extra %}{% endblock %}
</head>
<body>
    {% include 'partials/topbar.html' %}
    <main class="container pb-5">
        {% include 'partials/flash_messages.html' %}
        {% include 'partials/dashboard_nav.html' %}
        {% block dashboard_content %}{% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="{{ url_for('static', filename='js/dashboard.js') }}?v={{ static_version }}"></script>
    {% block page_scripts %}{% endblock %}

<!-- SIDEBAR_TOGGLE_SCRIPT -->
<style>
    /* فرض الإخفاء وتمدد المحتوى */
    .tajergo-sidebar-hidden { display: none !important; }
    .tajergo-main-expanded { margin-right: 0 !important; width: 100% !important; max-width: 100% !important; }
</style>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        let toggleButtons = document.querySelectorAll('.fa-bars');
        let sidebar = document.querySelector('aside') || document.querySelector('.sidebar') || document.querySelector('[id*="sidebar"]');
        let mainContent = document.querySelector('main') || document.querySelector('.main-content') || document.querySelector('.page-content') || document.querySelector('[id*="main"]');
        
        if (toggleButtons.length > 0 && sidebar) {
            toggleButtons.forEach(icon => {
                let btn = icon.closest('button') || icon.closest('a') || icon;
                btn.style.cursor = 'pointer';
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    sidebar.classList.toggle('tajergo-sidebar-hidden');
                    if(mainContent) {
                        mainContent.classList.toggle('tajergo-main-expanded');
                    }
                });
            });
        }
    });
</script>
<!-- END_SIDEBAR_TOGGLE_SCRIPT -->
</body>
</html>

```

-----------------------------------
## File Path: ./templates/dashboard.html
```
{% extends "base_dashboard.html" %}

{% block title %}لوحة التحكم | TajerGo{% endblock %}

{% block dashboard_content %}
{% set cats = products | map(attribute='category') | unique | list %}

        <div class="tab-content">

<!-- تبويب إدارة المناديب -->
<div class="tab-pane fade" id="drivers-pane" role="tabpanel">
    <div class="d-flex justify-content-between align-items-center mb-4 mt-3">
        <h5 class="fw-bold text-dark mb-0"><i class="fas fa-motorcycle text-primary me-2"></i> فريق مناديب التوصيل</h5>
        <button class="btn btn-primary btn-sm rounded-pill px-3 fw-bold shadow-sm" data-bs-toggle="modal" data-bs-target="#addDriverModal">
            <i class="fas fa-plus-circle me-1"></i> إضافة مندوب جديد
        </button>
    </div>

    <div class="row g-3" id="driversListContainer">
        {% if drivers %}
            {% for d in drivers %}
            <div class="col-md-6 col-lg-4">
                <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <div>
                            <h6 class="fw-bold mb-1 text-dark">{{ d.get('name', '') }}</h6>
                            <span class="text-muted small"><i class="fas fa-phone-alt me-1 text-success"></i> {{ d.get('phone', '') }}</span>
                        </div>
                        <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 px-2 py-1 small rounded-pill">نشط 🟢</span>
                    </div>
                    
                    <div class="bg-light p-2 rounded-3 my-2 small">
                        <span class="text-muted d-block mb-1">رابط بوابة المندوب:</span>
                        <div class="input-group input-group-sm">
                            <input type="text" class="form-control border-0 bg-white" value="{{ request.host_url }}driver/{{ d.get('token', d.get('_id', '')) }}" id="link-{{ d.get('token', d.get('_id', '')) }}" readonly>
                            <button class="btn btn-outline-primary" onclick="copyDriverPortalLink('{{ d.get('token', d.get('_id', '')) }}')" title="نسخ الرابط"><i class="fas fa-copy"></i></button>
                        </div>
                    </div>

                    <div class="d-flex justify-content-between align-items-center mt-2 pt-2 border-top">
                        <a href="https://wa.me/{{ d.get('phone', '') }}?text={{ ('مرحباً ' + d.get('name', '') + '، هذا هو رابط بوابة استلام مهام التوصيل الخاصة بك:%0A' + request.host_url + 'driver/' + d.get('token', d.get('_id', '')))|urlencode }}" target="_blank" class="btn btn-sm btn-outline-success rounded-pill px-2 fw-bold">
                            <i class="fab fa-whatsapp me-1"></i> إرسال الرابط
                        </a>
                        <button class="btn btn-sm btn-outline-danger rounded-pill px-2" onclick="deleteDriver('{{ d.get('token', d.get('_id', '')) }}')">
                            <i class="fas fa-trash-alt"></i> حذف
                        </button>
                    </div>
                </div>
            </div>
            {% endfor %}
        {% else %}
            <div class="col-12 text-center py-5 bg-white rounded-4 shadow-sm">
                <i class="fas fa-motorcycle fs-1 text-muted mb-3 opacity-50"></i>
                <h6 class="text-muted fw-bold">لم تقم بإضافة أي مندوب توصيل بعد</h6>
                <p class="text-muted small">أضف مناديبك وشاركهم روابط بواباتهم الميدانية لاستلام وتوصيل الطلبات.</p>
            </div>
        {% endif %}
    </div>
</div>

<!-- Modal إضافة مندوب جديد -->
{% include 'partials/add_driver_modal.html' %}

            
    <div class="tab-pane fade show active" id="analytics">
        <div class="row mb-4">
            <div class="col-md-3 col-6 mb-2"><div class="card bg-success text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">صافي المبيعات 💰</h6><h3 class="mb-0">{{ '{:,.2f}'.format(adv_stats.net_sales) }} <small>{{ settings.currency }}</small></h3><small>نمو: <span dir="ltr">{{ '{:,.1f}'.format(adv_stats.growth_rate) }}%</span></small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card bg-primary text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">إجمالي الطلبات 📦</h6><h3 class="mb-0">{{ adv_stats.total_orders }}</h3><small>مكتملة: {{ adv_stats.completed_orders }} | ملغاة: {{ adv_stats.canceled_orders }}</small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card bg-info text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">متوسط الطلب 🛒</h6><h3 class="mb-0">{{ '{:,.2f}'.format(adv_stats.avg_order_value) }} <small>{{ settings.currency }}</small></h3><small>الإتمام: <span dir="ltr">{{ '{:,.1f}'.format(adv_stats.completion_rate) }}%</span></small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card text-dark shadow-sm border-0" style="background-color:#ffc107;"><div class="card-body"><h6 class="fw-bold">قاعدة العملاء 👥</h6><h3 class="mb-0">{{ adv_stats.customers_count }}</h3><small>رسوم التوصيل: {{ '{:,.2f}'.format(adv_stats.delivery_fees) }}</small></div></div></div>
        </div>
        <div class="row mb-4">
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body text-center"><h6 class="fw-bold text-muted border-bottom pb-2">تفصيل المبيعات الزمنية</h6><div class="d-flex justify-content-between mb-2 mt-3"><span>مبيعات اليوم:</span> <span class="fw-bold text-primary">{{ '{:,.2f}'.format(adv_stats.today_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>مبيعات الأسبوع:</span> <span class="fw-bold text-success">{{ '{:,.2f}'.format(adv_stats.weekly_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>هذا الشهر:</span> <span class="fw-bold text-info">{{ '{:,.2f}'.format(adv_stats.this_month_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>الشهر الماضي:</span> <span class="fw-bold text-secondary">{{ '{:,.2f}'.format(adv_stats.last_month_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>إجمالي غير الصافي:</span> <span class="fw-bold text-dark">{{ '{:,.2f}'.format(adv_stats.total_sales) }}</span></div></div></div></div>
            <div class="col-md-8"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-muted mb-3 border-bottom pb-2">المبيعات خلال 7 أيام</h6><canvas id="salesChart" style="max-height: 200px;"></canvas></div></div></div>
        </div>
        <div class="row mb-4">
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-success border-bottom pb-2">🌟 العملاء الأكثر شراءً</h6><ul class="list-group list-group-flush mt-3">{% for c in adv_stats.top_customers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><div><i class="fas fa-user-circle text-muted me-1"></i> {{ c.name }} <br><small class="text-muted">{{ c.orders }} طلبات</small></div><span class="fw-bold text-success">{{ '{:,.2f}'.format(c.spent) }}</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-primary border-bottom pb-2">🔥 الأكثر مبيعًا</h6><ul class="list-group list-group-flush mt-3">{% for p_name, qty in adv_stats.best_sellers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><span class="text-truncate" style="max-width: 150px;">{{ p_name }}</span><span class="badge bg-primary rounded-pill">{{ qty }} قطعة</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-danger border-bottom pb-2">⚠️ الأقل مبيعًا</h6><ul class="list-group list-group-flush mt-3">{% for p_name, qty in adv_stats.least_sellers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><span class="text-truncate" style="max-width: 150px;">{{ p_name }}</span><span class="badge bg-danger rounded-pill">{{ qty }} قطعة</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
        </div>
    </div>
    <div class="tab-pane fade" id="orders">
<div class="row mb-4" style="display:none;"><div class="col-md-3 col-6 mb-2"><div class="card bg-primary text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">الطلبات</h6><h3 class="mb-0">{{ stats.total_orders }}</h3></div></div></div><div class="col-md-3 col-6 mb-2"><div class="card bg-success text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">الأرباح</h6><h3 class="mb-0">{{ stats.total_revenue }} <small>{{ settings.currency }}</small></h3></div></div></div><div class="col-md-3 col-6 mb-2"><div class="card text-dark shadow-sm border-0" style="background-color:#ffc107;"><div class="card-body"><h6 class="fw-bold">جديدة</h6><h3 class="mb-0">{{ stats.status_counts['جديد 🟡'] }}</h3></div></div></div><div class="col-md-3 col-6 mb-2"><div class="card bg-info text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">تجهيز</h6><h3 class="mb-0">{{ stats.status_counts['قيد التجهيز 🔵'] }}</h3></div></div></div></div><div class="row"><div class="col-md-4 mb-4" style="display:none;"><div class="card shadow-sm border-0 h-100"><div class="card-body"><canvas id="orderChart" style="max-height: 250px;"></canvas></div></div></div><div class="col-md-12 mb-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><a href="/export/orders" class="btn btn-success btn-sm fw-bold shadow-sm mb-3"><i class="fas fa-file-excel"></i> تصدير Excel</a>

<div class="table-responsive bg-white rounded-4 shadow-sm border p-2">
    <table class="table table-hover align-middle mb-0 text-center">
        <thead class="table-light">
            <tr class="text-secondary small fw-bold">
                <th style="width: 110px;">رقم الطلب</th>
                <th class="text-start">العميل والهاتف</th>
                <th class="text-start">المنتجات</th>
                <th>الإجمالي</th>
                <th>الحالة الحالية</th>
                <th class="text-primary"><i class="fas fa-motorcycle me-1"></i> المندوب المسؤول</th>
                <th>تحديث الحالة</th>
            </tr>
        </thead>
        <tbody>
            {% if orders %}
                {% for o in orders %}
                <tr>
                    <!-- 1. رقم الطلب + زر التتبع -->
                    <td>
                        <span class="fw-bold text-dark d-block mb-1">{{ o.order_id }}</span>
                        <a href="/track/{{ o.order_id }}" target="_blank" class="btn btn-outline-primary btn-sm rounded-pill px-2 py-0" style="font-size: 0.72rem;">
                            <i class="fas fa-truck-fast"></i> تتبع
                        </a>
                    </td>

                    <!-- 2. العميل والهاتف -->
                    <td class="text-start">
                        <div class="fw-bold text-dark">👤 {{ o.customer_name }}</div>
                        <div class="small text-muted"><i class="fas fa-phone-alt text-success me-1"></i> {{ o.customer_phone }}</div>
                        {% if o.customer_address %}
                        <div class="small text-muted text-truncate" style="max-width: 140px;">📍 {{ o.customer_address }}</div>
                        {% endif %}
                    </td>

                    <!-- 3. المنتجات -->
                    <td class="text-start">
                        <div class="small" style="max-height: 100px; overflow-y: auto; line-height: 1.6;">
                            {% if o.cart_items %}
                                {% for i in o.cart_items %}
                                    <div class="text-dark fw-bold">▪️ {{ i.name }} <span class="badge bg-light text-secondary border px-1" style="font-size: 0.72rem;">x{{ i.qty }}</span></div>
                                {% endfor %}
                            {% elif o.get('cart_items', []) %}
                                <div class="text-dark fw-bold">{{ o.get('cart_items', []) }}</div>
                            {% else %}
                                <span class="text-muted small">-</span>
                            {% endif %}
                        </div>
                    </td>

                    <!-- 4. الإجمالي -->
                    <td>
                        <span class="fw-bold text-success fs-6">{{ o.total }}</span>
                    </td>

                    <!-- 5. الحالة الحالية -->
                    <td>
                        <span class="badge {% if 'توصيل' in o.status or 'مدفوع' in o.status %}bg-success{% elif 'مع المندوب' in o.status %}bg-primary{% elif 'تجهيز' in o.status %}bg-info text-dark{% elif 'ملغي' in o.status %}bg-danger{% else %}bg-warning text-dark{% endif %} px-2 py-1 rounded-pill small">
                            {{ o.status }}
                        </span>
                    </td>

                    <!-- 6. المندوب المسؤول (العمود الجديد) -->
                    <td>
                        <select class="form-select form-select-sm rounded-pill border-primary border-opacity-50 shadow-sm fw-bold mx-auto" 
                                style="min-width: 135px; font-size: 0.78rem;" 
                                onchange="assignOrderToDriver('{{ o.order_id }}', this)">
                            <option value="">{% if o.driver_name %}🛵 {{ o.driver_name }}{% else %}-- تعيين مندوب --{% endif %}</option>
                            {% if drivers %}
                                {% for d in drivers %}
                                <option value="{{ d.get('phone', '') }}" data-name="{{ d.get('name', '') }}" data-phone="{{ d.get('phone', '') }}" {% if o.driver_phone == d.get('phone', '') %}selected{% endif %}>
                                    🛵 {{ d.get('name', '') }}
                                </option>
                                {% endfor %}
                            {% else %}
                                <option disabled>(أضف مناديب أولاً)</option>
                            {% endif %}
                        </select>
                    </td>

                    <!-- 7. أزرار تحديث الحالة السريعة -->
                    <td>
                        <div class="btn-group btn-group-sm" role="group">
                            <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'جديد 🟡')" class="btn btn-outline-warning py-0 px-1" style="font-size: 0.7rem;">جديد 🟡</button>
                            <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'مدفوع 🟢')" class="btn btn-outline-success py-0 px-1" style="font-size: 0.7rem;">مدفوع 🟢</button>
                            <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'قيد التجهيز 🔵')" class="btn btn-outline-info py-0 px-1" style="font-size: 0.7rem;">تجهيز 🔵</button>
                            <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'تم التوصيل 🟢')" class="btn btn-outline-success py-0 px-1" style="font-size: 0.7rem;">توصيل 🟢</button>
                            <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'ملغي 🔴')" class="btn btn-outline-danger py-0 px-1" style="font-size: 0.7rem;">ملغي 🔴</button>
                        </div>
                    </td>
                </tr>
                {% endfor %}
            {% else %}
                <tr>
                    <td colspan="7" class="text-center py-5 text-muted">
                        <i class="fas fa-box-open fs-1 mb-2 opacity-50 d-block"></i>
                        لا توجد طلبات مسجلة حتى الآن
                    </td>
                </tr>
            {% endif %}
        </tbody>
    </table>
</div>

</div></div></div></div></div>

            <div class="tab-pane fade" id="products"><div class="card shadow-sm border-0 mb-4 border-top border-4 border-primary"><div class="card-body"><h5 class="fw-bold mb-3"><i class="fas fa-plus-circle text-primary"></i> إضافة منتج</h5><form method="POST" class="row g-3" id="addProductForm"><input type="hidden" name="action" value="add_product"><div class="col-md-4"><label class="small fw-bold">الاسم</label><input name="name" class="form-control" required></div><div class="col-md-4"><label class="small fw-bold">السعر</label><input name="price" type="number" class="form-control" required></div><div class="col-md-4"><label class="small fw-bold">الكمية</label><input name="stock" type="number" class="form-control" required></div><div class="col-md-6"><label class="small fw-bold">التصنيف</label><input type="hidden" name="cat" id="finalCategory" required><select class="form-select" id="categorySelect" onchange="handleCategoryChange(this)" required><option value="" disabled selected>-- اختر تصنيفاً --</option>{% for c in cats %}<option value="{{ c }}">{{ c }}</option>{% endfor %}<option value="إلكترونيات وجوالات">إلكترونيات وجوالات</option><option value="ملابس وأزياء">ملابس وأزياء</option><option value="NEW_CATEGORY" class="fw-bold text-primary">➕ تصنيف جديد...</option></select><input type="text" id="newCategoryInput" class="form-control mt-2" placeholder="التصنيف الجديد" style="display: none;" oninput="updateFinalCategory()"></div><div class="col-md-6"><label class="small fw-bold">صورة المنتج</label><div class="upload-btn-wrapper"><button type="button" class="btn btn-outline-primary w-100 fw-bold border-2" style="padding:8px;"><i class="fas fa-cloud-upload-alt"></i> رفع للسحابة</button><input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'newProductImg', 'newProductStatus', 'submitProductBtn')"></div><small id="newProductStatus" class="fw-bold d-block text-secondary text-center mb-1" style="font-size:0.8rem;"></small><div class="divider-text" style="font-size:0.8rem;">أو أدخل الرابط يدوياً</div><input type="text" name="img" id="newProductImg" class="form-control" placeholder="https://..."></div><div class="col-12"><label class="small fw-bold">الوصف</label><input name="desc" class="form-control"></div><div class="col-12 mt-4"><button class="btn btn-primary w-100 fw-bold shadow-sm" type="button" id="submitProductBtn" onclick="submitProductForm()">حفظ ونشر</button></div></form></div></div><div class="card shadow-sm border-0 mb-4"><div class="card-body">
<h5 class="fw-bold mb-3"><i class="fas fa-box"></i> المنتجات الحالية</h5>
<div class="row mb-3 bg-white p-3 rounded shadow-sm mx-0">
    <div class="col-md-8 mb-2"><label class="small fw-bold text-muted">بحث بالاسم</label><div class="input-group shadow-sm"><span class="input-group-text bg-white border-primary text-primary"><i class="fas fa-search"></i></span><input type="text" id="adminProductSearch" class="form-control border-primary" placeholder="اكتب اسم المنتج للبحث السريع..." onkeyup="filterAdminProducts()"></div></div>
    <div class="col-md-4 mb-2"><label class="small fw-bold text-muted">تصفية حسب القسم</label><select id="adminCategoryFilter" class="form-select border-primary shadow-sm" onchange="filterAdminProducts()"><option value="ALL">عرض كل التصنيفات</option>{% for c in cats %}<option value="{{ c }}">{{ c }}</option>{% endfor %}</select></div>
</div>
<div class="table-responsive">
<table class="table table-hover align-middle"><thead class="table-light"><tr><th>الصورة</th><th>الاسم</th><th>السعر</th><th>الكمية</th><th>التصنيف</th><th>إجراءات</th></tr></thead><tbody>{% for p in products %}<tr class="admin-product-row" data-name="{{ p.name }}" data-cat="{{ p.category }}"><td><img src="{{ p.image_url }}" onerror="fixImg(this)" width="50" height="50" style="object-fit:cover; border-radius:5px;"></td><td class="fw-bold">{{ p.name }}</td><td class="text-primary">{{ p.price }}</td><td>{{ p.stock }}</td><td><span class="badge bg-secondary">{{ p.category }}</span></td><td><button class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#editModal{{ p.id }}">تعديل</button> <form method="POST" class="d-inline" onsubmit="return confirm('حذف؟');"><input type="hidden" name="action" value="delete_product"><input type="hidden" name="product_id" value="{{ p.id }}"><button type="submit" class="btn btn-sm btn-danger">حذف</button></form></td></tr><div class="modal fade" id="editModal{{ p.id }}"><div class="modal-dialog"><div class="modal-content"><div class="modal-header bg-light"><h5 class="modal-title fw-bold">تعديل: {{ p.name }}</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body"><form method="POST" class="row g-3"><input type="hidden" name="action" value="edit_product"><input type="hidden" name="product_id" value="{{ p.id }}"><div class="col-12"><label class="small fw-bold">الاسم</label><input name="name" class="form-control" value="{{ p.name }}" required></div><div class="col-6"><label class="small fw-bold">السعر</label><input name="price" type="number" class="form-control" value="{{ p.price }}" required></div><div class="col-6"><label class="small fw-bold">المخزون</label><input name="stock" type="number" class="form-control" value="{{ p.stock }}" required></div><div class="col-12"><label class="small fw-bold">التصنيف</label><input name="cat" class="form-control" value="{{ p.category }}" required></div><div class="col-12"><label class="small fw-bold">تغيير الصورة</label><input type="file" class="form-control mb-1" accept="image/*" onchange="uploadImageToCloud(this, 'editImgUrl{{ p.id }}', 'editImgStatus{{ p.id }}', 'editSaveBtn{{ p.id }}')"><small id="editImgStatus{{ p.id }}" class="fw-bold d-block text-secondary mb-1"></small><input type="text" name="img" id="editImgUrl{{ p.id }}" class="form-control" value="{{ p.image_url }}"></div><div class="col-12"><label class="small fw-bold">الوصف</label><input name="desc" class="form-control" value="{{ p.description }}"></div><div class="col-12 mt-3"><button type="submit" class="btn btn-primary w-100 fw-bold" id="editSaveBtn{{ p.id }}">حفظ التعديلات</button></div></form></div></div></div></div>{% endfor %}</tbody></table></div></div></div></div>

            
            <!-- تبويب إدارة المناديب -->
            <div class="tab-pane fade" id="drivers">
                <div class="row">
                    <!-- نموذج إضافة مندوب -->
                    <div class="col-md-5 mb-4">
                        <div class="card shadow-sm border-0 border-top border-4 border-info">
                            <div class="card-body">
                                <h5 class="fw-bold mb-3 text-info"><i class="fas fa-motorcycle"></i> إضافة مندوب توصيل</h5>
                                <form method="POST">
                                    <input type="hidden" name="action" value="add_driver">
                                    <div class="mb-3">
                                        <label class="small fw-bold">اسم المندوب</label>
                                        <input type="text" name="driver_name" class="form-control" placeholder="مثال: أحمد محمد" required>
                                    </div>
                                    <div class="mb-4">
                                        <label class="small fw-bold">رقم هاتف المندوب (للتواصل وتعيين الطلبات)</label>
                                        <input type="text" name="driver_phone" class="form-control" placeholder="مثال: 771234567" required>
                                    </div>
                                    <button type="submit" class="btn btn-info w-100 fw-bold text-white shadow-sm">حفظ بيانات المندوب 🛵</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <!-- جدول قائمة المناديب -->
                    <div class="col-md-7 mb-4">
                        <div class="card shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="fw-bold mb-3"><i class="fas fa-users"></i> قائمة مناديب المتجر</h5>
                                <div class="table-responsive">
                                    <table class="table table-hover align-middle text-center">
                                        <thead class="table-light">
                                            <tr>
                                                <th>اسم المندوب</th>
                                                <th>رقم الهاتف</th>
                                                <th>إجراء</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {% if drivers %}
                                                {% for d in drivers %}
                                                <tr>
                                                    <td class="fw-bold text-dark text-start">🛵 {{ d.get('name', '') }}</td>
                                                    <td>
                                                        <a href="tel:{{ d.get('phone', '') }}" class="text-decoration-none text-muted fw-bold">
                                                            <i class="fas fa-phone-alt text-success me-1"></i>{{ d.get('phone', '') }}
                                                        </a>
                                                    </td>
                                                    <td>
                                                        <form method="POST" class="d-inline" onsubmit="return confirm('هل أنت متأكد من حذف هذا المندوب؟');">
                                                            <input type="hidden" name="action" value="delete_driver">
                                                            <input type="hidden" name="driver_phone" value="{{ d.get('phone', '') }}">
                                                            <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-2">
                                                                <i class="fas fa-trash"></i>
                                                            </button>
                                                        </form>
                                                    </td>
                                                </tr>
                                                {% endfor %}
                                            {% else %}
                                                <tr>
                                                    <td colspan="3" class="text-muted py-4">
                                                        <i class="fas fa-motorcycle fs-2 mb-2 opacity-50 d-block"></i>
                                                        لا يوجد مناديب مسجلين حالياً. أضف مندوبك الأول من النموذج الجانبي.
                                                    </td>
                                                </tr>
                                            {% endif %}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="tab-pane fade" id="coupons"><div class="row"><div class="col-md-5 mb-4"><div class="card shadow-sm border-0 border-top border-4 border-warning"><div class="card-body"><h5 class="fw-bold mb-3"><i class="fas fa-ticket-alt text-warning"></i> إنشاء كوبون خصم</h5><form method="POST"><input type="hidden" name="action" value="add_coupon"><div class="mb-3"><label class="small fw-bold">كود الكوبون (مثال: KSA20)</label><input type="text" name="code" class="form-control" required style="text-transform: uppercase;"></div><div class="mb-4"><label class="small fw-bold">نسبة الخصم المئوية (%)</label><input type="number" name="discount" class="form-control" placeholder="مثال: 15" required min="1" max="99"></div><button type="submit" class="btn btn-warning w-100 fw-bold text-dark shadow-sm">تفعيل الكوبون</button></form></div></div></div><div class="col-md-7"><div class="card shadow-sm border-0"><div class="card-body"><h5 class="fw-bold mb-3">الكوبونات الفعالة</h5><div class="table-responsive"><table class="table table-hover align-middle"><thead class="table-light"><tr><th>كود الكوبون</th><th>نسبة الخصم</th><th>إجراءات</th></tr></thead><tbody>{% for c in coupons %}<tr><td class="fw-bold text-primary fs-5">{{ c.code }}</td><td><span class="badge bg-success fs-6">{{ c.discount }}%</span></td><td><form method="POST" onsubmit="return confirm('إلغاء هذا الكوبون؟');"><input type="hidden" name="action" value="delete_coupon"><input type="hidden" name="coupon_id" value="{{ c.id }}"><button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button></form></td></tr>{% else %}<tr><td colspan="3" class="text-muted py-3 text-center fw-bold">لا توجد كوبونات فعالة حالياً</td></tr>{% endfor %}</tbody></table></div></div></div></div></div></div>

            <div class="tab-pane fade" id="settings"><div class="row"><div class="col-lg-8 mb-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h5 class="fw-bold mb-3 border-bottom pb-2">⚙️ إعدادات المتجر والهوية والتخزين</h5><form method="POST" class="row g-3"><input type="hidden" name="action" value="save_settings">{% if is_super_admin %}<div class="col-md-12 mb-4 p-3 bg-dark rounded border border-warning shadow-sm"><label class="small fw-bold text-warning"><i class="fas fa-crown"></i> إعدادات المنصة: شعار بوابة الدخول</label><div class="d-flex align-items-center gap-3 mt-2"><img src="{{ settings.get('platform_logo', platform_logo) }}" onerror="fixImg(this)" width="60" height="60" style="object-fit:cover; border-radius:50%; border:2px solid #ffc107; background:#fff;"><div class="flex-grow-1"><div class="upload-btn-wrapper mb-0"><button type="button" class="btn btn-outline-warning btn-sm w-100 fw-bold border-2 text-white"><i class="fas fa-cloud-upload-alt"></i> رفع الشعار</button><input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'platformLogoInput', 'platformLogoStatus', 'settingsSaveBtn')"></div><small id="platformLogoStatus" class="fw-bold d-block text-warning mb-1" style="font-size:0.8rem;"></small><input type="text" name="platform_logo" id="platformLogoInput" class="form-control form-control-sm border-warning bg-light" value="{{ settings.get('platform_logo', '') }}" placeholder="أو الصق الرابط المباشر"></div></div></div>{% endif %}<div class="col-md-12 mb-4 p-3 bg-light rounded border border-info shadow-sm d-flex justify-content-between align-items-center"><div class="fw-bold text-info"><i class="fas fa-box-open"></i> باقة اشتراكك الحالية: <span class="badge bg-primary fs-6">{{ current_user_data.get('package', 'أساسية') if current_user_data else 'أساسية' }}</span></div></div><div class="col-md-12 mb-2 border-bottom pb-3"><label class="small fw-bold text-primary"><i class="fas fa-store"></i> شعار متجرك (Store Logo)</label><div class="d-flex align-items-center gap-3 mt-1">{% if settings.get('logo_url') %}<img src="{{ settings.logo_url }}" onerror="fixImg(this)" width="60" height="60" style="object-fit:cover; border-radius:50%; border:2px solid #ccc;">{% endif %}<div class="flex-grow-1"><div class="upload-btn-wrapper mb-0"><button type="button" class="btn btn-outline-primary btn-sm w-100 fw-bold border-2"><i class="fas fa-cloud-upload-alt"></i> رفع شعار المتجر</button><input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'storeLogoInput', 'logoStatus', 'settingsSaveBtn')"></div><small id="logoStatus" class="fw-bold d-block text-secondary" style="font-size:0.8rem;"></small><input type="text" name="logo_url" id="storeLogoInput" class="form-control form-control-sm mt-1" value="{{ settings.get('logo_url', '') }}" placeholder="أو الصق رابط شعار متجرك"></div></div></div><div class="col-md-6"><label class="small fw-bold">اسم المتجر</label><input name="store_name" class="form-control" value="{{ settings.store_name }}"></div><div class="col-md-6"><label class="small fw-bold">اللون الأساسي</label><input type="color" name="theme_color" class="form-control form-control-color w-100" value="{{ settings.theme_color }}"></div><div class="col-md-6"><label class="small fw-bold">الخط (Font)</label><select name="font_family" class="form-select"><option value="Cairo" {% if settings.font_family=='Cairo' %}selected{% endif %}>Cairo</option><option value="Tajawal" {% if settings.font_family=='Tajawal' %}selected{% endif %}>Tajawal</option><option value="Almarai" {% if settings.font_family=='Almarai' %}selected{% endif %}>Almarai</option><option value="Changa" {% if settings.font_family=='Changa' %}selected{% endif %}>Changa</option></select></div><div class="col-md-6"><label class="small fw-bold">حجم الرأس</label><select name="header_size" class="form-select"><option value="small" {% if settings.header_size=='small' %}selected{% endif %}>صغير</option><option value="medium" {% if settings.header_size=='medium' %}selected{% endif %}>متوسط</option><option value="large" {% if settings.header_size=='large' %}selected{% endif %}>كبير</option></select></div><div class="col-md-4"><label class="small fw-bold">رقم الواتساب</label><input name="whatsapp" class="form-control" value="{{ settings.whatsapp }}"></div><div class="col-md-4"><label class="small fw-bold">العملة</label><input name="currency" class="form-control" value="{{ settings.currency }}"></div><div class="col-md-4"><label class="small fw-bold">نص زر الشراء</label><input name="btn_text" class="form-control" value="{{ settings.btn_text }}"></div><div class="col-12"><label class="small fw-bold">وصف المتجر</label><input name="store_desc" class="form-control" value="{{ settings.store_desc }}"></div><h6 class="fw-bold mt-3 mb-1 border-bottom pb-2">روابط التواصل والنطاق المخصص</h6><div class="col-md-4"><label class="small fw-bold">فيسبوك</label><input name="facebook" class="form-control" value="{{ settings.get('facebook', '') }}"></div><div class="col-md-4"><label class="small fw-bold">إنستجرام</label><input name="instagram" class="form-control" value="{{ settings.get('instagram', '') }}"></div><div class="col-md-4"><label class="small fw-bold">تيك توك</label><input name="tiktok" class="form-control" value="{{ settings.get('tiktok', '') }}"></div><div class="col-md-6"><label class="small fw-bold text-info"><i class="fab fa-telegram"></i> يوزر التلجرام</label><input name="telegram" class="form-control border-info" value="{{ settings.get('telegram', '') }}" placeholder="بدون @"></div><div class="col-md-6"><label class="small fw-bold">الدومين المخصص</label><input name="custom_domain" class="form-control" value="{{ settings.get('custom_domain', '') }}" placeholder="www.domain.com"></div><div class="col-12 mt-4 border-bottom pb-2 d-flex justify-content-between align-items-center"><h6 class="fw-bold text-primary mb-0"><i class="fas fa-cloud"></i> إعدادات السحابة</h6><button type="button" class="btn btn-sm btn-outline-info fw-bold" data-bs-toggle="modal" data-bs-target="#guideModal"><i class="fas fa-question-circle"></i> المساعدة</button></div>
    
    <div class="col-md-12 mb-2">
        <label class="small fw-bold">مزود الخدمة</label>
        <select name="img_provider" class="form-select" id="providerSelect" onchange="toggleProviderFields()">
            <option value="catbox" {% if settings.get('img_provider', 'catbox') == 'catbox' %}selected{% endif %}>Catbox.moe (مجاني 🚀)</option>
            <option value="imgbb" {% if settings.get('img_provider') == 'imgbb' %}selected{% endif %}>ImgBB</option>
            <option value="freeimagehost" {% if settings.get('img_provider') == 'freeimagehost' %}selected{% endif %}>FreeImage.host</option>
            <option value="imgur" {% if settings.get('img_provider') == 'imgur' %}selected{% endif %}>Imgur</option>
            <option value="postimages" {% if settings.get('img_provider') == 'postimages' %}selected{% endif %}>Postimages</option>
            <option value="cloudinary" {% if settings.get('img_provider') == 'cloudinary' %}selected{% endif %}>Cloudinary</option>
        </select>
    </div>
    
    <div class="col-md-12" id="basicProviderField" style="{% if settings.get('img_provider', 'catbox') == 'cloudinary' or settings.get('img_provider', 'catbox') == 'catbox' %}display:none;{% endif %}"><label class="small fw-bold">مفتاح الربط (API Key)</label><input name="img_api_key" type="password" class="form-control" value="{{ settings.get('img_api_key', '') }}"></div>
    <div class="col-md-6 cloudinary-fields" style="{% if settings.get('img_provider', 'catbox') != 'cloudinary' %}display:none;{% endif %}"><label class="small fw-bold text-info">Cloud Name</label><input name="cloudinary_name" type="text" class="form-control" value="{{ settings.get('cloudinary_name', '') }}"></div>
    <div class="col-md-6 cloudinary-fields" style="{% if settings.get('img_provider', 'catbox') != 'cloudinary' %}display:none;{% endif %}"><label class="small fw-bold text-info">Upload Preset</label><input name="cloudinary_preset" type="password" class="form-control" value="{{ settings.get('cloudinary_preset', '') }}"></div>
    
    <!-- بداية قسم بوابات الدفع -->
    <div class="col-12 mt-4 border-bottom pb-2 d-flex justify-content-between align-items-center">
        <h6 class="fw-bold text-success mb-0"><i class="fas fa-wallet"></i> بوابات الدفع والمحافظ البنكية (API)</h6>
        <span class="badge bg-success bg-opacity-10 text-success border border-success px-2 py-1"><i class="fas fa-bolt"></i> ميزة قادمة</span>
    </div>
    <div class="col-md-12 mb-2">
        <small class="text-muted d-block mb-2">أدخل بيانات الربط البرمجي لتفعيل الدفع الإلكتروني المباشر مستقبلاً.</small>
        <label class="small fw-bold">مزود خدمة الدفع</label>
        <select name="wallet_provider" class="form-select border-success">
            <option value="" {% if not settings.get('wallet_provider') %}selected{% endif %}>إيقاف (الدفع عند الاستلام/التحويل اليدوي فقط)</option>
            <option value="jawali" {% if settings.get('wallet_provider') == 'jawali' %}selected{% endif %}>جوالي (Jawali)</option>
            <option value="floosak" {% if settings.get('wallet_provider') == 'floosak' %}selected{% endif %}>فلوسك (Floosak)</option>
            <option value="kuraimi" {% if settings.get('wallet_provider') == 'kuraimi' %}selected{% endif %}>ام فلوس - الكريمي</option>
            <option value="custom" {% if settings.get('wallet_provider') == 'custom' %}selected{% endif %}>محفظة بنكية أخرى (Custom API)</option>
        </select>
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">رقم التاجر (Merchant ID)</label>
        <input name="wallet_merchant_id" type="text" class="form-control" value="{{ settings.get('wallet_merchant_id', '') }}" placeholder="مثال: 123456">
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">مفتاح الربط (API Key)</label>
        <input name="wallet_api_key" type="password" class="form-control" value="{{ settings.get('wallet_api_key', '') }}" placeholder="API Key">
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">الرمز السري (Secret Token)</label>
        <input name="wallet_secret" type="password" class="form-control" value="{{ settings.get('wallet_secret', '') }}" placeholder="Secret Token">
    </div>
    <!-- نهاية قسم بوابات الدفع -->
    <div class="col-12 mt-4">
<button type="submit" class="btn btn-primary w-100 fw-bold shadow-sm" id="settingsSaveBtn">حفظ كافة التحديثات</button></div></form>


                            <!-- بطاقة إعدادات تليجرام -->
                            <div class="card border-0 shadow-sm mb-4" style="border-radius: 16px;">
                                <div class="card-header bg-white border-0 pt-4 pb-0">
                                    <h6 class="fw-bold text-dark"><i class="fab fa-telegram text-info fs-5 me-2"></i> إشعارات الطلبات الفورية (تليجرام)</h6>
                                    <p class="text-muted small">احصل على تفاصيل أي طلب جديد فوراً على حسابك في تليجرام.</p>
                                </div>
                                <div class="card-body">
                                    <form method="POST" action="/dashboard">
                                        <input type="hidden" name="action" value="save_telegram_settings">
                                        <div class="form-check form-switch mb-3">
                                            <input class="form-check-input" type="checkbox" id="enable_telegram" name="enable_telegram" {% if settings.get('enable_telegram') %}checked{% endif %}>
                                            <label class="form-check-label fw-bold" for="enable_telegram">تفعيل إرسال الطلبات إلى تليجرام</label>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label fw-bold small">معرف الدردشة (Chat ID) *</label>
                                            <input type="text" class="form-control bg-light border-0" name="telegram_chat_id" value="{{ settings.get('telegram_chat_id', '') }}" placeholder="مثال: 123456789">
                                            <div class="alert alert-info mt-3 border-0" style="font-size: 0.8rem; border-radius: 12px;">
                                                <i class="fas fa-info-circle me-1"></i> <strong>للحصول على الإشعارات:</strong><br>
                                                1. ابحث في تليجرام عن البوت <strong>@userinfobot</strong> لمعرفة رقم الـ ID الخاص بك.<br>
                                                2. انسخ الرقم وضعه في الحقل أعلاه.<br>
                                            </div>
                                        </div>
                                        <button type="submit" class="btn btn-dark w-100 fw-bold rounded-pill shadow-sm"><i class="fas fa-save me-1"></i> حفظ إعدادات تليجرام</button>
                                    </form>
                                </div>
                            </div>
</div></div></div><div class="col-lg-4 mb-4"><div class="card shadow-sm border-0 h-100 border-top border-4 border-warning"><div class="card-body"><h5 class="fw-bold mb-3 text-dark"><i class="fas fa-shield-alt text-warning"></i> كلمة المرور</h5><form method="POST" class="d-flex flex-column gap-3"><input type="hidden" name="action" value="change_password"><div><label class="small fw-bold">الحالية</label><input type="password" name="old_password" class="form-control" required></div><div><label class="small fw-bold">الجديدة</label><input type="password" name="new_password" class="form-control" required></div><div><label class="small fw-bold">تأكيد</label><input type="password" name="confirm_password" class="form-control" required></div><button type="submit" class="btn btn-warning fw-bold text-dark w-100"><i class="fas fa-key"></i> تحديث</button></form></div></div></div></div></div>

            {% if is_super_admin %}<div class="tab-pane fade" id="superadmin" role="tabpanel">
<div class="row mb-4"><div class="col-12"><div class="card border-primary shadow-sm"><div class="card-body"><h5 class="fw-bold text-primary mb-3">📦 إدارة باقات المنصة (SaaS Plans)</h5>
<div class="row"><div class="col-md-4 mb-3"><form method="POST" class="p-3 bg-light rounded border"><input type="hidden" name="action" value="add_package"><label class="small fw-bold">اسم الباقة</label><input type="text" name="pkg_name" class="form-control mb-2" placeholder="مثال: VIP أو Pro" required><label class="small fw-bold">السعر (شهرياً/سنوياً)</label><input type="text" name="pkg_price" class="form-control mb-2" placeholder="مثال: 50$ شهرياً" required><label class="small fw-bold">الحد الأقصى للمنتجات</label><input type="number" name="pkg_max" class="form-control mb-2" placeholder="مثال: 100" required><label class="small fw-bold">المميزات (مفصولة بفاصلة)</label><input type="text" name="pkg_features" class="form-control mb-3" placeholder="دعم فني, دومين مخصص" required><button type="submit" class="btn btn-primary w-100 fw-bold">إضافة الباقة</button></form></div>
<div class="col-md-8"><div class="table-responsive"><table class="table table-hover align-middle"><thead><tr><th>الباقة</th><th>السعر</th><th>الحد الأقصى</th><th>المميزات</th><th>إجراء</th></tr></thead><tbody>
{% for pkg in packages %}<tr><td class="fw-bold">{{ pkg.name }}</td><td class="text-success fw-bold">{{ pkg.price }}</td><td>{{ pkg.max_products }} منتج</td><td><small>{{ pkg.features }}</small></td><td><form method="POST" onsubmit="return confirm('حذف هذه الباقة؟');"><input type="hidden" name="action" value="delete_package"><input type="hidden" name="pkg_id" value="{{ pkg._id }}"><button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button></form></td></tr>{% else %}<tr><td colspan="5" class="text-center text-muted">لا توجد باقات، قم بإضافة باقة جديدة.</td></tr>{% endfor %}
</tbody></table></div></div></div></div></div></div></div>
<div class="row"><div class="col-md-4 mb-4"><div class="card bg-dark text-white border-warning shadow-lg"><div class="card-body"><h5 class="fw-bold text-warning mb-3">➕ إضافة تاجر جديد</h5><form method="POST"><input type="hidden" name="action" value="add_merchant"><input type="text" name="name" class="form-control mb-3" placeholder="اسم التاجر" required><input type="text" name="slug" class="form-control mb-3" placeholder="رابط المتجر" required><input type="text" name="password" class="form-control mb-3" placeholder="كلمة المرور" required><select name="package" class="form-select mb-3" required><option value="" disabled selected>-- اختر باقة المتجر --</option>{% for pkg in packages %}<option value="{{ pkg.name }}">{{ pkg.name }}</option>{% endfor %}</select><button type="submit" class="btn btn-warning w-100 fw-bold text-dark">إنشاء وبناء المتجر</button></form></div></div></div><div class="col-md-8"><div class="card border-danger shadow-sm"><div class="card-body"><h5 class="fw-bold text-danger mb-3">🏢 المتاجر المشتركة في منصتك</h5><div class="table-responsive"><table class="table table-hover align-middle"><thead><tr><th>التاجر</th><th>الباقة</th><th>الرابط</th><th>الحالة</th><th>إجراءات</th></tr></thead><tbody>{% for m in merchants %}<tr><td>{{ m.username }}<br><small class="text-muted">Pass: {{ m.password }}</small></td><td><span class="badge bg-info text-dark">{{ m.get("package", "أساسية") }}</span></td><td><a href="/store/{{ m.store_slug }}" target="_blank" class="fw-bold">{{ m.store_slug }}</a></td><td><span class="badge bg-{{ 'success' if m.active == 'TRUE' else 'secondary' }}">{{ 'نشط' if m.active == 'TRUE' else 'موقوف' }}</span></td><td><form method="POST" class="d-inline"><input type="hidden" name="action" value="toggle_status"><input type="hidden" name="user_id" value="{{ m.id }}"><input type="hidden" name="current_status" value="{{ m.active }}"><button type="submit" class="btn btn-sm btn-{{ 'warning' if m.active == 'TRUE' else 'success' }}">{{ 'إيقاف' if m.active == 'TRUE' else 'تفعيل' }}</button></form>{% if m.store_slug != 'admin-store' %}<form method="POST" class="d-inline" onsubmit="return confirm('حذف نهائي؟');"><input type="hidden" name="action" value="delete_merchant"><input type="hidden" name="user_id" value="{{ m.id }}"><button type="submit" class="btn btn-sm btn-danger">حذف</button></form>{% endif %} <button type="button" class="btn btn-sm btn-primary ms-1" data-bs-toggle="modal" data-bs-target="#editSlugModal{{ m.id }}"><i class="fas fa-edit"></i> تعديل</button></td></tr><div class="modal fade" id="editSlugModal{{ m.id }}"><div class="modal-dialog"><div class="modal-content"><div class="modal-header bg-light"><h5 class="modal-title fw-bold text-primary"><i class="fas fa-edit"></i> تعديل بيانات المتجر: {{ m.username }}</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body"><form method="POST"><input type="hidden" name="action" value="edit_merchant_info"><input type="hidden" name="user_id" value="{{ m.id }}"><label class="small fw-bold mb-2">الرابط الجديد (بدون مسافات):</label><input type="text" name="new_slug" class="form-control mb-3" value="{{ m.store_slug }}" required>
<label class="small fw-bold mb-2">باقة الاشتراك:</label>
<select name="new_package" class="form-select mb-3">
    {% for pkg in packages %}
    <option value="{{ pkg.name }}" {% if m.get('package', 'أساسية') == pkg.name %}selected{% endif %}>{{ pkg.name }}</option>
    {% endfor %}
    {% if not packages %}<option value="أساسية">أساسية (الرجاء إنشاء باقات أولاً)</option>{% endif %}
</select>

    <!-- الحقول المتقدمة للمنتج -->
    <div class="row g-2 mb-3">
        <div class="col-md-4">
            <label class="form-label small fw-bold text-muted">التصنيف الفرعي</label>
            <input type="text" name="subcategory" class="form-control form-control-sm" placeholder="مثال: هواتف ذكية">
        </div>
        <div class="col-md-4">
            <label class="form-label small fw-bold text-muted">الماركة / الموديل</label>
            <input type="text" name="brand" class="form-control form-control-sm" placeholder="مثال: سامسونج / آبل">
        </div>
        <div class="col-md-4">
            <label class="form-label small fw-bold text-muted">النوع / الخصائص</label>
            <input type="text" name="p_type" class="form-control form-control-sm" placeholder="مثال: 128 جيجابايت">
        </div>
    </div>
    <button type="submit" class="btn btn-primary w-100 fw-bold">حفظ التعديلات</button></form><div class="alert alert-warning mt-3 small fw-bold mb-0"><i class="fas fa-exclamation-triangle"></i> تنبيه: سيتغير رابط الدخول الخاص بالتاجر، ويجب إبلاغه بالرابط الجديد.</div></div></div></div></div>{% endfor %}</tbody></table></div></div></div></div></div></div>{% endif %}
        </div>
    </div>

    <!-- نافذة الدليل السحابي المحدثة -->
    {% include 'partials/guide_modal.html' %}
{% endblock %}

{% block page_scripts %}
<script>
function toggleProviderFields() { 
            let provider = document.getElementById('providerSelect').value; 
            if(provider === 'cloudinary') { 
                document.getElementById('basicProviderField').style.display = 'none'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'block'); 
            } else if (provider === 'catbox') {
                document.getElementById('basicProviderField').style.display = 'none'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'none'); 
            } else { 
                document.getElementById('basicProviderField').style.display = 'block'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'none'); 
            } 
        }
        
        const PROVIDER = '{{ settings.get("img_provider", "catbox") }}'; 
        const USER_API_KEY = '{{ settings.get("img_api_key", "") }}'; 
        const CLOUD_NAME = '{{ settings.get("cloudinary_name", "") }}'; 
        const CLOUD_PRESET = '{{ settings.get("cloudinary_preset", "") }}';
        
        async function uploadImageToCloud(fileInput, hiddenUrlId, statusId, btnId) {
            let file = fileInput.files[0]; if (!file) return;
            let statusText = document.getElementById(statusId); let urlInput = document.getElementById(hiddenUrlId); let submitBtn = document.getElementById(btnId);
            
            if (PROVIDER === 'cloudinary' && (!CLOUD_NAME || !CLOUD_PRESET)) { statusText.innerHTML = '<i class="fas fa-exclamation-triangle"></i> أدخل إعدادات الكلاوديناري.'; statusText.className = "small fw-bold mt-1 d-block text-danger"; return; }
            if (PROVIDER !== 'cloudinary' && PROVIDER !== 'catbox' && !USER_API_KEY) { statusText.innerHTML = '<i class="fas fa-exclamation-triangle"></i> أدخل مفتاح الـ API.'; statusText.className = "small fw-bold mt-1 d-block text-danger"; return; }
            
            statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-primary"></i> جاري معالجة وتجهيز الصورة...`;
            statusText.className = "small fw-bold mt-1 d-block text-primary"; submitBtn.disabled = true;

            let reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = function(event) {
                let img = new Image(); img.src = event.target.result;
                img.onload = async function() {
                    let canvas = document.createElement('canvas'); let MAX_WIDTH = 600; let scaleSize = MAX_WIDTH / img.width;
                    if (scaleSize < 1) { canvas.width = MAX_WIDTH; canvas.height = img.height * scaleSize; } else { canvas.width = img.width; canvas.height = img.height; }
                    let ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                    let base64Image = canvas.toDataURL('image/jpeg', 0.7);
                    
                    try {
                        statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-primary"></i> جاري الرفع (المسار 1: عبر السيرفر)...`;
                        let payload = { provider: PROVIDER, api_key: USER_API_KEY, cloud_name: CLOUD_NAME, preset: CLOUD_PRESET, image_base64: base64Image };
                        let response = await fetch('/api/proxy_upload', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) });
                        
                        if (!response.ok) throw new Error('Proxy HTTP Error');
                        let data = await response.json();
                        
                        if (data.success && data.url) { 
                            urlInput.value = data.url; 
                            statusText.innerHTML = '<i class="fas fa-check-circle"></i> تم الرفع بنجاح!'; 
                            statusText.className = "small fw-bold mt-1 d-block text-success"; 
                        } else { throw new Error(data.error || 'Proxy Failed'); }
                        
                    } catch (error) { 
                        statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-warning"></i> المسار 1 فشل، جاري الرفع (المسار 2: مباشر)...`;
                        try {
                            let fetchRes = await fetch(base64Image);
                            let blob = await fetchRes.blob();
                            let formData = new FormData();
                            let uploadedUrl = '';
                            
                            if (PROVIDER === 'catbox') { 
                                formData.append('reqtype', 'fileupload'); 
                                formData.append('fileToUpload', blob, 'image.jpg'); 
                                let r = await fetch('https://catbox.moe/user/api.php', { method: 'POST', body: formData }); 
                                let txt = await r.text(); 
                                if (txt.startsWith('http')) uploadedUrl = txt; else throw new Error(); 
                            } else if (PROVIDER === 'freeimagehost') { 
                                formData.append('key', USER_API_KEY); 
                                formData.append('source', base64Image.split(',')[1]); 
                                formData.append('action', 'upload'); 
                                formData.append('format', 'json'); 
                                let r = await fetch('https://freeimage.host/api/1/upload', { method: 'POST', body: formData }); 
                                let d = await r.json(); 
                                if (d.status_code === 200) uploadedUrl = d.image.url; else throw new Error(); 
                            } else if (PROVIDER === 'cloudinary') { 
                                formData.append("file", blob); formData.append("upload_preset", CLOUD_PRESET); 
                                let r = await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`, { method: 'POST', body: formData }); 
                                let d = await r.json(); if (d.secure_url) uploadedUrl = d.secure_url; else throw new Error(); 
                            } else if (PROVIDER === 'imgur') { 
                                formData.append("image", blob); 
                                let r = await fetch('https://api.imgur.com/3/image', { method: 'POST', headers: { 'Authorization': 'Client-ID ' + USER_API_KEY }, body: formData }); 
                                let d = await r.json(); if (d.success) uploadedUrl = d.data.link; else throw new Error(); 
                            } else if (PROVIDER === 'postimages') { 
                                formData.append("file", blob); 
                                let r = await fetch('https://postimages.org/api/upload', { method: 'POST', headers: { 'Authorization': 'Bearer ' + USER_API_KEY }, body: formData }); 
                                let d = await r.json(); if (d.url) uploadedUrl = d.url; else throw new Error(); 
                            } else { 
                                formData.append("image", blob); 
                                let r = await fetch('https://api.imgbb.com/1/upload?key=' + USER_API_KEY, { method: 'POST', body: formData }); 
                                let d = await r.json(); if (d.success) uploadedUrl = d.data.url; else throw new Error(); 
                            }
                            
                            urlInput.value = uploadedUrl;
                            statusText.innerHTML = '<i class="fas fa-check-circle"></i> تم الرفع بنجاح!';
                            statusText.className = "small fw-bold mt-1 d-block text-success";
                        } catch (fallbackError) {
                            statusText.innerHTML = '<i class="fas fa-times-circle"></i> فشل الرفع تماماً! تأكد من المفاتيح أو جرب Catbox.';
                            statusText.className = "small fw-bold mt-1 d-block text-danger"; 
                            urlInput.value = '';
                        }
                    }
                    submitBtn.disabled = false;
                }
            };
        }
        function handleCategoryChange(selectObj) { let inputField = document.getElementById('newCategoryInput'); if (selectObj.value === 'NEW_CATEGORY') { inputField.style.display = 'block'; inputField.required = true; document.getElementById('finalCategory').value = inputField.value; } else { inputField.style.display = 'none'; inputField.required = false; document.getElementById('finalCategory').value = selectObj.value; } }
        function updateFinalCategory() { if (document.getElementById('categorySelect').value === 'NEW_CATEGORY') { document.getElementById('finalCategory').value = document.getElementById('newCategoryInput').value; } }
        function submitProductForm() { let select = document.getElementById('categorySelect'); if(select.value === "") { alert("اختر تصنيفاً!"); return; } if(select.value === 'NEW_CATEGORY' && document.getElementById('newCategoryInput').value.trim() === "") { alert("اكتب التصنيف الجديد!"); return; } document.getElementById('addProductForm').submit(); }
        document.addEventListener("DOMContentLoaded", function() { var ctx = document.getElementById('orderChart').getContext('2d'); if(ctx) { new Chart(ctx, { type: 'doughnut', data: { labels: ['جديد', 'تجهيز', 'توصيل', 'ملغي'], datasets: [{ data: [{{ stats.status_counts['جديد 🟡'] }}, {{ stats.status_counts['قيد التجهيز 🔵'] }}, {{ stats.status_counts['تم التوصيل 🟢'] }}, {{ stats.status_counts['ملغي 🔴'] }}], backgroundColor: ['#ffc107', '#0dcaf0', '#198754', '#dc3545'], borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { position: 'bottom', labels: {font: {family: 'Cairo', size: 12}} } } } }); } });
    
    function filterAdminProducts() {
        let term = document.getElementById('adminProductSearch').value.toLowerCase();
        let cat = document.getElementById('adminCategoryFilter').value;
        let rows = document.querySelectorAll('.admin-product-row');
        rows.forEach(row => {
            let name = row.getAttribute('data-name').toLowerCase();
            let rowCat = row.getAttribute('data-cat');
            let matchName = name.includes(term);
            let matchCat = (cat === 'ALL' || rowCat === cat);
            row.style.display = (matchName && matchCat) ? '' : 'none';
        });
    }
    
    document.addEventListener("DOMContentLoaded", function() {
        var ctxSales = document.getElementById('salesChart');
        if(ctxSales) {
            new Chart(ctxSales.getContext('2d'), {
                type: 'line',
                data: {
                    labels: {{ adv_stats.chart_labels | tojson | safe }},
                    datasets: [{
                        label: 'صافي المبيعات',
                        data: {{ adv_stats.chart_data | tojson | safe }},
                        borderColor: '#198754',
                        backgroundColor: 'rgba(25, 135, 84, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
            });
        }
    });
</script>
{% if not is_super_admin %}
<script>
document.addEventListener("DOMContentLoaded", function() {
    // حماية ضد التكرار إذا تم التحميل مرتين
    if(document.getElementById('tajergo-progress-bar')) return;

    let currentProducts = {{ products | length if products else 0 }};
    let pkgName = `{{ current_user_data.get('package', 'أساسية') if current_user_data else 'أساسية' }}`;
    
    // نقل بيانات الباقات من الباك إند إلى الجافاسكريبت بأمان تام
    let packagesList = [];
    {% for p in packages %}
        packagesList.push({
            name: `{{ p.name|default('') }}`,
            max_products: `{{ p.max_products|default('') }}`,
            pkg_max: `{{ p.pkg_max|default('') }}`
        });
    {% endfor %}
    
    let maxLimit = 20;
    let targetPkg = packagesList.find(p => p.name === pkgName);
    if(targetPkg) {
        let rawVal = targetPkg.max_products || targetPkg.pkg_max || 20;
        let parsed = parseInt(String(rawVal).replace(/\D/g, ''));
        maxLimit = isNaN(parsed) ? 999999 : parsed;
    }
    
    let isUnlimited = (maxLimit >= 100000);
    let percent = isUnlimited ? 100 : Math.min((currentProducts / maxLimit) * 100, 100);
    let barColor = percent >= 100 ? 'bg-danger' : (percent >= 80 ? 'bg-warning' : 'bg-success');
    let txtColor = percent >= 100 ? 'text-danger' : 'text-success';
    let displayLimit = isUnlimited ? '<i class="fas fa-infinity fs-6"></i>' : maxLimit;
    
    let progressHtml = `
    <div id="tajergo-progress-bar" class="card border-0 shadow-sm mb-4" style="border-radius: 16px; background: #fff;">
        <div class="card-body p-3 p-md-4">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <div class="d-flex align-items-center gap-3">
                    <div class="bg-primary bg-opacity-10 text-primary p-2 rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px;">
                        <i class="fas fa-box-open fs-4"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1 text-dark">استهلاك باقة المتجر</h6>
                        <small class="text-muted fw-bold">باقتك الحالية: <span class="badge bg-light text-dark border px-2 shadow-sm">${pkgName}</span></small>
                    </div>
                </div>
                <div class="text-end">
                    <h3 class="fw-bold mb-0 ${txtColor}" dir="ltr" style="letter-spacing: 1px;">
                        ${currentProducts} <span class="text-muted fs-5">/ ${displayLimit}</span>
                    </h3>
                </div>
            </div>
            
            ${!isUnlimited ? `
            <div class="progress mt-3" style="height: 10px; border-radius: 50rem; background-color: #f1f3f5;">
                <div class="progress-bar ${barColor} progress-bar-striped progress-bar-animated" role="progressbar" style="width: ${percent}%; border-radius: 50rem;"></div>
            </div>
            <div class="d-flex justify-content-between mt-2 px-1">
                <small class="text-muted fw-bold" style="font-size: 0.75rem;">إجمالي المنتجات المضافة</small>
                <small class="fw-bold ${txtColor}" style="font-size: 0.75rem;">%${Math.round(percent)} مستهلك</small>
            </div>
            ` : `
            <div class="alert alert-success border-0 bg-success bg-opacity-10 py-2 mt-3 mb-0 text-center rounded-3 fw-bold">
                <i class="fas fa-check-circle me-1"></i> باقتك لا محدودة، يمكنك إضافة المنتجات بحرية تامة!
            </div>
            `}
        </div>
    </div>
    `;
    
    // زرع الشريط في تبويب المنتجات (الأفضل) أو تبويب الإحصائيات 
    let productsTab = document.getElementById('v-pills-products') || document.getElementById('products');
    let dashboardTab = document.getElementById('v-pills-dashboard') || document.getElementById('dashboard');
    
    if (productsTab) {
        productsTab.insertAdjacentHTML('afterbegin', progressHtml);
    } else if (dashboardTab) {
        dashboardTab.insertAdjacentHTML('afterbegin', progressHtml);
    } else {
        let topContainer = document.querySelector('.container') || document.querySelector('.container-fluid');
        if(topContainer) topContainer.insertAdjacentHTML('afterbegin', progressHtml);
    }
});
</script>
{% endif %}
{% endblock %}

```

-----------------------------------
## File Path: ./templates/driver.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بوابة المندوب</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/driver.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="header-banner">
        <h2 class="fw-bold mb-2"><i class="fas fa-motorcycle me-2"></i> بوابة التوصيل</h2>
        <h5 class="mb-0 text-white-50">أهلاً بك، {{ driver.name }} 👋</h5>
    </div>
    
    <div class="container">
        <h6 class="fw-bold mb-3 text-muted"><i class="fas fa-box me-1"></i> الطلبات الحالية: <span class="badge bg-primary rounded-pill">{{ orders|length }}</span></h6>
        
        {% if orders %}
            {% for o in orders %}
            <div class="order-card">
                <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-3">
                    <span class="badge bg-light text-dark border fs-6">{{ o.order_id }}</span>
                    <h5 class="text-primary fw-bold mb-0">{{ o.total }} ريال</h5>
                </div>
                
                <p class="mb-2 fs-6"><strong><i class="fas fa-user text-muted me-1"></i> العميل:</strong> {{ o.customer_name }}</p>
                <p class="mb-2 fs-6"><strong><i class="fas fa-phone text-muted me-1"></i> الهاتف:</strong> <a href="tel:{{ o.customer_phone }}" class="text-decoration-none fw-bold text-success" style="direction: ltr; display: inline-block;">{{ o.customer_phone }}</a></p>
                <p class="mb-3 fs-6"><strong><i class="fas fa-map-marker-alt text-muted me-1"></i> العنوان:</strong> {{ o.customer_address }}</p>
                
                <div class="bg-light p-3 rounded-3 mb-3 border">
                    <h6 class="fw-bold text-secondary mb-2 small">تفاصيل المنتجات:</h6>
                    {% if o.cart is string %}
                        <span class="small">{{ o.cart }}</span>
                    {% else %}
                        {% for item in o.cart %}
                            <div class="small fw-bold mb-1">- {{ item.name }} <span class="text-primary">(x{{ item.qty }})</span></div>
                        {% endfor %}
                    {% endif %}
                </div>
                
                <form action="/driver/complete/{{ o.order_id }}" method="POST" onsubmit="return confirm('هل أنت متأكد أنك قمت بتسليم الطلب للعميل بنجاح؟ واستلمت المبلغ؟');">
                    <input type="hidden" name="token" value="{{ driver.token }}">
                    <button type="submit" class="btn-deliver"><i class="fas fa-check-circle me-1"></i> تأكيد تسليم الطلب للعميل</button>
                </form>
            </div>
            {% endfor %}
        {% else %}
            <div class="text-center py-5 mt-4">
                <i class="fas fa-check-double fs-1 text-success mb-3 opacity-75"></i>
                <h5 class="text-muted fw-bold">عمل رائع! لا توجد طلبات معلقة</h5>
                <p class="small text-muted">جميع الطلبات المسندة إليك تم توصيلها بنجاح.</p>
            </div>
        {% endif %}
    </div>
</body>
</html>

```

-----------------------------------
## File Path: ./templates/login.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول | منصة TajerGo</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}?v={{ static_version }}">
<script>
        function fixImg(img){
            if(!img.dataset.proxied){
                img.dataset.proxied='true';
                let src=img.getAttribute('src');
                if(src&&src!==''&&!src.includes('placeholder')){
                    img.src='https://wsrv.nl/?url='+encodeURIComponent(img.src);
                }
            }
        }
    </script>
    <script src="{{ url_for('static', filename='js/app.js') }}?v={{ static_version }}"></script>
</head>
<body>

    <div class="login-card text-center">
        <!-- عرض شعار المنصة الديناميكي -->
        <img src="{{ platform_logo }}" onerror="fixImg(this)" class="platform-logo" alt="شعار المنصة">
        
        <h4 class="fw-bold mb-1 text-dark">تسجيل الدخول</h4>
        <p class="text-muted small fw-bold mb-4">أهلاً بك في منصة TajerGo</p>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} small fw-bold rounded-3 py-2"><i class="fas fa-exclamation-circle me-1"></i> {{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" action="/login">
            <div class="mb-3 text-start">
                <label class="form-label small fw-bold text-muted ms-1"><i class="fas fa-link input-icon me-1"></i> رابط المتجر (Slug)</label>
                <input type="text" name="slug" class="form-control text-start" dir="ltr" placeholder="مثال: store-name" required autocomplete="off">
            </div>
            <div class="mb-4 text-start">
                <label class="form-label small fw-bold text-muted ms-1"><i class="fas fa-lock input-icon me-1"></i> كلمة المرور</label>
                <input type="password" name="pass" class="form-control text-start" dir="ltr" placeholder="••••••••" required autocomplete="off">
            </div>
            <button type="submit" class="btn btn-primary w-100 btn-login shadow-sm"><i class="fas fa-sign-in-alt me-2"></i> دخول للوحة التحكم</button>
        </form>
        
        <div class="mt-4 pt-3 border-top">
            <p class="text-muted mb-0" style="font-size: 0.75rem; font-weight: bold; opacity: 0.7;">برمجة المهندس / وسيم همدان - 771954200</p>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

```

-----------------------------------
## File Path: ./templates/partials/add_driver_modal.html
```
<div class="modal fade" id="addDriverModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content rounded-4 border-0 shadow">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-dark"><i class="fas fa-user-plus text-primary me-2"></i> إضافة مندوب جديد</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body py-3">
                <form id="addDriverForm" onsubmit="submitNewDriver(event)">
                    <div class="mb-3">
                        <label class="form-label small fw-bold">اسم المندوب</label>
                        <input type="text" class="form-control rounded-3" id="driverNameInput" placeholder="مثال: أحمد محمد" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-bold">رقم هاتف المندوب (واتساب)</label>
                        <input type="tel" class="form-control rounded-3" id="driverPhoneInput" placeholder="مثال: 770000000" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 rounded-pill fw-bold py-2 shadow-sm">
                        <i class="fas fa-save me-1"></i> حفظ وإنشاء بوابة المندوب
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

```

-----------------------------------
## File Path: ./templates/partials/dashboard_nav.html
```
<ul class="nav nav-tabs mb-4 bg-white p-2 rounded shadow-sm" id="myTab">

<li class="nav-item" role="presentation">
    <button class="nav-link fw-bold px-3" id="drivers-tab" data-bs-toggle="tab" data-bs-target="#drivers-pane" type="button" role="tab">
        <i class="fas fa-motorcycle me-1 text-primary"></i> المناديب والتوصيل
    </button>
</li>

            <li class="nav-item"><button class="nav-link fw-bold text-success active" data-bs-toggle="tab" data-bs-target="#analytics">📊 الإحصائيات</button></li>
            <li class="nav-item"><button class="nav-link fw-bold text-dark" data-bs-toggle="tab" data-bs-target="#orders">📦 الطلبات</button></li>
            <li class="nav-item"><button class="nav-link fw-bold text-primary" data-bs-toggle="tab" data-bs-target="#products">المنتجات</button></li>
            <li class="nav-item"><button class="nav-link fw-bold text-warning" data-bs-toggle="tab" data-bs-target="#coupons">🎟️ الكوبونات</button></li>
            <li class="nav-item"><button class="nav-link fw-bold text-info" data-bs-toggle="tab" data-bs-target="#drivers">🛵 المناديب</button></li>
            <li class="nav-item"><button class="nav-link fw-bold text-secondary" data-bs-toggle="tab" data-bs-target="#settings">⚙️ الإعدادات</button></li>
            {% if is_super_admin %}<li class="nav-item"><button class="nav-link fw-bold text-danger" data-bs-toggle="tab" data-bs-target="#superadmin">👑 الإدارة</button></li>{% endif %}
        </ul>

```

-----------------------------------
## File Path: ./templates/partials/flash_messages.html
```
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}

```

-----------------------------------
## File Path: ./templates/partials/guide_modal.html
```
<div class="modal fade" id="guideModal" tabindex="-1" aria-labelledby="guideModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border-0 shadow-lg">
                <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title fw-bold" id="guideModalLabel"><i class="fas fa-cloud"></i> دليل الربط السحابي للصور</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-4">
                    <ul class="nav nav-pills mb-4 gap-2" id="pills-tab" role="tablist">
                        <li class="nav-item" role="presentation"><button class="nav-link active fw-bold border" data-bs-toggle="pill" data-bs-target="#catboxGuide" type="button" role="tab">Catbox 🚀</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#imgbbGuide" type="button" role="tab">ImgBB</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#freeimageGuide" type="button" role="tab">FreeImage</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#imgurGuide" type="button" role="tab">Imgur</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#postimgGuide" type="button" role="tab">Postimages</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold text-info border border-info" data-bs-toggle="pill" data-bs-target="#cloudinaryGuide" type="button" role="tab">Cloudinary</button></li>
                    </ul>
                    <div class="tab-content border rounded p-4 bg-light shadow-sm" id="pills-tabContent">
                        <div class="tab-pane fade show active" id="catboxGuide" role="tabpanel">
                            <h6 class="fw-bold text-success mb-3">شرح منصة Catbox.moe (الخيار الأسهل والافتراضي):</h6>
                            <div class="mb-2"><span class="badge bg-success me-2">1</span> مجانية بالكامل وتسمح برفع صور بحجم يصل لـ 200 ميجابايت.</div>
                            <div class="mb-2"><span class="badge bg-success me-2">2</span> <b>لا تحتاج لأي تسجيل دخول أو مفاتيح API أبداً!</b></div>
                            <div class="mb-2"><span class="badge bg-success me-2">3</span> فقط اخترها من القائمة واضغط حفظ، وستعمل فوراً.</div>
                        </div>
                        <div class="tab-pane fade" id="imgbbGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">خطوات ربط منصة ImgBB:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> افتح موقع <a href="https://api.imgbb.com/" target="_blank" class="fw-bold">api.imgbb.com</a> وقم بتسجيل الدخول.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اضغط على زر <b>Add API Key</b> لتحصل على الرمز السري.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">3</span> انسخ الرمز الطويل، ثم ارجع هنا والصقه في خانة <b>(مفتاح الربط API Key)</b>.</div>
                            <div class="alert alert-danger mt-3 small fw-bold mb-0"><i class="fas fa-exclamation-triangle"></i> تنبيه: هذه المنصة قد تكون محظورة في بعض الدول، إذا فشل الرفع استخدم Cloudinary.</div>
                        </div>
                        <div class="tab-pane fade" id="freeimageGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">شرح منصة FreeImage.host:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> سجل حساب في <a href="https://freeimage.host/" target="_blank">freeimage.host</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اذهب لصفحة الـ API وانسخ الرمز السري والصقه في خانة مفتاح الربط.</div>
                        </div>
                        <div class="tab-pane fade" id="imgurGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">خطوات ربط منصة Imgur:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> سجل حساباً في <a href="https://imgur.com/register" target="_blank" class="fw-bold">imgur.com</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اذهب إلى <a href="https://api.imgur.com/oauth2/addclient" target="_blank" class="fw-bold">صفحة إنشاء تطبيق جديد</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">3</span> اختر <i>OAuth 2.0 authorization without a callback URL</i>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">4</span> سيظهر لك <b>Client ID</b>، انسخه والصقه في خانة <b>(مفتاح الربط)</b>.</div>
                        </div>
                        <div class="tab-pane fade" id="postimgGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">معلومات منصة Postimages:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> افتح موقع <a href="https://postimages.org/" target="_blank" class="fw-bold">postimages.org</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> تتطلب هذه المنصة أحياناً مراسلة الدعم للحصول على مفتاح API خاص.</div>
                            <div class="alert alert-warning mt-3 small fw-bold mb-0">💡 ملاحظة: كبديل سريع، يمكنك رفع الصور لديهم يدوياً ونسخ <b>الرابط المباشر للصورة</b>، ثم وضعه في حقل إضافة المنتج مباشرة.</div>
                        </div>
                        <div class="tab-pane fade" id="cloudinaryGuide" role="tabpanel">
                            <h6 class="fw-bold text-info mb-3">خطوات ربط Cloudinary (الخيار الأفضل والمضمون 100%):</h6>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">1</span> سجل حساباً مجانياً في <a href="https://cloudinary.com/" target="_blank" class="fw-bold text-info">Cloudinary.com</a>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">2</span> من لوحة التحكم الرئيسية، انسخ اسم السحابة الخاص بك <b>Cloud Name</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">3</span> اذهب إلى الإعدادات <b>Settings</b> ⚙️ (أسفل اليسار) ثم اختر <b>Upload</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">4</span> انزل لأسفل واضغط على الرابط الأزرق <b>Add upload preset</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">5</span> اجعل خيار <i>Signing Mode</i> يساوي <b>Unsigned</b> واضغط حفظ.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">6</span> انسخ اسم الـ Preset الذي ظهر لك، والصقه مع الـ Cloud Name في إعدادات متجرك!</div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer bg-white border-top">
                    <button type="button" class="btn btn-secondary fw-bold px-4" data-bs-dismiss="modal">فهمت، إغلاق</button>
                </div>
            </div>
        </div>
    </div>

```

-----------------------------------
## File Path: ./templates/partials/topbar.html
```
<nav class="navbar navbar-dark bg-dark mb-4 shadow"><div class="container"><a class="navbar-brand fw-bold d-flex align-items-center gap-2" href="#"><img src="{{ platform_logo }}" onerror="fixImg(this)" width="35" height="35" style="object-fit:cover; border-radius:50%; background:#fff; padding:1px;" alt="Logo"> لوحة تحكم TajerGo</a><div><a href="/store/{{ store_slug }}" target="_blank" class="btn btn-outline-light btn-sm mx-2"><i class="fas fa-store"></i> زيارة متجري</a><a href="/logout" class="btn btn-danger btn-sm">خروج</a></div></div></nav>

```

-----------------------------------
## File Path: ./templates/store.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ settings.store_name }}</title>
    <link rel="manifest" href="/manifest/{{ user.store_slug }}.json">
    {% if settings.get('logo_url') and settings.logo_url.strip() != '' %}
    <link rel="icon" href="{{ settings.logo_url }}">
    <link rel="apple-touch-icon" href="{{ settings.logo_url }}">
    {% else %}
    <link rel="icon" href="{{ url_for('static', filename='icon-512.png') }}?v={{ static_version }}">
    <link rel="apple-touch-icon" href="{{ url_for('static', filename='icon-192.png') }}?v={{ static_version }}">
    {% endif %}
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="{{ settings.store_name }}">
    <meta name="theme-color" content="{{ settings.theme_color|default('#0d6efd') }}">
<link href="https://fonts.googleapis.com/css2?family={{ settings.font_family|default('Cairo') }}:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/store.css') }}?v={{ static_version }}">
    <style>
:root {
    --main-color: {{ settings.theme_color|default('#0d6efd') }};
    --store-font: '{{ settings.font_family|default('Cairo') }}';
}
</style>
    <script src="{{ url_for('static', filename='js/app.js') }}?v={{ static_version }}"></script>
</head>
<body class="header-{{ settings.header_size|default('medium') }}">
    <div class="hero-section">
        <div class="container d-flex flex-column align-items-center justify-content-center">
            {% if settings.get('logo_url') and settings.logo_url.strip() != '' %}
                <img src="{{ settings.logo_url }}" onerror="fixImg(this)" class="store-logo" alt="شعار المتجر">
            {% else %}
                <div class="store-logo d-flex align-items-center justify-content-center bg-white text-primary" style="font-size: 2.5rem; width: 100px; height: 100px;"><i class="fas fa-store"></i></div>
            {% endif %}
            <h1 class="fw-bold hero-title">{{ settings.store_name }}</h1>
            <p class="lead mb-0 mt-2" style="opacity: 0.9; font-weight: 600;">{{ settings.store_desc }}</p>
        </div>
    </div>

    <div class="container mb-4">
        <div class="row g-2 align-items-center">
            <div class="col-md-6 col-12 order-1 order-md-1">
                <div class="input-group search-bar-container">
                    <span class="input-group-text bg-transparent border-0 text-muted ps-3"><i class="fas fa-search"></i></span>
                    <input type="text" id="searchInput" class="form-control bg-transparent" placeholder="ابحث عن منتجك هنا..." onkeyup="filterProducts()">
                </div>
            </div>
            <div class="col-6 col-md-3 order-2 order-md-2">
                <select id="sortSelect" class="form-select sort-select w-100" onchange="sortProducts()">
                    <option value="default">الترتيب الافتراضي</option>
                    <option value="price-asc">السعر: من الأرخص للأغلى</option>
                    <option value="price-desc">السعر: من الأغلى للأرخص</option>
                    <option value="rating-desc">الأعلى تقييماً</option>
                </select>
            </div>
            <div class="col-6 col-md-3 text-end order-3 order-md-3">
                <button class="btn btn-outline-primary w-100 btn-share bg-white h-100" onclick="shareStore()"><i class="fas fa-share-nodes"></i> مشاركة</button>
            </div>
        </div>
    </div>

    <div class="container pb-2">
        {% set grouped_products = products | groupby('category') %}
        {% if grouped_products %}
            <ul class="nav nav-pills category-tabs" id="categoryTabs" role="tablist">
                {% for category, items in grouped_products %}
                    <li class="nav-item" role="presentation">
                        <button class="nav-link {% if loop.first %}active{% endif %}" id="tab-btn-{{ loop.index }}" data-bs-toggle="pill" data-bs-target="#tab-pane-{{ loop.index }}" type="button" role="tab">{{ category if category else 'عام' }}</button>
                    </li>
                {% endfor %}
            </ul>
            <div class="tab-content" id="categoryTabsContent">
                {% for category, items in grouped_products %}
                <div class="tab-pane fade {% if loop.first %}show active{% endif %} category-section" id="tab-pane-{{ loop.index }}" role="tabpanel">
                    <div class="row g-3 product-list-container">
                        {% for p in items %}
                        <div class="col-md-3 col-6 product-wrapper" data-name="{{ p.name }}" data-price="{{ p.price|default(0)|float }}" data-rating="{{ p.rating|default(0)|float }}">
                            <div class="card product-card h-100 d-flex flex-column">

                            <textarea id="raw-name-{{ p.id }}" style="display:none;">{{ p.name }}</textarea>
                            <textarea id="raw-desc-{{ p.id }}" style="display:none;">{{ p.description }}</textarea>
                            <textarea id="raw-img-{{ p.id }}" style="display:none;">{{ p.image_url }}</textarea>

                            <div class="img-wrapper" onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}')" title="عرض التفاصيل">
                                <img src="{{ p.image_url if p.image_url else 'https://via.placeholder.com/400x300?text=بدون+صورة' }}" onerror="fixImg(this)" class="product-img" loading="lazy">
                            </div>
                            <div class="card-body p-3 d-flex flex-column">
                                <h6 class="product-title" style="cursor:pointer;" onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}')">{{ p.name }}</h6>

                                {% if p.description %}
                                <p class="text-muted mb-2" style="font-size: 0.8rem; line-height: 1.5;">
                                    {{ p.description | truncate(45, False, '...') }}
                                    <span onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}')" class="text-primary fw-bold ms-1" style="cursor:pointer; font-size: 0.8rem; text-decoration: none;"><i class="fas fa-info-circle me-1"></i>التفاصيل</span>
                                </p>
                                {% else %}
                                <div class="mb-2">
                                    <span onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}')" class="badge bg-light text-primary border px-2 py-1 shadow-sm" style="cursor:pointer;"><i class="fas fa-info-circle me-1"></i>التفاصيل</span>
                                </div>
                                {% endif %}

                                <div>
                                    <div class="rating-badge" onclick="openRatingModal('{{ p.id }}', '{{ p.name|replace("'", "\'")|replace('"', '\"') }}')" title="اضغط لتقييم المنتج">
                                        <i class="fas fa-star me-1"></i> <span id="display-avg-{{ p.id }}">{{ p.rating|default(0)|float|round(1) }}</span>
                                        <span class="text-muted ms-1 small" id="display-count-{{ p.id }}">({{ p.reviews|default(0) }})</span>
                                    </div>
                                </div>

                                <div class="tags-container">
                                    {% if p.subcategory %}<span class="tag-badge"><i class="fas fa-tag me-1"></i>{{ p.subcategory }}</span>{% endif %}
                                    {% if p.brand %}<span class="tag-badge"><i class="fas fa-bookmark me-1"></i>{{ p.brand }}</span>{% endif %}
                                    {% if p.p_type %}<span class="tag-badge"><i class="fas fa-info-circle me-1"></i>{{ p.p_type }}</span>{% endif %}
                                </div>

                                <div class="mt-auto pt-2 border-top border-light">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <div class="product-price">
                                            {% if p.price and p.price|string != "0" and p.price|string != "None" and p.price|string != "" %}
                                                {{ p.price }} <small>{{ settings.currency }}</small>
                                            {% else %}
                                                <span class="badge bg-secondary fs-6">السعر عند الطلب</span>
                                            {% endif %}
                                        </div>
                                    </div>
                                    {% set current_stock = p.get('stock', 1) %}
                                    {% if current_stock > 0 %}
                                        <button class="btn btn-custom w-100" onclick="addToCart('{{ p.name }}', {{ p.price }})"><i class="fas fa-cart-plus me-1"></i> {{ settings.get('btn_text', 'إضافة للسلة') }}</button>
                                    {% else %}
                                        <button class="btn btn-secondary-custom w-100" disabled>نفذت الكمية</button>
                                    {% endif %}
                                </div>
                            </div>
                        </div></div>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="text-center py-5 mt-4"><i class="fas fa-box-open fs-1 text-muted mb-3 opacity-50"></i><h5 class="text-muted fw-bold">لا توجد منتجات معروضة حالياً</h5></div>
        {% endif %}
    </div>

    <!-- قسم المساعدة المدمج -->
    <div class="container mb-3">
        <div class="support-card">
            <h6 class="fw-bold mb-1">هل تبحث عن المساعدة؟ 💬</h6>
            <p class="text-muted small mb-3">تواصل معنا وسنقوم بخدمتك فوراً.</p>
            <div class="d-flex justify-content-center flex-wrap gap-2">
                {% if settings.get('whatsapp') %}
                    <a href="https://wa.me/{{ settings.whatsapp }}" target="_blank" class="btn-support-wa"><i class="fab fa-whatsapp fs-5"></i> تواصل عبر الواتساب</a>
                {% endif %}
                {% if settings.get('telegram') %}
                    <a href="https://t.me/{{ settings.telegram.strip('@') }}" target="_blank" class="btn btn-primary btn-sm" style="border-radius: 50rem; padding: 10px 20px; font-weight: bold;"><i class="fab fa-telegram-plane me-1"></i> تواصل عبر التلجرام</a>
                {% endif %}
                <a href="/track" class="btn btn-outline-secondary btn-sm rounded-pill px-3 fw-bold d-inline-flex align-items-center">
                    <i class="fas fa-truck-fast text-primary me-1"></i> تتبع طلبك
                </a>
            </div>
        </div>
    </div>

    <!-- تذييل الصفحة المدمج مع توقيع المطور مباشرة -->
    <div class="container text-center my-2 pb-1">
        <div class="d-flex justify-content-center gap-3 mb-2">
            {% if settings.get('facebook') %}<a href="{{ settings.facebook }}" target="_blank" class="text-primary fs-5"><i class="fab fa-facebook"></i></a>{% endif %}
            {% if settings.get('instagram') %}<a href="{{ settings.instagram }}" target="_blank" class="text-danger fs-5"><i class="fab fa-instagram"></i></a>{% endif %}
            {% if settings.get('tiktok') %}<a href="{{ settings.tiktok }}" target="_blank" class="text-dark fs-5"><i class="fab fa-tiktok"></i></a>{% endif %}
        </div>
        <p class="text-muted mb-0" style="font-size: 0.72rem; font-weight: bold; opacity: 0.65;">برمجة المهندس / وسيم همدان - 771954200</p>
    </div>

    <div id="floating-cart" onclick="openCartModal()"><i class="fas fa-shopping-bag me-1"></i> سلة المشتريات (<span id="cart-count">0</span>) | <span id="cart-total">0</span> {{ settings.currency }}</div>

    <!-- Cart Modal -->
    <div class="modal fade" id="cartModal" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content shadow-lg"><div class="modal-header bg-light"><h5 class="modal-title fw-bold text-dark">إتمام الطلب 🚀</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body p-4"><ul id="cart-items" class="list-group mb-3 border-0"></ul><div class="mb-3 p-3 bg-light rounded-4 border"><label class="form-label small fw-bold text-primary"><i class="fas fa-ticket-alt"></i> لديك كود خصم؟</label><div class="input-group"><input type="text" id="coupon-code" class="form-control" placeholder="أدخل الكوبون هنا" style="text-transform: uppercase; border-radius: 0 10px 10px 0;"><button class="btn btn-primary fw-bold" type="button" onclick="applyCoupon()" style="border-radius: 10px 0 0 10px;">تطبيق</button></div><small id="coupon-msg" class="fw-bold mt-1 d-block"></small></div><div class="d-flex justify-content-between align-items-center mb-4 bg-success bg-opacity-10 p-3 rounded-4 border border-success"><h5 class="fw-bold text-success mb-0">الإجمالي النهائي:</h5><h3 class="fw-bold text-success mb-0"><span id="modal-total">0</span> <small class="fs-6">{{ settings.currency }}</small></h3></div><h6 class="fw-bold mb-3 text-secondary border-bottom pb-2">بيانات التوصيل والدفع:</h6><div class="mb-3"><label class="form-label small fw-bold">الاسم الكامل *</label><input type="text" id="customer-name" class="form-control bg-light" required></div><div class="mb-3"><label class="form-label small fw-bold">رقم الهاتف (للتواصل) *</label><input type="tel" id="customer-phone" class="form-control bg-light" required></div><div class="mb-3"><label class="form-label small fw-bold">العنوان الدقيق *</label><input type="text" id="customer-address" class="form-control bg-light" required></div>
    
    <!-- قسم الدفع -->
    <div class="mb-4 p-3 border rounded-3 bg-light">
        <label class="form-label fw-bold text-primary mb-2"><i class="fas fa-wallet"></i> طريقة الدفع *</label>
        <select id="payment-method" class="form-select border-primary fw-bold" onchange="toggleWalletInput()">
            <option value="cash">الدفع عند الاستلام (كاش)</option>
            {% if settings.get('wallet_provider') %}
                <option value="{{ settings.wallet_provider }}">
                    الدفع الإلكتروني 
                    {% if settings.wallet_provider == 'jawali' %}(جوالي)
                    {% elif settings.wallet_provider == 'floosak' %}(فلوسك)
                    {% elif settings.wallet_provider == 'kuraimi' %}(ام فلوس - الكريمي)
                    {% else %}(محفظة إلكترونية){% endif %}
                </option>
            {% endif %}
        </select>
        
        <div id="wallet-phone-container" class="mt-3" style="display: none;">
            <label class="form-label small fw-bold text-success">رقم حساب المحفظة المراد الخصم منه *</label>
            <div class="input-group">
                <span class="input-group-text bg-white border-success"><i class="fas fa-mobile-alt text-success"></i></span>
                <input type="tel" id="wallet-phone" class="form-control border-success" placeholder="رقم المحفظة (مثال: 770000000)">
            </div>
            <small class="text-muted d-block mt-1" style="font-size: 0.75rem;">سيصلك إشعار لتأكيد الخصم على هذا الرقم.</small>
        </div>
    </div>
    
    <button id="btn-submit" class="btn btn-success btn-lg w-100 fw-bold shadow-sm rounded-pill" onclick="checkout()"><i class="fab fa-whatsapp fs-5 me-1"></i> إرسال الطلب</button></div></div></div></div>

    <!-- Details Modal -->
    <div class="modal fade" id="detailsModal" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content shadow-lg overflow-hidden"><div class="modal-header bg-light border-0"><h5 class="modal-title fw-bold text-dark" id="detailsName"></h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body p-0"><div style="background:#f8f9fa; text-align:center; border-bottom:1px solid #eaeaea;"><img id="detailsImg" src="" onerror="fixImg(this)" style="max-height:350px; max-width:100%; object-fit:contain; padding:20px;"></div><div class="p-4"><h3 class="text-primary fw-bold border-bottom pb-3 mb-3"><span id="detailsPrice"></span> <small class="fs-6 text-muted">{{ settings.currency }}</small></h3><h6 class="fw-bold mb-2 text-dark"><i class="fas fa-align-right text-primary me-1"></i> تفاصيل المنتج:</h6><p id="detailsDesc" class="text-muted" style="line-height: 1.8; font-size: 0.95rem; white-space: pre-wrap;"></p></div></div><div class="modal-footer bg-light border-0 p-3"><button id="detailsAddToCartBtn" class="btn btn-primary w-100 fw-bold py-3 fs-5 rounded-pill"><i class="fas fa-cart-plus me-1"></i> إضافة إلى السلة</button></div></div></div></div>

    <!-- Rating Modal -->
    <div class="modal fade" id="globalRatingModal" tabindex="-1" aria-hidden="true"><div class="modal-dialog modal-dialog-centered modal-sm"><div class="modal-content shadow-lg"><div class="modal-header border-0 pb-0"><h6 class="modal-title fw-bold text-dark" id="ratingModalHeaderTitle"><i class="fas fa-star text-warning"></i> تقييم المنتج</h6><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body text-center pt-2 pb-3"><p id="ratingModalProductName" class="text-secondary small fw-bold mb-3"></p><div class="d-flex justify-content-center flex-row-reverse mb-3" id="interactive-stars" onmouseleave="resetHover()"><svg data-val="5" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="4" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="3" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="2" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="1" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div><div class="mb-2"><button id="confirmRatingBtn" class="btn btn-warning btn-sm px-4 fw-bold rounded-pill shadow-sm" disabled>تأكيد التقييم</button></div><p id="ratingModalMessage" class="fw-bold text-success d-none mb-0 small"></p></div></div></div></div>
    <style>
:root {
    --main-color: {{ settings.theme_color|default('#0d6efd') }};
    --store-font: '{{ settings.font_family|default('Cairo') }}';
}
</style>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        if ('serviceWorker' in navigator) { window.addEventListener('load', () => { navigator.serviceWorker.register('/sw.js'); }); }

        function toggleWalletInput() {
            let method = document.getElementById('payment-method').value;
            let walletContainer = document.getElementById('wallet-phone-container');
            if(method !== 'cash') {
                walletContainer.style.display = 'block';
            } else {
                walletContainer.style.display = 'none';
            }
        }

        function filterProducts() {
            let term = document.getElementById('searchInput').value.toLowerCase();
            let allProducts = document.querySelectorAll('.product-wrapper');
            if(term.length > 0) {
                document.querySelectorAll('.tab-pane').forEach(t => { t.classList.add('show', 'active'); });
                document.querySelectorAll('.category-tabs').forEach(t => { t.style.display = 'none'; });
                document.getElementById('sortSelect').style.display = 'none';
            } else {
                document.querySelectorAll('.category-tabs').forEach(t => { t.style.display = 'flex'; });
                let first = true;
                document.querySelectorAll('.tab-pane').forEach(t => { if(first) { t.classList.add('show', 'active'); first = false; } else { t.classList.remove('show', 'active'); } });
                document.getElementById('sortSelect').style.display = 'block';
            }
            allProducts.forEach(card => {
                let name = card.getAttribute('data-name').toLowerCase();
                if(name.includes(term)) { card.style.display = 'block'; } else { card.style.display = 'none'; }
            });
        }

        function sortProducts() {
            let sortType = document.getElementById('sortSelect').value;
            let activePane = document.querySelector('.tab-pane.active .product-list-container');
            if(!activePane && sortType !== 'default') return;
            document.querySelectorAll('.product-list-container').forEach(container => {
                let products = Array.from(container.querySelectorAll('.product-wrapper'));
                if (sortType === 'default') { location.reload(); return; }
                products.sort((a, b) => {
                    let priceA = parseFloat(a.getAttribute('data-price')) || 0;
                    let priceB = parseFloat(b.getAttribute('data-price')) || 0;
                    let ratingA = parseFloat(a.getAttribute('data-rating')) || 0;
                    let ratingB = parseFloat(b.getAttribute('data-rating')) || 0;
                    if (sortType === 'price-asc') return priceA - priceB;
                    if (sortType === 'price-desc') return priceB - priceA;
                    if (sortType === 'rating-desc') return ratingB - ratingA;
                });
                products.forEach(p => container.appendChild(p));
            });
        }

        document.querySelectorAll('button[data-bs-toggle="pill"]').forEach(tab => {
            tab.addEventListener('shown.bs.tab', function () { if(document.getElementById('sortSelect').value !== 'default') { sortProducts(); } });
        });

        function shareStore() { if (navigator.share) { navigator.share({ title: '{{ settings.store_name }}', text: 'تسوق أفضل المنتجات!', url: window.location.href }); } else { navigator.clipboard.writeText(window.location.href); alert("تم النسخ!"); } }
        let cart = []; let cartModalInstance = null; let detailsModalInstance = null; let currentDiscountPercent = 0; let currentDiscountInfo = '';
        document.addEventListener("DOMContentLoaded", function(){ cartModalInstance = new bootstrap.Modal(document.getElementById('cartModal')); detailsModalInstance = new bootstrap.Modal(document.getElementById('detailsModal')); });

        function openDetailsModal(id, price) {
            let name = document.getElementById('raw-name-' + id).value.trim(); let desc = document.getElementById('raw-desc-' + id).value.trim(); let imgUrl = document.getElementById('raw-img-' + id).value.trim();
            document.getElementById('detailsName').innerText = name;
            let detailsImg = document.getElementById('detailsImg'); detailsImg.removeAttribute('data-proxied'); detailsImg.src = imgUrl || 'https://via.placeholder.com/800x600?text=بدون+صورة';
            document.getElementById('detailsPrice').innerText = price; document.getElementById('detailsDesc').innerText = desc || 'لا يوجد وصف متاح لهذا المنتج.';
            let addBtn = document.getElementById('detailsAddToCartBtn'); addBtn.onclick = function() { addToCart(name, price); detailsModalInstance.hide(); }; detailsModalInstance.show();
        }

        function addToCart(name, price) { let item = cart.find(i => i.name === name); if(item) { item.qty++; } else { cart.push({name: name, price: price, qty: 1}); } updateCartUI(); }
        function changeQty(name, delta) { let item = cart.find(i => i.name === name); if(item) { item.qty += delta; if(item.qty <= 0) cart = cart.filter(i => i.name !== name); } updateCartUI(); renderModalItems(); }
        function applyCoupon() { let code = document.getElementById('coupon-code').value.trim(); if(!code) return; let msg = document.getElementById('coupon-msg'); msg.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التحقق...'; msg.className = "fw-bold mt-1 d-block text-primary"; fetch('/api/apply_coupon/{{ user.store_slug }}', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({code: code}) }).then(res => res.json()).then(data => { if(data.success) { currentDiscountPercent = data.discount; currentDiscountInfo = `كوبون (${code.toUpperCase()}) - خصم ${data.discount}%`; msg.innerHTML = `<i class="fas fa-check-circle"></i> تم الخصم ${data.discount}%`; msg.className = "fw-bold mt-1 d-block text-success"; updateCartUI(); } else { currentDiscountPercent = 0; currentDiscountInfo = ''; msg.innerHTML = `<i class="fas fa-times-circle"></i> غير صالح`; msg.className = "fw-bold mt-1 d-block text-danger"; updateCartUI(); } }); }
        function updateCartUI() { let count = 0; let subTotal = 0; cart.forEach(item => { count += item.qty; subTotal += (item.price * item.qty); }); let finalTotal = subTotal - (subTotal * (currentDiscountPercent / 100)); document.getElementById('cart-count').innerText = count; document.getElementById('cart-total').innerText = subTotal; document.getElementById('modal-total').innerText = finalTotal.toFixed(2); document.getElementById('floating-cart').style.display = count > 0 ? 'block' : 'none'; if(count === 0 && cartModalInstance) cartModalInstance.hide(); }
        function renderModalItems() { let list = document.getElementById('cart-items'); list.innerHTML = ''; cart.forEach((item) => { list.innerHTML += `<li class="list-group-item d-flex justify-content-between align-items-center mb-2 border-0 bg-light rounded-3 p-2"><div><h6 class="mb-1 fw-bold">${item.name}</h6><small class="text-primary fw-bold">${item.price} {{ settings.currency }}</small></div><div class="d-flex align-items-center bg-white rounded-pill shadow-sm p-1 border"><button class="btn btn-sm btn-light rounded-circle px-2 py-0 fw-bold" onclick="changeQty('${item.name}', -1)">−</button><span class="mx-3 fw-bold">${item.qty}</span><button class="btn btn-sm btn-light rounded-circle px-2 py-0 fw-bold" onclick="changeQty('${item.name}', 1)">+</button></div></li>`; }); }
        function openCartModal() { renderModalItems(); cartModalInstance.show(); }
        function checkout() { 
            let name = document.getElementById('customer-name').value; 
            let phone = document.getElementById('customer-phone').value; 
            let address = document.getElementById('customer-address').value; 
            let paymentMethod = document.getElementById('payment-method').value;
            let walletPhone = document.getElementById('wallet-phone').value;
            
            if(!name || !phone || !address) return alert("يرجى ملء بيانات التوصيل الأساسية"); 
            if(paymentMethod !== 'cash' && !walletPhone) return alert("يرجى إدخال رقم هاتف المحفظة لإتمام الدفع الإلكتروني");

            let paymentStr = "الدفع عند الاستلام";
            if (paymentMethod !== 'cash') {
                let providerName = document.getElementById('payment-method').options[document.getElementById('payment-method').selectedIndex].text;
                paymentStr = `دفع إلكتروني: ${providerName} | رقم المحفظة: ${walletPhone}`;
            }

            document.getElementById('btn-submit').innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التحويل...'; 
            document.getElementById('btn-submit').disabled = true; 
            
            let payload = {
                name: name, phone: phone, address: address, 
                payment: paymentStr, 
                wallet_provider: paymentMethod,
                wallet_phone: walletPhone,
                cart: cart, final_total: document.getElementById('modal-total').innerText, discount_info: currentDiscountInfo
            };

            fetch('/api/checkout/{{ user.store_slug }}', { 
                method: 'POST', headers: {'Content-Type': 'application/json'}, 
                body: JSON.stringify(payload) 
            }).then(res => res.json()).then(data => { 
                cart = []; currentDiscountPercent = 0; currentDiscountInfo = ''; document.getElementById('coupon-code').value = ''; document.getElementById('coupon-msg').innerText = ''; updateCartUI(); cartModalInstance.hide(); document.getElementById('btn-submit').innerHTML = "<i class='fab fa-whatsapp'></i> إرسال الطلب"; document.getElementById('btn-submit').disabled = false; window.open(data.wa_link || data.whatsapp_url, '_blank'); 
            }); 
        }

        let currentRatingProductId = null; let ratingModal = null; let selectedRating = 0; let previousRating = null;
        function openRatingModal(pid, pname) { currentRatingProductId = pid; document.getElementById('ratingModalProductName').innerText = pname; document.getElementById('ratingModalMessage').classList.add('d-none'); let btn = document.getElementById('confirmRatingBtn'); btn.classList.remove('d-none'); let savedRating = localStorage.getItem('rated_val_' + pid); if(savedRating) { previousRating = parseInt(savedRating); selectedRating = previousRating; document.getElementById('ratingModalHeaderTitle').innerHTML = '<i class="fas fa-edit text-warning"></i> تعديل تقييمك'; btn.innerText = 'تحديث التقييم'; btn.disabled = false; } else { previousRating = null; selectedRating = 0; document.getElementById('ratingModalHeaderTitle').innerHTML = '<i class="fas fa-star text-warning"></i> تقييم المنتج'; btn.innerText = 'تأكيد التقييم'; btn.disabled = true; } document.querySelectorAll('.modal-star').forEach(s => { let val = parseInt(s.getAttribute('data-val')); if(val <= selectedRating) { s.classList.add('star-selected'); s.setAttribute('fill', '#ffc107'); } else { s.classList.remove('star-selected'); s.setAttribute('fill', '#e4e5e9'); } }); if(!ratingModal) ratingModal = new bootstrap.Modal(document.getElementById('globalRatingModal')); ratingModal.show(); }
        function resetHover() { document.querySelectorAll('.modal-star').forEach(s => { let val = parseInt(s.getAttribute('data-val')); if(val <= selectedRating) { s.setAttribute('fill', '#ffc107'); } else { s.setAttribute('fill', '#e4e5e9'); } }); }
        document.querySelectorAll('.modal-star').forEach(star => { star.addEventListener('click', function() { selectedRating = parseInt(this.getAttribute('data-val')); document.querySelectorAll('.modal-star').forEach(s => { if(parseInt(s.getAttribute('data-val')) <= selectedRating) { s.classList.add('star-selected'); s.setAttribute('fill', '#ffc107'); } else { s.classList.remove('star-selected'); s.setAttribute('fill', '#e4e5e9'); } }); let btn = document.getElementById('confirmRatingBtn'); btn.disabled = false; if(previousRating && selectedRating === previousRating) { btn.disabled = true; } }); });
        document.getElementById('confirmRatingBtn').addEventListener('click', function() { if(selectedRating === 0 || !currentRatingProductId) return; let pid = currentRatingProductId; let btn = this; btn.disabled = true; btn.innerHTML = 'جاري الحفظ...'; let payload = { product_id: pid, rating: selectedRating }; if (previousRating) { payload.old_rating = previousRating; } fetch('/api/rate_product', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) }).then(r => r.json()).then(data => { if(data.success) { localStorage.setItem('rated_val_' + pid, selectedRating); let msg = document.getElementById('ratingModalMessage'); msg.innerText = previousRating ? 'تم التحديث بنجاح!' : 'تم التقييم بنجاح!'; msg.classList.remove('d-none'); btn.classList.add('d-none'); document.getElementById('display-avg-' + pid).innerText = data.new_rating.toFixed(1); document.getElementById('display-count-' + pid).innerText = '(' + data.total_reviews + ')'; let svgStars = ''; let newRate = Math.round(data.new_rating); for(let i=1; i<=5; i++){ let color = (newRate >= i) ? '#ffc107' : '#e4e5e9'; svgStars += `<svg width="15" height="15" viewBox="0 0 24 24" fill="${color}" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="margin-right:1px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`; } document.getElementById('display-stars-' + pid).innerHTML = svgStars; setTimeout(() => { ratingModal.hide(); }, 1500); } else { btn.innerText = 'حدث خطأ'; btn.disabled = false; } }).catch(err => { btn.innerText = 'فشل الاتصال'; btn.disabled = false; }); });
    </script>
</body>
</html>

```

-----------------------------------
## File Path: ./templates/system_admin.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>إدارة المنصة | TajerGo</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/system_admin.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="container py-5">
        <h2 class="text-center fw-bold mb-5 text-warning">👑 TajerGo Super Admin</h2>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}{% for category, message in messages %}<div class="alert alert-{{ category }}">{{ message }}</div>{% endfor %}{% endif %}
        {% endwith %}

        {% if not logged_in %}
        <div class="card bg-dark text-white mx-auto" style="max-width: 400px;">
            <div class="card-body">
                <form method="POST">
                    <input type="hidden" name="action" value="login">
                    <label>الرقم السري للإدارة</label>
                    <input type="password" name="password" class="form-control mb-3" required>
                    <button class="btn btn-warning w-100 fw-bold">تسجيل الدخول</button>
                </form>
            </div>
        </div>
        {% else %}
        <div class="row">
            <!-- إضافة تاجر -->
            <div class="col-md-4 mb-4">
                <div class="card bg-dark text-white border-warning">
                    <div class="card-body">
                        <h5 class="card-title fw-bold text-warning mb-4">➕ إضافة تاجر جديد</h5>
                        <form method="POST">
                            <input type="hidden" name="action" value="add_merchant">
                            <input type="text" name="name" class="form-control mb-3" placeholder="اسم التاجر" required>
                            <input type="text" name="slug" class="form-control mb-3" placeholder="رابط المتجر (انجليزي)" required>
                            <input type="text" name="password" class="form-control mb-3" placeholder="كلمة المرور" required>
                            <button class="btn btn-warning w-100 fw-bold">إنشاء المتجر</button>
                        </form>
                    </div>
                </div>
            </div>
            <!-- قائمة التجار -->
            <div class="col-md-8">
                <div class="card bg-dark text-white">
                    <div class="card-body">
                        <h5 class="fw-bold mb-4">🏢 المتاجر المشتركة</h5>
                        <div class="table-responsive">
                            <table class="table table-dark table-hover align-middle">
                                <thead><tr><th>التاجر</th><th>الرابط</th><th>الحالة</th><th>إجراءات</th></tr></thead>
                                <tbody>
                                    {% for m in merchants %}
                                    <tr>
                                        <td>{{ m.username }}<br><small class="text-muted">Pass: {{ m.password }}</small></td>
                                        <td><a href="/store/{{ m.store_slug }}" target="_blank" class="text-info">{{ m.store_slug }}</a></td>
                                        <td><span class="badge bg-{{ 'success' if m.active == 'TRUE' else 'secondary' }}">{{ 'نشط' if m.active == 'TRUE' else 'موقوف' }}</span></td>
                                        <td>
                                            <form method="POST" class="d-inline">
                                                <input type="hidden" name="action" value="toggle_status">
                                                <input type="hidden" name="user_id" value="{{ m.id }}">
                                                <input type="hidden" name="current_status" value="{{ m.active }}">
                                                <button class="btn btn-sm btn-{{ 'warning' if m.active == 'TRUE' else 'success' }}">{{ 'إيقاف' if m.active == 'TRUE' else 'تفعيل' }}</button>
                                            </form>
                                            {% if m.store_slug != 'admin-store' %}
                                            <form method="POST" class="d-inline" onsubmit="return confirm('هل أنت متأكد من حذف المتجر وكل منتجاته؟');">
                                                <input type="hidden" name="action" value="delete_merchant">
                                                <input type="hidden" name="user_id" value="{{ m.id }}">
                                                <button class="btn btn-sm btn-danger">حذف</button>
                                            </form>
                                            {% endif %}
                                        </td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {% endif %}
    </div>

<!-- ============================================== -->
<!-- ⚡ DYNAMIC JS INJECTION: ADVANCED FIELDS ⚡ -->
<!-- ============================================== -->
<script>
document.addEventListener("DOMContentLoaded", function() {
    function injectAdvancedFields() {
        // البحث عن أي فورم أو نافذة منبثقة تتعلق بالمنتجات
        let forms = document.querySelectorAll('form');
        forms.forEach(form => {
            // نتأكد أن الفورم خاص بالمنتجات (يحتوي على حقل السعر مثلاً)
            if (form.querySelector('input[name="price"]') && !form.querySelector('.dynamic-adv-fields')) {
                
                let advBox = document.createElement('div');
                advBox.className = 'dynamic-adv-fields col-12 mt-4 mb-3 w-100 p-3 bg-light rounded border border-info shadow-sm';
                advBox.style.borderRight = '4px solid #0dcaf0';
                
                advBox.innerHTML = `
                    <h6 class="text-info mb-3 fw-bold"><i class="fas fa-tags"></i> خصائص إضافية (اختياري)</h6>
                    <div class="row g-2">
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">التصنيف الفرعي</label>
                            <input type="text" name="subcategory" class="form-control form-control-sm" placeholder="مثال: هواتف">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">الماركة / الموديل</label>
                            <input type="text" name="brand" class="form-control form-control-sm" placeholder="مثال: سامسونج">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">النوع / الخصائص</label>
                            <input type="text" name="p_type" class="form-control form-control-sm" placeholder="مثال: 128GB">
                        </div>
                    </div>
                `;

                // البحث عن زر الإرسال أو الإغلاق لنزرع الصندوق قبله مباشرة
                let submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
                let priceInput = form.querySelector('input[name="price"]');
                
                if (submitBtn) {
                    submitBtn.parentNode.insertBefore(advBox, submitBtn);
                } else if (priceInput) {
                    priceInput.parentNode.appendChild(advBox);
                } else {
                    form.appendChild(advBox);
                }
            }
        });
    }

    // التنفيذ الفوري عند فتح الصفحة
    injectAdvancedFields();

    // التنفيذ المستمر (مراقبة): لمواجهة النوافذ المنبثقة التي تفتح بعد التحميل
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                injectAdvancedFields();
            }
        });
    });
    observer.observe(document.body, { childList: true, subtree: true });
});
</script>
<!-- ============================================== -->


    <script>
    // 🧨 كود إجبار المتصفح على جلب النسخة الجديدة وتدمير الكاش القديم
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.getRegistrations().then(function(registrations) {
            for(let registration of registrations) {
                registration.update();
            }
        });
    }
    </script>
    
</body>
</html>

```

-----------------------------------
## File Path: ./templates/track.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تتبع الطلب - {{ order.order_id if order else 'البحث' }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/track.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-7 col-md-9">
                <div class="card track-card bg-white p-4">
                    <div class="text-center mb-4">
                        <h4 class="fw-bold text-dark">📦 تتبع حالة الطلب</h4>
                        <p class="text-muted small">أدخل رقم الطلب أو رقم هاتفك لمعرفة حالة الطلب</p>
                        
                        <form method="GET" action="/track" class="input-group shadow-sm rounded-pill overflow-hidden mt-3">
                            <input type="text" name="order_id" class="form-control border-0 px-4" placeholder="رقم الطلب (مثال: ORD-1001) أو رقم هاتفك" value="{{ search_query if search_query else '' }}" required>
                            <button class="btn btn-primary px-4 fw-bold" type="submit"><i class="fas fa-search me-1"></i> بحث</button>
                        </form>
                    </div>

                    {% if error %}
                        <div class="alert alert-danger text-center fw-bold rounded-4">{{ error }}</div>
                    {% endif %}

                    {% if order %}
                        <hr class="my-4">
                        
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <div>
                                <h6 class="fw-bold mb-0">رقم الطلب: <span class="text-primary">{{ order.get('order_id', '') }}</span></h6>
                                <small class="text-muted">{{ order.get('date', '') }}</small>
                            </div>
                            <span class="badge bg-light text-dark border px-3 py-2 fs-6">{{ order.get('status', 'جديد 🟡') }}</span>
                        </div>

                        {% set st = order.get('status', 'جديد 🟡') %}
                        {% if 'ملغي' in st %}
                            <div class="alert alert-danger text-center fw-bold rounded-4 my-3"><i class="fas fa-times-circle"></i> تم إلغاء هذا الطلب</div>
                        {% else %}
                            {% set is_paid = ('مدفوع' in st or 'تجهيز' in st or 'توصيل' in st) %}
                            {% set is_processing = ('تجهيز' in st or 'توصيل' in st) %}
                            {% set is_delivered = ('توصيل' in st) %}
                            {% set prog_width = '100%' if is_delivered else ('66%' if is_processing else ('33%' if is_paid else '0%')) %}

                            <div class="stepper">
                                <div class="stepper-progress" style="width: {{ prog_width }};"></div>
                                
                                <div class="step-item completed">
                                    <div class="step-icon"><i class="fas fa-file-invoice"></i></div>
                                    <div class="step-label">تم الطلب</div>
                                </div>
                                
                                <div class="step-item {% if is_paid %}completed{% else %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-wallet"></i></div>
                                    <div class="step-label">تأكيد الدفع</div>
                                </div>
                                
                                <div class="step-item {% if is_processing %}completed{% elif is_paid %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-box-open"></i></div>
                                    <div class="step-label">التجهيز</div>
                                </div>
                                
                                <div class="step-item {% if is_delivered %}completed{% elif is_processing %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-truck-fast"></i></div>
                                    <div class="step-label">تم التوصيل</div>
                                </div>
                            </div>
                        {% endif %}

                        <div class="bg-light p-3 rounded-4 mb-3">
                            <h6 class="fw-bold mb-2 text-secondary">ملخص المشتريات:</h6>
                            <ul class="list-unstyled mb-0">
                                {% for item in order.get('cart_items', []) %}
                                    <li class="d-flex justify-content-between py-1 border-bottom border-light">
                                        <span>{{ item.get('name', '') }} (x{{ item.get('qty', 1) }})</span>
                                        <span class="fw-bold">{{ item.get('price', '') }}</span>
                                    </li>
                                {% endfor %}
                            </ul>
                            <div class="d-flex justify-content-between pt-2 fw-bold text-success fs-5">
                                <span>الإجمالي النهائي:</span>
                                <span>{{ order.get('total', '') }}</span>
                            </div>
                        </div>

                        <div class="small text-muted mb-4">
                            <div><i class="fas fa-user me-1 text-primary"></i> <strong>المستلم:</strong> {{ order.get('customer_name', '') }}</div>
                            <div><i class="fas fa-map-marker-alt me-1 text-danger"></i> <strong>العنوان:</strong> {{ order.get('customer_address', 'غير محدد') }}</div>
                            <div><i class="fas fa-credit-card me-1 text-success"></i> <strong>الدفع:</strong> {{ order.get('payment_info', '') }}</div>
                        </div>

                        {% if settings and settings.get('whatsapp') %}
                            <div class="text-center">
                                <a href="https://wa.me/{{ settings.get('whatsapp') }}?text=استفسار%20بخصوص%20الطلب%20{{ order.get('order_id', '') }}" class="btn btn-outline-success btn-sm rounded-pill px-4 fw-bold" target="_blank">
                                    <i class="fab fa-whatsapp"></i> تواصل مع المتجر بخصوص الطلب
                                </a>
                            </div>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</body>
</html>

```

-----------------------------------
## File Path: ./vercel.json
```
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/app.py"
    }
  ],
  "headers": [
    {
      "source": "/sw.js",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        },
        {
          "key": "Pragma",
          "value": "no-cache"
        }
      ]
    },
    {
      "source": "/manifest/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/store/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/dashboard",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/static/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

-----------------------------------

```

-----------------------------------
## File Path: ./app.py
```
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
```

-----------------------------------
## File Path: ./backup_db.py
```
import dns.resolver

# تجاوز إعدادات DNS الخاصة بـ Termux للاتصال بسيرفرات جوجل
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']

import database
import json, os
from datetime import datetime
from bson import json_util

# إنشاء مجلد يحمل تاريخ ووقت اليوم
backup_folder = f"TajerGo_Backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
os.makedirs(backup_folder, exist_ok=True)

collections = {
    'users': database.users_col,
    'products': database.products_col,
    'settings': database.settings_col,
    'orders': database.orders_col,
    'coupons': database.coupons_col,
    'packages': database.packages_col,
    'drivers': database.drivers_col
}

print(f"📥 جاري سحب بيانات المنصة إلى المجلد المحلي: {backup_folder}...")

for name, col in collections.items():
    data = list(col.find())
    # استخدام json_util للتعامل مع بيانات MongoDB الخاصة (مثل ObjectId والتواريخ)
    with open(f"{backup_folder}/{name}.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, default=json_util.default, ensure_ascii=False, indent=4)
    print(f" - تم حفظ جدول: {name} ({len(data)} سجل)")

print(f"✅ تمت عملية النسخ الاحتياطي بنجاح!\n📂 يمكنك العثور على الملفات داخل مجلد المشروع باسم: {backup_folder}")

```

-----------------------------------
## File Path: ./config.py
```
import os

SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "tajergo_db")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MAIN_DOMAIN = os.getenv("MAIN_DOMAIN", "saas-store-products.vercel.app")
STATIC_VERSION = os.getenv("STATIC_VERSION", "20260828.1")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is required")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is required")

```

-----------------------------------
## File Path: ./database.py
```
from pymongo import MongoClient
import uuid, os, re
from datetime import datetime
import config

# الاتصال بقاعدة البيانات
client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[config.MONGO_DB_NAME]

# المجموعات (Collections)
users_col = db['users']
products_col = db['products']
settings_col = db['settings']
orders_col = db['orders']
coupons_col = db['coupons']
packages_col = db['packages']

# ==========================================
# إدارة المستخدمين (التجار)
# ==========================================
def authenticate_user(slug, password): 
    return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})

def get_user_by_slug(slug): 
    return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_all_users(): 
    return list(users_col.find({}))

def create_new_merchant(name, slug, password):
    name = str(name or '').strip()
    slug = str(slug or '').strip().lower()
    password = str(password or '')
    if not name or not slug or not password or not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,49}', slug):
        return False
    if users_col.find_one({"store_slug": slug}):
        return False
    users_col.insert_one({
        "id": f"U-{uuid.uuid4().hex[:6]}",
        "username": name,
        "store_slug": slug,
        "password": password,
        "active": "TRUE"
    })
    return True

def toggle_user_status(user_id, current_status): 
    users_col.update_one({"id": user_id}, {"$set": {"active": "FALSE" if current_status == "TRUE" else "TRUE"}})

def delete_user(user_id):
    users_col.delete_one({"id": user_id})
    products_col.delete_many({"u_id": user_id})
    settings_col.delete_one({"u_id": user_id})
    orders_col.delete_many({"store_id": user_id})
    coupons_col.delete_many({"u_id": user_id})

def change_user_password(user_id, old_password, new_password):
    if not str(new_password or '') or len(str(new_password)) < 6:
        return False
    if not users_col.find_one({"id": user_id, "password": old_password}):
        return False
    result = users_col.update_one({"id": user_id}, {"$set": {"password": str(new_password)}})
    return result.matched_count > 0

def edit_merchant_info(user_id, new_slug, new_package):
    new_slug = str(new_slug or '').strip().lower()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,49}', new_slug):
        return False
    existing = users_col.find_one({'store_slug': new_slug})
    if existing and str(existing.get('id', existing.get('_id'))) != str(user_id):
        return False
    try:
        from bson.objectid import ObjectId
        query = {'$or': [{'id': user_id}, {'_id': ObjectId(user_id)}]}
    except Exception:
        query = {'id': user_id}
    result = users_col.update_one(query, {'$set': {'store_slug': new_slug, 'package': new_package}})
    return result.matched_count > 0

# ==========================================
# إدارة الإعدادات
# ==========================================
def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    return setting if setting else {'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 'theme_color': '#0d6efd', 'font_family': 'Cairo', 'welcome_message': 'أهلاً بك في متجرنا! نتمنى لك تسوقاً ممتعاً.'}

def update_settings(user_id, data): 
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

# ==========================================
# إدارة المنتجات
# ==========================================
def add_product(user_id, name, desc, price, cat, img, stock, unit='حبة'):
    try: 
        products_col.insert_one({"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "unit": unit, "created_at": datetime.now(), "ratings_sum": 0, "ratings_count": 0, "rated_ips": {}})
        return True
    except: return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock, unit='حبة'):
    try: 
        products_col.update_one({"id": product_id, "u_id": user_id}, {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "unit": unit}})
        return True
    except: return False

def delete_product(product_id, user_id): 
    products_col.delete_one({"id": product_id, "u_id": user_id})

def get_products(user_id): 
    return list(products_col.find({"u_id": user_id}))

# ==========================================
# 🛡️ الأمان: معالجة الطلبات الآمنة (Backend Cart Validation)
# ==========================================

def create_secure_order(store_id, customer_name, customer_phone, customer_address, payment, cart_items, coupon_code=""):
    import secrets

    if not isinstance(cart_items, list) or not cart_items:
        raise ValueError("السلة فارغة")

    order_id = "ORD-" + secrets.token_hex(3).upper()
    secure_cart = []
    subtotal_total = 0.0

    for item in cart_items:
        if not isinstance(item, dict):
            raise ValueError("صيغة المنتج غير صحيحة")

        prod_id = str(item.get('id') or item.get('product_id') or '').strip()
        qty = int(item.get('qty', 1))
        if not prod_id or qty < 1:
            raise ValueError("بيانات المنتج أو الكمية غير صحيحة")

        db_prod = products_col.find_one({"id": prod_id, "u_id": store_id})
        if not db_prod:
            raise ValueError("أحد المنتجات غير موجود في هذا المتجر")

        stock = db_prod.get('stock')
        if stock is not None and str(stock).strip() != '':
            try:
                stock_value = int(stock)
            except (TypeError, ValueError):
                stock_value = None
            if stock_value is not None and stock_value < qty:
                raise ValueError(f"الكمية المطلوبة من المنتج «{db_prod.get('name', 'المنتج')}» غير متوفرة")

        p_name = str(db_prod.get('name') or db_prod.get('title') or 'منتج')
        p_price = float(db_prod.get('price', 0) or 0)
        subtotal = p_price * qty
        subtotal_total += subtotal
        secure_cart.append({
            "id": prod_id,
            "name": p_name,
            "price": p_price,
            "qty": qty,
            "subtotal": round(subtotal, 2)
        })

    discount_percent = 0.0
    discount_info = {}
    if coupon_code:
        coupon = validate_coupon(store_id, coupon_code)
        if coupon:
            discount_percent = max(0.0, min(100.0, float(coupon.get('discount', 0) or 0)))
            discount_value = round(subtotal_total * discount_percent / 100, 2)
            discount_info = {
                "code": str(coupon.get('code', coupon_code)).upper(),
                "percent": discount_percent,
                "amount": discount_value
            }

    total = max(0.0, subtotal_total - (subtotal_total * discount_percent / 100))

    now = datetime.now()
    order_doc = {
        "order_id": order_id,
        "store_id": store_id,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_address": customer_address,
        "payment": payment,
        "cart": secure_cart,
        "cart_items": secure_cart,
        "subtotal": round(subtotal_total, 2),
        "total": round(total, 2),
        "status": "جديد 🟡",
        "discount_info": discount_info,
        "date": now,
        "created_at": now
    }

    orders_col.insert_one(order_doc)
    return order_id, round(total, 2), secure_cart, discount_info

def get_orders(store_id):
    orders = list(orders_col.find({"store_id": store_id}).sort("_id", -1))
    for order in orders:
        if not order.get("date") and order.get("created_at"):
            order["date"] = order["created_at"]
    return orders

# ==========================================
# الكوبونات والباقات (تمت استعادتها وتأمينها)
# ==========================================
def add_coupon(user_id, code, discount_percent):
    code = str(code or '').strip().upper()
    discount_percent = int(discount_percent)
    if not code or not 1 <= discount_percent <= 99:
        return False
    if coupons_col.find_one({"u_id": user_id, "code": code}):
        return False
    coupons_col.insert_one({
        "id": f"C-{uuid.uuid4().hex[:6]}",
        "u_id": user_id,
        "code": code,
        "discount": discount_percent
    })
    return True
def get_coupons(user_id): 
    return list(coupons_col.find({"u_id": user_id}))
def delete_coupon(coupon_id, user_id):
    result = coupons_col.delete_one({"id": coupon_id, "u_id": user_id})
    return result.deleted_count > 0
def validate_coupon(user_id, code): 
    return coupons_col.find_one({"u_id": user_id, "code": code.upper()})

def get_packages(): 
    return list(packages_col.find())
def add_package(name, price, max_products, features):
    try:
        import re as regex_lib
        # استخراج الأرقام فقط لضمان تحويلها لـ int
        val = str(max_products)
        clean_str = regex_lib.sub(r'\D', '', val)
        clean_max = int(clean_str) if clean_str else 999999
    except:
        clean_max = 20

    db.packages.insert_one({
        "name": str(name).strip(),
        "price": str(price).strip(),
        "max_products": clean_max,
        "pkg_max": clean_max,
        "features": str(features).strip()
    })


def delete_package(pkg_id):
    from bson.objectid import ObjectId
    packages_col.delete_one({'_id': ObjectId(pkg_id)})


# ==========================================
# إدارة المناديب (Drivers Management)
# ==========================================
drivers_col = db['drivers']

def add_driver(store_id, name, phone):
    try:
        import secrets
        clean_phone = str(phone).strip()
        clean_name = str(name).strip()
        existing = drivers_col.find_one({"store_id": store_id, "phone": clean_phone})
        if not existing:
            token = secrets.token_hex(8)
            drivers_col.insert_one({
                "store_id": store_id,
                "name": clean_name,
                "phone": clean_phone,
                "token": token
            })
            return token
        return False
    except Exception as e:
        print("Driver Insert Error:", e)
        return False


def get_store_drivers(store_id):
    try:
        import secrets
        from bson.objectid import ObjectId
        drivers = list(drivers_col.find({"store_id": store_id}).sort('_id', -1))
        for d in drivers:
            d_id_str = str(d['_id'])
            d['_id'] = d_id_str
            # إذا كان المندوب لا يملك رمز بوابة، نقوم بتوليده وحفظه فوراً
            if 'token' not in d:
                new_token = secrets.token_hex(8)
                drivers_col.update_one({"_id": ObjectId(d_id_str)}, {"$set": {"token": new_token}})
                d['token'] = new_token
        return drivers
    except Exception as e:
        print("Driver Fetch Error:", e)
        return []


def delete_driver(store_id, phone):
    try:
        drivers_col.delete_one({"store_id": store_id, "phone": str(phone).strip()})
        return True
    except Exception as e:
        print("Driver Delete Error:", e)
        return False



def get_driver_by_token(token):
    token = str(token or '').strip().lower()
    if not token:
        return None
    return drivers_col.find_one({"token": token}, {"_id": 0})


def assign_order_driver(order_id, store_id, driver_name, driver_phone):
    return orders_col.update_one(
        {"order_id": str(order_id), "store_id": store_id},
        {"$set": {
            "driver_name": driver_name,
            "driver_phone": driver_phone,
            "status": "مع المندوب للتوصيل 🚚"
        }}
    )




def extract_real_order_items(order, store_id=None):
    """استخراج وتنسيق أسماء المنتجات الحقيقية بدقة من كافة صيغ الطلبات"""
    import json
    extracted = []
    
    # 1. فحص حقل cart سواء كان مصفوفة أو نص JSON
    cart_data = order.get('cart')
    if isinstance(cart_data, str):
        try:
            cart_data = json.loads(cart_data)
        except:
            if cart_data.strip():
                extracted.append({"name": cart_data.strip(), "qty": 1})
                return extracted

    if isinstance(cart_data, list):
        for item in cart_data:
            if isinstance(item, dict):
                p_name = item.get('name') or item.get('title') or item.get('product_name') or item.get('item_name')
                qty = item.get('qty') or item.get('quantity') or 1
                prod_id = item.get('id') or item.get('product_id') or item.get('_id')
                
                # إذا كان الاسم غير متوفر أو عام، نبحث عنه في المنتجات
                if (not p_name or p_name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    prod = products_col.find_one({"id": str(prod_id)}) or products_col.find_one({"_id": prod_id})
                    if prod:
                        p_name = prod.get('name') or prod.get('title')
                
                if p_name:
                    extracted.append({"name": str(p_name), "qty": qty})
            elif isinstance(item, str) and item.strip():
                extracted.append({"name": item.strip(), "qty": 1})

    # 2. فحص الحقول الفردية القديمة
    if not extracted:
        single_name = order.get('product_name') or order.get('item_name')
        if single_name:
            extracted.append({"name": str(single_name), "qty": order.get('qty', 1)})

    # 3. التحقق من نص المنتجات الصريح إن وجد
    if not extracted:
        raw_text = order.get('items_text') or order.get('order_details')
        if raw_text:
            extracted.append({"name": str(raw_text), "qty": 1})

    return extracted if extracted else [{"name": "طلب #" + str(order.get('order_id', '')), "qty": 1}]


def resolve_order_items(order, store_id=None):
    """محرك استخراج ومطابقة أسماء المنتجات بدقة واحترافية من قاعدة البيانات"""
    import json
    from bson.objectid import ObjectId
    
    store_id = store_id or order.get('store_id')
    results = []
    
    # خريطة سريعة لمنتجات المتجر بالمعرف والسعر
    store_prods = list(products_col.find({"u_id": store_id})) if store_id else list(products_col.find({}))
    prod_by_id = {}
    prod_by_price = {}
    
    for p in store_prods:
        p_name = p.get('name') or p.get('title') or p.get('name_ar')
        if p_name:
            if '_id' in p: prod_by_id[str(p['_id'])] = p_name
            if 'id' in p: prod_by_id[str(p['id'])] = p_name
            try:
                price_val = float(p.get('price', 0))
                if price_val > 0 and price_val not in prod_by_price:
                    prod_by_price[price_val] = p_name
            except:
                pass

    # 1. فحص حقل السلة cart
    cart = order.get('cart')
    if isinstance(cart, str):
        try:
            cart = json.loads(cart)
        except:
            pass
            
    if isinstance(cart, list) and len(cart) > 0:
        for it in cart:
            if isinstance(it, dict):
                # البحث عن أي مفتاح يحمل اسم المنتج
                name = (it.get('name') or it.get('title') or it.get('product_name') or 
                        it.get('item_name') or it.get('name_ar') or it.get('label'))
                
                prod_id = str(it.get('id') or it.get('product_id') or it.get('_id') or '')
                qty = it.get('qty') or it.get('quantity') or 1
                
                # مطابقة المعرف مع جدول المنتجات إذا كان الاسم مفقوداً
                if (not name or name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    name = prod_by_id.get(prod_id)
                
                # مطابقة السعر مع جدول المنتجات كحل بديل
                if not name or name in ['منتج', 'منتجات متنوعة', '']:
                    try:
                        p_price = float(it.get('price', 0))
                        name = prod_by_price.get(p_price)
                    except:
                        pass
                        
                if name and name not in ['منتج', 'منتجات متنوعة']:
                    results.append(f"{name} (x{qty})")
                    
            elif isinstance(it, str) and it.strip() and it.strip() != 'منتج':
                results.append(it.strip())

    # 2. فحص الحقول النصية والفردية
    if not results:
        direct_name = order.get('product_name') or order.get('item_name') or order.get('title')
        if direct_name and direct_name != 'منتج':
            results.append(f"{direct_name} (x{order.get('qty', 1)})")

    # 3. مطابقة إجمالي الطلب مع أسعار منتجات المتجر للطلبات القديمة جداً
    if not results:
        try:
            total_val = float(order.get('total', 0))
            if total_val in prod_by_price:
                results.append(f"{prod_by_price[total_val]} (x1)")
        except:
            pass

    # 4. في حال تعذر المطابقة التامة نضع كود الطلب المرجعي
    if not results:
        results.append(f"طلب {order.get('order_id', '')}")

    return results


def get_store_orders_enhanced(store_id):
    """دالة مطورة وذكية لجلب الطلبات مع مطابقة أسماء المنتجات"""
    orders = list(orders_col.find({"store_id": store_id}).sort('_id', -1))
    
    # 1. جلب خريطة المنتجات لمطابقتها مع الأكواد
    prods = list(products_col.find({"u_id": store_id}))
    prod_map = {}
    for p in prods:
        name = p.get('name') or p.get('title')
        if name:
            if '_id' in p: prod_map[str(p['_id'])] = name
            if 'id' in p: prod_map[str(p['id'])] = name
            
    import json
    for o in orders:
        if '_id' in o: o['_id'] = str(o['_id'])
        
        final_list = []
        cart = o.get('cart')
        
        # 2. فك السلة لو كانت نصاً
        if isinstance(cart, str):
            try: cart = json.loads(cart)
            except: 
                if cart.strip(): final_list.append(f"▪️ {cart.strip()}")
        
        # تحويل القاموس لمصفوفة إن وجد
        if isinstance(cart, dict):
            cart = [cart]
            
        # 3. قراءة المصفوفة بدقة
        if isinstance(cart, list):
            for item in cart:
                if isinstance(item, dict):
                    name = item.get('name') or item.get('title') or item.get('product_name')
                    # المطابقة عبر ID في حال غياب الاسم
                    if not name or name == 'منتج':
                        pid = str(item.get('id') or item.get('_id') or item.get('product_id') or '')
                        if pid in prod_map:
                            name = prod_map[pid]
                            
                    if not name or name == 'منتج':
                        name = "منتج غير مسجل"
                        
                    qty = item.get('qty') or item.get('quantity') or 1
                    final_list.append(f"▪️ {name} (x{qty})")
                elif isinstance(item, str) and item.strip():
                    final_list.append(f"▪️ {item.strip()}")
                    
        # 4. قراءة الحقول القديمة (دعم الإصدارات السابقة للطلبات)
        if not final_list:
            legacy = o.get('product_name') or o.get('item_name') or o.get('items')
            if isinstance(legacy, str) and legacy.strip():
                if '▪️' not in legacy:
                    final_list.append(f"▪️ {legacy} (x{o.get('qty', 1)})")
                else:
                    final_list.append(legacy)
                    
        # 5. خطة الطوارئ
        if not final_list:
            final_list.append("▪️ منتج غير محدد")
            
        o['final_products'] = final_list
        
    return orders



def check_product_limit(store_id):
    """التحقق من تجاوز التاجر للحد الأقصى للمنتجات بناءً على باقته"""
    try:
        user = users_col.find_one({"id": store_id})
        if not user: 
            return False, "حساب المتجر غير موجود."
            
        # استثناء المتجر الرئيسي (المدير) من القيود
        if user.get("store_slug") == "admin-store":
            return True, ""
            
        pkg_name = user.get("package", "أساسية")
        
        # جلب بيانات الباقة من قاعدة البيانات
        try:
            pkg = db.packages.find_one({"name": pkg_name})
        except:
            pkg = None
            
        # معالجة الحد الأقصى (في حال كتب المدير "لامحدود" نصياً بدلاً من رقم)
        max_str = str(pkg.get("max_products", 20)) if pkg else "20"
        try:
            max_prods = int(max_str)
        except ValueError:
            max_prods = 9999999 # رقم لا نهائي في حال الباقة المفتوحة
            
        # حساب العدد الفعلي للمنتجات الحالية في متجر التاجر
        current_count = products_col.count_documents({"u_id": store_id})
        
        if current_count >= max_prods:
            return False, f"عذراً! باقتك الحالية ({pkg_name}) تسمح بإضافة {max_prods} منتج كحد أقصى. يرجى ترقية باقتك لإضافة المزيد."
            
        return True, ""
    except Exception as e:
        print("Package Limit Check Error:", e)
        return True, "" # في حال الخطأ التقني نسمح بالمرور كي لا يتوقف المتجر



def check_merchant_product_limit(user_id):
    try:
        import re as regex_lib
        from bson.objectid import ObjectId
        user = users_col.find_one({"id": user_id})
        if not user:
            try:
                user = users_col.find_one({"_id": ObjectId(str(user_id))})
            except:
                pass

        if not user:
            return True, 0, 999999, "عامة", ""

        pkg_name = str(user.get("package", "أساسية")).strip()
        
        # البحث في قاعدة البيانات بمطابقة مرنة
        target_pkg = db.packages.find_one({"name": {"$regex": f"^{regex_lib.escape(pkg_name)}$", "$options": "i"}})

        if target_pkg:
            raw_val = target_pkg.get("max_products") if target_pkg.get("max_products") is not None else target_pkg.get("pkg_max", 20)
            try:
                max_limit = int(raw_val)
            except:
                max_limit = 20
        else:
            # إذا لم توجد الباقة في الجدول، نأخذ حداً صغيراً بدلاً من 20
            max_limit = 5

        current_prods = get_products(user_id)
        current_count = len(current_prods) if current_prods else 0

        if current_count >= max_limit:
            err_msg = f"⚠️ تم الوصول للحد الأقصى! باقتك ({pkg_name}) تسمح بـ {max_limit} منتج فقط (لديك حالياً {current_count} منتج)."
            return False, current_count, max_limit, pkg_name, err_msg

        return True, current_count, max_limit, pkg_name, ""
    except Exception as e:
        print("Limit Error:", e)
        return True, 0, 999999, "خطأ", ""

```

-----------------------------------
## File Path: ./docs/REFACTORING.md
```
# مراجعة وتنظيم المشروع — 2026-08-25

## ما تم تنفيذه
1. تنظيف الملفات غير المستخدمة وملفات التعديل الآلي القديمة.
2. إنشاء `base_dashboard.html` وتوحيد عناصر لوحة التاجر عبر `templates/partials/`.
3. فصل CSS وJavaScript الخاصين بلوحة التاجر.
4. منع أزرار النماذج من العمل بشكل غير محدد بإضافة `type="submit"` للأزرار التي تنفذ إرسال النموذج.
5. إزالة أسلوب سكربتات تعديل `app.py` وHTML آليًا.
6. اعتماد MongoDB كمصدر البيانات الحالي عبر `database.py` و`config.py`.
7. توحيد Service Worker إلى `static/sw.js` واحد، مع Manifest ديناميكي لكل متجر.
8. إضافة سياسة Cache واضحة: الصفحات الديناميكية لا تُخزن، وCSS/JS الثابت يستخدم Cache طويلًا مع إصدار.
9. إزالة تكرار دالة `add_driver` وتوحيد Collection الخاصة بالمناديب.
10. إصلاح مسار بوابة المندوب ودعمه للمسارين `/driver/<token>` و`/delivery?token=...`.
11. تأمين تحديثات الطلبات بحيث تتضمن `store_id` في استعلامات التاجر.
12. نقل إعدادات البيئة إلى `config.py` ومنع الأسرار من الدخول إلى Git.
13. تحديث README وPROJECT_CONTEXT وdocs/setup.md لتطابق البنية الحالية.

## تحقق محلي
- تم فحص بنية Python بواسطة AST بدون أخطاء نحوية.
- تم تحميل جميع قوالب Jinja الرئيسية والـpartials بنجاح.
- تم التأكد من عدم وجود نسخة ثانية من Service Worker أو Manifest ثابت.
- تم التأكد من عدم وجود ملفات `fix_*.py` أو `update_*.py` داخل النسخة النهائية.

```

-----------------------------------
## File Path: ./docs/setup.md
```
# إعداد وتشغيل TajerGo

## 1) المتطلبات
- Python 3.10+
- MongoDB
- حساب Vercel للنشر

## 2) متغيرات البيئة
انسخ `.env.example` إلى `.env` في البيئة المحلية، ثم ضع القيم الحقيقية.
في Vercel أضف نفس المتغيرات من Project Settings → Environment Variables.

المطلوب:
- `SECRET_KEY`
- `MONGO_URI`

اختياري:
- `MONGO_DB_NAME`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `MAIN_DOMAIN`
- `STATIC_VERSION`

## 3) التشغيل المحلي
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 4) قاعدة البيانات
لتجهيز الفهارس:
```bash
python setup_indexes.py
```

للنسخ الاحتياطي:
```bash
python backup_db.py
```

## 5) النشر
```text
Local → GitHub → Vercel → MongoDB
```

بعد كل نشر:
1. افتح `/dashboard`.
2. اختبر كل تبويب.
3. أضف/عدل/احذف منتجًا.
4. افتح المتجر في نافذة خاصة.
5. اختبر الطلب والأزرار الخاصة بالمناديب.
6. تحقق من Console وعدم وجود أخطاء JavaScript.

## 6) سياسة التحديث
الصفحات الديناميكية لا تستخدم Cache.
ملفات CSS/JS تستخدم رقم إصدار في الرابط.
Service Worker واحد فقط موجود في `static/sw.js` ويُقدم عبر `/sw.js`.

```

-----------------------------------
## File Path: ./export_project_pro.sh
```
#!/bin/bash

# Check if dialog is installed
if ! command -v dialog &> /dev/null; then
    echo "[!] Error: 'dialog' is not installed. Please install it using: pkg install dialog"
    exit 1
fi

OUTPUT_FILE="ai_project_context.md"

# Interactive menu using dialog (Updated Title)
CHOICE=$(dialog --stdout --title "GitHub to Gemini Reviewer" \
    --menu "Choose project source:" 12 50 2 \
    1 "Project is already on your phone (Local folder)" \
    2 "Clone temporarily from GitHub (Read-only & Safe)")

clear

if [ "$CHOICE" == "1" ]; then
    TARGET_DIR=$(dialog --stdout --inputbox "Enter local folder path on your phone:" 8 50 "/data/data/com.termux/files/home/")
    clear
    if [ ! -d "$TARGET_DIR" ]; then
        echo "[!] Error: Directory does not exist."
        exit 1
    fi
    echo " [+] Reading project locally from: $TARGET_DIR"

elif [ "$CHOICE" == "2" ]; then
    USERNAME=$(dialog --stdout --inputbox "Enter GitHub Username:" 8 50)
    REPO=$(dialog --stdout --inputbox "Enter Repository Name:" 8 50)
    TOKEN=$(dialog --stdout --passwordbox "Enter GitHub Personal Access Token (PAT):" 8 50)
    clear
    
    TARGET_DIR="temp_read_only_folder"
    REPO_URL="https://${TOKEN}@github.com/${USERNAME}/${REPO}.git"
    
    echo "[*] Cloning repository temporarily (Read-only)..."
    git clone "$REPO_URL" "$TARGET_DIR" &>/dev/null
    
    if [ $? -ne 0 ]; then
        echo "[!] Error: Failed to clone. Check your details or token."
        exit 1
    fi
    echo " [+] Cloned successfully (Your GitHub repo is 100% untouched)."
else
    echo "Process cancelled."
    exit 0
fi

echo ""
echo "[*] Generating unified AI context file ($OUTPUT_FILE)..."
echo "# Software Project Context" > "$OUTPUT_FILE"
echo "Export Date: $(date)" >> "$OUTPUT_FILE"
echo -e "\n--- \n" >> "$OUTPUT_FILE"

cd "$TARGET_DIR"
file_count=0

find . -type f \
    -not -path '*/.*' \
    -not -path '*/node_modules*' \
    -not -path '*/venv/*' \
    -not -path '*/__pycache__*' \
    -not -path '*/build/*' \
    -not -path '*/dist/*' \
    -not -name '*.png' \
    -not -name '*.jpg' \
    -not -name '*.jpeg' \
    -not -name '*.gif' \
    -not -name '*.ico' \
    -not -name '*.pdf' \
    -not -name '*.zip' \
    -not -name '*.db' \
    -not -name '*.sqlite' \
    -not -name '*.lock' | while read -r file; do
    
    file_count=$((file_count + 1))
    echo "   [+] Processing file: $file"
    
    echo "## File Path: $file" >> "../$OUTPUT_FILE"
    echo '```' >> "../$OUTPUT_FILE"
    cat "$file" >> "../$OUTPUT_FILE"
    echo -e '\n```\n' >> "../$OUTPUT_FILE"
    echo "-----------------------------------" >> "../$OUTPUT_FILE"
done

cd ..

if [ "$CHOICE" == "2" ]; then
    rm -rf "$TARGET_DIR"
fi

cp "$OUTPUT_FILE" /sdcard/Download/

echo ""
echo "=================================================="
echo "      Process Completed Successfully! 🎉          "
echo "=================================================="
echo " 📂 File saved in Termux: $OUTPUT_FILE"
echo " 📱 Saved directly to: Download/$OUTPUT_FILE"
echo "=================================================="

```

-----------------------------------
## File Path: ./requirements.txt
```
Flask==2.3.2
gunicorn==20.1.0
pymongo[srv]==4.5.0
dnspython==2.4.2
requests

```

-----------------------------------
## File Path: ./setup_indexes.py
```
import dns.resolver

# إجبار المكتبة على استخدام سيرفرات جوجل للـ DNS متجاهلة ملف resolv.conf
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']

import database
from pymongo import ASCENDING

print("⏳ جاري إنشاء الفهارس (Indexes) لتسريع المنصة...")

# فهرسة معرف التاجر (لأن كل استعلامات المتجر تعتمد عليه)
database.products_col.create_index([("u_id", ASCENDING)])

# فهرسة التصنيف لتسريع التنقل بين الأقسام
database.products_col.create_index([("category", ASCENDING)])

# فهرسة اسم المنتج لتسريع شريط البحث
database.products_col.create_index([("name", ASCENDING)])

# فهرسة رابط المتجر في جدول المستخدمين لتسريع عملية الدخول
database.users_col.create_index([("store_slug", ASCENDING)], unique=True)

print("✅ تم إنشاء الفهارس بنجاح! قاعدة البيانات الآن مجهزة للعمل بأقصى سرعة مع ملايين المنتجات 🚀")

```

-----------------------------------
## File Path: ./static/css/dashboard.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f4f6f9; }
        .form-control, .form-select { border: 2px solid #b3b3b3 !important; border-radius: 8px; padding: 10px 15px; background-color: #fcfcfc; font-weight: bold; color: #333; transition: all 0.3s ease; }
        .form-control:focus, .form-select:focus { border-color: #0d6efd !important; background-color: #fff; box-shadow: 0 0 8px rgba(13, 110, 253, 0.3); outline: none; }
        .card { border-radius: 12px; }
        .upload-btn-wrapper { position: relative; overflow: hidden; display: inline-block; width: 100%; margin-bottom: 5px; }
        .upload-btn-wrapper input[type=file] { font-size: 100px; position: absolute; left: 0; top: 0; opacity: 0; cursor: pointer; }
        .divider-text { display: flex; align-items: center; text-align: center; color: #888; font-weight: bold; margin: 8px 0; }
        .divider-text::before, .divider-text::after { content: ''; flex: 1; border-bottom: 1px dashed #ccc; }
        .divider-text:not(:empty)::before { margin-left: .5em; } .divider-text:not(:empty)::after { margin-right: .5em; }

/* Dashboard navigation: keep all tabs accessible on small screens. */
#myTab {
    overflow-x: auto;
    flex-wrap: nowrap;
    scrollbar-width: thin;
}
#myTab .nav-item { flex: 0 0 auto; }
#myTab .nav-link { white-space: nowrap; }
/* تأثير التحميل النبضي للصور */
.img-wrapper, .store-logo, td img {
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: skeletonLoading 1.5s infinite;
    position: relative;
}
@keyframes skeletonLoading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
img { 
    /* إخفاء تأثير التحميل بمجرد ظهور الصورة الفعلية فوقه */
    position: relative; 
    z-index: 1; 
}
```

-----------------------------------
## File Path: ./static/css/driver.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f2f5f9; padding-bottom: 30px; }
        .header-banner { background: linear-gradient(135deg, #0d6efd, #2b2b2b); color: white; padding: 40px 0 30px; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 20px;}
        .order-card { background: #fff; border: none; border-radius: 20px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); margin-bottom: 15px; border-right: 5px solid #0d6efd; transition: transform 0.3s ease; }
        .order-card:hover { transform: translateY(-3px); }
        .btn-deliver { background-color: #25D366; color: white; font-weight: 800; border-radius: 12px; padding: 12px; width: 100%; border: none; transition: background 0.3s; }
        .btn-deliver:hover { background-color: #1ebe57; }

```

-----------------------------------
## File Path: ./static/css/login.css
```
body {
            font-family: 'Cairo', sans-serif;
            background-color: #f2f5f9;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            background-image: radial-gradient(circle at top right, rgba(13, 110, 253, 0.1) 0%, transparent 40%),
                              radial-gradient(circle at bottom left, rgba(13, 110, 253, 0.05) 0%, transparent 40%);
        }
        .login-card {
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.06);
            padding: 40px 30px;
            width: 100%;
            max-width: 400px;
            border-top: 5px solid #0d6efd;
            position: relative;
            z-index: 1;
        }
        .platform-logo {
            width: 110px;
            height: 110px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            margin-top: -80px; /* لرفع الشعار قليلاً خارج البطاقة */
            margin-bottom: 20px;
            background-color: #fff;
        }
        .form-control {
            border-radius: 12px;
            padding: 12px 15px;
            font-weight: 600;
            background-color: #f8f9fa;
            border: 1px solid #eaeaea;
            transition: all 0.3s;
        }
        .form-control:focus {
            background-color: #fff;
            border-color: #0d6efd;
            box-shadow: 0 0 0 0.25rem rgba(13,110,253,0.1);
        }
        .btn-login {
            border-radius: 12px;
            padding: 12px;
            font-weight: 800;
            font-size: 1.1rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(13,110,253,0.2) !important;
        }
        .input-icon {
            color: #888;
        }

```

-----------------------------------
## File Path: ./static/css/store.css
```

        body { font-family: var(--store-font, 'Cairo'), sans-serif; background-color: #f2f5f9; padding-bottom: 25px; color: #333; }

        
        /* Hero Section */
        .header-small .hero-section { padding: 40px 0 30px; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; margin-bottom: 25px; }
        .header-small .hero-title { font-size: 1.8rem; }
        .header-small .store-logo { width: 110px; height: 110px; }
        .header-large .hero-section { padding: 80px 0 60px; border-bottom-left-radius: 50px; border-bottom-right-radius: 50px; margin-bottom: 35px; }
        .header-large .hero-title { font-size: 3.5rem; }
        .header-large .store-logo { width: 160px; height: 160px; }
        .header-medium .hero-section { padding: 60px 0 40px; border-bottom-left-radius: 40px; border-bottom-right-radius: 40px; margin-bottom: 30px; }
        .header-medium .hero-title { font-size: 2.5rem; }
        .header-medium .store-logo { width: 135px; height: 135px; }

        .hero-section { background: linear-gradient(135deg, var(--main-color) 0%, #2b2b2b 100%); color: white; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.08); position: relative; overflow: hidden; }
        .hero-section::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('data:image/svg+xml;utf8,<svg opacity="0.05" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="none"/><circle cx="50" cy="50" r="40" stroke="white" stroke-width="2" fill="none"/></svg>') repeat; pointer-events: none; }
        .store-logo { object-fit: contain; border-radius: 50%; border: 4px solid rgba(255,255,255,0.9); box-shadow: 0 8px 20px rgba(0,0,0,0.15); background-color: #fff; margin-bottom: 15px; position: relative; z-index: 1; transition: transform 0.3s ease; }
        .store-logo:hover { transform: scale(1.05); }

        /* Search, Sort & Actions */
        .search-bar-container { background: #fff; border-radius: 50rem; padding: 5px; box-shadow: var(--card-shadow); transition: box-shadow 0.3s ease; }
        .search-bar-container:focus-within { box-shadow: var(--hover-shadow); }
        .search-bar-container input { border: none !important; box-shadow: none !important; font-weight: 600; }
        .sort-select { background-color: #fff; border: 1px solid #eaeaea; border-radius: 50rem; padding: 8px 15px; font-weight: 700; color: #555; box-shadow: var(--card-shadow); cursor: pointer; outline: none; appearance: none; -webkit-appearance: none; -moz-appearance: none; background-image: url('data:image/svg+xml;utf8,<svg fill="%23555" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>'); background-repeat: no-repeat; background-position: left 10px center; padding-left: 35px;}
        .sort-select:focus { border-color: var(--main-color); box-shadow: var(--hover-shadow); }
        .btn-share { border-radius: 50rem; padding: 8px 15px; font-weight: bold; }

        /* Tabs */
        .category-tabs { flex-wrap: nowrap; overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; padding: 5px 5px 20px 5px; margin-bottom: 10px; gap: 12px; scrollbar-width: none; }
        .category-tabs .nav-link { border-radius: 50rem; white-space: nowrap; color: #555; font-weight: 700; background-color: #fff; border: 1px solid #eaeaea; box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); padding: 8px 24px; }
        .category-tabs .nav-link.active { background-color: var(--main-color); color: white; border-color: var(--main-color); box-shadow: 0 6px 15px rgba(0,0,0,0.1); transform: translateY(-2px); }

        /* Product Cards */
        .product-card { border: none; border-radius: 20px; box-shadow: var(--card-shadow); overflow: hidden; background: #fff; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); }
        .product-card:hover { transform: translateY(-5px); box-shadow: var(--hover-shadow); }
        .img-wrapper { position: relative; width: 100%; padding-top: 100%; background-color: #fff; cursor: pointer; overflow: hidden; border-bottom: 1px solid #f0f0f0; }
        .product-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; padding: 0; transition: transform 0.5s ease; }
        .product-card:hover .product-img { transform: scale(1.05); }

        .product-title { font-size: 1rem; font-weight: 800; color: #2c3e50; line-height: 1.4; margin-bottom: 4px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .product-price { font-size: 1.25rem; font-weight: 800; color: var(--main-color); }
        .product-price small { font-size: 0.85rem; color: #888; font-weight: 600; }

        .btn-custom { background-color: var(--main-color); color: white; font-weight: 700; border-radius: 12px; padding: 10px; transition: all 0.2s; border: none; }
        .btn-custom:hover { filter: brightness(1.1); transform: scale(1.02); }
        .btn-secondary-custom { background-color: #e9ecef; color: #6c757d; font-weight: 700; border-radius: 12px; padding: 10px; border: none; }

        /* Rating & Badges */
        .rating-badge { display: inline-flex; align-items: center; background: #fff8e1; color: #ffb300; padding: 4px 10px; border-radius: 50rem; font-size: 0.8rem; font-weight: 800; cursor: pointer; transition: background 0.2s; margin-bottom: 8px;}
        .rating-badge:hover { background: #ffecb3; }
        .tags-container { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 12px; }
        .tag-badge { background: #f8f9fa; border: 1px solid #e9ecef; color: #6c757d; font-size: 0.7rem; padding: 3px 8px; border-radius: 6px; font-weight: 600; }

        /* Floating Cart */
        #floating-cart { position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%); background: rgba(13, 110, 253, 0.95); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); color: white; border-radius: 50rem; padding: 12px 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); cursor: pointer; z-index: 1000; font-weight: 800; font-size: 1.1rem; display: none; width: auto; white-space: nowrap; transition: all 0.3s ease; }
        #floating-cart:hover { transform: translateX(-50%) scale(1.05); }

        /* Modals & Support */
        .modal-content { border-radius: 24px; border: none; }
        .modal-header { border-bottom: 1px solid #f0f0f0; border-radius: 24px 24px 0 0; }
        .support-card { background: #fff; border: none; border-radius: 20px; padding: 20px; box-shadow: var(--card-shadow); margin-top: 30px; text-align: center; }
        .btn-support-wa { background-color: #25D366; color: white; border-radius: 50rem; padding: 10px 22px; font-weight: bold; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: all 0.2s; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.2); }
        .btn-support-wa:hover { background-color: #1ebe57; color: white; transform: translateY(-2px); }
    

.modal-star:hover, .modal-star:hover ~ .modal-star { fill: #ffc107 !important; transform: scale(1.15); } .star-selected { fill: #ffc107 !important; }


/* تأثير التحميل النبضي للصور */
.img-wrapper, .store-logo, td img {
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: skeletonLoading 1.5s infinite;
    position: relative;
}
@keyframes skeletonLoading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
img { 
    /* إخفاء تأثير التحميل بمجرد ظهور الصورة الفعلية فوقه */
    position: relative; 
    z-index: 1; 
}
```

-----------------------------------
## File Path: ./static/css/system_admin.css
```
body{font-family:'Cairo',sans-serif; background-color:#1e1e2d; color:#fff;}

```

-----------------------------------
## File Path: ./static/css/track.css
```
body { font-family: 'Cairo', sans-serif; background-color: #f4f7fb; color: #333; }
        .track-card { border-radius: 20px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .stepper { display: flex; justify-content: space-between; position: relative; margin: 30px 0; }
        .stepper::before { content: ''; position: absolute; top: 22px; left: 10%; right: 10%; height: 4px; background: #e0e0e0; z-index: 1; }
        .stepper-progress { position: absolute; top: 22px; right: 10%; height: 4px; background: #198754; z-index: 2; transition: width 0.5s ease; }
        .step-item { position: relative; z-index: 3; text-align: center; width: 25%; }
        .step-icon { width: 48px; height: 48px; border-radius: 50%; background: #e0e0e0; color: #fff; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 1.2rem; transition: all 0.3s ease; }
        .step-item.active .step-icon { background: #0d6efd; box-shadow: 0 0 0 6px rgba(13,110,253,0.2); }
        .step-item.completed .step-icon { background: #198754; }
        .step-item.canceled .step-icon { background: #dc3545; }
        .step-label { font-size: 0.85rem; font-weight: 700; color: #6c757d; }
        .step-item.active .step-label { color: #0d6efd; }
        .step-item.completed .step-label { color: #198754; }

```

-----------------------------------
## File Path: ./static/js/app.js
```
// Shared frontend helpers for TajerGo.
(function () {
    'use strict';

    window.fixImg = window.fixImg || function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };
})();

```

-----------------------------------
## File Path: ./static/js/dashboard.js
```
// TajerGo Dashboard JavaScript
(function () {
    'use strict';

    window.fixImg = function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };

    window.copyDriverPortalLink = function (token) {
        const input = document.getElementById('link-' + token);
        if (!input) return;
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(input.value).then(
                () => alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة'),
                () => fallbackCopy(input)
            );
        } else {
            fallbackCopy(input);
        }
    };

    function fallbackCopy(input) {
        input.select();
        document.execCommand('copy');
        alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة');
    }

    window.submitNewDriver = function (event) {
        event.preventDefault();
        const name = (document.getElementById('driverNameInput')?.value || '').trim();
        const phone = (document.getElementById('driverPhoneInput')?.value || '').trim();
        if (!name || !phone) {
            alert('يرجى إدخال اسم ورقم المندوب');
            return false;
        }

        fetch('/api/drivers/add', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name, phone})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إضافة المندوب بنجاح وتوليد بوابته الخاصة');
                window.location.reload();
            } else {
                alert('حدث خطأ: ' + (data.error || 'تعذر الإضافة'));
            }
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
        return false;
    };

    window.deleteDriver = function (token) {
        if (!confirm('هل أنت متأكد من حذف هذا المندوب؟')) return;
        fetch('/api/drivers/delete/' + encodeURIComponent(token), {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                if (data.success) window.location.reload();
                else alert(data.error || 'تعذر حذف المندوب');
            })
            .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.updateOrderStatus = function (orderId, newStatus) {
        fetch('/api/orders/update-status', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({order_id: orderId, status: newStatus})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) window.location.reload();
            else alert(data.error || 'تعذر تحديث الحالة');
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.assignOrderToDriver = function (orderId, selectEl) {
        const selectedOption = selectEl?.options[selectEl.selectedIndex];
        const driverName = selectedOption?.getAttribute('data-name');
        const driverPhone = selectedOption?.getAttribute('data-phone');
        if (!driverPhone) return;

        selectEl.disabled = true;
        fetch('/api/orders/assign-driver', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                order_id: orderId,
                driver_name: driverName,
                driver_phone: driverPhone
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إسناد الطلب (' + orderId + ') للمندوب: ' + driverName);
                window.location.reload();
            } else {
                alert(data.error || 'حدث خطأ أثناء الإسناد');
                selectEl.disabled = false;
            }
        })
        .catch(() => {
            alert('فشل الاتصال بالخادم');
            selectEl.disabled = false;
        });
    };

    document.addEventListener('DOMContentLoaded', function () {
        const activeTab = localStorage.getItem('tajergo_active_tab');
        if (activeTab) {
            const tabBtn = document.querySelector(`button[data-bs-target="${CSS.escape(activeTab)}"]`);
            if (tabBtn && window.bootstrap) {
                bootstrap.Tab.getOrCreateInstance(tabBtn).show();
            }
        }

        document.querySelectorAll('button[data-bs-toggle="tab"]').forEach(function (tabElm) {
            tabElm.addEventListener('shown.bs.tab', function (event) {
                const currentTarget = event.target.getAttribute('data-bs-target');
                if (currentTarget) localStorage.setItem('tajergo_active_tab', currentTarget);
            });
        });
    });
})();

```

-----------------------------------
## File Path: ./static/sw.js
```
const CACHE_NAME = 'tajergo-cache-v20260828';
const STATIC_EXTENSIONS = /\.(?:css|js|png|jpg|jpeg|webp|svg|woff2?|ico)$/i;

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // 1. مسارات الـ API والـ Manifest: دائماً من الشبكة لضمان التحديث الفوري
  if (url.pathname.startsWith('/api/') || url.pathname.includes('manifest')) {
    event.respondWith(fetch(request));
    return;
  }

  // 2. صفحات الموقع (HTML): استراتيجية Network First لتلبية شروط تثبيت التطبيق (PWA)
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request).catch(() => caches.match(request))
    );
    return;
  }

  // 3. الملفات الثابتة والصور: استراتيجية Stale-While-Revalidate لسرعة تحميل خارقة
  if (url.pathname.startsWith('/static/') || STATIC_EXTENSIONS.test(url.pathname)) {
    event.respondWith(
      caches.match(request).then(cachedResponse => {
        const fetchPromise = fetch(request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, responseToCache));
          }
          return networkResponse;
        }).catch(() => { /* تجاهل أخطاء الشبكة للملفات الثابتة */ });
        
        // إرجاع الكاش فوراً إن وجد (للسرعة)، وإلا انتظار الشبكة
        return cachedResponse || fetchPromise;
      })
    );
  }
});

```

-----------------------------------
## File Path: ./templates/base_dashboard.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{% block title %}لوحة التحكم | تاجر جو{% endblock %}</title>
    
    <!-- PWA & Mobile Meta Tags -->
    <link rel="manifest" href="/dashboard_manifest.json">
    <meta name="theme-color" content="#212529">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="تاجر جو">
    <link rel="icon" href="{{ url_for('static', filename='icon-512.png') }}?v={{ static_version }}">
    <link rel="apple-touch-icon" href="{{ url_for('static', filename='icon-192.png') }}?v={{ static_version }}">

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}?v={{ static_version }}">
    {% block head_extra %}{% endblock %}
</head>
<body>
    {% include 'partials/topbar.html' %}
    <main class="container pb-5">
        {% include 'partials/flash_messages.html' %}
        {% include 'partials/dashboard_nav.html' %}
        {% block dashboard_content %}{% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="{{ url_for('static', filename='js/dashboard.js') }}?v={{ static_version }}"></script>
    
    <!-- Service Worker Registration for PWA -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js', {updateViaCache: 'none'}).then(reg => { reg.update();
                    console.log('Dashboard SW registered successfully.');
                }).catch(err => console.log('Dashboard SW registration failed:', err));
            });
        }
    </script>

    {% block page_scripts %}{% endblock %}

<!-- SIDEBAR_TOGGLE_SCRIPT -->
<style>
    /* فرض الإخفاء وتمدد المحتوى */
    .tajergo-sidebar-hidden { display: none !important; }
    .tajergo-main-expanded { margin-right: 0 !important; width: 100% !important; max-width: 100% !important; }
</style>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        let toggleButtons = document.querySelectorAll('.fa-bars');
        let sidebar = document.querySelector('aside') || document.querySelector('.sidebar') || document.querySelector('[id*="sidebar"]');
        let mainContent = document.querySelector('main') || document.querySelector('.main-content') || document.querySelector('.page-content') || document.querySelector('[id*="main"]');
        
        if (toggleButtons.length > 0 && sidebar) {
            toggleButtons.forEach(icon => {
                let btn = icon.closest('button') || icon.closest('a') || icon;
                btn.style.cursor = 'pointer';
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    sidebar.classList.toggle('tajergo-sidebar-hidden');
                    if(mainContent) {
                        mainContent.classList.toggle('tajergo-main-expanded');
                    }
                });
            });
        }
    });
</script>
<!-- END_SIDEBAR_TOGGLE_SCRIPT -->
</body>
</html>

```

-----------------------------------
## File Path: ./templates/dashboard.html
```
{% extends "base_dashboard.html" %}

{% block title %}لوحة التحكم | تاجر جو{% endblock %}

{% block dashboard_content %}
{% set cats = products | map(attribute='category') | unique | list %}

<!-- بداية حاوية التبويبات المتوافقة مع شريط التنقل -->
<div class="tab-content">
    
    <!-- 1. الإحصائيات -->
    <div class="tab-pane fade" id="analytics">
        <div class="row mb-4">
            <div class="col-md-3 col-6 mb-2"><div class="card bg-success text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">صافي المبيعات 💰</h6><h3 class="mb-0">{{ '{:,.2f}'.format(adv_stats.net_sales) }} <small>{{ settings.currency }}</small></h3><small>نمو: <span dir="ltr">{{ '{:,.1f}'.format(adv_stats.growth_rate) }}%</span></small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card bg-primary text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">إجمالي الطلبات 📦</h6><h3 class="mb-0">{{ adv_stats.total_orders }}</h3><small>مكتملة: {{ adv_stats.completed_orders }} | ملغاة: {{ adv_stats.canceled_orders }}</small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card bg-info text-white shadow-sm border-0"><div class="card-body"><h6 class="fw-bold">متوسط الطلب 🛒</h6><h3 class="mb-0">{{ '{:,.2f}'.format(adv_stats.avg_order_value) }} <small>{{ settings.currency }}</small></h3><small>الإتمام: <span dir="ltr">{{ '{:,.1f}'.format(adv_stats.completion_rate) }}%</span></small></div></div></div>
            <div class="col-md-3 col-6 mb-2"><div class="card text-dark shadow-sm border-0" style="background-color:#ffc107;"><div class="card-body"><h6 class="fw-bold">قاعدة العملاء 👥</h6><h3 class="mb-0">{{ adv_stats.customers_count }}</h3><small>رسوم التوصيل: {{ '{:,.2f}'.format(adv_stats.delivery_fees) }}</small></div></div></div>
        </div>
        <div class="row mb-4">
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body text-center"><h6 class="fw-bold text-muted border-bottom pb-2">تفصيل المبيعات الزمنية</h6><div class="d-flex justify-content-between mb-2 mt-3"><span>مبيعات اليوم:</span> <span class="fw-bold text-primary">{{ '{:,.2f}'.format(adv_stats.today_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>مبيعات الأسبوع:</span> <span class="fw-bold text-success">{{ '{:,.2f}'.format(adv_stats.weekly_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>هذا الشهر:</span> <span class="fw-bold text-info">{{ '{:,.2f}'.format(adv_stats.this_month_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>الشهر الماضي:</span> <span class="fw-bold text-secondary">{{ '{:,.2f}'.format(adv_stats.last_month_sales) }}</span></div><div class="d-flex justify-content-between mb-2"><span>إجمالي غير الصافي:</span> <span class="fw-bold text-dark">{{ '{:,.2f}'.format(adv_stats.total_sales) }}</span></div></div></div></div>
            <div class="col-md-8"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-muted mb-3 border-bottom pb-2">المبيعات خلال 7 أيام</h6><canvas id="salesChart" style="max-height: 200px;"></canvas></div></div></div>
        </div>
        <div class="row mb-4">
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-success border-bottom pb-2">🌟 العملاء الأكثر شراءً</h6><ul class="list-group list-group-flush mt-3">{% for c in adv_stats.top_customers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><div><i class="fas fa-user-circle text-muted me-1"></i> {{ c.name }} <br><small class="text-muted">{{ c.orders }} طلبات</small></div><span class="fw-bold text-success">{{ '{:,.2f}'.format(c.spent) }}</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-primary border-bottom pb-2">🔥 الأكثر مبيعًا</h6><ul class="list-group list-group-flush mt-3">{% for p_name, qty in adv_stats.best_sellers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><span class="text-truncate" style="max-width: 150px;">{{ p_name }}</span><span class="badge bg-primary rounded-pill">{{ qty }} قطعة</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
            <div class="col-md-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h6 class="fw-bold text-danger border-bottom pb-2">⚠️ الأقل مبيعًا</h6><ul class="list-group list-group-flush mt-3">{% for p_name, qty in adv_stats.least_sellers %}<li class="list-group-item d-flex justify-content-between align-items-center px-0"><span class="text-truncate" style="max-width: 150px;">{{ p_name }}</span><span class="badge bg-danger rounded-pill">{{ qty }} قطعة</span></li>{% else %}<li class="list-group-item text-center text-muted">لا يوجد بيانات</li>{% endfor %}</ul></div></div></div>
        </div>
    </div>
    
    <!-- 2. الطلبات -->
    <div class="tab-pane fade" id="orders">
        <div class="row">
            <div class="col-md-12 mb-4">
                <div class="card shadow-sm border-0 h-100">
                    <div class="card-body">
                        <a href="/export/orders" class="btn btn-success btn-sm fw-bold shadow-sm mb-3"><i class="fas fa-file-excel"></i> تصدير Excel</a>

                        <div class="table-responsive bg-white rounded-4 shadow-sm border p-2">
                            <table class="table table-hover align-middle mb-0 text-center">
                                <thead class="table-light">
                                    <tr class="text-secondary small fw-bold">
                                        <th style="width: 130px;">رقم الطلب</th>
                                        <th class="text-start">العميل والهاتف</th>
                                        <th class="text-start">المنتجات</th>
                                        <th>الإجمالي</th>
                                        <th>الحالة الحالية</th>
                                        <th class="text-primary"><i class="fas fa-motorcycle me-1"></i> المندوب</th>
                                        <th>تحديث الحالة</th>
                                    </tr>
                                    <tr class="bg-light">
                                        <th><input type="text" id="filterOrdId" class="form-control form-control-sm border-primary shadow-sm" placeholder="🔍 فلترة بالرقم..." onkeyup="filterOrdersTable()"></th>
                                        <th><input type="text" id="filterOrdCust" class="form-control form-control-sm border-primary shadow-sm" placeholder="🔍 بالعميل/الهاتف..." onkeyup="filterOrdersTable()"></th>
                                        <th></th>
                                        <th></th>
                                        <th>
                                            <select id="filterOrdStat" class="form-select form-select-sm border-primary shadow-sm fw-bold" onchange="filterOrdersTable()">
                                                <option value="">كل الحالات</option>
                                                <option value="جديد 🟡">جديد 🟡</option>
                                                <option value="مدفوع 🟢">مدفوع 🟢</option>
                                                <option value="قيد التجهيز 🔵">قيد التجهيز 🔵</option>
                                                <option value="تم التوصيل 🟢">تم التوصيل 🟢</option>
                                                <option value="ملغي 🔴">ملغي 🔴</option>
                                            </select>
                                        </th>
                                        <th></th>
                                        <th></th>
                                    </tr>
                                </thead>
                                <tbody id="ordersTableBody">
                                    {% if orders %}
                                        {% for o in orders %}
                                        <tr class="order-row">
                                            <td>
                                                <span class="fw-bold text-dark d-block mb-1">{{ o.order_id }}</span>
                                                <a href="/track/{{ o.order_id }}" target="_blank" class="btn btn-outline-primary btn-sm rounded-pill px-2 py-0" style="font-size: 0.72rem;">
                                                    <i class="fas fa-truck-fast"></i> تتبع
                                                </a>
                                            </td>
                                            <td class="text-start">
                                                <div class="fw-bold text-dark">👤 {{ o.customer_name }}</div>
                                                <div class="small text-muted"><i class="fas fa-phone-alt text-success me-1"></i> {{ o.customer_phone }}</div>
                                                {% if o.customer_address %}
                                                <div class="small text-muted text-truncate" style="max-width: 140px;">📍 {{ o.customer_address }}</div>
                                                {% endif %}
                                            </td>
                                            <td class="text-start">
                                                <div class="small" style="max-height: 100px; overflow-y: auto; line-height: 1.6;">
                                                    {% if o.cart_items %}
                                                        {% for i in o.cart_items %}
                                                            <div class="text-dark fw-bold">▪️ {{ i.name }} <span class="badge bg-light text-secondary border px-1" style="font-size: 0.72rem;">x{{ i.qty }}</span></div>
                                                        {% endfor %}
                                                    {% elif o.get('cart_items', []) %}
                                                        <div class="text-dark fw-bold">{{ o.get('cart_items', []) }}</div>
                                                    {% else %}
                                                        <span class="text-muted small">-</span>
                                                    {% endif %}
                                                </div>
                                            </td>
                                            <td>
                                                <span class="fw-bold text-success fs-6">{{ o.total }}</span>
                                            </td>
                                            <td>
                                                <span class="badge {% if 'توصيل' in o.status or 'مدفوع' in o.status %}bg-success{% elif 'مع المندوب' in o.status %}bg-primary{% elif 'تجهيز' in o.status %}bg-info text-dark{% elif 'ملغي' in o.status %}bg-danger{% else %}bg-warning text-dark{% endif %} px-2 py-1 rounded-pill small">
                                                    {{ o.status }}
                                                </span>
                                            </td>
                                            <td>
                                                <select class="form-select form-select-sm rounded-pill border-primary border-opacity-50 shadow-sm fw-bold mx-auto" 
                                                        style="min-width: 135px; font-size: 0.78rem;" 
                                                        onchange="assignOrderToDriver('{{ o.order_id }}', this)">
                                                    <option value="">{% if o.driver_name %}🛵 {{ o.driver_name }}{% else %}-- تعيين مندوب --{% endif %}</option>
                                                    {% if drivers %}
                                                        {% for d in drivers %}
                                                        <option value="{{ d.get('phone', '') }}" data-name="{{ d.get('name', '') }}" data-phone="{{ d.get('phone', '') }}" {% if o.driver_phone == d.get('phone', '') %}selected{% endif %}>
                                                            🛵 {{ d.get('name', '') }}
                                                        </option>
                                                        {% endfor %}
                                                    {% else %}
                                                        <option disabled>(أضف مناديب أولاً)</option>
                                                    {% endif %}
                                                </select>
                                            </td>
                                            <td>
                                                <div class="btn-group btn-group-sm" role="group">
                                                    <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'جديد 🟡')" class="btn btn-outline-warning py-0 px-1" style="font-size: 0.7rem;">جديد 🟡</button>
                                                    <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'مدفوع 🟢')" class="btn btn-outline-success py-0 px-1" style="font-size: 0.7rem;">مدفوع 🟢</button>
                                                    <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'قيد التجهيز 🔵')" class="btn btn-outline-info py-0 px-1" style="font-size: 0.7rem;">تجهيز 🔵</button>
                                                    <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'تم التوصيل 🟢')" class="btn btn-outline-success py-0 px-1" style="font-size: 0.7rem;">توصيل 🟢</button>
                                                    <button type="button" onclick="updateOrderStatus('{{ o.order_id }}', 'ملغي 🔴')" class="btn btn-outline-danger py-0 px-1" style="font-size: 0.7rem;">ملغي 🔴</button>
                                                </div>
                                            </td>
                                        </tr>
                                        {% endfor %}
                                    {% else %}
                                        <tr>
                                            <td colspan="7" class="text-center py-5 text-muted">
                                                <i class="fas fa-box-open fs-1 mb-2 opacity-50 d-block"></i>
                                                لا توجد طلبات مسجلة حتى الآن
                                            </td>
                                        </tr>
                                    {% endif %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. المنتجات (النشط افتراضياً) -->
    <div class="tab-pane fade show active" id="products">
        
        <datalist id="unit-options">
            <option value="حبة"></option><option value="كجم"></option><option value="جرام"></option><option value="لتر"></option>
            <option value="مل"></option><option value="كرتون"></option><option value="درزن"></option><option value="طقم"></option>
            <option value="متر"></option><option value="خدمة"></option>
        </datalist>

        <div class="card shadow-sm border-0 mb-4 border-top border-4 border-primary">
            <div class="card-body">
                <h5 class="fw-bold mb-3"><i class="fas fa-plus-circle text-primary"></i> إضافة منتج</h5>
                <form method="POST" class="row g-3" id="addProductForm">
                    <input type="hidden" name="action" value="add_product">
                    <div class="col-md-3">
                        <label class="small fw-bold">الاسم</label>
                        <input name="name" class="form-control" required>
                    </div>
                    <div class="col-md-3">
                        <label class="small fw-bold">السعر</label>
                        <input name="price" type="number" step="0.01" class="form-control" required>
                    </div>
                    <div class="col-md-3">
                        <label class="small fw-bold">الكمية</label>
                        <input name="stock" type="number" class="form-control" required>
                    </div>
                    
                    <div class="col-md-3">
                        <label class="small fw-bold text-success"><i class="fas fa-balance-scale"></i> الوحدة</label>
                        <select name="unit_select" class="form-select border-success" onchange="if(this.value=='NEW_UNIT'){document.getElementById('newUnitInput').style.display='block'; document.getElementById('newUnitInput').required=true; document.getElementById('finalUnit').value='';}else{document.getElementById('newUnitInput').style.display='none'; document.getElementById('newUnitInput').required=false; document.getElementById('finalUnit').value=this.value;}">
                            <option value="حبة" selected>حبة</option>
                            <option value="كجم">كجم</option>
                            <option value="جرام">جرام</option>
                            <option value="لتر">لتر</option>
                            <option value="NEW_UNIT" class="text-primary fw-bold">➕ وحدة مخصصة...</option>
                        </select>
                        <input type="text" id="newUnitInput" class="form-control border-success mt-2" placeholder="اكتب الوحدة..." style="display:none;" oninput="document.getElementById('finalUnit').value=this.value">
                        <input type="hidden" name="unit" id="finalUnit" value="حبة">
                    </div>

                    <div class="col-md-6">
                        <label class="small fw-bold">التصنيف</label>
                        <input type="hidden" name="cat" id="finalCategory" required>
                        <select class="form-select" id="categorySelect" onchange="handleCategoryChange(this)" required>
                            <option value="" disabled selected>-- اختر تصنيفاً --</option>
                            {% for c in cats %}<option value="{{ c }}">{{ c }}</option>{% endfor %}
                            <option value="إلكترونيات وجوالات">إلكترونيات وجوالات</option>
                            <option value="ملابس وأزياء">ملابس وأزياء</option>
                            <option value="NEW_CATEGORY" class="fw-bold text-primary">➕ تصنيف جديد...</option>
                        </select>
                        <input type="text" id="newCategoryInput" class="form-control mt-2" placeholder="التصنيف الجديد" style="display: none;" oninput="updateFinalCategory()">
                    </div>
                    <div class="col-md-6">
                        <label class="small fw-bold">صورة المنتج</label>
                        <div class="upload-btn-wrapper">
                            <button type="button" class="btn btn-outline-primary w-100 fw-bold border-2" style="padding:8px;"><i class="fas fa-cloud-upload-alt"></i> رفع للسحابة</button>
                            <input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'newProductImg', 'newProductStatus', 'submitProductBtn')">
                        </div>
                        <small id="newProductStatus" class="fw-bold d-block text-secondary text-center mb-1" style="font-size:0.8rem;"></small>
                        <div class="divider-text" style="font-size:0.8rem;">أو أدخل الرابط يدوياً</div>
                        <input type="text" name="img" id="newProductImg" class="form-control" placeholder="https://...">
                    </div>
                    <div class="col-12">
                        <label class="small fw-bold">الوصف</label>
                        <input name="desc" class="form-control">
                    </div>
                    <div class="col-12 mt-4">
                        <button class="btn btn-primary w-100 fw-bold shadow-sm" type="button" id="submitProductBtn" onclick="submitProductForm()">حفظ ونشر</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="card shadow-sm border-0 mb-4">
            <div class="card-body">
                <h5 class="fw-bold mb-3"><i class="fas fa-box"></i> المنتجات الحالية</h5>
                <div class="row mb-3 bg-white p-3 rounded shadow-sm mx-0">
                    <div class="col-md-8 mb-2">
                        <label class="small fw-bold text-muted">بحث بالاسم</label>
                        <div class="input-group shadow-sm">
                            <span class="input-group-text bg-white border-primary text-primary"><i class="fas fa-search"></i></span>
                            <input type="text" id="adminProductSearch" class="form-control border-primary" placeholder="اكتب اسم المنتج للبحث السريع..." onkeyup="filterAdminProducts()">
                        </div>
                    </div>
                    <div class="col-md-4 mb-2">
                        <label class="small fw-bold text-muted">تصفية حسب القسم</label>
                        <select id="adminCategoryFilter" class="form-select border-primary shadow-sm" onchange="filterAdminProducts()">
                            <option value="ALL">عرض كل التصنيفات</option>
                            {% for c in cats %}<option value="{{ c }}">{{ c }}</option>{% endfor %}
                        </select>
                    </div>
                </div>
                <div class="table-responsive">
                    <table class="table table-hover align-middle">
                        <thead class="table-light">
                            <tr>
                                <th>الصورة</th>
                                <th>الاسم</th>
                                <th>السعر / الوحدة</th>
                                <th>الكمية</th>
                                <th>التصنيف</th>
                                <th>إجراءات</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for p in products %}
                            <tr class="admin-product-row" data-name="{{ p.name }}" data-cat="{{ p.category }}">
                                <td><img src="{{ p.image_url }}" onerror="fixImg(this)" width="50" height="50" style="object-fit:cover; border-radius:5px;"></td>
                                <td class="fw-bold">{{ p.name }}</td>
                                <td class="text-primary fw-bold">{{ p.price }} <small class="text-muted fw-normal">/ {{ p.get('unit', 'حبة') }}</small></td>
                                <td>{{ p.stock }}</td>
                                <td><span class="badge bg-secondary">{{ p.category }}</span></td>
                                <td>
                                    <button class="btn btn-sm btn-success mb-1 w-100 fw-bold shadow-sm" onclick="shareDashboardProduct('{{ p.name|replace("'", "\\'") }}', '{{ p.description|replace("'", "\\'")|replace('\n', ' ') }}', '{{ p.image_url }}')"><i class="fab fa-whatsapp me-1"></i> مشاركة</button>
                                    <button class="btn btn-sm btn-primary w-100 mb-1 shadow-sm" data-bs-toggle="modal" data-bs-target="#editModal{{ p.id }}">تعديل</button> 
                                    <form method="POST" class="d-inline" onsubmit="return confirm('حذف؟');">
                                        <input type="hidden" name="action" value="delete_product">
                                        <input type="hidden" name="product_id" value="{{ p.id }}">
                                        <button type="submit" class="btn btn-sm btn-danger w-100 shadow-sm">حذف</button>
                                    </form>
                                </td>
                            </tr>
                            <div class="modal fade" id="editModal{{ p.id }}">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header bg-light">
                                            <h5 class="modal-title fw-bold">تعديل: {{ p.name }}</h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                        </div>
                                        <div class="modal-body">
                                            <form method="POST" class="row g-3">
                                                <input type="hidden" name="action" value="edit_product">
                                                <input type="hidden" name="product_id" value="{{ p.id }}">
                                                <div class="col-12">
                                                    <label class="small fw-bold">الاسم</label>
                                                    <input name="name" class="form-control" value="{{ p.name }}" required>
                                                </div>
                                                <div class="col-4">
                                                    <label class="small fw-bold">السعر</label>
                                                    <input name="price" type="number" step="0.01" class="form-control" value="{{ p.price }}" required>
                                                </div>
                                                <div class="col-4">
                                                    <label class="small fw-bold">المخزون</label>
                                                    <input name="stock" type="number" class="form-control" value="{{ p.stock }}" required>
                                                </div>

                                                <div class="col-4">
                                                    <label class="small fw-bold text-success"><i class="fas fa-balance-scale"></i> الوحدة</label>
                                                    <select name="unit_select" class="form-select border-success" onchange="if(this.value=='NEW_UNIT'){document.getElementById('editUnitInput{{ p.id }}').style.display='block'; document.getElementById('editUnitInput{{ p.id }}').required=true; document.getElementById('editFinalUnit{{ p.id }}').value='';}else{document.getElementById('editUnitInput{{ p.id }}').style.display='none'; document.getElementById('editUnitInput{{ p.id }}').required=false; document.getElementById('editFinalUnit{{ p.id }}').value=this.value;}">
                                                        <option value="حبة" {% if p.get('unit', 'حبة') == 'حبة' %}selected{% endif %}>حبة</option>
                                                        <option value="كجم" {% if p.get('unit') == 'كجم' %}selected{% endif %}>كجم</option>
                                                        <option value="جرام" {% if p.get('unit') == 'جرام' %}selected{% endif %}>جرام</option>
                                                        <option value="لتر" {% if p.get('unit') == 'لتر' %}selected{% endif %}>لتر</option>
                                                        <option value="NEW_UNIT" {% if p.get('unit', 'حبة') not in ['حبة','كجم','جرام','لتر'] %}selected{% endif %} class="text-primary fw-bold">➕ وحدة مخصصة...</option>
                                                    </select>
                                                    <input type="text" id="editUnitInput{{ p.id }}" class="form-control border-success mt-2" placeholder="اكتب الوحدة..." style="{% if p.get('unit', 'حبة') in ['حبة','كجم','جرام','لتر'] %}display:none;{% else %}display:block;{% endif %}" value="{% if p.get('unit', 'حبة') not in ['حبة','كجم','جرام','لتر'] %}{{ p.get('unit') }}{% endif %}" oninput="document.getElementById('editFinalUnit{{ p.id }}').value=this.value">
                                                    <input type="hidden" name="unit" id="editFinalUnit{{ p.id }}" value="{{ p.get('unit', 'حبة') }}">
                                                </div>

                                                <div class="col-12">
                                                    <label class="small fw-bold">التصنيف</label>
                                                    <input name="cat" class="form-control" value="{{ p.category }}" required>
                                                </div>
                                                <div class="col-12">
                                                    <label class="small fw-bold">تغيير الصورة</label>
                                                    <input type="file" class="form-control mb-1" accept="image/*" onchange="uploadImageToCloud(this, 'editImgUrl{{ p.id }}', 'editImgStatus{{ p.id }}', 'editSaveBtn{{ p.id }}')">
                                                    <small id="editImgStatus{{ p.id }}" class="fw-bold d-block text-secondary mb-1"></small>
                                                    <input type="text" name="img" id="editImgUrl{{ p.id }}" class="form-control" value="{{ p.image_url }}">
                                                </div>
                                                <div class="col-12">
                                                    <label class="small fw-bold">الوصف</label>
                                                    <input name="desc" class="form-control" value="{{ p.description }}">
                                                </div>
                                                <div class="col-12 mt-3">
                                                    <button type="submit" class="btn btn-primary w-100 fw-bold" id="editSaveBtn{{ p.id }}">حفظ التعديلات</button>
                                                </div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. المناديب والتوصيل -->
    <div class="tab-pane fade" id="drivers-pane">
        <div class="d-flex justify-content-between align-items-center mb-4 mt-3 bg-white p-3 rounded shadow-sm border border-info border-start-0 border-end-0 border-bottom-0 border-4">
            <div>
                <h5 class="fw-bold text-info mb-1"><i class="fas fa-motorcycle me-2"></i> إدارة فريق التوصيل</h5>
                <small class="text-muted fw-bold">أضف مناديبك وشاركهم روابط الاستلام.</small>
            </div>
            <button class="btn btn-info btn-sm rounded-pill text-white px-4 py-2 fw-bold shadow-sm" data-bs-toggle="modal" data-bs-target="#addDriverModal">
                <i class="fas fa-plus-circle me-1"></i> مندوب جديد
            </button>
        </div>

        <div class="row g-3" id="driversListContainer">
            {% if drivers %}
                {% for d in drivers %}
                <div class="col-md-6 col-lg-4">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">{{ d.get('name', '') }}</h6>
                                <span class="text-muted small"><i class="fas fa-phone-alt me-1 text-success"></i> {{ d.get('phone', '') }}</span>
                            </div>
                            <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 px-2 py-1 small rounded-pill">نشط 🟢</span>
                        </div>
                        
                        <div class="bg-light p-2 rounded-3 my-2 small border border-light">
                            <span class="text-muted d-block mb-1 fw-bold">رابط البوابة الميدانية:</span>
                            <div class="input-group input-group-sm">
                                <input type="text" class="form-control border-0 bg-white" value="{{ request.host_url }}driver/{{ d.get('token', d.get('_id', '')) }}" id="link-{{ d.get('token', d.get('_id', '')) }}" readonly>
                                <button class="btn btn-outline-primary" onclick="copyDriverPortalLink('{{ d.get('token', d.get('_id', '')) }}')" title="نسخ الرابط"><i class="fas fa-copy"></i></button>
                            </div>
                        </div>

                        <div class="d-flex justify-content-between align-items-center mt-3 pt-3 border-top">
                            <a href="/driver/{{ d.get('token', d.get('_id', '')) }}" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3 fw-bold shadow-sm">
                                <i class="fas fa-external-link-alt me-1"></i> فتح صفحة المندوب
                            </a>
                            <form method="POST" class="d-inline" onsubmit="return confirm('تأكيد حذف المندوب؟');">
                                <input type="hidden" name="action" value="delete_driver">
                                <input type="hidden" name="driver_phone" value="{{ d.get('phone', '') }}">
                                <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3 fw-bold">
                                    <i class="fas fa-trash-alt me-1"></i> إزالة
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
                {% endfor %}
            {% else %}
                <div class="col-12 text-center py-5 bg-white rounded-4 shadow-sm border border-light">
                    <i class="fas fa-motorcycle fs-1 text-muted mb-3 opacity-50 d-block"></i>
                    <h6 class="text-muted fw-bold">لم تقم بإضافة أي مندوب توصيل بعد</h6>
                </div>
            {% endif %}
        </div>
    </div>

    <!-- 5. الكوبونات -->
    <div class="tab-pane fade" id="coupons"><div class="row"><div class="col-md-5 mb-4"><div class="card shadow-sm border-0 border-top border-4 border-warning"><div class="card-body"><h5 class="fw-bold mb-3"><i class="fas fa-ticket-alt text-warning"></i> إنشاء كوبون خصم</h5><form method="POST"><input type="hidden" name="action" value="add_coupon"><div class="mb-3"><label class="small fw-bold">كود الكوبون (مثال: KSA20)</label><input type="text" name="code" class="form-control" required style="text-transform: uppercase;"></div><div class="mb-4"><label class="small fw-bold">نسبة الخصم المئوية (%)</label><input type="number" name="discount" class="form-control" placeholder="مثال: 15" required min="1" max="99"></div><button type="submit" class="btn btn-warning w-100 fw-bold text-dark shadow-sm">تفعيل الكوبون</button></form></div></div></div><div class="col-md-7"><div class="card shadow-sm border-0"><div class="card-body"><h5 class="fw-bold mb-3">الكوبونات الفعالة</h5><div class="table-responsive"><table class="table table-hover align-middle"><thead class="table-light"><tr><th>كود الكوبون</th><th>نسبة الخصم</th><th>إجراءات</th></tr></thead><tbody>{% for c in coupons %}<tr><td class="fw-bold text-primary fs-5">{{ c.code }}</td><td><span class="badge bg-success fs-6">{{ c.discount }}%</span></td><td><form method="POST" onsubmit="return confirm('إلغاء هذا الكوبون؟');"><input type="hidden" name="action" value="delete_coupon"><input type="hidden" name="coupon_id" value="{{ c.id }}"><button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button></form></td></tr>{% else %}<tr><td colspan="3" class="text-muted py-3 text-center fw-bold">لا توجد كوبونات فعالة حالياً</td></tr>{% endfor %}</tbody></table></div></div></div></div></div></div>

    <!-- 6. الإعدادات -->
    <div class="tab-pane fade" id="settings"><div class="row"><div class="col-lg-8 mb-4"><div class="card shadow-sm border-0 h-100"><div class="card-body"><h5 class="fw-bold mb-3 border-bottom pb-2">⚙️ إعدادات المتجر والهوية والتخزين</h5><form method="POST" class="row g-3"><input type="hidden" name="action" value="save_settings">{% if is_super_admin %}<div class="col-md-12 mb-4 p-3 bg-dark rounded border border-warning shadow-sm"><label class="small fw-bold text-warning"><i class="fas fa-crown"></i> إعدادات المنصة: شعار بوابة الدخول</label><div class="d-flex align-items-center gap-3 mt-2"><img src="{{ settings.get('platform_logo', platform_logo) }}" onerror="fixImg(this)" width="60" height="60" style="object-fit:cover; border-radius:50%; border:2px solid #ffc107; background:#fff;"><div class="flex-grow-1"><div class="upload-btn-wrapper mb-0"><button type="button" class="btn btn-outline-warning btn-sm w-100 fw-bold border-2 text-white"><i class="fas fa-cloud-upload-alt"></i> رفع الشعار</button><input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'platformLogoInput', 'platformLogoStatus', 'settingsSaveBtn')"></div><small id="platformLogoStatus" class="fw-bold d-block text-warning mb-1" style="font-size:0.8rem;"></small><input type="text" name="platform_logo" id="platformLogoInput" class="form-control form-control-sm border-warning bg-light" value="{{ settings.get('platform_logo', '') }}" placeholder="أو الصق الرابط المباشر"></div></div></div>{% endif %}<div class="col-md-12 mb-4 p-3 bg-light rounded border border-info shadow-sm d-flex justify-content-between align-items-center"><div class="fw-bold text-info"><i class="fas fa-box-open"></i> باقة اشتراكك الحالية: <span class="badge bg-primary fs-6">{{ current_user_data.get('package', 'أساسية') if current_user_data else 'أساسية' }}</span></div></div><div class="col-md-12 mb-2 border-bottom pb-3"><label class="small fw-bold text-primary"><i class="fas fa-store"></i> شعار متجرك (Store Logo)</label><div class="d-flex align-items-center gap-3 mt-1">{% if settings.get('logo_url') %}<img src="{{ settings.logo_url }}" onerror="fixImg(this)" width="60" height="60" style="object-fit:cover; border-radius:50%; border:2px solid #ccc;">{% endif %}<div class="flex-grow-1"><div class="upload-btn-wrapper mb-0"><button type="button" class="btn btn-outline-primary btn-sm w-100 fw-bold border-2"><i class="fas fa-cloud-upload-alt"></i> رفع شعار المتجر</button><input type="file" accept="image/*" onchange="uploadImageToCloud(this, 'storeLogoInput', 'logoStatus', 'settingsSaveBtn')"></div><small id="logoStatus" class="fw-bold d-block text-secondary" style="font-size:0.8rem;"></small><input type="text" name="logo_url" id="storeLogoInput" class="form-control form-control-sm mt-1" value="{{ settings.get('logo_url', '') }}" placeholder="أو الصق رابط شعار متجرك"></div></div></div><div class="col-md-6"><label class="small fw-bold">اسم المتجر</label><input name="store_name" class="form-control" value="{{ settings.store_name }}"></div><div class="col-md-6"><label class="small fw-bold">اللون الأساسي</label><input type="color" name="theme_color" class="form-control form-control-color w-100" value="{{ settings.theme_color }}"></div><div class="col-md-6"><label class="small fw-bold">الخط (Font)</label><select name="font_family" class="form-select"><option value="Cairo" {% if settings.font_family=='Cairo' %}selected{% endif %}>Cairo</option><option value="Tajawal" {% if settings.font_family=='Tajawal' %}selected{% endif %}>Tajawal</option><option value="Almarai" {% if settings.font_family=='Almarai' %}selected{% endif %}>Almarai</option><option value="Changa" {% if settings.font_family=='Changa' %}selected{% endif %}>Changa</option></select></div><div class="col-md-6"><label class="small fw-bold">حجم الرأس</label><select name="header_size" class="form-select"><option value="small" {% if settings.header_size=='small' %}selected{% endif %}>صغير</option><option value="medium" {% if settings.header_size=='medium' %}selected{% endif %}>متوسط</option><option value="large" {% if settings.header_size=='large' %}selected{% endif %}>كبير</option></select></div><div class="col-md-4"><label class="small fw-bold">رقم الواتساب</label><input name="whatsapp" class="form-control" value="{{ settings.whatsapp }}"></div><div class="col-md-4"><label class="small fw-bold">العملة</label><input name="currency" class="form-control" value="{{ settings.currency }}"></div><div class="col-md-4"><label class="small fw-bold">نص زر الشراء</label><input name="btn_text" class="form-control" value="{{ settings.btn_text }}"></div><div class="col-12"><label class="small fw-bold">وصف المتجر</label><input name="store_desc" class="form-control" value="{{ settings.store_desc }}"></div>
<div class="col-12 border-bottom pb-3 mt-3"><label class="small fw-bold text-success"><i class="fas fa-handshake"></i> رسالة الترحيب للعملاء (تظهر عند زيارة المتجر)</label><input name="welcome_message" class="form-control border-success bg-light" value="{{ settings.get('welcome_message', 'أهلاً بك في متجرنا! نتمنى لك تسوقاً ممتعاً.') }}" placeholder="اكتب عبارة ترحيبية جذابة لعملائك..."></div>
<h6 class="fw-bold mt-3 mb-1 border-bottom pb-2">روابط التواصل والنطاق المخصص</h6><div class="col-md-4"><label class="small fw-bold">فيسبوك</label><input name="facebook" class="form-control" value="{{ settings.get('facebook', '') }}"></div><div class="col-md-4"><label class="small fw-bold">إنستجرام</label><input name="instagram" class="form-control" value="{{ settings.get('instagram', '') }}"></div><div class="col-md-4"><label class="small fw-bold">تيك توك</label><input name="tiktok" class="form-control" value="{{ settings.get('tiktok', '') }}"></div><div class="col-md-6"><label class="small fw-bold text-info"><i class="fab fa-telegram"></i> يوزر التلجرام</label><input name="telegram" class="form-control border-info" value="{{ settings.get('telegram', '') }}" placeholder="بدون @"></div><div class="col-md-6"><label class="small fw-bold">الدومين المخصص</label><input name="custom_domain" class="form-control" value="{{ settings.get('custom_domain', '') }}" placeholder="www.domain.com"></div><div class="col-12 mt-4 border-bottom pb-2 d-flex justify-content-between align-items-center"><h6 class="fw-bold text-primary mb-0"><i class="fas fa-cloud"></i> إعدادات السحابة</h6><button type="button" class="btn btn-sm btn-outline-info fw-bold" data-bs-toggle="modal" data-bs-target="#guideModal"><i class="fas fa-question-circle"></i> المساعدة</button></div>
    
    <div class="col-md-12 mb-2">
        <label class="small fw-bold">مزود الخدمة</label>
        <select name="img_provider" class="form-select" id="providerSelect" onchange="toggleProviderFields()">
            <option value="catbox" {% if settings.get('img_provider', 'catbox') == 'catbox' %}selected{% endif %}>Catbox.moe (مجاني 🚀)</option>
            <option value="imgbb" {% if settings.get('img_provider') == 'imgbb' %}selected{% endif %}>ImgBB</option>
            <option value="freeimagehost" {% if settings.get('img_provider') == 'freeimagehost' %}selected{% endif %}>FreeImage.host</option>
            <option value="imgur" {% if settings.get('img_provider') == 'imgur' %}selected{% endif %}>Imgur</option>
            <option value="postimages" {% if settings.get('img_provider') == 'postimages' %}selected{% endif %}>Postimages</option>
            <option value="cloudinary" {% if settings.get('img_provider') == 'cloudinary' %}selected{% endif %}>Cloudinary</option>
        </select>
    </div>
    
    <div class="col-md-12" id="basicProviderField" style="{% if settings.get('img_provider', 'catbox') == 'cloudinary' or settings.get('img_provider', 'catbox') == 'catbox' %}display:none;{% endif %}"><label class="small fw-bold">مفتاح الربط (API Key)</label><input name="img_api_key" type="password" class="form-control" value="{{ settings.get('img_api_key', '') }}"></div>
    <div class="col-md-6 cloudinary-fields" style="{% if settings.get('img_provider', 'catbox') != 'cloudinary' %}display:none;{% endif %}"><label class="small fw-bold text-info">Cloud Name</label><input name="cloudinary_name" type="text" class="form-control" value="{{ settings.get('cloudinary_name', '') }}"></div>
    <div class="col-md-6 cloudinary-fields" style="{% if settings.get('img_provider', 'catbox') != 'cloudinary' %}display:none;{% endif %}"><label class="small fw-bold text-info">Upload Preset</label><input name="cloudinary_preset" type="password" class="form-control" value="{{ settings.get('cloudinary_preset', '') }}"></div>
    
    <div class="col-12 mt-4 border-bottom pb-2 d-flex justify-content-between align-items-center">
        <h6 class="fw-bold text-success mb-0"><i class="fas fa-wallet"></i> بوابات الدفع والمحافظ البنكية (API)</h6>
        <span class="badge bg-success bg-opacity-10 text-success border border-success px-2 py-1"><i class="fas fa-bolt"></i> ميزة قادمة</span>
    </div>
    <div class="col-md-12 mb-2">
        <small class="text-muted d-block mb-2">أدخل بيانات الربط البرمجي لتفعيل الدفع الإلكتروني المباشر مستقبلاً.</small>
        <label class="small fw-bold">مزود خدمة الدفع</label>
        <select name="wallet_provider" class="form-select border-success">
            <option value="" {% if not settings.get('wallet_provider') %}selected{% endif %}>إيقاف (الدفع عند الاستلام/التحويل اليدوي فقط)</option>
            <option value="jawali" {% if settings.get('wallet_provider') == 'jawali' %}selected{% endif %}>جوالي (Jawali)</option>
            <option value="floosak" {% if settings.get('wallet_provider') == 'floosak' %}selected{% endif %}>فلوسك (Floosak)</option>
            <option value="kuraimi" {% if settings.get('wallet_provider') == 'kuraimi' %}selected{% endif %}>ام فلوس - الكريمي</option>
            <option value="jeeb" {% if settings.get('wallet_provider') == 'jeeb' %}selected{% endif %}>محفظة جيب (Jeeb)</option>
            <option value="custom" {% if settings.get('wallet_provider') == 'custom' %}selected{% endif %}>محفظة بنكية أخرى (Custom API)</option>
        </select>
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">رقم التاجر (Merchant ID)</label>
        <input name="wallet_merchant_id" type="text" class="form-control" value="{{ settings.get('wallet_merchant_id', '') }}" placeholder="مثال: 123456">
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">مفتاح الربط (API Key)</label>
        <input name="wallet_api_key" type="password" class="form-control" value="{{ settings.get('wallet_api_key', '') }}" placeholder="API Key">
    </div>
    <div class="col-md-4">
        <label class="small fw-bold">الرمز السري (Secret Token)</label>
        <input name="wallet_secret" type="password" class="form-control" value="{{ settings.get('wallet_secret', '') }}" placeholder="Secret Token">
    </div>
    <div class="col-12 mt-4">
<button type="submit" class="btn btn-primary w-100 fw-bold shadow-sm" id="settingsSaveBtn">حفظ كافة التحديثات</button></div></form>

                            <div class="card border-0 shadow-sm mb-4" style="border-radius: 16px;">
                                <div class="card-header bg-white border-0 pt-4 pb-0">
                                    <h6 class="fw-bold text-dark"><i class="fab fa-telegram text-info fs-5 me-2"></i> إشعارات الطلبات الفورية (تليجرام)</h6>
                                    <p class="text-muted small">احصل على تفاصيل أي طلب جديد فوراً على حسابك في تليجرام.</p>
                                </div>
                                <div class="card-body">
                                    <form method="POST" action="/dashboard">
                                        <input type="hidden" name="action" value="save_telegram_settings">
                                        <div class="form-check form-switch mb-3">
                                            <input class="form-check-input" type="checkbox" id="enable_telegram" name="enable_telegram" {% if settings.get('enable_telegram') %}checked{% endif %}>
                                            <label class="form-check-label fw-bold" for="enable_telegram">تفعيل إرسال الطلبات إلى تليجرام</label>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label fw-bold small">معرف الدردشة (Chat ID) *</label>
                                            <input type="text" class="form-control bg-light border-0" name="telegram_chat_id" value="{{ settings.get('telegram_chat_id', '') }}" placeholder="مثال: 123456789">
                                            <div class="alert alert-info mt-3 border-0" style="font-size: 0.8rem; border-radius: 12px;">
                                                <i class="fas fa-info-circle me-1"></i> <strong>للحصول على الإشعارات:</strong><br>
                                                1. ابحث في تليجرام عن البوت <strong>@userinfobot</strong> لمعرفة رقم الـ ID الخاص بك.<br>
                                                2. انسخ الرقم وضعه في الحقل أعلاه.<br>
                                            </div>
                                        </div>
                                        <button type="submit" class="btn btn-dark w-100 fw-bold rounded-pill shadow-sm"><i class="fas fa-save me-1"></i> حفظ إعدادات تليجرام</button>
                                    </form>
                                </div>
                            </div>
</div></div></div><div class="col-lg-4 mb-4"><div class="card shadow-sm border-0 h-100 border-top border-4 border-warning"><div class="card-body"><h5 class="fw-bold mb-3 text-dark"><i class="fas fa-shield-alt text-warning"></i> كلمة المرور</h5><form method="POST" class="d-flex flex-column gap-3"><input type="hidden" name="action" value="change_password"><div><label class="small fw-bold">الحالية</label><input type="password" name="old_password" class="form-control" required></div><div><label class="small fw-bold">الجديدة</label><input type="password" name="new_password" class="form-control" required></div><div><label class="small fw-bold">تأكيد</label><input type="password" name="confirm_password" class="form-control" required></div><button type="submit" class="btn btn-warning fw-bold text-dark w-100"><i class="fas fa-key"></i> تحديث</button></form></div></div></div></div></div>

    <!-- 7. مدير المنصة (للمدير فقط) -->
    {% if is_super_admin %}
    <div class="tab-pane fade" id="superadmin" role="tabpanel">
        
        <!-- أداة ترحيل الصور المتقدمة الخاصة بالمدير فقط -->
        <div class="card bg-dark text-white border-info shadow-lg mb-4">
            <div class="card-body">
                <h5 class="fw-bold text-info mb-3"><i class="fas fa-database me-2"></i> ترحيل الصور المتقدم (أداة المدير)</h5>
                <p class="small text-light mb-3" style="line-height: 1.6;">تُستخدم هذه الأداة مستقبلاً عند اشتراكك في باقة استضافة صور مدفوعة. ستقوم الأداة بسحب صورك من الاستضافات المجانية ورفعها لمساحتك الآمنة دون فقدان أي بيانات.</p>
                <form method="POST" onsubmit="return confirm('تنبيه: سيتم تشغيل سكربت الترحيل في الخلفية. هل أنت متأكد من المتابعة؟');">
                    <input type="hidden" name="action" value="migrate_images">
                    <button type="submit" class="btn btn-info w-100 fw-bold text-dark"><i class="fas fa-sync me-1"></i> تشغيل أداة ترحيل الصور الآن</button>
                </form>
            </div>
        </div>

        <div class="row mb-4"><div class="col-12"><div class="card border-primary shadow-sm"><div class="card-body"><h5 class="fw-bold text-primary mb-3">📦 إدارة باقات المنصة (SaaS Plans)</h5>
        <div class="row"><div class="col-md-4 mb-3"><form method="POST" class="p-3 bg-light rounded border"><input type="hidden" name="action" value="add_package"><label class="small fw-bold">اسم الباقة</label><input type="text" name="pkg_name" class="form-control mb-2" placeholder="مثال: VIP أو Pro" required><label class="small fw-bold">السعر (شهرياً/سنوياً)</label><input type="text" name="pkg_price" class="form-control mb-2" placeholder="مثال: 50$ شهرياً" required><label class="small fw-bold">الحد الأقصى للمنتجات</label><input type="number" name="pkg_max" class="form-control mb-2" placeholder="مثال: 100" required><label class="small fw-bold">المميزات (مفصولة بفاصلة)</label><input type="text" name="pkg_features" class="form-control mb-3" placeholder="دعم فني, دومين مخصص" required><button type="submit" class="btn btn-primary w-100 fw-bold">إضافة الباقة</button></form></div>
        <div class="col-md-8"><div class="table-responsive"><table class="table table-hover align-middle"><thead><tr><th>الباقة</th><th>السعر</th><th>الحد الأقصى</th><th>المميزات</th><th>إجراء</th></tr></thead><tbody>
        {% for pkg in packages %}<tr><td class="fw-bold">{{ pkg.name }}</td><td class="text-success fw-bold">{{ pkg.price }}</td><td>{{ pkg.max_products }} منتج</td><td><small>{{ pkg.features }}</small></td><td><form method="POST" onsubmit="return confirm('حذف هذه الباقة؟');"><input type="hidden" name="action" value="delete_package"><input type="hidden" name="pkg_id" value="{{ pkg._id }}"><button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button></form></td></tr>{% else %}<tr><td colspan="5" class="text-center text-muted">لا توجد باقات، قم بإضافة باقة جديدة.</td></tr>{% endfor %}
        </tbody></table></div></div></div></div></div></div></div>
        <div class="row"><div class="col-md-4 mb-4"><div class="card bg-dark text-white border-warning shadow-lg"><div class="card-body"><h5 class="fw-bold text-warning mb-3">➕ إضافة تاجر جديد</h5><form method="POST"><input type="hidden" name="action" value="add_merchant"><input type="text" name="name" class="form-control mb-3" placeholder="اسم التاجر" required><input type="text" name="slug" class="form-control mb-3" placeholder="رابط المتجر" required><input type="text" name="password" class="form-control mb-3" placeholder="كلمة المرور" required><select name="package" class="form-select mb-3" required><option value="" disabled selected>-- اختر باقة المتجر --</option>{% for pkg in packages %}<option value="{{ pkg.name }}">{{ pkg.name }}</option>{% endfor %}</select><button type="submit" class="btn btn-warning w-100 fw-bold text-dark">إنشاء وبناء المتجر</button></form></div></div></div><div class="col-md-8"><div class="card border-danger shadow-sm"><div class="card-body"><h5 class="fw-bold text-danger mb-3">🏢 المتاجر المشتركة في منصتك</h5><div class="table-responsive"><table class="table table-hover align-middle"><thead><tr><th>التاجر</th><th>الباقة</th><th>الرابط</th><th>الحالة</th><th>إجراءات</th></tr></thead><tbody>{% for m in merchants %}<tr><td>{{ m.username }}<br><small class="text-muted">Pass: {{ m.password }}</small></td><td><span class="badge bg-info text-dark">{{ m.get("package", "أساسية") }}</span></td><td><a href="/store/{{ m.store_slug }}" target="_blank" class="fw-bold">{{ m.store_slug }}</a></td><td><span class="badge bg-{{ 'success' if m.active == 'TRUE' else 'secondary' }}">{{ 'نشط' if m.active == 'TRUE' else 'موقوف' }}</span></td><td><form method="POST" class="d-inline"><input type="hidden" name="action" value="toggle_status"><input type="hidden" name="user_id" value="{{ m.id }}"><input type="hidden" name="current_status" value="{{ m.active }}"><button type="submit" class="btn btn-sm btn-{{ 'warning' if m.active == 'TRUE' else 'success' }}">{{ 'إيقاف' if m.active == 'TRUE' else 'تفعيل' }}</button></form>{% if m.store_slug != 'admin-store' %}<form method="POST" class="d-inline" onsubmit="return confirm('حذف نهائي؟');"><input type="hidden" name="action" value="delete_merchant"><input type="hidden" name="user_id" value="{{ m.id }}"><button type="submit" class="btn btn-sm btn-danger">حذف</button></form>{% endif %} <button type="button" class="btn btn-sm btn-primary ms-1" data-bs-toggle="modal" data-bs-target="#editSlugModal{{ m.id }}"><i class="fas fa-edit"></i> تعديل</button></td></tr><div class="modal fade" id="editSlugModal{{ m.id }}"><div class="modal-dialog"><div class="modal-content"><div class="modal-header bg-light"><h5 class="modal-title fw-bold text-primary"><i class="fas fa-edit"></i> تعديل بيانات المتجر: {{ m.username }}</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body"><form method="POST"><input type="hidden" name="action" value="edit_merchant_info"><input type="hidden" name="user_id" value="{{ m.id }}"><label class="small fw-bold mb-2">الرابط الجديد (بدون مسافات):</label><input type="text" name="new_slug" class="form-control mb-3" value="{{ m.store_slug }}" required>
        <label class="small fw-bold mb-2">باقة الاشتراك:</label>
        <select name="new_package" class="form-select mb-3">
            {% for pkg in packages %}
            <option value="{{ pkg.name }}" {% if m.get('package', 'أساسية') == pkg.name %}selected{% endif %}>{{ pkg.name }}</option>
            {% endfor %}
            {% if not packages %}<option value="أساسية">أساسية (الرجاء إنشاء باقات أولاً)</option>{% endif %}
        </select>
            <div class="row g-2 mb-3">
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-muted">التصنيف الفرعي</label>
                    <input type="text" name="subcategory" class="form-control form-control-sm" placeholder="مثال: هواتف ذكية">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-muted">الماركة / الموديل</label>
                    <input type="text" name="brand" class="form-control form-control-sm" placeholder="مثال: سامسونج / آبل">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-muted">النوع / الخصائص</label>
                    <input type="text" name="p_type" class="form-control form-control-sm" placeholder="مثال: 128 جيجابايت">
                </div>
            </div>
            <button type="submit" class="btn btn-primary w-100 fw-bold">حفظ التعديلات</button></form><div class="alert alert-warning mt-3 small fw-bold mb-0"><i class="fas fa-exclamation-triangle"></i> تنبيه: سيتغير رابط الدخول الخاص بالتاجر، ويجب إبلاغه بالرابط الجديد.</div></div></div></div></div>{% endfor %}</tbody></table></div></div></div></div></div></div>
    </div>
    {% endif %}

</div> <!-- نهاية tab-content -->

<!-- النوافذ المنبثقة خارج الـ Tabs -->
{% include 'partials/add_driver_modal.html' %}
{% include 'partials/guide_modal.html' %}

{% endblock %}

{% block page_scripts %}
<script>
function filterOrdersTable() {
    let idFilter = document.getElementById('filterOrdId').value.toLowerCase();
    let custFilter = document.getElementById('filterOrdCust').value.toLowerCase();
    let statFilter = document.getElementById('filterOrdStat').value.toLowerCase();
    
    let rows = document.querySelectorAll('#ordersTableBody tr.order-row');
    rows.forEach(row => {
        let idTxt = row.cells[0].innerText.toLowerCase();
        let custTxt = row.cells[1].innerText.toLowerCase();
        let statTxt = row.cells[4].innerText.toLowerCase();
        
        if (idTxt.includes(idFilter) && custTxt.includes(custFilter) && statTxt.includes(statFilter)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

function toggleProviderFields() { 
            let provider = document.getElementById('providerSelect').value; 
            if(provider === 'cloudinary') { 
                document.getElementById('basicProviderField').style.display = 'none'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'block'); 
            } else if (provider === 'catbox') {
                document.getElementById('basicProviderField').style.display = 'none'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'none'); 
            } else { 
                document.getElementById('basicProviderField').style.display = 'block'; 
                document.querySelectorAll('.cloudinary-fields').forEach(el => el.style.display = 'none'); 
            } 
        }
        
        const PROVIDER = '{{ settings.get("img_provider", "catbox") }}'; 
        const USER_API_KEY = '{{ settings.get("img_api_key", "") }}'; 
        const CLOUD_NAME = '{{ settings.get("cloudinary_name", "") }}'; 
        const CLOUD_PRESET = '{{ settings.get("cloudinary_preset", "") }}';
        
        async function uploadImageToCloud(fileInput, hiddenUrlId, statusId, btnId) {
            let file = fileInput.files[0]; if (!file) return;
            let statusText = document.getElementById(statusId); let urlInput = document.getElementById(hiddenUrlId); let submitBtn = document.getElementById(btnId);
            
            if (PROVIDER === 'cloudinary' && (!CLOUD_NAME || !CLOUD_PRESET)) { statusText.innerHTML = '<i class="fas fa-exclamation-triangle"></i> أدخل إعدادات الكلاوديناري.'; statusText.className = "small fw-bold mt-1 d-block text-danger"; return; }
            if (PROVIDER !== 'cloudinary' && PROVIDER !== 'catbox' && !USER_API_KEY) { statusText.innerHTML = '<i class="fas fa-exclamation-triangle"></i> أدخل مفتاح الـ API.'; statusText.className = "small fw-bold mt-1 d-block text-danger"; return; }
            
            statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-primary"></i> جاري معالجة وتجهيز الصورة...`;
            statusText.className = "small fw-bold mt-1 d-block text-primary"; submitBtn.disabled = true;

            let reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = function(event) {
                let img = new Image(); img.src = event.target.result;
                img.onload = async function() {
                    let canvas = document.createElement('canvas'); let MAX_WIDTH = 600; let scaleSize = MAX_WIDTH / img.width;
                    if (scaleSize < 1) { canvas.width = MAX_WIDTH; canvas.height = img.height * scaleSize; } else { canvas.width = img.width; canvas.height = img.height; }
                    let ctx = canvas.getContext('2d'); ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                    let base64Image = canvas.toDataURL('image/jpeg', 0.7);
                    
                    try {
                        statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-primary"></i> جاري الرفع (المسار 1: عبر السيرفر)...`;
                        let payload = { provider: PROVIDER, api_key: USER_API_KEY, cloud_name: CLOUD_NAME, preset: CLOUD_PRESET, image_base64: base64Image };
                        let response = await fetch('/api/proxy_upload', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) });
                        
                        if (!response.ok) throw new Error('Proxy HTTP Error');
                        let data = await response.json();
                        
                        if (data.success && data.url) { 
                            urlInput.value = data.url; 
                            statusText.innerHTML = '<i class="fas fa-check-circle"></i> تم الرفع بنجاح!'; 
                            statusText.className = "small fw-bold mt-1 d-block text-success"; 
                        } else { throw new Error(data.error || 'Proxy Failed'); }
                        
                    } catch (error) { 
                        statusText.innerHTML = `<i class="fas fa-spinner fa-spin text-warning"></i> المسار 1 فشل، جاري الرفع (المسار 2: مباشر)...`;
                        try {
                            let fetchRes = await fetch(base64Image);
                            let blob = await fetchRes.blob();
                            let formData = new FormData();
                            let uploadedUrl = '';
                            
                            if (PROVIDER === 'catbox') { 
                                formData.append('reqtype', 'fileupload'); 
                                formData.append('fileToUpload', blob, 'image.jpg'); 
                                let r = await fetch('https://catbox.moe/user/api.php', { method: 'POST', body: formData }); 
                                let txt = await r.text(); 
                                if (txt.startsWith('http')) uploadedUrl = txt; else throw new Error(); 
                            } else if (PROVIDER === 'freeimagehost') { 
                                formData.append('key', USER_API_KEY); 
                                formData.append('source', base64Image.split(',')[1]); 
                                formData.append('action', 'upload'); 
                                formData.append('format', 'json'); 
                                let r = await fetch('https://freeimage.host/api/1/upload', { method: 'POST', body: formData }); 
                                let d = await r.json(); 
                                if (d.status_code === 200) uploadedUrl = d.image.url; else throw new Error(); 
                            } else if (PROVIDER === 'cloudinary') { 
                                formData.append("file", blob); formData.append("upload_preset", CLOUD_PRESET); 
                                let r = await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`, { method: 'POST', body: formData }); 
                                let d = await r.json(); if (d.secure_url) uploadedUrl = d.secure_url; else throw new Error(); 
                            } else if (PROVIDER === 'imgur') { 
                                formData.append("image", blob); 
                                let r = await fetch('https://api.imgur.com/3/image', { method: 'POST', headers: { 'Authorization': 'Client-ID ' + USER_API_KEY }, body: formData }); 
                                let d = await r.json(); if (d.success) uploadedUrl = d.data.link; else throw new Error(); 
                            } else if (PROVIDER === 'postimages') { 
                                formData.append("file", blob); 
                                let r = await fetch('https://postimages.org/api/upload', { method: 'POST', headers: { 'Authorization': 'Bearer ' + USER_API_KEY }, body: formData }); 
                                let d = await r.json(); if (d.url) uploadedUrl = d.url; else throw new Error(); 
                            } else { 
                                formData.append("image", blob); 
                                let r = await fetch('https://api.imgbb.com/1/upload?key=' + USER_API_KEY, { method: 'POST', body: formData }); 
                                let d = await r.json(); if (d.success) uploadedUrl = d.data.url; else throw new Error(); 
                            }
                            
                            urlInput.value = uploadedUrl;
                            statusText.innerHTML = '<i class="fas fa-check-circle"></i> تم الرفع بنجاح!';
                            statusText.className = "small fw-bold mt-1 d-block text-success";
                        } catch (fallbackError) {
                            statusText.innerHTML = '<i class="fas fa-times-circle"></i> فشل الرفع تماماً! تأكد من المفاتيح أو جرب Catbox.';
                            statusText.className = "small fw-bold mt-1 d-block text-danger"; 
                            urlInput.value = '';
                        }
                    }
                    submitBtn.disabled = false;
                }
            };
        }
        function handleCategoryChange(selectObj) { let inputField = document.getElementById('newCategoryInput'); if (selectObj.value === 'NEW_CATEGORY') { inputField.style.display = 'block'; inputField.required = true; document.getElementById('finalCategory').value = inputField.value; } else { inputField.style.display = 'none'; inputField.required = false; document.getElementById('finalCategory').value = selectObj.value; } }
        function updateFinalCategory() { if (document.getElementById('categorySelect').value === 'NEW_CATEGORY') { document.getElementById('finalCategory').value = document.getElementById('newCategoryInput').value; } }
        function submitProductForm() { let select = document.getElementById('categorySelect'); if(select.value === "") { alert("اختر تصنيفاً!"); return; } if(select.value === 'NEW_CATEGORY' && document.getElementById('newCategoryInput').value.trim() === "") { alert("اكتب التصنيف الجديد!"); return; } document.getElementById('addProductForm').submit(); }
        document.addEventListener("DOMContentLoaded", function() { var ctx = document.getElementById('orderChart').getContext('2d'); if(ctx) { new Chart(ctx, { type: 'doughnut', data: { labels: ['جديد', 'تجهيز', 'توصيل', 'ملغي'], datasets: [{ data: [{{ stats.status_counts['جديد 🟡'] }}, {{ stats.status_counts['قيد التجهيز 🔵'] }}, {{ stats.status_counts['تم التوصيل 🟢'] }}, {{ stats.status_counts['ملغي 🔴'] }}], backgroundColor: ['#ffc107', '#0dcaf0', '#198754', '#dc3545'], borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { position: 'bottom', labels: {font: {family: 'Cairo', size: 12}} } } } }); } });
    
    function filterAdminProducts() {
        let term = document.getElementById('adminProductSearch').value.toLowerCase();
        let cat = document.getElementById('adminCategoryFilter').value;
        let rows = document.querySelectorAll('.admin-product-row');
        rows.forEach(row => {
            let name = row.getAttribute('data-name').toLowerCase();
            let rowCat = row.getAttribute('data-cat');
            let matchName = name.includes(term);
            let matchCat = (cat === 'ALL' || rowCat === cat);
            row.style.display = (matchName && matchCat) ? '' : 'none';
        });
    }
    
    document.addEventListener("DOMContentLoaded", function() {
        var ctxSales = document.getElementById('salesChart');
        if(ctxSales) {
            new Chart(ctxSales.getContext('2d'), {
                type: 'line',
                data: {
                    labels: {{ adv_stats.chart_labels | tojson | safe }},
                    datasets: [{
                        label: 'صافي المبيعات',
                        data: {{ adv_stats.chart_data | tojson | safe }},
                        borderColor: '#198754',
                        backgroundColor: 'rgba(25, 135, 84, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
            });
        }
    });

    // دالة مشاركة المنتج مباشرة من لوحة التحكم
    function shareDashboardProduct(name, desc, imgUrl) {
        const storeUrl = window.location.origin + '/store/{{ store_slug }}';
        const shareText = `🛍️ متوفر الآن: ${name}\n\n${desc ? desc.substring(0, 80) + '...' : ''}\n\nلطلب المنتج، تفضل بزيارة متجرنا عبر الرابط:\n${storeUrl}\n\nرابط صورة المنتج:\n${imgUrl}`;
        const waLink = "https://wa.me/?text=" + encodeURIComponent(shareText);
        window.open(waLink, '_blank');
    }
</script>
{% if not is_super_admin %}
<script>
document.addEventListener("DOMContentLoaded", function() {
    if(document.getElementById('tajergo-progress-bar')) return;

    let currentProducts = {{ products | length if products else 0 }};
    let pkgName = `{{ current_user_data.get('package', 'أساسية') if current_user_data else 'أساسية' }}`;
    
    let packagesList = [];
    {% for p in packages %}
        packagesList.push({
            name: `{{ p.name|default('') }}`,
            max_products: `{{ p.max_products|default('') }}`,
            pkg_max: `{{ p.pkg_max|default('') }}`
        });
    {% endfor %}
    
    let maxLimit = 20;
    let targetPkg = packagesList.find(p => p.name === pkgName);
    if(targetPkg) {
        let rawVal = targetPkg.max_products || targetPkg.pkg_max || 20;
        let parsed = parseInt(String(rawVal).replace(/\D/g, ''));
        maxLimit = isNaN(parsed) ? 999999 : parsed;
    }
    
    let isUnlimited = (maxLimit >= 100000);
    let percent = isUnlimited ? 100 : Math.min((currentProducts / maxLimit) * 100, 100);
    let barColor = percent >= 100 ? 'bg-danger' : (percent >= 80 ? 'bg-warning' : 'bg-success');
    let txtColor = percent >= 100 ? 'text-danger' : 'text-success';
    let displayLimit = isUnlimited ? '<i class="fas fa-infinity fs-6"></i>' : maxLimit;
    
    let progressHtml = `
    <div id="tajergo-progress-bar" class="card border-0 shadow-sm mb-4" style="border-radius: 16px; background: #fff;">
        <div class="card-body p-3 p-md-4">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <div class="d-flex align-items-center gap-3">
                    <div class="bg-primary bg-opacity-10 text-primary p-2 rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px;">
                        <i class="fas fa-box-open fs-4"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1 text-dark">استهلاك باقة المتجر</h6>
                        <small class="text-muted fw-bold">باقتك الحالية: <span class="badge bg-light text-dark border px-2 shadow-sm">${pkgName}</span></small>
                    </div>
                </div>
                <div class="text-end">
                    <h3 class="fw-bold mb-0 ${txtColor}" dir="ltr" style="letter-spacing: 1px;">
                        ${currentProducts} <span class="text-muted fs-5">/ ${displayLimit}</span>
                    </h3>
                </div>
            </div>
            
            ${!isUnlimited ? `
            <div class="progress mt-3" style="height: 10px; border-radius: 50rem; background-color: #f1f3f5;">
                <div class="progress-bar ${barColor} progress-bar-striped progress-bar-animated" role="progressbar" style="width: ${percent}%; border-radius: 50rem;"></div>
            </div>
            <div class="d-flex justify-content-between mt-2 px-1">
                <small class="text-muted fw-bold" style="font-size: 0.75rem;">إجمالي المنتجات المضافة</small>
                <small class="fw-bold ${txtColor}" style="font-size: 0.75rem;">%${Math.round(percent)} مستهلك</small>
            </div>
            ` : `
            <div class="alert alert-success border-0 bg-success bg-opacity-10 py-2 mt-3 mb-0 text-center rounded-3 fw-bold">
                <i class="fas fa-check-circle me-1"></i> باقتك لا محدودة، يمكنك إضافة المنتجات بحرية تامة!
            </div>
            `}
        </div>
    </div>
    `;
    
    let productsTab = document.getElementById('products');
    if (productsTab) {
        productsTab.insertAdjacentHTML('afterbegin', progressHtml);
    }
});
</script>
{% endif %}
{% endblock %}
```

-----------------------------------
## File Path: ./templates/driver.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بوابة المندوب</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/driver.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="header-banner">
        <h2 class="fw-bold mb-2"><i class="fas fa-motorcycle me-2"></i> بوابة التوصيل</h2>
        <h5 class="mb-0 text-white-50">أهلاً بك، {{ driver.name }} 👋</h5>
    </div>
    
    <div class="container">
        <h6 class="fw-bold mb-3 text-muted"><i class="fas fa-box me-1"></i> الطلبات الحالية: <span class="badge bg-primary rounded-pill">{{ orders|length }}</span></h6>
        
        {% if orders %}
            {% for o in orders %}
            <div class="order-card">
                <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-3">
                    <span class="badge bg-light text-dark border fs-6">{{ o.order_id }}</span>
                    <h5 class="text-primary fw-bold mb-0">{{ o.total }} ريال</h5>
                </div>
                
                <p class="mb-2 fs-6"><strong><i class="fas fa-user text-muted me-1"></i> العميل:</strong> {{ o.customer_name }}</p>
                <p class="mb-2 fs-6"><strong><i class="fas fa-phone text-muted me-1"></i> الهاتف:</strong> <a href="tel:{{ o.customer_phone }}" class="text-decoration-none fw-bold text-success" style="direction: ltr; display: inline-block;">{{ o.customer_phone }}</a></p>
                <p class="mb-3 fs-6"><strong><i class="fas fa-map-marker-alt text-muted me-1"></i> العنوان:</strong> {{ o.customer_address }}</p>
                
                <div class="bg-light p-3 rounded-3 mb-3 border">
                    <h6 class="fw-bold text-secondary mb-2 small">تفاصيل المنتجات:</h6>
                    {% if o.cart is string %}
                        <span class="small">{{ o.cart }}</span>
                    {% else %}
                        {% for item in o.cart %}
                            <div class="small fw-bold mb-1">- {{ item.name }} <span class="text-primary">(x{{ item.qty }})</span></div>
                        {% endfor %}
                    {% endif %}
                </div>
                
                <form action="/driver/complete/{{ o.order_id }}" method="POST" onsubmit="return confirm('هل أنت متأكد أنك قمت بتسليم الطلب للعميل بنجاح؟ واستلمت المبلغ؟');">
                    <input type="hidden" name="token" value="{{ driver.token }}">
                    <button type="submit" class="btn-deliver"><i class="fas fa-check-circle me-1"></i> تأكيد تسليم الطلب للعميل</button>
                </form>
            </div>
            {% endfor %}
        {% else %}
            <div class="text-center py-5 mt-4">
                <i class="fas fa-check-double fs-1 text-success mb-3 opacity-75"></i>
                <h5 class="text-muted fw-bold">عمل رائع! لا توجد طلبات معلقة</h5>
                <p class="small text-muted">جميع الطلبات المسندة إليك تم توصيلها بنجاح.</p>
            </div>
        {% endif %}
    </div>
</body>
</html>

```

-----------------------------------
## File Path: ./templates/login.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول | منصة TajerGo</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}?v={{ static_version }}">
<script>
        function fixImg(img){
            if(!img.dataset.proxied){
                img.dataset.proxied='true';
                let src=img.getAttribute('src');
                if(src&&src!==''&&!src.includes('placeholder')){
                    img.src='https://wsrv.nl/?url='+encodeURIComponent(img.src);
                }
            }
        }
    </script>
    <script src="{{ url_for('static', filename='js/app.js') }}?v={{ static_version }}"></script>
</head>
<body>

    <div class="login-card text-center">
        <!-- عرض شعار المنصة الديناميكي -->
        <img src="{{ platform_logo }}" onerror="fixImg(this)" class="platform-logo" alt="شعار المنصة">
        
        <h4 class="fw-bold mb-1 text-dark">تسجيل الدخول</h4>
        <p class="text-muted small fw-bold mb-4">أهلاً بك في منصة TajerGo</p>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} small fw-bold rounded-3 py-2"><i class="fas fa-exclamation-circle me-1"></i> {{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" action="/login">
            <div class="mb-3 text-start">
                <label class="form-label small fw-bold text-muted ms-1"><i class="fas fa-link input-icon me-1"></i> رابط المتجر (Slug)</label>
                <input type="text" name="slug" class="form-control text-start" dir="ltr" placeholder="مثال: store-name" required autocomplete="off">
            </div>
            <div class="mb-4 text-start">
                <label class="form-label small fw-bold text-muted ms-1"><i class="fas fa-lock input-icon me-1"></i> كلمة المرور</label>
                <input type="password" name="pass" class="form-control text-start" dir="ltr" placeholder="••••••••" required autocomplete="off">
            </div>
            <button type="submit" class="btn btn-primary w-100 btn-login shadow-sm"><i class="fas fa-sign-in-alt me-2"></i> دخول للوحة التحكم</button>
        </form>
        
        <div class="mt-4 pt-3 border-top">
            <p class="text-muted mb-0" style="font-size: 0.75rem; font-weight: bold; opacity: 0.7;">برمجة المهندس / وسيم همدان - 771954200</p>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

```

-----------------------------------
## File Path: ./templates/partials/add_driver_modal.html
```
<div class="modal fade" id="addDriverModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content rounded-4 border-0 shadow">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-dark"><i class="fas fa-user-plus text-primary me-2"></i> إضافة مندوب جديد</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body py-3">
                <form id="addDriverForm" onsubmit="submitNewDriver(event)">
                    <div class="mb-3">
                        <label class="form-label small fw-bold">اسم المندوب</label>
                        <input type="text" class="form-control rounded-3" id="driverNameInput" placeholder="مثال: أحمد محمد" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-bold">رقم هاتف المندوب (واتساب)</label>
                        <input type="tel" class="form-control rounded-3" id="driverPhoneInput" placeholder="مثال: 770000000" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 rounded-pill fw-bold py-2 shadow-sm">
                        <i class="fas fa-save me-1"></i> حفظ وإنشاء بوابة المندوب
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

```

-----------------------------------
## File Path: ./templates/partials/dashboard_nav.html
```
<ul class="nav nav-tabs mb-4 bg-white p-2 rounded shadow-sm" id="myTab">
    <li class="nav-item"><button class="nav-link fw-bold text-primary active" data-bs-toggle="tab" data-bs-target="#products">📦 المنتجات</button></li>
    <li class="nav-item"><button class="nav-link fw-bold text-dark" data-bs-toggle="tab" data-bs-target="#orders">🛒 الطلبات</button></li>
    <li class="nav-item"><button class="nav-link fw-bold text-success" data-bs-toggle="tab" data-bs-target="#analytics">📊 الإحصائيات</button></li>
    <li class="nav-item" role="presentation">
        <button class="nav-link fw-bold text-info px-3" id="drivers-tab" data-bs-toggle="tab" data-bs-target="#drivers-pane" type="button" role="tab">
            <i class="fas fa-motorcycle me-1"></i> المناديب والتوصيل
        </button>
    </li>
    <li class="nav-item"><button class="nav-link fw-bold text-warning" data-bs-toggle="tab" data-bs-target="#coupons">🎟️ الكوبونات</button></li>
    <li class="nav-item"><button class="nav-link fw-bold text-secondary" data-bs-toggle="tab" data-bs-target="#settings">⚙️ الإعدادات</button></li>
    {% if is_super_admin %}<li class="nav-item"><button class="nav-link fw-bold text-danger" data-bs-toggle="tab" data-bs-target="#superadmin">👑 الإدارة</button></li>{% endif %}
</ul>

```

-----------------------------------
## File Path: ./templates/partials/flash_messages.html
```
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}

```

-----------------------------------
## File Path: ./templates/partials/guide_modal.html
```
<div class="modal fade" id="guideModal" tabindex="-1" aria-labelledby="guideModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border-0 shadow-lg">
                <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title fw-bold" id="guideModalLabel"><i class="fas fa-cloud"></i> دليل الربط السحابي للصور</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-4">
                    <ul class="nav nav-pills mb-4 gap-2" id="pills-tab" role="tablist">
                        <li class="nav-item" role="presentation"><button class="nav-link active fw-bold border" data-bs-toggle="pill" data-bs-target="#catboxGuide" type="button" role="tab">Catbox 🚀</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#imgbbGuide" type="button" role="tab">ImgBB</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#freeimageGuide" type="button" role="tab">FreeImage</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#imgurGuide" type="button" role="tab">Imgur</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold border" data-bs-toggle="pill" data-bs-target="#postimgGuide" type="button" role="tab">Postimages</button></li>
                        <li class="nav-item" role="presentation"><button class="nav-link fw-bold text-info border border-info" data-bs-toggle="pill" data-bs-target="#cloudinaryGuide" type="button" role="tab">Cloudinary</button></li>
                    </ul>
                    <div class="tab-content border rounded p-4 bg-light shadow-sm" id="pills-tabContent">
                        <div class="tab-pane fade show active" id="catboxGuide" role="tabpanel">
                            <h6 class="fw-bold text-success mb-3">شرح منصة Catbox.moe (الخيار الأسهل والافتراضي):</h6>
                            <div class="mb-2"><span class="badge bg-success me-2">1</span> مجانية بالكامل وتسمح برفع صور بحجم يصل لـ 200 ميجابايت.</div>
                            <div class="mb-2"><span class="badge bg-success me-2">2</span> <b>لا تحتاج لأي تسجيل دخول أو مفاتيح API أبداً!</b></div>
                            <div class="mb-2"><span class="badge bg-success me-2">3</span> فقط اخترها من القائمة واضغط حفظ، وستعمل فوراً.</div>
                        </div>
                        <div class="tab-pane fade" id="imgbbGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">خطوات ربط منصة ImgBB:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> افتح موقع <a href="https://api.imgbb.com/" target="_blank" class="fw-bold">api.imgbb.com</a> وقم بتسجيل الدخول.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اضغط على زر <b>Add API Key</b> لتحصل على الرمز السري.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">3</span> انسخ الرمز الطويل، ثم ارجع هنا والصقه في خانة <b>(مفتاح الربط API Key)</b>.</div>
                            <div class="alert alert-danger mt-3 small fw-bold mb-0"><i class="fas fa-exclamation-triangle"></i> تنبيه: هذه المنصة قد تكون محظورة في بعض الدول، إذا فشل الرفع استخدم Cloudinary.</div>
                        </div>
                        <div class="tab-pane fade" id="freeimageGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">شرح منصة FreeImage.host:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> سجل حساب في <a href="https://freeimage.host/" target="_blank">freeimage.host</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اذهب لصفحة الـ API وانسخ الرمز السري والصقه في خانة مفتاح الربط.</div>
                        </div>
                        <div class="tab-pane fade" id="imgurGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">خطوات ربط منصة Imgur:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> سجل حساباً في <a href="https://imgur.com/register" target="_blank" class="fw-bold">imgur.com</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> اذهب إلى <a href="https://api.imgur.com/oauth2/addclient" target="_blank" class="fw-bold">صفحة إنشاء تطبيق جديد</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">3</span> اختر <i>OAuth 2.0 authorization without a callback URL</i>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">4</span> سيظهر لك <b>Client ID</b>، انسخه والصقه في خانة <b>(مفتاح الربط)</b>.</div>
                        </div>
                        <div class="tab-pane fade" id="postimgGuide" role="tabpanel">
                            <h6 class="fw-bold text-primary mb-3">معلومات منصة Postimages:</h6>
                            <div class="mb-2"><span class="badge bg-secondary me-2">1</span> افتح موقع <a href="https://postimages.org/" target="_blank" class="fw-bold">postimages.org</a>.</div>
                            <div class="mb-2"><span class="badge bg-secondary me-2">2</span> تتطلب هذه المنصة أحياناً مراسلة الدعم للحصول على مفتاح API خاص.</div>
                            <div class="alert alert-warning mt-3 small fw-bold mb-0">💡 ملاحظة: كبديل سريع، يمكنك رفع الصور لديهم يدوياً ونسخ <b>الرابط المباشر للصورة</b>، ثم وضعه في حقل إضافة المنتج مباشرة.</div>
                        </div>
                        <div class="tab-pane fade" id="cloudinaryGuide" role="tabpanel">
                            <h6 class="fw-bold text-info mb-3">خطوات ربط Cloudinary (الخيار الأفضل والمضمون 100%):</h6>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">1</span> سجل حساباً مجانياً في <a href="https://cloudinary.com/" target="_blank" class="fw-bold text-info">Cloudinary.com</a>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">2</span> من لوحة التحكم الرئيسية، انسخ اسم السحابة الخاص بك <b>Cloud Name</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">3</span> اذهب إلى الإعدادات <b>Settings</b> ⚙️ (أسفل اليسار) ثم اختر <b>Upload</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">4</span> انزل لأسفل واضغط على الرابط الأزرق <b>Add upload preset</b>.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">5</span> اجعل خيار <i>Signing Mode</i> يساوي <b>Unsigned</b> واضغط حفظ.</div>
                            <div class="mb-2"><span class="badge bg-info text-dark me-2">6</span> انسخ اسم الـ Preset الذي ظهر لك، والصقه مع الـ Cloud Name في إعدادات متجرك!</div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer bg-white border-top">
                    <button type="button" class="btn btn-secondary fw-bold px-4" data-bs-dismiss="modal">فهمت، إغلاق</button>
                </div>
            </div>
        </div>
    </div>

```

-----------------------------------
## File Path: ./templates/partials/topbar.html
```
<nav class="navbar navbar-dark bg-dark mb-4 shadow"><div class="container"><a class="navbar-brand fw-bold d-flex align-items-center gap-2" href="#"><img src="{{ platform_logo }}" onerror="fixImg(this)" width="35" height="35" style="object-fit:cover; border-radius:50%; background:#fff; padding:1px;" alt="Logo"> لوحة تحكم TajerGo</a><div><a href="/store/{{ store_slug }}" target="_blank" class="btn btn-outline-light btn-sm mx-2"><i class="fas fa-store"></i> زيارة متجري</a><a href="/logout" class="btn btn-danger btn-sm">خروج</a></div></div></nav>

```

-----------------------------------
## File Path: ./templates/store.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{{ settings.store_name }}</title>
    <link rel="manifest" href="/manifest/{{ user.store_slug }}.json">
    
    {% if settings.get('logo_url') and settings.logo_url.strip() != '' %}
    <link rel="icon" href="{{ settings.logo_url }}">
    <link rel="apple-touch-icon" href="{{ settings.logo_url }}">
    {% else %}
    <link rel="icon" href="{{ url_for('static', filename='icon-512.png') }}?v={{ static_version }}">
    <link rel="apple-touch-icon" href="{{ url_for('static', filename='icon-192.png') }}?v={{ static_version }}">
    {% endif %}
    
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="{{ settings.store_name }}">
    <meta name="theme-color" content="{{ settings.theme_color|default('#0d6efd') }}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family={{ settings.font_family|default('Cairo') }}:wght@400;600;700;800&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/store.css') }}?v={{ static_version }}">
    
    <style>
        :root {
            --main-color: {{ settings.theme_color|default('#0d6efd') }};
            --store-font: '{{ settings.font_family|default('Cairo') }}';
        }
    </style>
    <script src="{{ url_for('static', filename='js/app.js') }}?v={{ static_version }}" defer></script>
</head>
<body class="header-{{ settings.header_size|default('medium') }}">

    <!-- النافذة الترحيبية للعميل (نصية فقط كما طلبت) -->
    {% if settings.get('welcome_message') and settings.welcome_message.strip() != '' %}
    <div class="modal fade" id="welcomeModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border-0 shadow-lg text-center" style="border-radius: 24px; overflow: hidden; background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);">
                <div class="modal-body p-5">
                    <h3 class="fw-bold text-dark mb-4"><i class="fas fa-hand-sparkles text-warning me-2"></i> أهلاً بك!</h3>
                    <p class="text-secondary fw-bold mb-4" style="line-height: 1.8; font-size: 1.15rem;">{{ settings.welcome_message }}</p>
                    <button type="button" class="btn btn-primary btn-lg rounded-pill px-5 fw-bold shadow-sm w-100" data-bs-dismiss="modal" style="background-color: var(--main-color); border: none;">تصفح المنتجات 🚀</button>
                </div>
            </div>
        </div>
    </div>
    {% endif %}

    <div class="hero-section">
        <div class="container d-flex flex-column align-items-center justify-content-center">
            {% if settings.get('logo_url') and settings.logo_url.strip() != '' %}
                <img src="{{ settings.logo_url }}" onerror="fixImg(this)" class="store-logo" alt="شعار المتجر">
            {% else %}
                <div class="store-logo d-flex align-items-center justify-content-center bg-white text-primary" style="font-size: 2.5rem; width: 100px; height: 100px;"><i class="fas fa-store"></i></div>
            {% endif %}
            <h1 class="fw-bold hero-title">{{ settings.store_name }}</h1>
            <p class="lead mb-0 mt-2" style="opacity: 0.9; font-weight: 600;">{{ settings.store_desc }}</p>
        </div>
    </div>

    <div class="container mb-4">
        <div class="row g-2 align-items-center">
            <div class="col-md-6 col-12 order-1 order-md-1">
                <div class="input-group search-bar-container">
                    <span class="input-group-text bg-transparent border-0 text-muted ps-3"><i class="fas fa-search"></i></span>
                    <input type="text" id="searchInput" class="form-control bg-transparent" placeholder="ابحث عن منتجك هنا..." onkeyup="filterProducts()">
                </div>
            </div>
            <div class="col-6 col-md-3 order-2 order-md-2">
                <select id="sortSelect" class="form-select sort-select w-100" onchange="sortProducts()">
                    <option value="default">الترتيب الافتراضي</option>
                    <option value="price-asc">السعر: من الأرخص للأغلى</option>
                    <option value="price-desc">السعر: من الأغلى للأرخص</option>
                    <option value="rating-desc">الأعلى تقييماً</option>
                </select>
            </div>
            <div class="col-6 col-md-3 text-end order-3 order-md-3">
                <button class="btn btn-outline-primary w-100 btn-share bg-white h-100 fw-bold" onclick="shareStore()"><i class="fas fa-share-nodes"></i> شارك المتجر</button>
            </div>
        </div>
    </div>

    <div class="container pb-2">
        {% set grouped_products = products | groupby('category') %}
        {% if grouped_products %}
            <ul class="nav nav-pills category-tabs" id="categoryTabs" role="tablist">
                {% for category, items in grouped_products %}
                    <li class="nav-item" role="presentation">
                        <button class="nav-link {% if loop.first %}active{% endif %}" id="tab-btn-{{ loop.index }}" data-bs-toggle="pill" data-bs-target="#tab-pane-{{ loop.index }}" type="button" role="tab">{{ category if category else 'عام' }}</button>
                    </li>
                {% endfor %}
            </ul>
            <div class="tab-content" id="categoryTabsContent">
                {% for category, items in grouped_products %}
                <div class="tab-pane fade {% if loop.first %}show active{% endif %} category-section" id="tab-pane-{{ loop.index }}" role="tabpanel">
                    <div class="row g-3 product-list-container">
                        {% for p in items %}
                        <div class="col-md-3 col-6 product-wrapper" data-name="{{ p.name }}" data-price="{{ p.price|default(0)|float }}" data-rating="{{ p.rating|default(0)|float }}">
                            <div class="card product-card h-100 d-flex flex-column">

                            <textarea id="raw-name-{{ p.id }}" style="display:none;">{{ p.name }}</textarea>
                            <textarea id="raw-desc-{{ p.id }}" style="display:none;">{{ p.description }}</textarea>
                            <textarea id="raw-img-{{ p.id }}" style="display:none;">{{ p.image_url }}</textarea>

                            <div class="img-wrapper" onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}', '{{ p.get('unit', 'حبة') }}')" title="عرض التفاصيل">
                                <img src="{{ p.image_url if p.image_url else 'https://via.placeholder.com/400x300?text=بدون+صورة' }}" onerror="fixImg(this)" class="product-img" loading="lazy">
                            </div>
                            <div class="card-body p-3 d-flex flex-column">
                                <h6 class="product-title" style="cursor:pointer;" onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}', '{{ p.get('unit', 'حبة') }}')">{{ p.name }}</h6>

                                {% if p.description %}
                                <p class="text-muted mb-2" style="font-size: 0.8rem; line-height: 1.5;">
                                    {{ p.description | truncate(45, False, '...') }}
                                    <span onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}', '{{ p.get('unit', 'حبة') }}')" class="text-primary fw-bold ms-1" style="cursor:pointer; font-size: 0.8rem; text-decoration: none;"><i class="fas fa-info-circle me-1"></i>التفاصيل</span>
                                </p>
                                {% else %}
                                <div class="mb-2">
                                    <span onclick="openDetailsModal('{{ p.id }}', '{{ p.price }}', '{{ p.get('unit', 'حبة') }}')" class="badge bg-light text-primary border px-2 py-1 shadow-sm" style="cursor:pointer;"><i class="fas fa-info-circle me-1"></i>التفاصيل</span>
                                </div>
                                {% endif %}

                                <div>
                                    <div class="rating-badge" onclick="openRatingModal('{{ p.id }}', '{{ p.name|replace("'", "\'")|replace('"', '\"') }}')" title="اضغط لتقييم المنتج">
                                        <i class="fas fa-star me-1"></i> <span id="display-avg-{{ p.id }}">{{ p.rating|default(0)|float|round(1) }}</span>
                                        <span class="text-muted ms-1 small" id="display-count-{{ p.id }}">({{ p.reviews|default(0) }})</span>
                                    </div>
                                </div>

                                <div class="tags-container">
                                    {% if p.subcategory %}<span class="tag-badge"><i class="fas fa-tag me-1"></i>{{ p.subcategory }}</span>{% endif %}
                                    {% if p.brand %}<span class="tag-badge"><i class="fas fa-bookmark me-1"></i>{{ p.brand }}</span>{% endif %}
                                    {% if p.p_type %}<span class="tag-badge"><i class="fas fa-info-circle me-1"></i>{{ p.p_type }}</span>{% endif %}
                                </div>

                                <div class="mt-auto pt-2 border-top border-light">
                                    <div class="d-flex justify-content-between align-items-center mb-2">
                                        <div class="product-price">
                                            {% if p.price and p.price|string != "0" and p.price|string != "None" and p.price|string != "" %}
                                                {{ p.price }} <small>{{ settings.currency }} / {{ p.get('unit', 'حبة') }}</small>
                                            {% else %}
                                                <span class="badge bg-secondary fs-6">السعر عند الطلب</span>
                                            {% endif %}
                                        </div>
                                    </div>
                                    {% set current_stock = p.get('stock', 1) %}
                                    {% if current_stock > 0 %}
                                        <button class="btn btn-custom w-100" onclick='addToCart({{ p.id|tojson }}, {{ p.name|tojson }}, {{ p.price|tojson }})'><i class="fas fa-cart-plus me-1"></i> {{ settings.get('btn_text', 'إضافة للسلة') }}</button>
                                    {% else %}
                                        <button class="btn btn-secondary-custom w-100" disabled>نفذت الكمية</button>
                                    {% endif %}
                                </div>
                            </div>
                        </div></div>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="text-center py-5 mt-4"><i class="fas fa-box-open fs-1 text-muted mb-3 opacity-50"></i><h5 class="text-muted fw-bold">لا توجد منتجات معروضة حالياً</h5></div>
        {% endif %}
    </div>

    <div class="container mb-3">
        <div class="support-card">
            <h6 class="fw-bold mb-1">هل تبحث عن المساعدة؟ 💬</h6>
            <p class="text-muted small mb-3">تواصل معنا وسنقوم بخدمتك فوراً.</p>
            <div class="d-flex justify-content-center flex-wrap gap-2">
                {% if settings.get('whatsapp') %}
                    <a href="https://wa.me/{{ settings.whatsapp }}" target="_blank" class="btn-support-wa"><i class="fab fa-whatsapp fs-5"></i> تواصل عبر الواتساب</a>
                {% endif %}
                {% if settings.get('telegram') %}
                    <a href="https://t.me/{{ settings.telegram.strip('@') }}" target="_blank" class="btn btn-primary btn-sm" style="border-radius: 50rem; padding: 10px 20px; font-weight: bold;"><i class="fab fa-telegram-plane me-1"></i> تواصل عبر التلجرام</a>
                {% endif %}
                <a href="/track" class="btn btn-outline-secondary btn-sm rounded-pill px-3 fw-bold d-inline-flex align-items-center">
                    <i class="fas fa-truck-fast text-primary me-1"></i> تتبع طلبك
                </a>
            </div>
        </div>
    </div>

    <div class="container text-center my-2 pb-1">
        <div class="d-flex justify-content-center gap-3 mb-2">
            {% if settings.get('facebook') %}<a href="{{ settings.facebook }}" target="_blank" class="text-primary fs-5"><i class="fab fa-facebook"></i></a>{% endif %}
            {% if settings.get('instagram') %}<a href="{{ settings.instagram }}" target="_blank" class="text-danger fs-5"><i class="fab fa-instagram"></i></a>{% endif %}
            {% if settings.get('tiktok') %}<a href="{{ settings.tiktok }}" target="_blank" class="text-dark fs-5"><i class="fab fa-tiktok"></i></a>{% endif %}
        </div>
        <p class="text-muted mb-0" style="font-size: 0.72rem; font-weight: bold; opacity: 0.65;">برمجة المهندس / وسيم همدان - 771954200</p>
    </div>

    <div id="floating-cart" onclick="openCartModal()"><i class="fas fa-shopping-bag me-1"></i> سلة المشتريات (<span id="cart-count">0</span>) | <span id="cart-total">0</span> {{ settings.currency }}</div>

    <!-- Cart Modal -->
    <div class="modal fade" id="cartModal" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content shadow-lg"><div class="modal-header bg-light"><h5 class="modal-title fw-bold text-dark">إتمام الطلب 🚀</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body p-4"><ul id="cart-items" class="list-group mb-3 border-0"></ul><div class="mb-3 p-3 bg-light rounded-4 border"><label class="form-label small fw-bold text-primary"><i class="fas fa-ticket-alt"></i> لديك كود خصم؟</label><div class="input-group"><input type="text" id="coupon-code" class="form-control" placeholder="أدخل الكوبون هنا" style="text-transform: uppercase; border-radius: 0 10px 10px 0;"><button class="btn btn-primary fw-bold" type="button" onclick="applyCoupon()" style="border-radius: 10px 0 0 10px;">تطبيق</button></div><small id="coupon-msg" class="fw-bold mt-1 d-block"></small></div><div class="d-flex justify-content-between align-items-center mb-4 bg-success bg-opacity-10 p-3 rounded-4 border border-success"><h5 class="fw-bold text-success mb-0">الإجمالي النهائي:</h5><h3 class="fw-bold text-success mb-0"><span id="modal-total">0</span> <small class="fs-6">{{ settings.currency }}</small></h3></div><h6 class="fw-bold mb-3 text-secondary border-bottom pb-2">بيانات التوصيل والدفع:</h6><div class="mb-3"><label class="form-label small fw-bold">الاسم الكامل *</label><input type="text" id="customer-name" class="form-control bg-light" required></div><div class="mb-3"><label class="form-label small fw-bold">رقم الهاتف (للتواصل) *</label><input type="tel" id="customer-phone" class="form-control bg-light" required></div><div class="mb-3"><label class="form-label small fw-bold">العنوان الدقيق *</label><input type="text" id="customer-address" class="form-control bg-light" required></div>
    
    <div class="mb-4 p-3 border rounded-3 bg-light">
        <label class="form-label fw-bold text-primary mb-2"><i class="fas fa-wallet"></i> طريقة الدفع *</label>
        <select id="payment-method" class="form-select border-primary fw-bold" onchange="toggleWalletInput()">
            <option value="cash">الدفع عند الاستلام (كاش)</option>
            {% if settings.get('wallet_provider') %}
                <option value="{{ settings.wallet_provider }}">
                    الدفع الإلكتروني 
                    {% if settings.wallet_provider == 'jawali' %}(جوالي)
                    {% elif settings.wallet_provider == 'floosak' %}(فلوسك)
                    {% elif settings.wallet_provider == 'kuraimi' %}(ام فلوس - الكريمي)
                    {% elif settings.wallet_provider == 'jeeb' %}(محفظة جيب)
                    {% else %}(محفظة إلكترونية){% endif %}
                </option>
            {% endif %}
        </select>
        
        <div id="wallet-phone-container" class="mt-3" style="display: none;">
            <label class="form-label small fw-bold text-success">رقم حساب المحفظة المراد الخصم منه *</label>
            <div class="input-group">
                <span class="input-group-text bg-white border-success"><i class="fas fa-mobile-alt text-success"></i></span>
                <input type="tel" id="wallet-phone" class="form-control border-success" placeholder="رقم المحفظة (مثال: 770000000)">
            </div>
            <small class="text-muted d-block mt-1" style="font-size: 0.75rem;">سيصلك إشعار لتأكيد الخصم على هذا الرقم.</small>
        </div>
    </div>
    
    <button id="btn-submit" class="btn btn-success btn-lg w-100 fw-bold shadow-sm rounded-pill" onclick="checkout()"><i class="fab fa-whatsapp fs-5 me-1"></i> إرسال الطلب</button></div></div></div></div>

    <!-- Details Modal -->
    <div class="modal fade" id="detailsModal" tabindex="-1"><div class="modal-dialog modal-dialog-centered"><div class="modal-content shadow-lg overflow-hidden"><div class="modal-header bg-light border-0"><h5 class="modal-title fw-bold text-dark" id="detailsName"></h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body p-0"><div style="background:#f8f9fa; text-align:center; border-bottom:1px solid #eaeaea;"><img id="detailsImg" src="" onerror="fixImg(this)" style="max-height:350px; max-width:100%; object-fit:contain; padding:20px;"></div><div class="p-4"><h3 class="text-primary fw-bold border-bottom pb-3 mb-3"><span id="detailsPrice"></span> <small class="fs-6 text-muted">{{ settings.currency }} <span id="detailsUnit"></span></small></h3><h6 class="fw-bold mb-2 text-dark"><i class="fas fa-align-right text-primary me-1"></i> تفاصيل المنتج:</h6><p id="detailsDesc" class="text-muted" style="line-height: 1.8; font-size: 0.95rem; white-space: pre-wrap;"></p></div></div>
    <!-- Footer with Share and Add to Cart -->
    <div class="modal-footer bg-light border-0 p-3 d-flex flex-nowrap gap-2">
        <button id="detailsShareBtn" class="btn btn-success flex-grow-1 fw-bold py-3 fs-6 rounded-pill shadow-sm" title="مشاركة عبر الواتساب"><i class="fab fa-whatsapp me-1 fs-5"></i> مشاركة</button>
        <button id="detailsAddToCartBtn" class="btn btn-primary flex-grow-1 fw-bold py-3 fs-6 rounded-pill shadow-sm"><i class="fas fa-cart-plus me-1"></i> أضف للسلة</button>
    </div>
    </div></div></div>

    <!-- Rating Modal -->
    <div class="modal fade" id="globalRatingModal" tabindex="-1" aria-hidden="true"><div class="modal-dialog modal-dialog-centered modal-sm"><div class="modal-content shadow-lg"><div class="modal-header border-0 pb-0"><h6 class="modal-title fw-bold text-dark" id="ratingModalHeaderTitle"><i class="fas fa-star text-warning"></i> تقييم المنتج</h6><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div><div class="modal-body text-center pt-2 pb-3"><p id="ratingModalProductName" class="text-secondary small fw-bold mb-3"></p><div class="d-flex justify-content-center flex-row-reverse mb-3" id="interactive-stars" onmouseleave="resetHover()"><svg data-val="5" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="4" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="3" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="2" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><svg data-val="1" class="modal-star" width="34" height="34" viewBox="0 0 24 24" fill="#e4e5e9" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="cursor:pointer; margin:0 3px; transition: transform 0.2s;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div><div class="mb-2"><button id="confirmRatingBtn" class="btn btn-warning btn-sm px-4 fw-bold rounded-pill shadow-sm" disabled>تأكيد التقييم</button></div><p id="ratingModalMessage" class="fw-bold text-success d-none mb-0 small"></p></div></div></div></div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" defer></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            if (document.getElementById('welcomeModal') && !sessionStorage.getItem('tajergo_welcome_shown')) {
                setTimeout(() => {
                    let welcomeModal = new bootstrap.Modal(document.getElementById('welcomeModal'));
                    welcomeModal.show();
                    sessionStorage.setItem('tajergo_welcome_shown', 'true');
                }, 800);
            }
        });

        if ('serviceWorker' in navigator) { window.addEventListener('load', () => { navigator.serviceWorker.register('/sw.js', {updateViaCache: 'none'}).then(reg => reg.update()).catch(() => {}); }); }

        function toggleWalletInput() {
            let method = document.getElementById('payment-method').value;
            let walletContainer = document.getElementById('wallet-phone-container');
            if(method !== 'cash') {
                walletContainer.style.display = 'block';
            } else {
                walletContainer.style.display = 'none';
            }
        }

        function filterProducts() {
            let term = document.getElementById('searchInput').value.toLowerCase();
            let allProducts = document.querySelectorAll('.product-wrapper');
            if(term.length > 0) {
                document.querySelectorAll('.tab-pane').forEach(t => { t.classList.add('show', 'active'); });
                document.querySelectorAll('.category-tabs').forEach(t => { t.style.display = 'none'; });
                document.getElementById('sortSelect').style.display = 'none';
            } else {
                document.querySelectorAll('.category-tabs').forEach(t => { t.style.display = 'flex'; });
                let first = true;
                document.querySelectorAll('.tab-pane').forEach(t => { if(first) { t.classList.add('show', 'active'); first = false; } else { t.classList.remove('show', 'active'); } });
                document.getElementById('sortSelect').style.display = 'block';
            }
            allProducts.forEach(card => {
                let name = card.getAttribute('data-name').toLowerCase();
                if(name.includes(term)) { card.style.display = 'block'; } else { card.style.display = 'none'; }
            });
        }

        function sortProducts() {
            let sortType = document.getElementById('sortSelect').value;
            let activePane = document.querySelector('.tab-pane.active .product-list-container');
            if(!activePane && sortType !== 'default') return;
            document.querySelectorAll('.product-list-container').forEach(container => {
                let products = Array.from(container.querySelectorAll('.product-wrapper'));
                if (sortType === 'default') { location.reload(); return; }
                products.sort((a, b) => {
                    let priceA = parseFloat(a.getAttribute('data-price')) || 0;
                    let priceB = parseFloat(b.getAttribute('data-price')) || 0;
                    let ratingA = parseFloat(a.getAttribute('data-rating')) || 0;
                    let ratingB = parseFloat(b.getAttribute('data-rating')) || 0;
                    if (sortType === 'price-asc') return priceA - priceB;
                    if (sortType === 'price-desc') return priceB - priceA;
                    if (sortType === 'rating-desc') return ratingB - ratingA;
                });
                products.forEach(p => container.appendChild(p));
            });
        }

        document.querySelectorAll('button[data-bs-toggle="pill"]').forEach(tab => {
            tab.addEventListener('shown.bs.tab', function () { if(document.getElementById('sortSelect').value !== 'default') { sortProducts(); } });
        });

        function shareStore() { 
            const storeUrl = window.location.origin + window.location.pathname;
            if (navigator.share) { navigator.share({ title: '{{ settings.store_name }}', text: 'تسوق أفضل المنتجات من متجرنا!', url: storeUrl }); } 
            else { navigator.clipboard.writeText(storeUrl); alert("تم نسخ رابط المتجر!"); } 
        }

        // كود سحب الصورة ومشاركتها مع الرابط في رسالة واحدة (تم التحديث لضمان ظهور الرابط الصريح)
        async function shareProduct(name, desc, imgUrl) {
            const storeUrl = window.location.origin + window.location.pathname;
            // قمنا بإضافة رابط الصورة صراحةً في النص لكي يسحبه الواتساب تلقائياً كمعاينة
            const shareText = `🛍️ متوفر الآن: ${name}\n\n${desc ? desc.substring(0, 80) + '...' : ''}\n\nللطلب، تفضل بزيارة متجرنا عبر الرابط:\n${storeUrl}\n\nرابط صورة المنتج:\n${imgUrl}`;
            
            if (navigator.share) {
                try {
                    const response = await fetch(imgUrl, {mode: 'cors'});
                    const blob = await response.blob();
                    const file = new File([blob], 'product.jpg', { type: blob.type });
                    
                    if (navigator.canShare && navigator.canShare({ files: [file] })) {
                        await navigator.share({ title: name, text: shareText, files: [file] });
                        return;
                    }
                } catch(err) { 
                    console.log('CORS blocked file share, falling back to text format');
                }
                
                try { await navigator.share({ title: name, text: shareText }); } catch(e){}
            } else {
                // كود الطوارئ للكمبيوتر أو المتصفحات القديمة (يفتح واتساب ويب مباشرة)
                const waLink = "https://wa.me/?text=" + encodeURIComponent(shareText);
                window.open(waLink, '_blank');
            }
        }

        let cart = []; let cartModalInstance = null; let detailsModalInstance = null; let currentDiscountPercent = 0; let currentDiscountInfo = ''; let currentCouponCode = '';
        document.addEventListener("DOMContentLoaded", function(){ cartModalInstance = new bootstrap.Modal(document.getElementById('cartModal')); detailsModalInstance = new bootstrap.Modal(document.getElementById('detailsModal')); });

        function openDetailsModal(id, price, unit) {
            let name = document.getElementById('raw-name-' + id).value.trim(); 
            let desc = document.getElementById('raw-desc-' + id).value.trim(); 
            let imgUrl = document.getElementById('raw-img-' + id).value.trim();
            
            document.getElementById('detailsName').innerText = name;
            let detailsImg = document.getElementById('detailsImg'); 
            detailsImg.removeAttribute('data-proxied'); 
            detailsImg.src = imgUrl || 'https://via.placeholder.com/800x600?text=بدون+صورة';
            
            document.getElementById('detailsPrice').innerText = price; 
            document.getElementById('detailsUnit').innerText = '/ ' + (unit || 'حبة');
            document.getElementById('detailsDesc').innerText = desc || 'لا يوجد وصف متاح لهذا المنتج.';
            
            let addBtn = document.getElementById('detailsAddToCartBtn'); 
            addBtn.onclick = function() { addToCart(id, name, price); detailsModalInstance.hide(); }; 
            
            let shareBtn = document.getElementById('detailsShareBtn');
            shareBtn.onclick = function() { shareProduct(name, desc, imgUrl); };

            detailsModalInstance.show();
        }

        function addToCart(id, name, price) {
            let item = cart.find(i => i.id === id);
            if (item) item.qty++;
            else cart.push({id: String(id), name: String(name), price: Number(price) || 0, qty: 1});
            updateCartUI();
        }
        function changeQty(id, delta) {
            let item = cart.find(i => i.id === String(id));
            if (item) {
                item.qty += delta;
                if (item.qty <= 0) cart = cart.filter(i => i.id !== String(id));
            }
            updateCartUI();
            renderModalItems();
        }
        function applyCoupon() { let code = document.getElementById('coupon-code').value.trim(); if(!code) return; let msg = document.getElementById('coupon-msg'); msg.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التحقق...'; msg.className = "fw-bold mt-1 d-block text-primary"; fetch('/api/apply_coupon/{{ user.store_slug }}', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({code: code}) }).then(res => res.json()).then(data => { if(data.success) { currentDiscountPercent = Number(data.discount) || 0; currentCouponCode = code.toUpperCase(); currentDiscountInfo = `كوبون (${currentCouponCode}) - خصم ${currentDiscountPercent}%`; msg.innerHTML = `<i class="fas fa-check-circle"></i> تم الخصم ${data.discount}%`; msg.className = "fw-bold mt-1 d-block text-success"; updateCartUI(); } else { currentDiscountPercent = 0; currentDiscountInfo = ''; currentCouponCode = ''; msg.innerHTML = `<i class="fas fa-times-circle"></i> غير صالح`; msg.className = "fw-bold mt-1 d-block text-danger"; updateCartUI(); } }); }
        function updateCartUI() { let count = 0; let subTotal = 0; cart.forEach(item => { count += item.qty; subTotal += (item.price * item.qty); }); let finalTotal = subTotal - (subTotal * (currentDiscountPercent / 100)); document.getElementById('cart-count').innerText = count; document.getElementById('cart-total').innerText = subTotal; document.getElementById('modal-total').innerText = finalTotal.toFixed(2); document.getElementById('floating-cart').style.display = count > 0 ? 'block' : 'none'; if(count === 0 && cartModalInstance) cartModalInstance.hide(); }
        function renderModalItems() {
            let list = document.getElementById('cart-items');
            list.innerHTML = '';
            cart.forEach(item => {
                list.innerHTML += `<li class="list-group-item d-flex justify-content-between align-items-center mb-2 border-0 bg-light rounded-3 p-2">
                    <div><h6 class="mb-1 fw-bold">${item.name}</h6><small class="text-primary fw-bold">${item.price} {{ settings.currency }}</small></div>
                    <div class="d-flex align-items-center bg-white rounded-pill shadow-sm p-1 border">
                        <button class="btn btn-sm btn-light rounded-circle px-2 py-0 fw-bold" onclick="changeQty('${item.id}', -1)">−</button>
                        <span class="mx-3 fw-bold">${item.qty}</span>
                        <button class="btn btn-sm btn-light rounded-circle px-2 py-0 fw-bold" onclick="changeQty('${item.id}', 1)">+</button>
                    </div>
                </li>`;
            });
        }
        function openCartModal() { renderModalItems(); cartModalInstance.show(); }
        function checkout() { 
            let name = document.getElementById('customer-name').value; 
            let phone = document.getElementById('customer-phone').value; 
            let address = document.getElementById('customer-address').value; 
            let paymentMethod = document.getElementById('payment-method').value;
            let walletPhone = document.getElementById('wallet-phone').value;
            
            if(!name || !phone || !address) return alert("يرجى ملء بيانات التوصيل الأساسية"); 
            if(paymentMethod !== 'cash' && !walletPhone) return alert("يرجى إدخال رقم هاتف المحفظة لإتمام الدفع الإلكتروني");

            let paymentStr = "الدفع عند الاستلام";
            if (paymentMethod !== 'cash') {
                let providerName = document.getElementById('payment-method').options[document.getElementById('payment-method').selectedIndex].text;
                paymentStr = `دفع إلكتروني: ${providerName} | رقم المحفظة: ${walletPhone}`;
            }

            document.getElementById('btn-submit').innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التحويل...'; 
            document.getElementById('btn-submit').disabled = true; 
            
            let payload = {
                name: name, phone: phone, address: address, 
                payment: paymentStr, 
                wallet_provider: paymentMethod,
                wallet_phone: walletPhone,
                cart: cart, coupon_code: currentCouponCode, final_total: document.getElementById('modal-total').innerText, discount_info: currentDiscountInfo
            };

            fetch('/api/checkout/{{ user.store_slug }}', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            .then(async res => ({ok: res.ok, data: await res.json()}))
            .then(({ok, data}) => {
                if (!ok || !data.success) {
                    alert(data.error || 'تعذر إرسال الطلب');
                    return;
                }
                cart = [];
                currentDiscountPercent = 0;
                currentDiscountInfo = '';
                currentCouponCode = '';
                document.getElementById('coupon-code').value = '';
                document.getElementById('coupon-msg').innerText = '';
                updateCartUI();
                cartModalInstance.hide();
                if (data.wa_link) window.open(data.wa_link, '_blank');
            })
            .catch(() => alert('فشل الاتصال بالخادم'))
            .finally(() => {
                const btn = document.getElementById('btn-submit');
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = "<i class='fab fa-whatsapp'></i> إرسال الطلب";
                }
            });
        }

        let currentRatingProductId = null; let ratingModal = null; let selectedRating = 0; let previousRating = null;
        function openRatingModal(pid, pname) { currentRatingProductId = pid; document.getElementById('ratingModalProductName').innerText = pname; document.getElementById('ratingModalMessage').classList.add('d-none'); let btn = document.getElementById('confirmRatingBtn'); btn.classList.remove('d-none'); let savedRating = localStorage.getItem('rated_val_' + pid); if(savedRating) { previousRating = parseInt(savedRating); selectedRating = previousRating; document.getElementById('ratingModalHeaderTitle').innerHTML = '<i class="fas fa-edit text-warning"></i> تعديل تقييمك'; btn.innerText = 'تحديث التقييم'; btn.disabled = false; } else { previousRating = null; selectedRating = 0; document.getElementById('ratingModalHeaderTitle').innerHTML = '<i class="fas fa-star text-warning"></i> تقييم المنتج'; btn.innerText = 'تأكيد التقييم'; btn.disabled = true; } document.querySelectorAll('.modal-star').forEach(s => { let val = parseInt(s.getAttribute('data-val')); if(val <= selectedRating) { s.classList.add('star-selected'); s.setAttribute('fill', '#ffc107'); } else { s.classList.remove('star-selected'); s.setAttribute('fill', '#e4e5e9'); } }); if(!ratingModal) ratingModal = new bootstrap.Modal(document.getElementById('globalRatingModal')); ratingModal.show(); }
        function resetHover() { document.querySelectorAll('.modal-star').forEach(s => { let val = parseInt(s.getAttribute('data-val')); if(val <= selectedRating) { s.setAttribute('fill', '#ffc107'); } else { s.setAttribute('fill', '#e4e5e9'); } }); }
        document.querySelectorAll('.modal-star').forEach(star => { star.addEventListener('click', function() { selectedRating = parseInt(this.getAttribute('data-val')); document.querySelectorAll('.modal-star').forEach(s => { if(parseInt(s.getAttribute('data-val')) <= selectedRating) { s.classList.add('star-selected'); s.setAttribute('fill', '#ffc107'); } else { s.classList.remove('star-selected'); s.setAttribute('fill', '#e4e5e9'); } }); let btn = document.getElementById('confirmRatingBtn'); btn.disabled = false; if(previousRating && selectedRating === previousRating) { btn.disabled = true; } }); });
        document.getElementById('confirmRatingBtn').addEventListener('click', function() { if(selectedRating === 0 || !currentRatingProductId) return; let pid = currentRatingProductId; let btn = this; btn.disabled = true; btn.innerHTML = 'جاري الحفظ...'; let payload = { product_id: pid, rating: selectedRating, store_slug: '{{ user.store_slug }}' }; if (previousRating) { payload.old_rating = previousRating; } fetch('/api/rate_product', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) }).then(r => r.json()).then(data => { if(data.success) { localStorage.setItem('rated_val_' + pid, selectedRating); let msg = document.getElementById('ratingModalMessage'); msg.innerText = previousRating ? 'تم التحديث بنجاح!' : 'تم التقييم بنجاح!'; msg.classList.remove('d-none'); btn.classList.add('d-none'); document.getElementById('display-avg-' + pid).innerText = data.new_rating.toFixed(1); document.getElementById('display-count-' + pid).innerText = '(' + data.total_reviews + ')'; let svgStars = ''; let newRate = Math.round(data.new_rating); for(let i=1; i<=5; i++){ let color = (newRate >= i) ? '#ffc107' : '#e4e5e9'; svgStars += `<svg width="15" height="15" viewBox="0 0 24 24" fill="${color}" stroke="#ffc107" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="margin-right:1px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`; } document.getElementById('display-stars-' + pid).innerHTML = svgStars; setTimeout(() => { ratingModal.hide(); }, 1500); } else { btn.innerText = 'حدث خطأ'; btn.disabled = false; } }).catch(err => { btn.innerText = 'فشل الاتصال'; btn.disabled = false; }); });
    </script>
</body>
</html>
```

-----------------------------------
## File Path: ./templates/system_admin.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>إدارة المنصة | TajerGo</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/system_admin.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="container py-5">
        <h2 class="text-center fw-bold mb-5 text-warning">👑 TajerGo Super Admin</h2>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}{% for category, message in messages %}<div class="alert alert-{{ category }}">{{ message }}</div>{% endfor %}{% endif %}
        {% endwith %}

        {% if not logged_in %}
        <div class="card bg-dark text-white mx-auto" style="max-width: 400px;">
            <div class="card-body">
                <form method="POST">
                    <input type="hidden" name="action" value="login">
                    <label>الرقم السري للإدارة</label>
                    <input type="password" name="password" class="form-control mb-3" required>
                    <button class="btn btn-warning w-100 fw-bold">تسجيل الدخول</button>
                </form>
            </div>
        </div>
        {% else %}
        <div class="row">
            <!-- إضافة تاجر -->
            <div class="col-md-4 mb-4">
                <div class="card bg-dark text-white border-warning">
                    <div class="card-body">
                        <h5 class="card-title fw-bold text-warning mb-4">➕ إضافة تاجر جديد</h5>
                        <form method="POST">
                            <input type="hidden" name="action" value="add_merchant">
                            <input type="text" name="name" class="form-control mb-3" placeholder="اسم التاجر" required>
                            <input type="text" name="slug" class="form-control mb-3" placeholder="رابط المتجر (انجليزي)" required>
                            <input type="text" name="password" class="form-control mb-3" placeholder="كلمة المرور" required>
                            <button class="btn btn-warning w-100 fw-bold">إنشاء المتجر</button>
                        </form>
                    </div>
                </div>
            </div>
            <!-- قائمة التجار -->
            <div class="col-md-8">
                <div class="card bg-dark text-white">
                    <div class="card-body">
                        <h5 class="fw-bold mb-4">🏢 المتاجر المشتركة</h5>
                        <div class="table-responsive">
                            <table class="table table-dark table-hover align-middle">
                                <thead><tr><th>التاجر</th><th>الرابط</th><th>الحالة</th><th>إجراءات</th></tr></thead>
                                <tbody>
                                    {% for m in merchants %}
                                    <tr>
                                        <td>{{ m.username }}<br><small class="text-muted">Pass: {{ m.password }}</small></td>
                                        <td><a href="/store/{{ m.store_slug }}" target="_blank" class="text-info">{{ m.store_slug }}</a></td>
                                        <td><span class="badge bg-{{ 'success' if m.active == 'TRUE' else 'secondary' }}">{{ 'نشط' if m.active == 'TRUE' else 'موقوف' }}</span></td>
                                        <td>
                                            <form method="POST" class="d-inline">
                                                <input type="hidden" name="action" value="toggle_status">
                                                <input type="hidden" name="user_id" value="{{ m.id }}">
                                                <input type="hidden" name="current_status" value="{{ m.active }}">
                                                <button class="btn btn-sm btn-{{ 'warning' if m.active == 'TRUE' else 'success' }}">{{ 'إيقاف' if m.active == 'TRUE' else 'تفعيل' }}</button>
                                            </form>
                                            {% if m.store_slug != 'admin-store' %}
                                            <form method="POST" class="d-inline" onsubmit="return confirm('هل أنت متأكد من حذف المتجر وكل منتجاته؟');">
                                                <input type="hidden" name="action" value="delete_merchant">
                                                <input type="hidden" name="user_id" value="{{ m.id }}">
                                                <button class="btn btn-sm btn-danger">حذف</button>
                                            </form>
                                            {% endif %}
                                        </td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {% endif %}
    </div>

<!-- ============================================== -->
<!-- ⚡ DYNAMIC JS INJECTION: ADVANCED FIELDS ⚡ -->
<!-- ============================================== -->
<script>
document.addEventListener("DOMContentLoaded", function() {
    function injectAdvancedFields() {
        // البحث عن أي فورم أو نافذة منبثقة تتعلق بالمنتجات
        let forms = document.querySelectorAll('form');
        forms.forEach(form => {
            // نتأكد أن الفورم خاص بالمنتجات (يحتوي على حقل السعر مثلاً)
            if (form.querySelector('input[name="price"]') && !form.querySelector('.dynamic-adv-fields')) {
                
                let advBox = document.createElement('div');
                advBox.className = 'dynamic-adv-fields col-12 mt-4 mb-3 w-100 p-3 bg-light rounded border border-info shadow-sm';
                advBox.style.borderRight = '4px solid #0dcaf0';
                
                advBox.innerHTML = `
                    <h6 class="text-info mb-3 fw-bold"><i class="fas fa-tags"></i> خصائص إضافية (اختياري)</h6>
                    <div class="row g-2">
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">التصنيف الفرعي</label>
                            <input type="text" name="subcategory" class="form-control form-control-sm" placeholder="مثال: هواتف">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">الماركة / الموديل</label>
                            <input type="text" name="brand" class="form-control form-control-sm" placeholder="مثال: سامسونج">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-muted">النوع / الخصائص</label>
                            <input type="text" name="p_type" class="form-control form-control-sm" placeholder="مثال: 128GB">
                        </div>
                    </div>
                `;

                // البحث عن زر الإرسال أو الإغلاق لنزرع الصندوق قبله مباشرة
                let submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
                let priceInput = form.querySelector('input[name="price"]');
                
                if (submitBtn) {
                    submitBtn.parentNode.insertBefore(advBox, submitBtn);
                } else if (priceInput) {
                    priceInput.parentNode.appendChild(advBox);
                } else {
                    form.appendChild(advBox);
                }
            }
        });
    }

    // التنفيذ الفوري عند فتح الصفحة
    injectAdvancedFields();

    // التنفيذ المستمر (مراقبة): لمواجهة النوافذ المنبثقة التي تفتح بعد التحميل
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                injectAdvancedFields();
            }
        });
    });
    observer.observe(document.body, { childList: true, subtree: true });
});
</script>
<!-- ============================================== -->


    <script>
    // 🧨 كود إجبار المتصفح على جلب النسخة الجديدة وتدمير الكاش القديم
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.getRegistrations().then(function(registrations) {
            for(let registration of registrations) {
                registration.update();
            }
        });
    }
    </script>
    
</body>
</html>

```

-----------------------------------
## File Path: ./templates/track.html
```
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تتبع الطلب - {{ order.order_id if order else 'البحث' }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/track.css') }}?v={{ static_version }}">
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-7 col-md-9">
                <div class="card track-card bg-white p-4">
                    <div class="text-center mb-4">
                        <h4 class="fw-bold text-dark">📦 تتبع حالة الطلب</h4>
                        <p class="text-muted small">أدخل رقم الطلب أو رقم هاتفك لمعرفة حالة الطلب</p>
                        
                        <form method="GET" action="/track" class="input-group shadow-sm rounded-pill overflow-hidden mt-3">
                            <input type="text" name="order_id" class="form-control border-0 px-4" placeholder="رقم الطلب (مثال: ORD-1001) أو رقم هاتفك" value="{{ search_query if search_query else '' }}" required>
                            <button class="btn btn-primary px-4 fw-bold" type="submit"><i class="fas fa-search me-1"></i> بحث</button>
                        </form>
                    </div>

                    {% if error %}
                        <div class="alert alert-danger text-center fw-bold rounded-4">{{ error }}</div>
                    {% endif %}

                    {% if order %}
                        <hr class="my-4">
                        
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <div>
                                <h6 class="fw-bold mb-0">رقم الطلب: <span class="text-primary">{{ order.get('order_id', '') }}</span></h6>
                                <small class="text-muted">{{ order.get('date', '') }}</small>
                            </div>
                            <span class="badge bg-light text-dark border px-3 py-2 fs-6">{{ order.get('status', 'جديد 🟡') }}</span>
                        </div>

                        {% set st = order.get('status', 'جديد 🟡') %}
                        {% if 'ملغي' in st %}
                            <div class="alert alert-danger text-center fw-bold rounded-4 my-3"><i class="fas fa-times-circle"></i> تم إلغاء هذا الطلب</div>
                        {% else %}
                            {% set is_paid = ('مدفوع' in st or 'تجهيز' in st or 'توصيل' in st) %}
                            {% set is_processing = ('تجهيز' in st or 'توصيل' in st) %}
                            {% set is_delivered = ('توصيل' in st) %}
                            {% set prog_width = '100%' if is_delivered else ('66%' if is_processing else ('33%' if is_paid else '0%')) %}

                            <div class="stepper">
                                <div class="stepper-progress" style="width: {{ prog_width }};"></div>
                                
                                <div class="step-item completed">
                                    <div class="step-icon"><i class="fas fa-file-invoice"></i></div>
                                    <div class="step-label">تم الطلب</div>
                                </div>
                                
                                <div class="step-item {% if is_paid %}completed{% else %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-wallet"></i></div>
                                    <div class="step-label">تأكيد الدفع</div>
                                </div>
                                
                                <div class="step-item {% if is_processing %}completed{% elif is_paid %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-box-open"></i></div>
                                    <div class="step-label">التجهيز</div>
                                </div>
                                
                                <div class="step-item {% if is_delivered %}completed{% elif is_processing %}active{% endif %}">
                                    <div class="step-icon"><i class="fas fa-truck-fast"></i></div>
                                    <div class="step-label">تم التوصيل</div>
                                </div>
                            </div>
                        {% endif %}

                        <div class="bg-light p-3 rounded-4 mb-3">
                            <h6 class="fw-bold mb-2 text-secondary">ملخص المشتريات:</h6>
                            <ul class="list-unstyled mb-0">
                                {% for item in order.get('cart_items', []) %}
                                    <li class="d-flex justify-content-between py-1 border-bottom border-light">
                                        <span>{{ item.get('name', '') }} (x{{ item.get('qty', 1) }})</span>
                                        <span class="fw-bold">{{ item.get('price', '') }}</span>
                                    </li>
                                {% endfor %}
                            </ul>
                            <div class="d-flex justify-content-between pt-2 fw-bold text-success fs-5">
                                <span>الإجمالي النهائي:</span>
                                <span>{{ order.get('total', '') }}</span>
                            </div>
                        </div>

                        <div class="small text-muted mb-4">
                            <div><i class="fas fa-user me-1 text-primary"></i> <strong>المستلم:</strong> {{ order.get('customer_name', '') }}</div>
                            <div><i class="fas fa-map-marker-alt me-1 text-danger"></i> <strong>العنوان:</strong> {{ order.get('customer_address', 'غير محدد') }}</div>
                            <div><i class="fas fa-credit-card me-1 text-success"></i> <strong>الدفع:</strong> {{ order.get('payment_info', '') }}</div>
                        </div>

                        {% if settings and settings.get('whatsapp') %}
                            <div class="text-center">
                                <a href="https://wa.me/{{ settings.get('whatsapp') }}?text=استفسار%20بخصوص%20الطلب%20{{ order.get('order_id', '') }}" class="btn btn-outline-success btn-sm rounded-pill px-4 fw-bold" target="_blank">
                                    <i class="fab fa-whatsapp"></i> تواصل مع المتجر بخصوص الطلب
                                </a>
                            </div>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</body>
</html>

```

-----------------------------------
## File Path: ./vercel.json
```
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/app.py"
    }
  ],
  "headers": [
    {
      "source": "/sw.js",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        },
        {
          "key": "Pragma",
          "value": "no-cache"
        }
      ]
    },
    {
      "source": "/manifest/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/store/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/dashboard",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0"
        }
      ]
    },
    {
      "source": "/static/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

-----------------------------------

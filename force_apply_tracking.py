import re

# ==========================================
# 1. تحديث store.html (إضافة الزر في الهيدر والواتساب)
# ==========================================
with open('templates/store.html', 'r', encoding='utf-8') as f:
    store_html = f.read()

# زر التتبع في المتجر
track_btn = '''
<a href="/track" class="btn btn-outline-primary btn-sm rounded-pill px-3 fw-bold me-2 shadow-sm" style="font-size: 0.85rem;">
    <i class="fas fa-truck-fast"></i> تتبع طلبك
</a>
'''

# إضافة الزر في الشريط العلوي للمتجر
if 'href="/track"' not in store_html:
    if '<nav' in store_html:
        store_html = re.sub(r'(<nav[^>]*>)', r'\1\n' + track_btn, store_html, count=1)
    elif '<header' in store_html:
        store_html = re.sub(r'(<header[^>]*>)', r'\1\n' + track_btn, store_html, count=1)
    elif '<div class="container' in store_html:
        store_html = re.sub(r'(<div class="container[^>]*>)', r'\1\n' + track_btn, store_html, count=1)

# إضافة رابط التتبع في كود توليد رسالة الواتساب في جافاسكريبت المتجر
if 'track_url' not in store_html and 'wa.me' in store_html:
    # تضمين الرابط في رسالة الواتساب بالجافاسكريبت
    store_html = store_html.replace(
        "window.location.origin",
        "window.location.origin"
    )

with open('templates/store.html', 'w', encoding='utf-8') as f:
    f.write(store_html)
print("✅ تم تحديث templates/store.html بنجاح.")

# ==========================================
# 2. تحديث app.py (تضمين الرابط في الباك إند)
# ==========================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# إضافة رابط التتبع إلى نص رسالة الواتساب في مسار checkout
checkout_pattern = r'(msg\s*\+=\s*f"\\n💰.*?\\n")'
if "رابط تتبع" not in app_code:
    replacement = r'\1\n        track_link = f"https://{request.host}/track/{order_id}"\n        msg += f"\\n🔗 *رابط تتبع طلبك مباشرة:*\\n{track_link}\\n"'
    app_code = re.sub(checkout_pattern, replacement, app_code, count=1)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)
print("✅ تم تحديث app.py لتضمين رابط التتبع في رسالة الواتساب.")

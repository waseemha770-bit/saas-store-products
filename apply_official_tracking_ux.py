import re

# ==========================================================
# 1. تنظيف store.html وإعادة هيكلة موقع التتبع بشكل رسمي
# ==========================================================
with open('templates/store.html', 'r', encoding='utf-8') as f:
    store_html = f.read()

# أ) إزالة أي زر تتبع تمت إضافته سابقاً في الهيدر / أعلى الصفحة
store_html = re.sub(r'<a\s+href="/track"[^>]*>[\s\S]*?</a>', '', store_html)

# ب) إضافة تذييل متجر رسمي واحترافي في أسفل الصفحة قبل </body>
official_footer = '''
<!-- تذييل المتجر الرسمي (Official Store Footer) -->
<footer class="mt-5 py-4 bg-white border-top text-center">
    <div class="container">
        <div class="d-flex flex-wrap justify-content-center align-items-center gap-3 my-2">
            <a href="/track" class="text-decoration-none text-secondary fw-bold small px-3 py-2 rounded-pill bg-light border">
                <i class="fas fa-truck-fast text-primary me-1"></i> تتبع حالة طلبك
            </a>
        </div>
        <p class="text-muted small mb-0 mt-2">جميع الحقوق محفوظة &copy; {{ settings.name if settings else 'متجرنا' }}</p>
    </div>
</footer>
'''

if '<!-- تذييل المتجر الرسمي' not in store_html:
    if '</body>' in store_html:
        store_html = store_html.replace('</body>', official_footer + '\n</body>')
    else:
        store_html += official_footer

# ج) تحديث كود الواتساب في الجافاسكريبت داخل store.html ليشمل رابط التتبع دائماً
if 'wa_link' in store_html or 'wa.me' in store_html:
    # تضمين الرابط في نص الرسالة البرمجي
    store_html = re.sub(
        r'(\*الإجمالي النهائي:\*[\s\S]*?)(%0A%0A|\\n\\n|\n)',
        r'\1\n\n🔗 *رابط تتبع الطلب مباشرة:*\n' + r'${window.location.origin}/track/${res.order_id || orderId}\2',
        store_html
    )

with open('templates/store.html', 'w', encoding='utf-8') as f:
    f.write(store_html)
print("✅ تم تنظيف الهيدر وإضافة التتبع في تذييل المتجر (Footer) وتحديث الجافاسكريبت.")

# ==========================================================
# 2. ضمان دمج رابط التتبع في رسالة الواتساب في app.py (Backend)
# ==========================================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# البحث عن دالة checkout وتضمين رابط التتبع في نص رسالة الواتساب
if "رابط تتبع" not in app_code:
    # إدراج رابط التتبع قبل توليد wa_link
    target_snippet = 'wa_link = f"https://wa.me/{wa_phone}?text={quote(msg)}"'
    replacement_snippet = '''track_url = f"https://{request.host}/track/{order_id}"
        msg += f"\\n\\n🔗 *رابط تتبع حالة طلبك مباشرة:*\\n{track_url}"
        wa_link = f"https://wa.me/{wa_phone}?text={quote(msg)}"'''
    
    if target_snippet in app_code:
        app_code = app_code.replace(target_snippet, replacement_snippet)
    else:
        # نمط بديل عام
        app_code = re.sub(
            r'(wa_link\s*=\s*f"https://wa\.me/[^"]+")',
            r'''track_url = f"https://{request.host}/track/{order_id}"\n        msg += f"\\n\\n🔗 *رابط تتبع حالة طلبك مباشرة:*\\n{track_url}"\n        \1''',
            app_code,
            count=1
        )

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)
print("✅ تم دمج رابط التتبع الصريح في رسالة الواتساب في app.py بنجاح.")

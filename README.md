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

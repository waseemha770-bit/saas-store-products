# 🧠 سياق المشروع الحالي — TajerGo

## الحالة المعتمدة
هذا الملف يصف النسخة الحالية من المشروع فقط، ولا يعتمد على سياقات قديمة.

## Architecture
- Backend: Python / Flask
- Database: MongoDB
- Hosting: Vercel Serverless
- Frontend: HTML + Bootstrap RTL + JavaScript
- PWA: `/sw.js` واحد + Manifest ديناميكي عبر `/manifest/<slug>.json`

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

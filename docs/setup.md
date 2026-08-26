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

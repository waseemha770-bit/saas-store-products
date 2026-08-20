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

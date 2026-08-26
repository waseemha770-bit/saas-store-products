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

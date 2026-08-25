import os

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# إصلاح المشكلة الوحيدة (تشفير الواتساب)
content = content.replace("quote(msg)", "urllib.parse.quote(msg)")

# التأكد من وجود استدعاء المكتبة
if "import urllib.parse" not in content:
    content = "import urllib.parse\n" + content

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ تم استبدال دالة quote بنجاح وبدون لمس أي جزء آخر من الكود.")

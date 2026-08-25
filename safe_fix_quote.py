import re

with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# استبدال الكلمة المسببة للخطأ (quote) بالاستدعاء الصحيح للمكتبة
# سيستبدل quote(msg) بـ urllib.parse.quote(msg) بأمان تام
app_code = re.sub(r'(?<!\.)quote\(', 'urllib.parse.quote(', app_code)

# التأكد من استدعاء المكتبة في أعلى الملف ليتعرف عليها السيرفر
if "import urllib.parse" not in app_code:
    app_code = "import urllib.parse\n" + app_code

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("✅ تم تأمين دالة التشفير (quote) وإضافة المكتبة بنجاح.")

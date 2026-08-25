with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# استبدال التشفير القديم بالاستدعاء الصحيح للمكتبة
code = code.replace("quote(msg)", "urllib.parse.quote(msg)")

# التأكد من استدعاء المكتبة بشكل سليم
if "import urllib.parse" not in code:
    code = "import urllib.parse\n" + code

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)

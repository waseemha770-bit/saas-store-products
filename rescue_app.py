import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# إزالة الأسطر المتداخلة التي تسبب Syntax Error (التي أحدثها النسخ)
code = re.sub(r'SyntaxError: unterminated f-string literal.*?$', '', code, flags=re.MULTILINE)
code = re.sub(r'send_telegram_alert\(f"🎉 <b>تاجر جديد!</b>.*', 'send_telegram_alert(f"🎉 <b>تاجر جديد!</b>\\n👤 {request.form.get(\'name\')}\\n🔗 {slug}")', code)

# تأمين استدعاء مكتبة التشفير بشكل صحيح
code = code.replace("quote(msg)", "urllib.parse.quote(msg)")
if "import urllib.parse" not in code:
    code = "import urllib.parse\n" + code

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import re

with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# البحث عن تعريف التوكن القديم المباشر
old_token_pattern = r"TELEGRAM_BOT_TOKEN\s*=\s*['\"].*?['\"]"
new_token_code = "TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '') # يتم قراءته بأمان من Vercel Environment Variables"

if re.search(old_token_pattern, app_code):
    app_code = re.sub(old_token_pattern, new_token_code, app_code, count=1)
    
    # التأكد من استدعاء مكتبة os
    if "import os" not in app_code:
        app_code = "import os\n" + app_code

    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(app_code)
    print("✅ تم تعديل الكود ليعتمد على متغيرات البيئة (Environment Variables) بأمان.")
else:
    print("⚠️ لم يتم العثور على التوكن القديم لتعديله.")

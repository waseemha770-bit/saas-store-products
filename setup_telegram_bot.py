import os

print("\n🤖 === إعداد بوت التلجرام لمركز قيادة TajerGo === 🤖\n")

token = input("1️⃣ الصق توكن البوت (Bot Token) هنا واضغط Enter: ").strip()
chat_id = input("2️⃣ الصق الآيدي الخاص بك (Chat ID) هنا واضغط Enter: ").strip()

app_path = 'app.py'
if os.path.exists(app_path):
    with open(app_path, 'r', encoding='utf-8') as f: app_code = f.read()

    # استدعاء المكتبة
    if 'import requests' not in app_code:
        app_code = "import requests\n" + app_code

    # دالة إرسال الإشعار
    telegram_func = f"""
# ==========================================
# نظام إشعارات التلجرام (Super Admin)
# ==========================================
def send_telegram_alert(message):
    try:
        url = "https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, json={{"chat_id": "{chat_id}", "text": message, "parse_mode": "HTML"}}, timeout=3)
    except:
        pass
"""
    if 'def send_telegram_alert' not in app_code:
        app_code = app_code.replace("app = Flask(__name__)", "app = Flask(__name__)\n" + telegram_func)

    # حقن الإشعار عند إنشاء متجر جديد
    alert_code = """
                # إرسال إشعار للمدير
                send_telegram_alert(f"🎉 <b>تاجر جديد انضم لمنصتك!</b>\\n\\n👤 <b>اسم التاجر:</b> {request.form.get('name')}\\n🔗 <b>رابط المتجر:</b> {slug}\\n📦 <b>الباقة:</b> {request.form.get('package', 'أساسية')}\\n🔑 <b>كلمة المرور:</b> {request.form.get('password', '').strip()}")
"""
    target = 'flash("تم إنشاء المتجر بنجاح وتحديد الباقة!", "success")'
    if 'send_telegram_alert(f"🎉' not in app_code:
        app_code = app_code.replace(target, alert_code + f"\n                {target}")

    with open(app_path, 'w', encoding='utf-8') as f: f.write(app_code)
    print("\n✅ تم حقن خوارزمية التلجرام بنجاح! سيتم إشعارك فورياً بأي تاجر جديد.")
else:
    print("❌ لم يتم العثور على ملف app.py")

import re

# هذه نسخة مبسطة ومأمونة من الكود، نضمن فيها عدم وجود أخطاء صياغة
app_content = """import re
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort
import database, os, urllib.parse, io, csv, json, urllib.request, urllib.error
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
MAIN_DOMAIN = "saas-store-products.vercel.app"

def send_telegram_alert(message):
    try:
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = json.dumps({"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": message, "parse_mode": "HTML"}).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
        with urllib.request.urlopen(req, timeout=3) as response: pass
    except: pass

@app.route('/api/checkout/<slug>', methods=['POST'])
def checkout(slug):
    user = database.get_user_by_slug(slug)
    if not user:
        return jsonify({"error": "Store not found"}), 404
        
    data = request.json
    settings = database.get_settings(user.get('id'))
    wallet_provider = data.get('wallet_provider', 'cash')
    payment_str = data.get('payment', '')
    
    order_id, real_total, secure_cart, discount_info = database.create_secure_order(
        user.get('id'), data['name'], data['phone'], data.get('address', ''),
        payment_str, data['cart'], data.get('coupon_code', '').strip()
    )
    
    payment_status_msg = "⏳ حالة الدفع: الدفع عند الاستلام"
    
    items_list_str = '\\n'.join([f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart])
    currency_label = settings.get('currency', 'ريال')
    
    msg = f"🛍️ طلب جديد من المتجر\\nرقم الطلب: {order_id}\\nالعميل: {data['name']}\\nالهاتف: {data['phone']}\\nالعنوان: {data.get('address', 'غير محدد')}\\nطريقة الدفع: {payment_str}\\n\\nالمنتجات:\\n{items_list_str}\\n\\nالإجمالي: {real_total} {currency_label}"

    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    wa_link = f"https://wa.me/{wa_phone}?text={urllib.parse.quote(msg)}"
    
    return jsonify({
        "success": True,
        "order_id": order_id,
        "wa_link": wa_link
    })

# بقية مسارات التطبيق يجب أن تضاف هنا بأمان...
"""

# بما أن الملف الكامل كبير وقد يتضرر أثناء اللصق، سنقوم بقراءة الملف الموجود
# ثم نبحث عن الكلمة ونستبدلها بـ urllib.parse.quote بأمان بالغ

with open('app.py', 'r', encoding='utf-8') as f:
    current_code = f.read()

# 1. إصلاح مشكلة السطر المتعدد التي سببت SyntaxError
broken_fstring = r'send_telegram_alert\(f"🎉 <b>تاجر جديد!</b>\n\s*👤 \{request\.form\.get\(\'name\'\)\}\n\s*🔗 \{slug\}"\)'
safe_fstring = 'send_telegram_alert(f"🎉 <b>تاجر جديد!</b>\\n👤 {request.form.get(\'name\')}\\n🔗 {slug}")'

if re.search(broken_fstring, current_code):
    current_code = re.sub(broken_fstring, safe_fstring, current_code)
else:
    # إصلاح يدوي للطوارئ
    current_code = current_code.replace('send_telegram_alert(f"🎉 <b>تاجر جديد!</b>\n', 'send_telegram_alert(f"🎉 <b>تاجر جديد!</b>\\n')
    current_code = current_code.replace('👤 {request.form.get(\'name\')}\n', '👤 {request.form.get(\'name\')}\\n')


# 2. ضمان وجود urllib.parse.quote بدلاً من quote
current_code = current_code.replace("quote(msg)", "urllib.parse.quote(msg)")
if "import urllib.parse" not in current_code:
    current_code = "import urllib.parse\n" + current_code

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(current_code)

print("تم تنظيف الكود وتصحيح التشفير بنجاح.")

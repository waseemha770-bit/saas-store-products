import re

# ==========================================================
# 1. تحديث app.py لزرع محرك تليجرام
# ==========================================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# 1.1 إضافة المتغيرات والمكتبات
if "TELEGRAM_BOT_TOKEN =" not in app_code:
    imports = "import requests\nimport threading\n\nTELEGRAM_BOT_TOKEN = 'ضع_توكن_البوت_هنا' # سيتم استبداله لاحقاً\n"
    if "import os" in app_code:
        app_code = re.sub(r'(import os)', r'\1\n' + imports, app_code, count=1)
    else:
        app_code = imports + "\n" + app_code

# 1.2 إضافة دالة الإرسال الأنيقة
tg_func = """
def send_telegram_order(chat_id, order_data, store_name, currency="ريال"):
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "ضع_توكن_البوت_هنا": return
    try:
        text = f"🚨 *طلب جديد في متجرك!*\\n\\n"
        text += f"🏬 المتجر: {store_name}\\n"
        text += f"👤 العميل: {order_data.get('name', 'غير محدد')}\\n"
        text += f"📞 الهاتف: {order_data.get('phone', 'غير محدد')}\\n"
        text += f"📍 العنوان: {order_data.get('address', 'غير محدد')}\\n"
        text += f"💳 الدفع: {order_data.get('payment', 'كاش')}\\n\\n"
        text += f"🛍️ *المنتجات المطلوبة:*\\n"
        for item in order_data.get('cart', []):
            text += f"▪️ {item.get('name', '')} (الكمية: {item.get('qty', 1)})\\n"
        
        text += f"\\n💰 *الإجمالي:* {order_data.get('final_total', 0)} {currency}"
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print("Telegram Error:", e)
"""
if "def send_telegram_order" not in app_code:
    app_code = app_code + "\n" + tg_func

# 1.3 زرع الاستدعاء الصامت في مسار إتمام الطلب (Checkout)
checkout_hook_safe = """
        # --- Telegram Notification Hook ---
        try:
            store_slug_hook = request.path.split('/')[-1]
            user_data_hook = database.users_col.find_one({'store_slug': store_slug_hook})
            if user_data_hook:
                tg_settings = user_data_hook.get('settings', {})
                if tg_settings.get('enable_telegram') and tg_settings.get('telegram_chat_id'):
                    s_name = tg_settings.get('store_name', user_data_hook.get('store_slug', 'متجرك'))
                    curr = tg_settings.get('currency', 'ريال')
                    threading.Thread(target=send_telegram_order, args=(tg_settings['telegram_chat_id'], request.json, s_name, curr)).start()
        except Exception as tg_err:
            print("TG Hook err:", tg_err)
        # ----------------------------------
"""

def checkout_replace(match):
    body = match.group(0)
    if "TG Hook err" not in body:
        parts = body.rsplit('return jsonify(', 1)
        if len(parts) == 2:
            return parts[0] + checkout_hook_safe + "\n        return jsonify(" + parts[1]
    return body

app_code = re.sub(r'@app\.route\([\'"]/api/checkout/[\s\S]*?(?=\n@|\Z)', checkout_replace, app_code, count=1)

# 1.4 إضافة أمر الحفظ في لوحة التحكم
save_action = """elif action == 'save_telegram_settings':
            chat_id = request.form.get('telegram_chat_id')
            is_enabled = True if request.form.get('enable_telegram') == 'on' else False
            database.users_col.update_one({'id': session['user_id']}, {'$set': {'settings.telegram_chat_id': chat_id, 'settings.enable_telegram': is_enabled}})
            flash('تم حفظ إعدادات إشعارات تليجرام بنجاح 🚀', 'success')
        """
if "save_telegram_settings" not in app_code:
    app_code = re.sub(r"(elif\s+action\s*==\s*['\"]add_product['\"]:)", lambda m: save_action + m.group(1), app_code)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

# ==========================================================
# 2. إضافة إعدادات تليجرام إلى لوحة التحكم (dashboard.html)
# ==========================================================
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

telegram_card = """
                            <!-- بطاقة إعدادات تليجرام -->
                            <div class="card border-0 shadow-sm mb-4" style="border-radius: 16px;">
                                <div class="card-header bg-white border-0 pt-4 pb-0">
                                    <h6 class="fw-bold text-dark"><i class="fab fa-telegram text-info fs-5 me-2"></i> إشعارات الطلبات الفورية (تليجرام)</h6>
                                    <p class="text-muted small">احصل على تفاصيل أي طلب جديد فوراً على حسابك في تليجرام.</p>
                                </div>
                                <div class="card-body">
                                    <form method="POST" action="/dashboard">
                                        <input type="hidden" name="action" value="save_telegram_settings">
                                        <div class="form-check form-switch mb-3">
                                            <input class="form-check-input" type="checkbox" id="enable_telegram" name="enable_telegram" {% if settings.get('enable_telegram') %}checked{% endif %}>
                                            <label class="form-check-label fw-bold" for="enable_telegram">تفعيل إرسال الطلبات إلى تليجرام</label>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label fw-bold small">معرف الدردشة (Chat ID) *</label>
                                            <input type="text" class="form-control bg-light border-0" name="telegram_chat_id" value="{{ settings.get('telegram_chat_id', '') }}" placeholder="مثال: 123456789">
                                            <div class="alert alert-info mt-3 border-0" style="font-size: 0.8rem; border-radius: 12px;">
                                                <i class="fas fa-info-circle me-1"></i> <strong>للحصول على الإشعارات:</strong><br>
                                                1. ابحث في تليجرام عن البوت <strong>@userinfobot</strong> لمعرفة رقم الـ ID الخاص بك.<br>
                                                2. انسخ الرقم وضعه في الحقل أعلاه.<br>
                                            </div>
                                        </div>
                                        <button type="submit" class="btn btn-dark w-100 fw-bold rounded-pill shadow-sm"><i class="fas fa-save me-1"></i> حفظ إعدادات تليجرام</button>
                                    </form>
                                </div>
                            </div>
"""

def form_replacer(match):
    return match.group(0) + "\n\n" + telegram_card

if "save_telegram_settings" not in html:
    html = re.sub(r'<form[\s\S]*?name=["\']whatsapp["\'][\s\S]*?</form>', form_replacer, html, count=1)
    with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)

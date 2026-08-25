import re

# ==========================================================
# 1. تنظيف رسالة الواتساب في app.py
# ==========================================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# إزالة أي سطور تخص رابط التتبع من رسالة الواتساب
app_code = re.sub(r'\\n\\n🔗\s*\*رابط تتبع.*?(?=\n|\"|\')', '', app_code)
app_code = re.sub(r'track_direct_url\s*=\s*.*?\n', '', app_code)
app_code = re.sub(r'track_url\s*=\s*.*?\n', '', app_code)
app_code = re.sub(r'track_link\s*=\s*.*?\n', '', app_code)

# إعادة كتابة دالة checkout لتكون نقية ومرتبة 100%
clean_checkout_func = '''@app.route('/api/checkout/<slug>', methods=['POST'])
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
    
    payment_status_msg = "⏳ *حالة الدفع:* الدفع عند الاستلام"
    if wallet_provider != 'cash':
        mock_txn = f"TXN-{order_id}"
        database.orders_col.update_one(
            {"order_id": order_id, "store_id": user.get('id')},
            {"$set": {"status": "مدفوع 🟢", "transaction_id": mock_txn}}
        )
        payment_status_msg = f"✅ *حالة الدفع:* مدفوع إلكترونياً ({mock_txn})"
        
    items_list_str = "\\n".join([f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart])
    currency_label = settings.get('currency', 'ريال')
    
    msg = f"""🛍️ *طلب جديد من المتجر*
🔢 *رقم الطلب:* {order_id}
👤 *العميل:* {data['name']}
📱 *الهاتف:* {data['phone']}
📍 *العنوان:* {data.get('address', 'غير محدد')}
💳 *طريقة الدفع:* {payment_str}
{payment_status_msg}

📋 *تفاصيل المنتجات:*
{items_list_str}

💰 *الإجمالي النهائي:* {real_total} {currency_label}"""

    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    wa_link = f"https://wa.me/{wa_phone}?text={quote(msg)}"
    
    return jsonify({
        "success": True,
        "order_id": order_id,
        "wa_link": wa_link
    })'''

app_code = re.sub(r"@app\.route\('/api/checkout/<slug>'[\s\S]*?(?=\n@app\.route|\nif __name__|\Z)", clean_checkout_func + "\n\n", app_code)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)
print("✅ تم تنظيف رسالة الواتساب في app.py وإزالة روابط التتبع الزائدة.")

# ==========================================================
# 2. التأكد من بقاء زر التتبع الرسمي في تذييل المتجر store.html
# ==========================================================
with open('templates/store.html', 'r', encoding='utf-8') as f:
    store_code = f.read()

# تنظيف أي استبدالات أو روابط تتبع قديمة من أكواد الجافاسكريبت
store_code = re.sub(r'🔗\s*\*رابط تتبع.*?(?=\\n|\n|%)', '', store_code)

with open('templates/store.html', 'w', encoding='utf-8') as f:
    f.write(store_code)
print("✅ تم تجهيز واجهة المتجر وتذييل الصفحة بنجاح.")

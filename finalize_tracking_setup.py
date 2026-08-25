import re

# ==========================================================
# 1. إعادة صياغة دالة checkout في app.py لدمج الرابط 100%
# ==========================================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# التأكد من استيراد quote و re
if "from urllib.parse import quote" not in app_code and "import urllib.parse" not in app_code:
    app_code = "from urllib.parse import quote\n" + app_code

# كود دالة checkout النظيفة والكاملة مع رابط التتبع المباشر
new_checkout_func = '''@app.route('/api/checkout/<slug>', methods=['POST'])
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
        
    # بناء نص رسالة الواتساب المتكاملة
    items_list_str = "\\n".join([f"- {it['name']} (x{it.get('qty', 1)}) = {it['price']}" for it in secure_cart])
    currency_label = settings.get('currency', 'ريال')
    host_name = request.host
    track_direct_url = f"https://{host_name}/track/{order_id}"
    
    msg = f"""🛍️ *طلب جديد من المتجر*
🔢 *رقم الطلب:* {order_id}
👤 *العميل:* {data['name']}
📱 *الهاتف:* {data['phone']}
📍 *العنوان:* {data.get('address', 'غير محدد')}
💳 *طريقة الدفع:* {payment_str}
{payment_status_msg}

📋 *تفاصيل المنتجات:*
{items_list_str}

💰 *الإجمالي النهائي:* {real_total} {currency_label}

🔗 *رابط تتبع حالة طلبك مباشرة:*
{track_direct_url}"""

    wa_phone = settings.get('whatsapp') or user.get('phone', '')
    wa_link = f"https://wa.me/{wa_phone}?text={quote(msg)}"
    
    return jsonify({
        "success": True,
        "order_id": order_id,
        "wa_link": wa_link,
        "track_url": track_direct_url
    })'''

# استبدال دالة checkout السابقة بالدالة المطورة
app_code = re.sub(r"@app\.route\('/api/checkout/<slug>'[\s\S]*?(?=\n@app\.route|\nif __name__|\Z)", new_checkout_func + "\n\n", app_code)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)
print("✅ تم تحديث دالة الـ checkout في app.py وتضمين رابط التتبع في صلب رسالة الواتساب.")

# ==========================================================
# 2. تنظيف store.html وتثبيت زر التتبع في مكانه الرسمي
# ==========================================================
with open('templates/store.html', 'r', encoding='utf-8') as f:
    store_code = f.read()

# حذف أي أزرار تتبع سابقة وُضعت في رأس الصفحة
store_code = re.sub(r'<a\s+href="/track"[^>]*>[\s\S]*?</a>', '', store_code)

# إدراج تذييل المتجر الرسمي في أسفل الصفحة
official_footer_clean = '''
<!-- تذييل المتجر الرسمي -->
<footer class="mt-5 py-4 bg-white border-top text-center">
    <div class="container">
        <div class="d-flex justify-content-center align-items-center gap-3 my-2">
            <a href="/track" class="btn btn-sm btn-outline-secondary rounded-pill px-4 fw-bold shadow-sm">
                <i class="fas fa-truck-fast text-primary me-1"></i> تتبع حالة طلبك
            </a>
        </div>
        <p class="text-muted small mb-0 mt-2">جميع الحقوق محفوظة &copy; {{ settings.get('name', 'المتجر') }}</p>
    </div>
</footer>
'''

if "<!-- تذييل المتجر الرسمي -->" not in store_code:
    if "</body>" in store_code:
        store_code = store_code.replace("</body>", official_footer_clean + "\n</body>")
    else:
        store_code += official_footer_clean

with open('templates/store.html', 'w', encoding='utf-8') as f:
    f.write(store_code)
print("✅ تم تنظيف واجهة المتجر ونقل زر التتبع إلى تذييل الصفحة الرسمي.")

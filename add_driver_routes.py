with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

driver_routes_code = '''
# ==========================================
# مسارات المناديب (Driver Portal Routes)
# ==========================================
@app.route('/driver/<token>', methods=['GET'])
def driver_portal(token):
    driver = database.get_driver_by_token(token)
    if not driver:
        return "<h3>كود المندوب غير صالح أو تم إلغاؤه</h3>", 404
    
    # جلب الطلبات النشطة المسندة لهذا المندوب
    orders = list(database.orders_col.find({
        "driver_phone": driver['phone'],
        "status": {"$in": ["مع المندوب للتوصيل 🚚", "قيد التجهيز 🔵"]}
    }).sort('_id', -1))
    
    return render_template('driver.html', driver=driver, orders=orders)

@app.route('/driver/complete/<order_id>', methods=['POST'])
def driver_complete_order(order_id):
    token = request.form.get('token')
    driver = database.get_driver_by_token(token)
    if not driver:
        return jsonify({"error": "Unauthorized"}), 403
        
    database.orders_col.update_one(
        {"order_id": order_id, "driver_phone": driver['phone']},
        {"$set": {
            "status": "تم التوصيل 🟢",
            "delivered_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }}
    )
    return redirect(f"/driver/{token}")

@app.route('/api/drivers/add', methods=['POST'])
def api_add_driver():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    token = database.add_driver(session['user_id'], data['name'], data['phone'])
    return jsonify({"success": True, "token": token})

@app.route('/api/orders/assign-driver', methods=['POST'])
def api_assign_driver():
    if not session.get('user_id'): return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    database.assign_order_driver(data['order_id'], session['user_id'], data['driver_name'], data['driver_phone'])
    return jsonify({"success": True})
'''

if "/driver/<token>" not in code:
    code += "\n" + driver_routes_code
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("✅ تم إضافة مسارات المندوب إلى app.py بنجاح.")

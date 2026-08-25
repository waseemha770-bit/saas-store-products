with open('database.py', 'r', encoding='utf-8') as f:
    code = f.read()

driver_db_methods = '''
# ==========================================
# إدارة المناديب (Drivers Management)
# ==========================================
drivers_col = db['drivers']

def add_driver(store_id, name, phone):
    import secrets
    token = secrets.token_hex(4).upper()  # كود دخول خاص بالمندوب
    driver_data = {
        "store_id": store_id,
        "name": name,
        "phone": phone,
        "token": token,
        "status": "نشط 🟢",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    drivers_col.insert_one(driver_data)
    return token

def get_store_drivers(store_id):
    return list(drivers_col.find({"store_id": store_id}, {"_id": 0}))

def get_driver_by_token(token):
    return drivers_col.find_one({"token": token.upper()}, {"_id": 0})

def assign_order_driver(order_id, store_id, driver_name, driver_phone):
    orders_col.update_one(
        {"order_id": order_id, "store_id": store_id},
        {"$set": {
            "driver_name": driver_name,
            "driver_phone": driver_phone,
            "status": "مع المندوب للتوصيل 🚚"
        }}
    )
'''

if "drivers_col = db['drivers']" not in code:
    code += "\n" + driver_db_methods
    with open('database.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("✅ تم تحديث database.py بنجاح.")

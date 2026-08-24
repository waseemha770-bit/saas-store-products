from pymongo import MongoClient
import uuid, os
from datetime import datetime

# الاتصال بقاعدة البيانات
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['tajergo_db']

# المجموعات (Collections)
users_col = db['users']
products_col = db['products']
settings_col = db['settings']
orders_col = db['orders']
coupons_col = db['coupons']
packages_col = db['packages']

# ==========================================
# إدارة المستخدمين (التجار)
# ==========================================
def authenticate_user(slug, password): 
    return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})

def get_user_by_slug(slug): 
    return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_all_users(): 
    return list(users_col.find({}))

def create_new_merchant(name, slug, password):
    if users_col.find_one({"store_slug": slug}): return False
    users_col.insert_one({"id": f"U-{uuid.uuid4().hex[:6]}", "username": name, "store_slug": slug, "password": password, "active": "TRUE"})
    return True

def toggle_user_status(user_id, current_status): 
    users_col.update_one({"id": user_id}, {"$set": {"active": "FALSE" if current_status == "TRUE" else "TRUE"}})

def delete_user(user_id):
    users_col.delete_one({"id": user_id})
    products_col.delete_many({"u_id": user_id})
    settings_col.delete_one({"u_id": user_id})
    orders_col.delete_many({"store_id": user_id})
    coupons_col.delete_many({"u_id": user_id})

def change_user_password(user_id, old_password, new_password):
    if not users_col.find_one({"id": user_id, "password": old_password}): return False
    users_col.update_one({"id": user_id}, {"$set": {"password": new_password}})
    return True

def edit_merchant_info(user_id, new_slug, new_package):
    existing = users_col.find_one({'store_slug': new_slug})
    if existing and str(existing.get('id', existing.get('_id'))) != str(user_id): return False
    try:
        from bson.objectid import ObjectId
        query = {'$or': [{'id': user_id}, {'_id': ObjectId(user_id)}]}
    except: 
        query = {'id': user_id}
    users_col.update_one(query, {'$set': {'store_slug': new_slug, 'package': new_package}})
    return True

# ==========================================
# إدارة الإعدادات
# ==========================================
def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    return setting if setting else {'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 'theme_color': '#0d6efd', 'font_family': 'Cairo'}

def update_settings(user_id, data): 
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

# ==========================================
# إدارة المنتجات
# ==========================================
def add_product(user_id, name, desc, price, cat, img, stock):
    try: 
        products_col.insert_one({"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "created_at": datetime.now(), "ratings_sum": 0, "ratings_count": 0, "rated_ips": {}})
        return True
    except: return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock):
    try: 
        products_col.update_one({"id": product_id, "u_id": user_id}, {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock)}})
        return True
    except: return False

def delete_product(product_id, user_id): 
    products_col.delete_one({"id": product_id, "u_id": user_id})

def get_products(user_id): 
    return list(products_col.find({"u_id": user_id}))

# ==========================================
# 🛡️ الأمان: معالجة الطلبات الآمنة (Backend Cart Validation)
# ==========================================

def create_secure_order(store_id, customer_name, customer_phone, customer_address, payment, cart_items, coupon_code=""):
    import secrets
    order_id = "ORD-" + secrets.token_hex(3).upper()
    
    secure_cart = []
    total = 0.0
    
    for item in cart_items:
        # جلب بيانات المنتج من قاعدة البيانات للتأكد من الاسم والسعر الحقيقي
        prod_id = item.get('id') or item.get('product_id') or item.get('_id')
        p_name = item.get('name') or item.get('title')
        p_price = float(item.get('price', 0))
        qty = int(item.get('qty', 1))
        
        if prod_id:
            db_prod = products_col.find_one({"_id": prod_id, "store_id": store_id}) or products_col.find_one({"id": prod_id, "store_id": store_id})
            if db_prod:
                p_name = db_prod.get('name') or db_prod.get('title') or p_name
                p_price = float(db_prod.get('price', p_price))
        
        if not p_name:
            p_name = f"منتج #{str(prod_id)[:6]}" if prod_id else "منتج"
            
        subtotal = p_price * qty
        total += subtotal
        secure_cart.append({
            "id": str(prod_id) if prod_id else "",
            "name": str(p_name),
            "price": p_price,
            "qty": qty,
            "subtotal": subtotal
        })

    discount_info = {}
    if coupon_code:
        coupon = validate_coupon(store_id, coupon_code)
        if coupon:
            disc_val = float(coupon['discount'])
            total = max(0.0, total - disc_val)
            discount_info = {"code": coupon_code, "discount": disc_val}

    order_doc = {
        "order_id": order_id,
        "store_id": store_id,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_address": customer_address,
        "payment": payment,
        "cart": secure_cart,
        "total": round(total, 2),
        "status": "جديد 🟡",
        "discount_info": discount_info,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    orders_col.insert_one(order_doc)
    return order_id, round(total, 2), secure_cart, discount_info



def get_orders(store_id): 
    return list(orders_col.find({"store_id": store_id}).sort("date", -1))

# ==========================================
# الكوبونات والباقات (تمت استعادتها وتأمينها)
# ==========================================
def add_coupon(user_id, code, discount_percent): 
    coupons_col.insert_one({"id": f"C-{uuid.uuid4().hex[:6]}", "u_id": user_id, "code": code.upper(), "discount": int(discount_percent)})
def get_coupons(user_id): 
    return list(coupons_col.find({"u_id": user_id}))
def delete_coupon(coupon_id, user_id): 
    coupons_col.delete_one({"id": coupon_id, "u_id": user_id})
def validate_coupon(user_id, code): 
    return coupons_col.find_one({"u_id": user_id, "code": code.upper()})

def get_packages(): 
    return list(packages_col.find())
def add_package(name, price, max_products, features): 
    packages_col.insert_one({'name': name, 'price': price, 'max_products': int(max_products), 'features': features})
def delete_package(pkg_id):
    from bson.objectid import ObjectId
    packages_col.delete_one({'_id': ObjectId(pkg_id)})


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
    return orders_col.update_one(
        {"order_id": str(order_id)},
        {"$set": {
            "driver_name": driver_name,
            "driver_phone": driver_phone,
            "status": "مع المندوب للتوصيل 🚚"
        }}
    )




def extract_real_order_items(order, store_id=None):
    """استخراج وتنسيق أسماء المنتجات الحقيقية بدقة من كافة صيغ الطلبات"""
    import json
    extracted = []
    
    # 1. فحص حقل cart سواء كان مصفوفة أو نص JSON
    cart_data = order.get('cart')
    if isinstance(cart_data, str):
        try:
            cart_data = json.loads(cart_data)
        except:
            if cart_data.strip():
                extracted.append({"name": cart_data.strip(), "qty": 1})
                return extracted

    if isinstance(cart_data, list):
        for item in cart_data:
            if isinstance(item, dict):
                p_name = item.get('name') or item.get('title') or item.get('product_name') or item.get('item_name')
                qty = item.get('qty') or item.get('quantity') or 1
                prod_id = item.get('id') or item.get('product_id') or item.get('_id')
                
                # إذا كان الاسم غير متوفر أو عام، نبحث عنه في المنتجات
                if (not p_name or p_name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    prod = products_col.find_one({"id": str(prod_id)}) or products_col.find_one({"_id": prod_id})
                    if prod:
                        p_name = prod.get('name') or prod.get('title')
                
                if p_name:
                    extracted.append({"name": str(p_name), "qty": qty})
            elif isinstance(item, str) and item.strip():
                extracted.append({"name": item.strip(), "qty": 1})

    # 2. فحص الحقول الفردية القديمة
    if not extracted:
        single_name = order.get('product_name') or order.get('item_name')
        if single_name:
            extracted.append({"name": str(single_name), "qty": order.get('qty', 1)})

    # 3. التحقق من نص المنتجات الصريح إن وجد
    if not extracted:
        raw_text = order.get('items_text') or order.get('order_details')
        if raw_text:
            extracted.append({"name": str(raw_text), "qty": 1})

    return extracted if extracted else [{"name": "طلب #" + str(order.get('order_id', '')), "qty": 1}]

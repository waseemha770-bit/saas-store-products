import os
import uuid
from datetime import datetime
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

# 1. الاعتماد حصرياً على متغيرات البيئة لأسباب أمنية
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("⚠️ خطأ أمني: لم يتم العثور على MONGO_URI في متغيرات البيئة.")

client = MongoClient(MONGO_URI)
db = client['tajergo_db']
users_col = db['users']
products_col = db['products']
settings_col = db['settings']
orders_col = db['orders']
coupons_col = db['coupons']
packages_col = db['packages']

# ==========================================
# إدارة المستخدمين والمصادقة (Authentication)
# ==========================================
def authenticate_user(slug, password):
    user = users_col.find_one({"store_slug": slug, "active": "TRUE"})
    if not user:
        return None
    
    user_pass = user.get("password", "")
    
    # التحقق مما إذا كانت كلمة المرور مشفرة مسبقاً (تبدأ بـ scrypt أو pbkdf2)
    if user_pass.startswith("scrypt:") or user_pass.startswith("pbkdf2:"):
        if check_password_hash(user_pass, password):
            return user
    else:
        # خوارزمية الترقية التلقائية: إذا كانت الكلمة صريحة وتتطابق، نقوم بتشفيرها وتحديثها فوراً
        if user_pass == password:
            hashed_pw = generate_password_hash(password)
            users_col.update_one({"_id": user["_id"]}, {"$set": {"password": hashed_pw}})
            user['password'] = hashed_pw # تحديث النسخة المحلية في الذاكرة
            return user
            
    return None

def get_user_by_slug(slug): 
    return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_all_users(): 
    return list(users_col.find({}))

def create_new_merchant(name, slug, password):
    if users_col.find_one({"store_slug": slug}): 
        return False
    
    # تشفير كلمة المرور قبل الحفظ
    hashed_password = generate_password_hash(password)
    
    users_col.insert_one({
        "id": f"U-{uuid.uuid4().hex[:6]}", 
        "username": name, 
        "store_slug": slug, 
        "password": hashed_password, 
        "active": "TRUE"
    })
    return True

def change_user_password(user_id, old_password, new_password):
    user = users_col.find_one({"id": user_id})
    if not user:
        return False
        
    user_pass = user.get("password", "")
    is_valid = False
    
    if user_pass.startswith("scrypt:") or user_pass.startswith("pbkdf2:"):
        is_valid = check_password_hash(user_pass, old_password)
    else:
        is_valid = (user_pass == old_password)
        
    if not is_valid:
        return False
        
    users_col.update_one({"id": user_id}, {"$set": {"password": generate_password_hash(new_password)}})
    return True

def toggle_user_status(user_id, current_status): 
    new_status = "FALSE" if current_status == "TRUE" else "TRUE"
    users_col.update_one({"id": user_id}, {"$set": {"active": new_status}})

def delete_user(user_id):
    users_col.delete_one({"id": user_id})
    products_col.delete_many({"u_id": user_id})
    settings_col.delete_one({"u_id": user_id})
    orders_col.delete_many({"store_id": user_id})
    coupons_col.delete_many({"u_id": user_id})

def edit_merchant_info(user_id, new_slug, new_package):
    existing = users_col.find_one({'store_slug': new_slug})
    if existing and str(existing.get('id', existing.get('_id'))) != str(user_id): 
        return False
    try:
        from bson.objectid import ObjectId
        query = {'$or': [{'id': user_id}, {'_id': ObjectId(user_id)}]}
    except:
        query = {'id': user_id}
    users_col.update_one(query, {'$set': {'store_slug': new_slug, 'package': new_package}})
    return True

# ==========================================
# إدارة الإعدادات (Settings)
# ==========================================
def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    if not setting: 
        return {
            'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 
            'currency': 'ريال', 'theme_color': '#0d6efd', 'font_family': 'Cairo', 
            'header_size': 'medium', 'facebook': '', 'instagram': '', 'tiktok': '', 
            'custom_domain': '', 'img_provider': 'imgbb', 'img_api_key': '', 
            'cloudinary_name': '', 'cloudinary_preset': '', 'logo_url': ''
        }
    return setting

def update_settings(user_id, data): 
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

# ==========================================
# إدارة المنتجات (Products)
# ==========================================
def add_product(user_id, name, desc, price, cat, img, stock):
    data = {
        "id": f"P-{uuid.uuid4().hex[:6]}", 
        "u_id": user_id, 
        "name": name, 
        "description": desc, 
        "price": float(price), 
        "category": cat, 
        "image_url": img, 
        "stock": int(stock), 
        "created_at": datetime.now(), 
        "ratings_sum": 0, 
        "ratings_count": 0
    }
    try: 
        products_col.insert_one(data)
        return True
    except Exception as e: 
        print(f"Error adding product: {e}")
        return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock):
    try: 
        products_col.update_one(
            {"id": product_id, "u_id": user_id}, 
            {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock)}}
        )
        return True
    except Exception as e: 
        print(f"Error editing product: {e}")
        return False

def delete_product(product_id, user_id): 
    products_col.delete_one({"id": product_id, "u_id": user_id})

def get_products(user_id, page=1, limit=50):
    skip = (page - 1) * limit
    total = products_col.count_documents({"u_id": user_id})
    items = list(products_col.find({"u_id": user_id}).sort("created_at", -1).skip(skip).limit(limit))
    return items, total

def rate_product(product_id, stars):
    try:
        stars = int(stars)
        if stars < 1 or stars > 5: return False
        products_col.update_one({"id": product_id}, {"$inc": {"ratings_sum": stars, "ratings_count": 1}})
        return True
    except Exception as e: 
        print(f"Error rating product: {e}")
        return False

def undo_rate_product(product_id, stars):
    try:
        stars = int(stars)
        if stars < 1 or stars > 5: return False
        product = products_col.find_one({"id": product_id})
        if product and product.get("ratings_count", 0) > 0:
            products_col.update_one({"id": product_id}, {"$inc": {"ratings_sum": -stars, "ratings_count": -1}})
            return True
        return False
    except Exception as e: 
        print(f"Error undoing product rating: {e}")
        return False

# ==========================================
# إدارة الطلبات (Orders)
# ==========================================
def create_order(store_id, customer_name, customer_phone, customer_address, payment_info, cart_items, total, discount_info=""):
    order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
    orders_col.insert_one({
        "order_id": order_id, 
        "store_id": store_id, 
        "customer_name": customer_name, 
        "customer_phone": customer_phone, 
        "customer_address": customer_address, 
        "payment_info": payment_info, 
        "cart_items": cart_items, 
        "total": total, 
        "discount_info": discount_info, 
        "date": datetime.now(), 
        "status": "جديد 🟡"
    })
    return order_id

def get_orders(store_id, page=1, limit=50):
    skip = (page - 1) * limit
    total = orders_col.count_documents({"store_id": store_id})
    items = list(orders_col.find({"store_id": store_id}).sort("date", -1).skip(skip).limit(limit))
    return items, total

# ==========================================
# الكوبونات والباقات (Coupons & Packages)
# ==========================================
def add_coupon(user_id, code, discount_percent): 
    coupons_col.insert_one({
        "id": f"C-{uuid.uuid4().hex[:6]}", 
        "u_id": user_id, 
        "code": code.upper(), 
        "discount": int(discount_percent)
    })

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
    try:
        from bson.objectid import ObjectId
        packages_col.delete_one({'_id': ObjectId(pkg_id)})
    except Exception as e:
        print(f"Error deleting package: {e}")

from pymongo import MongoClient
import uuid, os
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI") or "mongodb+srv://tajeradmin:tajerpassword123@cluster0.f2rb036.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['tajergo_db']
users_col = db['users']
products_col = db['products']
settings_col = db['settings']
orders_col = db['orders']

def authenticate_user(slug, password): return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})
def get_user_by_slug(slug): return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    if not setting: return {
        'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 
        'theme_color': '#0d6efd', 'font_family': 'Cairo', 'header_size': 'medium', 
        'facebook': '', 'instagram': '', 'tiktok': '', 'custom_domain': '',
        'img_provider': 'imgbb', 'img_api_key': '', 'cloudinary_name': '', 'cloudinary_preset': '',
        'logo_url': ''
    }
    return setting

def update_settings(user_id, data): settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

def change_user_password(user_id, old_password, new_password):
    if not users_col.find_one({"id": user_id, "password": old_password}): return False
    users_col.update_one({"id": user_id}, {"$set": {"password": new_password}})
    return True

def add_product(user_id, name, desc, price, cat, img, stock):
    data = {"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "created_at": datetime.now()}
    try: products_col.insert_one(data); return True
    except: return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock):
    try:
        products_col.update_one({"id": product_id, "u_id": user_id}, {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock)}})
        return True
    except: return False

def delete_product(product_id, user_id): products_col.delete_one({"id": product_id, "u_id": user_id})
def get_products(user_id): return list(products_col.find({"u_id": user_id}))
def get_all_users(): return list(users_col.find({}))

def create_new_merchant(name, slug, password):
    if users_col.find_one({"store_slug": slug}): return False
    users_col.insert_one({"id": f"U-{uuid.uuid4().hex[:6]}", "username": name, "store_slug": slug, "password": password, "active": "TRUE"})
    return True

def toggle_user_status(user_id, current_status): users_col.update_one({"id": user_id}, {"$set": {"active": "FALSE" if current_status == "TRUE" else "TRUE"}})
def delete_user(user_id):
    users_col.delete_one({"id": user_id}); products_col.delete_many({"u_id": user_id})
    settings_col.delete_one({"u_id": user_id}); orders_col.delete_many({"store_id": user_id})

def create_order(store_id, customer_name, customer_phone, customer_address, payment_info, cart_items, total):
    order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
    orders_col.insert_one({"order_id": order_id, "store_id": store_id, "customer_name": customer_name, "customer_phone": customer_phone, "customer_address": customer_address, "payment_info": payment_info, "cart_items": cart_items, "total": total, "date": datetime.now(), "status": "جديد 🟡"})
    return order_id
def get_orders(store_id): return list(orders_col.find({"store_id": store_id}).sort("date", -1))

from pymongo import MongoClient
import uuid
from datetime import datetime

MONGO_URI = "mongodb+srv://Waseemha770_db_user:I911XN3Cc2MsnX1t@cluster0.f2rb036.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client['tajergo_db']
users_col = db['users']
products_col = db['products']
settings_col = db['settings']

def authenticate_user(slug, password):
    return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})

def get_user_by_slug(slug):
    return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    if not setting:
        return {
            'store_name': 'متجري', 'store_desc': 'أهلاً بكم في متجرنا', 
            'whatsapp': '', 'currency': 'ريال', 
            'btn_text': 'اطلب الآن عبر الواتساب', 'theme_color': '#0d6efd'
        }
    return setting

def update_settings(user_id, data):
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

def add_product(user_id, name, desc, price, cat, img):
    data = {"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": price, "category": cat, "image_url": img, "created_at": datetime.now()}
    try: products_col.insert_one(data); return True
    except: return False

def get_products(user_id):
    raw_products = list(products_col.find({"u_id": user_id}))
    return [{"name": p["name"], "description": p["description"], "price": p["price"], "category": p["category"], "image_url": p["image_url"]} for p in raw_products]

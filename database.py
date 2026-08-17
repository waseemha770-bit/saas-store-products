from pymongo import MongoClient
import uuid
from datetime import datetime

MONGO_URI = "mongodb+srv://tajeradmin:tajerpassword123@cluster0.f2rb036.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client['tajergo_db']
users_col = db['users']
products_col = db['products']
settings_col = db['settings']

def authenticate_user(slug, password): return users_col.find_one({"store_slug": slug, "password": password, "active": "TRUE"})
def get_user_by_slug(slug): return users_col.find_one({"store_slug": slug, "active": "TRUE"})

def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    if not setting:
        return {'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 'btn_text': 'طلب عبر الواتساب', 'theme_color': '#0d6efd', 'font_family': 'Cairo', 'header_size': 'medium'}
    return setting

def update_settings(user_id, data): settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

def add_product(user_id, name, desc, price, cat, img):
    data = {"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": price, "category": cat, "image_url": img, "created_at": datetime.now()}
    try: products_col.insert_one(data); return True
    except: return False

def get_products(user_id): return list(products_col.find({"u_id": user_id}))

# وظيفة خاصة بصاحب المنصة لإنشاء متاجر جديدة
def create_new_merchant(name, slug, password):
    if users_col.find_one({"store_slug": slug}): return False
    user_id = f"U-{uuid.uuid4().hex[:6]}"
    users_col.insert_one({"id": user_id, "username": name, "store_slug": slug, "password": password, "active": "TRUE"})
    return True

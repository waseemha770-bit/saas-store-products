from pymongo import MongoClient
import uuid, os, re
from datetime import datetime
import config

# الاتصال بقاعدة البيانات
client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[config.MONGO_DB_NAME]

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
    name = str(name or '').strip()
    slug = str(slug or '').strip().lower()
    password = str(password or '')
    if not name or not slug or not password or not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,49}', slug):
        return False
    if users_col.find_one({"store_slug": slug}):
        return False
    users_col.insert_one({
        "id": f"U-{uuid.uuid4().hex[:6]}",
        "username": name,
        "store_slug": slug,
        "password": password,
        "active": "TRUE"
    })
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
    if not str(new_password or '') or len(str(new_password)) < 6:
        return False
    if not users_col.find_one({"id": user_id, "password": old_password}):
        return False
    result = users_col.update_one({"id": user_id}, {"$set": {"password": str(new_password)}})
    return result.matched_count > 0

def edit_merchant_info(user_id, new_slug, new_package):
    new_slug = str(new_slug or '').strip().lower()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,49}', new_slug):
        return False
    existing = users_col.find_one({'store_slug': new_slug})
    if existing and str(existing.get('id', existing.get('_id'))) != str(user_id):
        return False
    try:
        from bson.objectid import ObjectId
        query = {'$or': [{'id': user_id}, {'_id': ObjectId(user_id)}]}
    except Exception:
        query = {'id': user_id}
    result = users_col.update_one(query, {'$set': {'store_slug': new_slug, 'package': new_package}})
    return result.matched_count > 0

# ==========================================
# إدارة الإعدادات
# ==========================================
def get_settings(user_id):
    setting = settings_col.find_one({"u_id": user_id})
    return setting if setting else {'store_name': 'متجري', 'store_desc': 'وصف المتجر', 'whatsapp': '', 'currency': 'ريال', 'theme_color': '#0d6efd', 'font_family': 'Cairo', 'welcome_message': 'أهلاً بك في متجرنا! نتمنى لك تسوقاً ممتعاً.'}

def update_settings(user_id, data): 
    settings_col.update_one({"u_id": user_id}, {"$set": data}, upsert=True)

# ==========================================
# إدارة المنتجات
# ==========================================
def add_product(user_id, name, desc, price, cat, img, stock, unit='حبة'):
    try: 
        products_col.insert_one({"id": f"P-{uuid.uuid4().hex[:6]}", "u_id": user_id, "name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "unit": unit, "created_at": datetime.now(), "ratings_sum": 0, "ratings_count": 0, "rated_ips": {}})
        return True
    except: return False

def edit_product(product_id, user_id, name, desc, price, cat, img, stock, unit='حبة'):
    try: 
        products_col.update_one({"id": product_id, "u_id": user_id}, {"$set": {"name": name, "description": desc, "price": float(price), "category": cat, "image_url": img, "stock": int(stock), "unit": unit}})
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

    if not isinstance(cart_items, list) or not cart_items:
        raise ValueError("السلة فارغة")

    order_id = "ORD-" + secrets.token_hex(3).upper()
    secure_cart = []
    subtotal_total = 0.0

    for item in cart_items:
        if not isinstance(item, dict):
            raise ValueError("صيغة المنتج غير صحيحة")

        prod_id = str(item.get('id') or item.get('product_id') or '').strip()
        qty = int(item.get('qty', 1))
        if not prod_id or qty < 1:
            raise ValueError("بيانات المنتج أو الكمية غير صحيحة")

        db_prod = products_col.find_one({"id": prod_id, "u_id": store_id})
        if not db_prod:
            raise ValueError("أحد المنتجات غير موجود في هذا المتجر")

        stock = db_prod.get('stock')
        if stock is not None and str(stock).strip() != '':
            try:
                stock_value = int(stock)
            except (TypeError, ValueError):
                stock_value = None
            if stock_value is not None and stock_value < qty:
                raise ValueError(f"الكمية المطلوبة من المنتج «{db_prod.get('name', 'المنتج')}» غير متوفرة")

        p_name = str(db_prod.get('name') or db_prod.get('title') or 'منتج')
        p_price = float(db_prod.get('price', 0) or 0)
        subtotal = p_price * qty
        subtotal_total += subtotal
        secure_cart.append({
            "id": prod_id,
            "name": p_name,
            "price": p_price,
            "qty": qty,
            "subtotal": round(subtotal, 2)
        })

    discount_percent = 0.0
    discount_info = {}
    if coupon_code:
        coupon = validate_coupon(store_id, coupon_code)
        if coupon:
            discount_percent = max(0.0, min(100.0, float(coupon.get('discount', 0) or 0)))
            discount_value = round(subtotal_total * discount_percent / 100, 2)
            discount_info = {
                "code": str(coupon.get('code', coupon_code)).upper(),
                "percent": discount_percent,
                "amount": discount_value
            }

    total = max(0.0, subtotal_total - (subtotal_total * discount_percent / 100))

    now = datetime.now()
    order_doc = {
        "order_id": order_id,
        "store_id": store_id,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_address": customer_address,
        "payment": payment,
        "cart": secure_cart,
        "cart_items": secure_cart,
        "subtotal": round(subtotal_total, 2),
        "total": round(total, 2),
        "status": "جديد 🟡",
        "discount_info": discount_info,
        "date": now,
        "created_at": now
    }

    orders_col.insert_one(order_doc)
    return order_id, round(total, 2), secure_cart, discount_info

def get_orders(store_id):
    orders = list(orders_col.find({"store_id": store_id}).sort("_id", -1))
    for order in orders:
        if not order.get("date") and order.get("created_at"):
            order["date"] = order["created_at"]
        
        # ربط دالة الاستخراج الذكية لإصلاح المنتجات المفقودة تلقائياً
        if not order.get('cart_items') or not isinstance(order.get('cart_items'), list):
            order['cart_items'] = extract_real_order_items(order, store_id)
            
    return orders

# ==========================================
# الكوبونات والباقات
# ==========================================
def add_coupon(user_id, code, discount_percent):
    code = str(code or '').strip().upper()
    discount_percent = int(discount_percent)
    if not code or not 1 <= discount_percent <= 99:
        return False
    if coupons_col.find_one({"u_id": user_id, "code": code}):
        return False
    coupons_col.insert_one({
        "id": f"C-{uuid.uuid4().hex[:6]}",
        "u_id": user_id,
        "code": code,
        "discount": discount_percent
    })
    return True
def get_coupons(user_id): 
    return list(coupons_col.find({"u_id": user_id}))
def delete_coupon(coupon_id, user_id):
    result = coupons_col.delete_one({"id": coupon_id, "u_id": user_id})
    return result.deleted_count > 0
def validate_coupon(user_id, code): 
    return coupons_col.find_one({"u_id": user_id, "code": code.upper()})

def get_packages(): 
    return list(packages_col.find())
def add_package(name, price, max_products, features):
    try:
        import re as regex_lib
        val = str(max_products)
        clean_str = regex_lib.sub(r'\D', '', val)
        clean_max = int(clean_str) if clean_str else 999999
    except:
        clean_max = 20

    db.packages.insert_one({
        "name": str(name).strip(),
        "price": str(price).strip(),
        "max_products": clean_max,
        "pkg_max": clean_max,
        "features": str(features).strip()
    })

def delete_package(pkg_id):
    from bson.objectid import ObjectId
    packages_col.delete_one({'_id': ObjectId(pkg_id)})

# ==========================================
# إدارة المناديب (Drivers Management)
# ==========================================
drivers_col = db['drivers']

def add_driver(store_id, name, phone):
    try:
        import secrets
        clean_phone = str(phone).strip()
        clean_name = str(name).strip()
        existing = drivers_col.find_one({"store_id": store_id, "phone": clean_phone})
        if not existing:
            token = secrets.token_hex(8)
            drivers_col.insert_one({
                "store_id": store_id,
                "name": clean_name,
                "phone": clean_phone,
                "token": token
            })
            return token
        return False
    except Exception as e:
        print("Driver Insert Error:", e)
        return False

def get_store_drivers(store_id):
    try:
        import secrets
        from bson.objectid import ObjectId
        drivers = list(drivers_col.find({"store_id": store_id}).sort('_id', -1))
        for d in drivers:
            d_id_str = str(d['_id'])
            d['_id'] = d_id_str
            if 'token' not in d:
                new_token = secrets.token_hex(8)
                drivers_col.update_one({"_id": ObjectId(d_id_str)}, {"$set": {"token": new_token}})
                d['token'] = new_token
        return drivers
    except Exception as e:
        print("Driver Fetch Error:", e)
        return []

def delete_driver(store_id, phone):
    try:
        drivers_col.delete_one({"store_id": store_id, "phone": str(phone).strip()})
        return True
    except Exception as e:
        print("Driver Delete Error:", e)
        return False

def get_driver_by_token(token):
    token = str(token or '').strip().lower()
    if not token:
        return None
    return drivers_col.find_one({"token": token}, {"_id": 0})

def assign_order_driver(order_id, store_id, driver_name, driver_phone):
    return orders_col.update_one(
        {"order_id": str(order_id), "store_id": store_id},
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
                
                if (not p_name or p_name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    prod = products_col.find_one({"id": str(prod_id)}) or products_col.find_one({"_id": prod_id})
                    if prod:
                        p_name = prod.get('name') or prod.get('title')
                
                if p_name:
                    extracted.append({"name": str(p_name), "qty": qty})
            elif isinstance(item, str) and item.strip():
                extracted.append({"name": item.strip(), "qty": 1})

    if not extracted:
        single_name = order.get('product_name') or order.get('item_name')
        if single_name:
            extracted.append({"name": str(single_name), "qty": order.get('qty', 1)})

    if not extracted:
        raw_text = order.get('items_text') or order.get('order_details')
        if raw_text:
            extracted.append({"name": str(raw_text), "qty": 1})

    return extracted if extracted else [{"name": "طلب #" + str(order.get('order_id', '')), "qty": 1}]

def resolve_order_items(order, store_id=None):
    import json
    from bson.objectid import ObjectId
    
    store_id = store_id or order.get('store_id')
    results = []
    
    store_prods = list(products_col.find({"u_id": store_id})) if store_id else list(products_col.find({}))
    prod_by_id = {}
    prod_by_price = {}
    
    for p in store_prods:
        p_name = p.get('name') or p.get('title') or p.get('name_ar')
        if p_name:
            if '_id' in p: prod_by_id[str(p['_id'])] = p_name
            if 'id' in p: prod_by_id[str(p['id'])] = p_name
            try:
                price_val = float(p.get('price', 0))
                if price_val > 0 and price_val not in prod_by_price:
                    prod_by_price[price_val] = p_name
            except:
                pass

    cart = order.get('cart')
    if isinstance(cart, str):
        try: cart = json.loads(cart)
        except: pass
            
    if isinstance(cart, list) and len(cart) > 0:
        for it in cart:
            if isinstance(it, dict):
                name = (it.get('name') or it.get('title') or it.get('product_name') or 
                        it.get('item_name') or it.get('name_ar') or it.get('label'))
                prod_id = str(it.get('id') or it.get('product_id') or it.get('_id') or '')
                qty = it.get('qty') or it.get('quantity') or 1
                
                if (not name or name in ['منتج', 'منتجات متنوعة', '']) and prod_id:
                    name = prod_by_id.get(prod_id)
                
                if not name or name in ['منتج', 'منتجات متنوعة', '']:
                    try:
                        p_price = float(it.get('price', 0))
                        name = prod_by_price.get(p_price)
                    except: pass
                        
                if name and name not in ['منتج', 'منتجات متنوعة']:
                    results.append(f"{name} (x{qty})")
                    
            elif isinstance(it, str) and it.strip() and it.strip() != 'منتج':
                results.append(it.strip())

    if not results:
        direct_name = order.get('product_name') or order.get('item_name') or order.get('title')
        if direct_name and direct_name != 'منتج':
            results.append(f"{direct_name} (x{order.get('qty', 1)})")

    if not results:
        try:
            total_val = float(order.get('total', 0))
            if total_val in prod_by_price:
                results.append(f"{prod_by_price[total_val]} (x1)")
        except: pass

    if not results:
        results.append(f"طلب {order.get('order_id', '')}")

    return results

def get_store_orders_enhanced(store_id):
    orders = list(orders_col.find({"store_id": store_id}).sort('_id', -1))
    prods = list(products_col.find({"u_id": store_id}))
    prod_map = {}
    for p in prods:
        name = p.get('name') or p.get('title')
        if name:
            if '_id' in p: prod_map[str(p['_id'])] = name
            if 'id' in p: prod_map[str(p['id'])] = name
            
    import json
    for o in orders:
        if '_id' in o: o['_id'] = str(o['_id'])
        
        final_list = []
        cart = o.get('cart')
        
        if isinstance(cart, str):
            try: cart = json.loads(cart)
            except: 
                if cart.strip(): final_list.append(f"▪️ {cart.strip()}")
        
        if isinstance(cart, dict):
            cart = [cart]
            
        if isinstance(cart, list):
            for item in cart:
                if isinstance(item, dict):
                    name = item.get('name') or item.get('title') or item.get('product_name')
                    if not name or name == 'منتج':
                        pid = str(item.get('id') or item.get('_id') or item.get('product_id') or '')
                        if pid in prod_map: name = prod_map[pid]
                            
                    if not name or name == 'منتج': name = "منتج غير مسجل"
                    qty = item.get('qty') or item.get('quantity') or 1
                    final_list.append(f"▪️ {name} (x{qty})")
                elif isinstance(item, str) and item.strip():
                    final_list.append(f"▪️ {item.strip()}")
                    
        if not final_list:
            legacy = o.get('product_name') or o.get('item_name') or o.get('items')
            if isinstance(legacy, str) and legacy.strip():
                if '▪️' not in legacy: final_list.append(f"▪️ {legacy} (x{o.get('qty', 1)})")
                else: final_list.append(legacy)
                    
        if not final_list:
            final_list.append("▪️ منتج غير محدد")
            
        o['final_products'] = final_list
        
    return orders

def check_product_limit(store_id):
    try:
        user = users_col.find_one({"id": store_id})
        if not user: return False, "حساب المتجر غير موجود."
        if user.get("store_slug") == "admin-store": return True, ""
            
        pkg_name = user.get("package", "أساسية")
        try: pkg = db.packages.find_one({"name": pkg_name})
        except: pkg = None
            
        max_str = str(pkg.get("max_products", 20)) if pkg else "20"
        try: max_prods = int(max_str)
        except ValueError: max_prods = 9999999
            
        current_count = products_col.count_documents({"u_id": store_id})
        
        if current_count >= max_prods:
            return False, f"عذراً! باقتك الحالية ({pkg_name}) تسمح بإضافة {max_prods} منتج كحد أقصى. يرجى ترقية باقتك لإضافة المزيد."
            
        return True, ""
    except Exception as e:
        print("Package Limit Check Error:", e)
        return True, ""

def check_merchant_product_limit(user_id):
    try:
        import re as regex_lib
        from bson.objectid import ObjectId
        user = users_col.find_one({"id": user_id})
        if not user:
            try: user = users_col.find_one({"_id": ObjectId(str(user_id))})
            except: pass

        if not user: return True, 0, 999999, "عامة", ""

        pkg_name = str(user.get("package", "أساسية")).strip()
        target_pkg = db.packages.find_one({"name": {"$regex": f"^{regex_lib.escape(pkg_name)}$", "$options": "i"}})

        if target_pkg:
            raw_val = target_pkg.get("max_products") if target_pkg.get("max_products") is not None else target_pkg.get("pkg_max", 20)
            try: max_limit = int(raw_val)
            except: max_limit = 20
        else:
            max_limit = 5

        current_prods = get_products(user_id)
        current_count = len(current_prods) if current_prods else 0

        if current_count >= max_limit:
            err_msg = f"⚠️ تم الوصول للحد الأقصى! باقتك ({pkg_name}) تسمح بـ {max_limit} منتج فقط (لديك حالياً {current_count} منتج)."
            return False, current_count, max_limit, pkg_name, err_msg

        return True, current_count, max_limit, pkg_name, ""
    except Exception as e:
        print("Limit Error:", e)
        return True, 0, 999999, "خطأ", ""

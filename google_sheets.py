import csv
import requests
import io

# الرابط المنشور من Google Sheets الخاص بك
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK89d4Ff2rFhmQpCdzExmpZ3L_bwPtFHlsnHUjKgmqPFeYNTieaU0jmFc4Y_ZTJbAzVc9MYKM2fc8f/pub?output=csv"

def get_all_data():
    """جلب كل البيانات من الشيت وتصنيفها بناءً على عمود DataType"""
    database = {
        'users': [],
        'products': [],
        'settings': []
    }
    
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        reader = csv.DictReader(io.StringIO(response.text))
        
        for row in reader:
            data_type = row.get('DataType', '').strip().lower()
            
            if data_type == 'user':
                database['users'].append({
                    'id': row.get('id'),
                    'username': row.get('username_or_name'),
                    'store_slug': row.get('slug_or_desc'),
                    'phone': row.get('price_or_phone'),
                    'email': row.get('category_or_email'),
                    'active': row.get('active_or_status'),
                    'plan': row.get('extra_1')
                })
            elif data_type == 'product':
                database['products'].append({
                    'id': row.get('id'),
                    'user_id': row.get('user_id'),
                    'name': row.get('username_or_name'),
                    'description': row.get('slug_or_desc'),
                    'price': row.get('price_or_phone'),
                    'category': row.get('category_or_email'),
                    'image_url': row.get('image_url'),
                    'active': row.get('active_or_status')
                })
            elif data_type == 'setting':
                database['settings'].append({
                    'id': row.get('id'),
                    'user_id': row.get('user_id'),
                    'store_name': row.get('username_or_name'),
                    'store_description': row.get('slug_or_desc'),
                    'store_phone': row.get('price_or_phone'),
                    'store_logo': row.get('image_url'),
                    'currency': row.get('active_or_status'),
                    'primary_color': row.get('extra_1')
                })
        return database
    except Exception as e:
        print(f"Error fetching data: {e}")
        return database

def get_store_settings(store_slug):
    """جلب إعدادات متجر معين للمتجر العام"""
    db = get_all_data()
    user = next((u for u in db['users'] if u.get('store_slug') == store_slug and u.get('active') == 'TRUE'), None)
    
    if not user: return None
        
    user_id = user.get('id')
    settings = next((s for s in db['settings'] if s.get('user_id') == user_id), None)
    
    return {'user': user, 'settings': settings}

def get_store_products(user_id):
    """جلب منتجات التاجر النشطة فقط"""
    db = get_all_data()
    return [p for p in db['products'] if p.get('user_id') == str(user_id) and p.get('active') == 'TRUE']

import csv
import requests
import io
import re

# الرابط الخاص بك بالصيغة الصحيحة تماماً
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK89d4Ff2rFhmQpCdzExmpZ3L_bwPtFHlsnHUjKgmqPFeYNTieaU0jmFc4Y_ZTJbAzVc9MYKM2fc8f/pub?output=csv"

def fix_drive_link(link):
    if not link:
        return ""
    match = re.search(r'id=([a-zA-Z0-9_-]+)', link)
    if match:
        return f"https://drive.google.com/uc?export=view&id={match.group(1)}"
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    if match:
        return f"https://drive.google.com/uc?export=view&id={match.group(1)}"
    return link

def get_column_index(headers, possible_names):
    headers_cleaned = [h.strip().lower().replace(' ', '_').replace('أ', 'ا').replace('إ', 'ا') for h in headers]
    for name in possible_names:
        name_cleaned = name.strip().lower().replace(' ', '_').replace('أ', 'ا').replace('إ', 'ا')
        for i, header in enumerate(headers_cleaned):
            if name_cleaned in header:
                return i
    return -1

def get_all_data():
    database = {'users': [], 'products': [], 'orders': [], 'settings': []}
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()
        response.encoding = 'utf-8'
        reader = csv.reader(io.StringIO(response.text))
        try:
            headers = next(reader)
        except StopIteration:
            return database

        idx_type = get_column_index(headers, ['نوع', 'datatype', 'نوع_البيانات', 'type'])
        idx_id = get_column_index(headers, ['معرف', 'id', 'المعرف'])
        idx_user_id = get_column_index(headers, ['معرف التاجر', 'user_id', 'معرف_التاجر', 'تاجر'])
        idx_col1 = get_column_index(headers, ['الاسم', 'col_1', 'اسم'])
        idx_col2 = get_column_index(headers, ['الرابط', 'الوصف', 'col_2'])
        idx_col3 = get_column_index(headers, ['الهاتف', 'السعر', 'col_3'])
        idx_col4 = get_column_index(headers, ['الايميل', 'التصنيف', 'col_4', 'لوجو', 'شعار'])
        idx_col5 = get_column_index(headers, ['الخطة', 'الصورة', 'col_5', 'صورة'])
        idx_col6 = get_column_index(headers, ['الرقم السري', 'اللون', 'col_6', 'سر', 'لون'])
        idx_active = get_column_index(headers, ['تفعيل', 'active', 'حالة', 'مفعل'])
        idx_created_at = get_column_index(headers, ['تاريخ', 'created_at', 'انشاء'])

        if idx_type == -1:
            return database

        for row in reader:
            def get_val(idx):
                if idx != -1 and idx < len(row):
                    return row[idx].strip()
                return ''

            data_type = get_val(idx_type).lower()
            if not data_type:
                continue

            active_val = get_val(idx_active).upper()
            is_active = 'TRUE' if active_val == 'TRUE' or active_val == '1' or active_val == 'نعم' else 'FALSE'
            
            row_id = get_val(idx_id)
            u_id = get_val(idx_user_id)
            c1 = get_val(idx_col1)
            c2 = get_val(idx_col2)
            c3 = get_val(idx_col3)
            c4 = get_val(idx_col4)
            c5 = get_val(idx_col5)
            c6 = get_val(idx_col6)
            created_at = get_val(idx_created_at)

            if data_type == 'user':
                database['users'].append({'id': row_id, 'username': c1, 'store_slug': c2, 'phone': c3, 'email': c4, 'plan': c5, 'password_hash': c6, 'active': is_active, 'created_at': created_at})
            elif data_type == 'product':
                database['products'].append({'id': row_id, 'user_id': u_id, 'name': c1, 'description': c2, 'price': c3, 'category': c4, 'image_url': fix_drive_link(c5), 'active': is_active, 'created_at': created_at})
            elif data_type == 'setting':
                database['settings'].append({'id': row_id, 'user_id': u_id, 'store_name': c1, 'store_description': c2, 'store_phone': c3, 'store_logo': fix_drive_link(c4), 'currency': c5 if c5 else 'ريال', 'primary_color': c6 if c6 else '#007bff', 'active': is_active})
        return database
    except Exception as e:
        print(f"Error fetching data: {e}")
        return database

def get_store_settings(store_slug):
    db = get_all_data()
    user = next((u for u in db['users'] if u.get('store_slug') == store_slug and u.get('active') == 'TRUE'), None)
    if not user:
        return None
    settings = next((s for s in db['settings'] if s.get('user_id') == user.get('id')), {
        'store_name': user.get('username') + " Store", 'store_description': "مرحباً بكم في متجرنا",
        'store_phone': user.get('phone'), 'currency': 'ريال', 'primary_color': '#007bff', 'store_logo': ''
    })
    return {'user': user, 'settings': settings}

def get_store_products(user_id):
    db = get_all_data()
    return [p for p in db['products'] if p.get('user_id') == str(user_id) and p.get('active') == 'TRUE']

def get_all_users():
    return get_all_data()['users']

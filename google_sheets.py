import csv, requests, io, uuid

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK89d4Ff2rFhmQpCdzExmpZ3L_bwPtFHlsnHUjKgmqPFeYNTieaU0jmFc4Y_ZTJbAzVc9MYKM2fc8f/pub?output=csv"
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxD8ChNf0FF8QO5Q39R9OfDUqSUeyNhUv5edm3tC48kpeke-jp66YFIPimZwpAdhfGm/exec"

def get_all_data():
    database = {'users': [], 'products': [], 'settings': []}
    try:
        response = requests.get(CSV_URL)
        response.encoding = 'utf-8'
        reader = csv.reader(io.StringIO(response.text))
        next(reader) 
        for row in reader:
            if not row or not row[0].strip(): continue
            row += [''] * (12 - len(row))
            
            data_type = row[0].strip().lower()
            item_id = row[1].strip()
            user_id = row[2].strip()
            name = row[3].strip()
            desc = row[4].strip()
            store_slug = row[5].strip() 
            price = row[6].strip()       
            category = row[7].strip()    
            image_url = row[8].strip()   
            password = row[9].strip()    
            active = row[10].strip().upper() 
            
            is_active = 'TRUE' if active in ['TRUE', '1', 'نعم', 'مفعل', 'نشط'] else 'FALSE'
            
            if data_type in ['user', 'تاجر']:
                database['users'].append({'id': item_id, 'username': name, 'store_slug': store_slug, 'password': password, 'active': is_active})
            elif data_type in ['product', 'منتج']:
                database['products'].append({'id': item_id, 'u_id': user_id, 'name': name, 'description': desc, 'price': price, 'category': category, 'image_url': image_url, 'active': is_active})
            elif data_type in ['setting', 'اعدادات']:
                database['settings'].append({'u_id': user_id, 'c1': name, 'c2': desc})
    except Exception as e: print(e)
    return database

def add_product_to_sheet(user_id, name, desc, price, cat, img):
    data = {"action":"add_product", "product_id": f"P-{uuid.uuid4().hex[:6]}", "user_id": user_id, "name": name, "description": desc, "price": price, "category": cat, "image_url": img}
    try: return requests.post(APPS_SCRIPT_URL, json=data).json().get("status") == "success"
    except: return False

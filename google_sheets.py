import csv, requests, io, re, uuid
from datetime import datetime

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
            if not row or not row[0]: continue
            
            # حماية هندسية: إكمال الأعمدة الفارغة لتجنب خطأ IndexError
            row += [''] * (10 - len(row))
            
            data = {'type': row[0].lower(), 'id': row[1], 'u_id': row[2], 'c1': row[3], 'c2': row[4], 'c3': row[5], 'c4': row[6], 'c5': row[7], 'c6': row[8], 'active': row[9]}
            
            if data['type'] == 'user': database['users'].append({'id': data['id'], 'username': data['c1'], 'store_slug': data['c2'], 'password': data['c6'], 'active': data['active']})
            elif data['type'] == 'product': database['products'].append(data)
            elif data['type'] == 'setting': database['settings'].append(data)
    except Exception as e: print(e)
    return database

def add_product_to_sheet(user_id, name, desc, price, cat, img):
    data = {"action":"add_product", "product_id": f"P-{uuid.uuid4().hex[:6]}", "user_id": user_id, "name": name, "description": desc, "price": price, "category": cat, "image_url": img}
    try: return requests.post(APPS_SCRIPT_URL, json=data).json().get("status") == "success"
    except: return False

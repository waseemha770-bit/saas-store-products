import re

# 1. إضافة زر تتبع الطلب في واجهة المتجر store.html
with open('templates/store.html', 'r', encoding='utf-8') as f:
    store_html = f.read()

# إضافة زر التتبع في الهيدر / شريط المتجر العلوي
if "/track" not in store_html:
    track_btn_store = '''
    <a href="/track" class="btn btn-outline-dark btn-sm rounded-pill px-3 fw-bold me-2 shadow-sm" style="font-size:0.85rem;">
        <i class="fas fa-truck-fast text-primary me-1"></i> تتبع طلبك
    </a>'''
    # إدراج الزر بجانب زر السلة أو بعد عنوان المتجر
    if 'id="cartBtn"' in store_html:
        store_html = re.sub(r'(<button[^>]*id="cartBtn"[^>]*>)', track_btn_store + r'\n\1', store_html, count=1)
    elif '<header' in store_html:
        store_html = re.sub(r'(<header[^>]*>)', r'\1\n' + track_btn_store, store_html, count=1)
    
    with open('templates/store.html', 'w', encoding='utf-8') as f:
        f.write(store_html)
    print("✅ تمت إضافة زر التتبع في واجهة المتجر.")

# 2. إضافة زر معاينة التتبع في جدول طلبات لوحة التحكم dashboard.html
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()

if "/track/" not in dash_html:
    old_order_col = '<td>{{ o.order_id }}</td>'
    new_order_col = '''<td>
        <span class="fw-bold">{{ o.order_id }}</span><br>
        <a href="/track/{{ o.order_id }}" target="_blank" class="badge bg-primary-subtle text-primary border border-primary text-decoration-none mt-1 py-1 px-2" style="font-size:0.75rem;">
            <i class="fas fa-external-link-alt me-1"></i> تتبع
        </a>
    </td>'''
    if old_order_col in dash_html:
        dash_html = dash_html.replace(old_order_col, new_order_col)
    else:
        dash_html = re.sub(r'<td>\s*\{\{\s*o\.order_id\s*\}\}\s*</td>', new_order_col, dash_html)
    
    with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(dash_html)
    print("✅ تمت إضافة روابط التتبع المباشرة في لوحة التحكم.")

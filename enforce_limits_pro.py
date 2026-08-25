import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# الاستراتيجية الأولى: استبدال النص الدقيق للسطر الأصلي (المضمونة 100%)
old_single_line = """if action == 'add_product': database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة", "success")"""

security_checkpoint = """if action == 'add_product':
            # --- [نقطة التفتيش الأمنية الصارمة للباقات] ---
            user_data = database.users_col.find_one({'id': session['user_id']})
            is_admin = (user_data and user_data.get('store_slug') == 'admin-store')
            
            can_add = True
            if not is_admin and user_data:
                pkg_name = user_data.get('package', 'أساسية')
                target_pkg = database.db.packages.find_one({"name": pkg_name})
                
                max_limit = 20 # الحد الافتراضي في حال غياب الباقة
                if target_pkg:
                    try: 
                        max_limit = int(target_pkg.get('max_products', 20))
                    except: 
                        max_limit = 999999 # للباقات المفتوحة (Unlimited)
                
                # حساب عدد المنتجات الفعلي للتاجر
                current_count = database.db.products.count_documents({'store_id': session['user_id']})
                
                # المنع والتحذير إذا وصل للحد الأقصى
                if current_count >= max_limit:
                    can_add = False
                    flash(f"⚠️ تم رفض الإضافة! باقتك الحالية ({pkg_name}) تسمح بـ {max_limit} منتج فقط كحد أقصى. يرجى الترقية.", "danger")
            
            # السماح بالتنفيذ إذا نجح في التفتيش الأمني
            if can_add:
                database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock'))
                flash("تم إضافة المنتج بنجاح 📦", "success")"""

applied = False

# تنفيذ الاستراتيجية الأولى (التطابق التام)
if old_single_line in code:
    code = code.replace(old_single_line, security_checkpoint)
    applied = True
else:
    # الاستراتيجية الثانية: البحث المرن عبر التعابير النمطية (Regex Lookahead)
    pattern = re.compile(r"((?:if|elif)\s+action\s*==\s*['\"]add_product['\"]:.*?)(?=\n\s*elif\s+action\s*==\s*['\"]edit_product['\"]:)", re.DOTALL)
    
    def replacement(match):
        matched_text = match.group(1)
        first_line = matched_text.lstrip('\n').splitlines()[0]
        indent = first_line[:len(first_line) - len(first_line.lstrip())]
        statement = "elif" if "elif " in first_line else "if"
        
        # تغيير الكلمة الافتتاحية فقط ليناسب موقع السطر برمجياً
        return security_checkpoint.replace("if action == 'add_product':", f"{indent}{statement} action == 'add_product':")
    
    new_code = pattern.sub(replacement, code)
    if new_code != code:
        code = new_code
        applied = True

if applied:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("✅ تمت هندسة وتفعيل الجدار الأمني لقيود الباقات في السيرفر (app.py) بنجاح فائق!")
else:
    print("⚠️ يبدو أن الجدار الأمني موجود بالفعل، لم يتم العثور على ثغرات لتعديلها.")

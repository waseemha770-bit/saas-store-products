import re

# ==========================================================
# 1. بناء دالة التفتيش والقيود في قاعدة البيانات (database.py)
# ==========================================================
with open('database.py', 'r', encoding='utf-8') as f:
    db_code = f.read()

limit_checker = '''
def check_product_limit(store_id):
    """التحقق من تجاوز التاجر للحد الأقصى للمنتجات بناءً على باقته"""
    try:
        user = users_col.find_one({"id": store_id})
        if not user: 
            return False, "حساب المتجر غير موجود."
            
        # استثناء المتجر الرئيسي (المدير) من القيود
        if user.get("store_slug") == "admin-store":
            return True, ""
            
        pkg_name = user.get("package", "أساسية")
        
        # جلب بيانات الباقة من قاعدة البيانات
        try:
            pkg = db.packages.find_one({"name": pkg_name})
        except:
            pkg = None
            
        # معالجة الحد الأقصى (في حال كتب المدير "لامحدود" نصياً بدلاً من رقم)
        max_str = str(pkg.get("max_products", 20)) if pkg else "20"
        try:
            max_prods = int(max_str)
        except ValueError:
            max_prods = 9999999 # رقم لا نهائي في حال الباقة المفتوحة
            
        # حساب العدد الفعلي للمنتجات الحالية في متجر التاجر
        current_count = products_col.count_documents({"store_id": store_id})
        
        if current_count >= max_prods:
            return False, f"عذراً! باقتك الحالية ({pkg_name}) تسمح بإضافة {max_prods} منتج كحد أقصى. يرجى ترقية باقتك لإضافة المزيد."
            
        return True, ""
    except Exception as e:
        print("Package Limit Check Error:", e)
        return True, "" # في حال الخطأ التقني نسمح بالمرور كي لا يتوقف المتجر
'''

if "def check_product_limit(" not in db_code:
    with open('database.py', 'a', encoding='utf-8') as f:
        f.write("\n" + limit_checker + "\n")
    print("✅ تم بناء محرك التفتيش الخاص بالباقات في database.py.")
else:
    print("⚠️ محرك التفتيش موجود مسبقاً.")


# ==========================================================
# 2. تفعيل التفتيش قبل إضافة المنتج في السيرفر (app.py)
# ==========================================================
with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

old_add_logic = '''elif action == 'add_product': database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock')); flash("تم الإضافة", "success")'''

new_restricted_logic = '''elif action == 'add_product':
            # التحقق من باقة التاجر قبل السماح له بإضافة المنتج
            can_add, error_msg = database.check_product_limit(session['user_id'])
            if not can_add:
                flash(error_msg, "danger")
            else:
                database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), (request.form.get('price') or 0), request.form.get('cat'), request.form.get('img'), request.form.get('stock'))
                flash("تم إضافة المنتج بنجاح 📦", "success")'''

if "database.check_product_limit" not in app_code:
    if old_add_logic in app_code:
        app_code = app_code.replace(old_add_logic, new_restricted_logic)
    else:
        # استخدام التعبيرات النمطية في حال تم تغيير المسافات
        app_code = re.sub(r"elif action == 'add_product':.*?flash\([\'\"]تم الإضافة[\'\"],\s*[\'\"]success[\'\"]\)", new_restricted_logic, app_code, flags=re.DOTALL)
        
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(app_code)
    print("✅ تم ربط إضافة المنتجات بنظام الباقات الصارم في app.py.")
else:
    print("⚠️ نظام المنع مربوط مسبقاً.")


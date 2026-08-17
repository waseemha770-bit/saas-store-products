from flask import Flask, render_template, request, redirect, url_for, session, flash
import database

app = Flask(__name__)
app.secret_key = 'tajergo_super_secure_key_2026'

@app.route('/')
def home(): return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug):
    user = database.get_user_by_slug(slug)
    if not user: return "المتجر غير موجود", 404
    settings = database.get_settings(user.get('id'))
    products = database.get_products(user.get('id'))
    return render_template('store.html', user=user, settings=settings, products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = database.authenticate_user(request.form.get('slug'), request.form.get('pass'))
        if user:
            session['user_id'] = user.get('id')
            session['store_slug'] = user.get('store_slug')
            return redirect(url_for('dashboard'))
        flash("بيانات الدخول خاطئة", "danger")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_product':
            database.add_product(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'))
            flash("تم إضافة المنتج بنجاح!", "success")
        elif action == 'save_settings':
            settings_data = {
                'store_name': request.form.get('store_name'), 'store_desc': request.form.get('store_desc'),
                'whatsapp': request.form.get('whatsapp'), 'currency': request.form.get('currency'),
                'btn_text': request.form.get('btn_text'), 'theme_color': request.form.get('theme_color'),
                'font_family': request.form.get('font_family'), 'header_size': request.form.get('header_size')
            }
            database.update_settings(session['user_id'], settings_data)
            flash("تم تحديث المظهر بنجاح!", "success")
        return redirect(url_for('dashboard'))
        
    products = database.get_products(session['user_id'])
    settings = database.get_settings(session['user_id'])
    return render_template('dashboard.html', products=products, settings=settings, store_slug=session['store_slug'])

# صفحة سرية لمدير النظام (أنت) لإضافة تجار جدد
@app.route('/system-admin', methods=['GET', 'POST'])
def system_admin():
    if request.method == 'POST':
        admin_pass = request.form.get('admin_pass')
        if admin_pass != 'waseem2026': return "رقم سري خاطئ", 403
        if database.create_new_merchant(request.form.get('name'), request.form.get('slug'), request.form.get('password')):
            return f"تم إنشاء المتجر بنجاح! يمكن للتاجر الدخول باسم: {request.form.get('slug')}"
        return "خطأ: رابط المتجر مستخدم مسبقاً!"
    return '''<html dir="rtl"><body style="font-family:Arial; padding:40px;">
    <h2>إضافة تاجر جديد للمنصة</h2><form method="POST">
    <input name="admin_pass" type="password" placeholder="الرقم السري للنظام" required><br><br>
    <input name="name" placeholder="اسم التاجر" required><br><br>
    <input name="slug" placeholder="رابط المتجر (انجليزي فقط)" required><br><br>
    <input name="password" placeholder="الرقم السري للتاجر" required><br><br>
    <button type="submit">إنشاء المتجر</button></form></body></html>'''

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect(url_for('login'))

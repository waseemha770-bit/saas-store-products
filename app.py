from flask import Flask, render_template, request, redirect, url_for, session, flash
import google_sheets

app = Flask(__name__)
app.secret_key = 'tajergo_secure_key_2026'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/store/<slug>')
def view_store(slug):
    db = google_sheets.get_all_data()
    user = next((u for u in db['users'] if u.get('store_slug') == slug and u.get('active') == 'TRUE'), None)
    if not user: return "المتجر غير موجود أو غير مفعل", 404
    
    # الحل الآمن هنا: استخدام get() بدلاً من الأقواس المربعة
    settings = next((s for s in db.get('settings', []) if s.get('u_id') == user.get('id')), {
        'c1': user.get('username'), 
        'c2': 'مرحباً بكم في متجري'
    })
    
    products = [{'name': p.get('c1'), 'price': p.get('c3'), 'description': p.get('c2'), 'category': p.get('c4'), 'image_url': p.get('c5')} for p in db.get('products', []) if p.get('u_id') == user.get('id')]
    
    return render_template('store.html', user=user, settings=settings, products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = google_sheets.get_all_data()
        # تأمين تسجيل الدخول أيضاً
        user = next((u for u in db['users'] if u.get('store_slug') == request.form.get('slug') and u.get('password') == request.form.get('pass')), None)
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
        success = google_sheets.add_product_to_sheet(session['user_id'], request.form.get('name'), request.form.get('desc'), request.form.get('price'), request.form.get('cat'), request.form.get('img'))
        if success:
            flash("تم إضافة المنتج بنجاح", "success")
        else:
            flash("حدث خطأ في الاتصال بقاعدة البيانات", "danger")
        return redirect(url_for('dashboard'))
        
    products = [p for p in google_sheets.get_all_data().get('products', []) if p.get('u_id') == session['user_id']]
    return render_template('dashboard.html', products=products, store_slug=session['store_slug'])

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

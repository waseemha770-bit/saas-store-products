from flask import Flask, render_template, abort, request, redirect, url_for, session, flash
from google_sheets import get_store_settings, get_store_products, get_all_data

app = Flask(__name__)
app.secret_key = 'tajergo_super_secret_key_2026'

# ==========================================
# 1. الصفحات العامة (الرئيسية والمصادقة)
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        db = get_all_data()
        # محاكاة تسجيل الدخول البسيط (مقارنة الاسم فقط في نسخة العرض)
        user = next((u for u in db['users'] if u.get('username') == username and u.get('active') == 'TRUE'), None)
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash("بيانات الدخول غير صحيحة أو الحساب غير مفعل.", "danger")
            
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# ==========================================
# 2. واجهة المتجر العام (Multi-Tenant)
# ==========================================
@app.route('/store/<store_slug>')
def view_store(store_slug):
    store_data = get_store_settings(store_slug)
    if not store_data:
        abort(404, description="عذراً، هذا المتجر غير موجود أو غير مفعل حالياً.")
    
    products = get_store_products(store_data['user']['id'])
    return render_template('store/store.html', store=store_data['settings'], user=store_data['user'], products=products)

# ==========================================
# 3. لوحة التحكم (التاجر)
# ==========================================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    products = get_store_products(user_id)
    return render_template('dashboard/dashboard.html', username=session['username'], products=products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# ⚠️ هام لـ Vercel: المتغير app موجود ومتاح

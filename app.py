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
    user = next((u for u in db['users'] if u['store_slug'] == slug and u['active'] == 'TRUE'), None)
    if not user: return "المتجر غير موجود", 404
    
    settings = next((s for s in db['settings'] if s['u_id'] == user['id']), {
        'store_name': user['username'], 
        'store_description': 'مرحباً بكم في متجري',
        'store_phone': '', 'currency': 'ريال', 'primary_color': '#0d6efd', 'store_logo': ''
    })
    products = [{'name': p['c1'], 'price': p['c3'], 'description': p['c2'], 'category': p['c4'], 'image_url': p['c5']} for p in db['products'] if p['u_id'] == user['id']]
    
    store_data = {'user': user, 'settings': settings}
    return render_template('store.html', store=store_data, products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = google_sheets.get_all_data()
        user = next((u for u in db['users'] if u['store_slug'] == request.form['slug'] and u['password'] == request.form['pass']), None)
        if user:
            session['user_id'] = user['id']
            session['store_slug'] = user['store_slug']
            return redirect(url_for('dashboard'))
        flash("بيانات الدخول خاطئة", "danger")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        google_sheets.add_product_to_sheet(session['user_id'], request.form['name'], request.form['desc'], request.form['price'], request.form['cat'], request.form['img'])
        flash("تم إضافة المنتج بنجاح", "success")
        return redirect(url_for('dashboard'))
    products = [p for p in google_sheets.get_all_data()['products'] if p['u_id'] == session['user_id']]
    return render_template('dashboard.html', products=products, store_slug=session['store_slug'])

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import google_sheets

app = Flask(__name__)

@app.route('/')
def index():
    return "مرحباً بك في منصة TajerGo. للوصول لمتجرك أضف /store/store-slug للرابط."

@app.route('/store/<store_slug>')
def view_store(store_slug):
    store_data = google_sheets.get_store_settings(store_slug)
    if not store_data:
        return "المتجر غير موجود أو غير مفعل حالياً.", 404
    
    user_id = store_data['user']['id']
    products = google_sheets.get_store_products(user_id)
    
    return render_template('store.html', store=store_data, products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        store_slug = request.form.get('store_slug')
        return redirect(url_for('view_store', store_slug=store_slug))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

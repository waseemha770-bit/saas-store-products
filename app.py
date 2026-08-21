from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response, abort, send_file
import os, json, time, re
from datetime import datetime, timedelta
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'saas_super_secret_key_2026'

# --- إعداد قاعدة البيانات (MongoDB Dummy/Local for Termux/Vercel) ---
class DummyDB:
    def __init__(self):
        self.products = self
        self.users = self
        self.store_stats = self
        self.visit_logs = self
    def find(self, *args, **kwargs): return []
    def find_one(self, *args, **kwargs): return None
    def insert_one(self, *args, **kwargs): pass
    def update_one(self, *args, **kwargs): pass
    def delete_one(self, *args, **kwargs): pass
    def count_documents(self, *args, **kwargs): return 0

class Database:
    def __init__(self):
        self.db = DummyDB()
database = Database()

# --- مسارات الـ PWA ---
@app.route('/manifest.json')
def serve_manifest():
    if os.path.exists('static/manifest.json'):
        return send_file('static/manifest.json', mimetype='application/json')
    return jsonify({"error": "not found"}), 404

@app.route('/sw.js')
def serve_sw():
    if os.path.exists('static/sw.js'):
        return send_file('static/sw.js', mimetype='application/javascript')
    return jsonify({"error": "not found"}), 404

# --- نظام الإحصائيات (تتبع الزيارات) ---
@app.before_request
def track_store_views():
    if request.method == 'GET' and not request.path.startswith(('/api', '/static', '/dashboard', '/login', '/logout', '/manifest', '/sw.js')):
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            month = datetime.now().strftime('%Y-%m')
            database.db.store_stats.update_one(
                {"_id": "views_tracker"},
                {"$inc": {"total": 1, f"daily.{today}": 1, f"monthly.{month}": 1}},
                upsert=True
            )
        except: pass

@app.context_processor
def inject_dashboard_stats():
    if request.path.startswith('/dashboard') or request.path.startswith('/admin'):
        try:
            stats = database.db.store_stats.find_one({"_id": "views_tracker"}) or {}
            today = datetime.now().strftime('%Y-%m-%d')
            month = datetime.now().strftime('%Y-%m')
            
            daily = stats.get('daily', {}).get(today, 0)
            monthly = stats.get('monthly', {}).get(month, 0)
            total = stats.get('total', 0)
            weekly = sum(stats.get('daily', {}).get((datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'), 0) for i in range(7))
            
            return dict(v_daily=daily, v_weekly=weekly, v_monthly=monthly, v_total=total)
        except Exception:
            return dict(v_daily=0, v_weekly=0, v_monthly=0, v_total=0)
    return {}

# --- مسارات المتجر الأساسية ---
@app.route('/')
@app.route('/store/<store_name>')
def store_front(store_name=None):
    try:
        products = list(database.db.products.find())
        return render_template('store.html', products=products)
    except Exception as e:
        return f"Error loading store: {str(e)}"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html') # Fallback if login.html is missing

@app.route('/logout')
def logout():
    return redirect(url_for('store_front'))

# --- نظام التقييم الآمن ---
@app.route('/api/rate_product', methods=['POST'])
def api_rate_product_ultimate():
    try:
        from flask import make_response
        data = request.get_json() if request.is_json else request.form
        pid = data.get('product_id') or data.get('id')
        rating_val = float(data.get('rating', 0))
        
        if request.cookies.get(f'rated_{pid}'):
            return jsonify({"success": False, "error": "already_rated"})
            
        user_ip = request.headers.get('x-real-ip', request.headers.get('X-Forwarded-For', request.remote_addr))
        if user_ip and ',' in user_ip: user_ip = user_ip.split(',')[0].strip()
            
        if not pid or rating_val < 1:
            return jsonify({"success": False, "error": "بيانات غير مكتملة"})
            
        try: query = {"_id": ObjectId(pid)}
        except: query = {"id": str(pid)}
        
        prod = database.db.products.find_one(query)
        if not prod:
            query = {"id": int(pid)} if str(pid).isdigit() else {"name": pid}
            prod = database.db.products.find_one(query)
            
        if prod:
            rated_ips = prod.get('rated_ips', [])
            if user_ip in rated_ips:
                return jsonify({"success": False, "error": "already_rated"})
                
            curr_rating = float(prod.get('rating', 0))
            curr_reviews = int(prod.get('reviews', 0))
            
            new_reviews = curr_reviews + 1
            new_rating = round(((curr_rating * curr_reviews) + rating_val) / new_reviews, 1)
            
            database.db.products.update_one(query, {
                "$set": {"rating": new_rating, "reviews": new_reviews},
                "$addToSet": {"rated_ips": user_ip}
            })
            
            resp = make_response(jsonify({"success": True, "new_rating": new_rating, "new_reviews": new_reviews}))
            resp.set_cookie(f'rated_{pid}', '1', max_age=31536000)
            return resp
            
        return jsonify({"success": False, "error": "المنتج غير موجود"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.1', port=5000)

import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# استبدال خلية المنتجات المعطوبة بالخلية المستقرة الصحيحة التي تقرأ o.cart_items
stable_products_cell = '''<!-- 3. المنتجات -->
                    <td class="text-start">
                        <div class="small" style="max-height: 100px; overflow-y: auto; line-height: 1.6;">
                            {% if o.cart_items %}
                                {% for i in o.cart_items %}
                                    <div class="text-dark fw-bold">▪️ {{ i.name }} <span class="badge bg-light text-secondary border px-1" style="font-size: 0.72rem;">x{{ i.qty }}</span></div>
                                {% endfor %}
                            {% elif o.items %}
                                <div class="text-dark fw-bold">{{ o.items }}</div>
                            {% else %}
                                <span class="text-muted small">-</span>
                            {% endif %}
                        </div>
                    </td>'''

# استبدال الخلية داخل الجدول
html = re.sub(r'<!-- 3\. المنتجات -->[\s\S]*?</td>', stable_products_cell, html, count=1)

# تنظيف أي أثر لكلمة o.items المسببة للتضارب إن وجدت
html = html.replace('o.items', "o.get('cart_items', [])")

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ تم إعادة ربط المنتجات بمفتاحها الصحيح o.cart_items بنجاح.")

import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# الهيكل المتكامل لجدول الطلبات مع مطابقة تامة لكل عمود (8 أعمدة متناسقة)
complete_orders_table = '''
<div class="table-responsive bg-white rounded-4 shadow-sm border p-2">
    <table class="table table-hover align-middle mb-0 text-nowrap">
        <thead class="table-light">
            <tr class="text-secondary small fw-bold">
                <th class="py-3 px-3">رقم الطلب</th>
                <th class="py-3">العميل والتواصل</th>
                <th class="py-3">المنتجات</th>
                <th class="py-3">طريقة الدفع</th>
                <th class="py-3">الإجمالي</th>
                <th class="py-3">الحالة</th>
                <th class="py-3 text-primary"><i class="fas fa-motorcycle me-1"></i> المندوب المسؤول</th>
                <th class="py-3 text-center px-3">الإجراءات</th>
            </tr>
        </thead>
        <tbody>
            {% if orders %}
                {% for o in orders %}
                <tr>
                    <!-- 1. رقم الطلب والتاريخ -->
                    <td class="px-3">
                        <span class="fw-bold text-dark d-block">{{ o.order_id }}</span>
                        <small class="text-muted" style="font-size: 0.75rem;">{{ o.created_at if o.created_at else '' }}</small>
                    </td>

                    <!-- 2. العميل والتواصل -->
                    <td>
                        <div class="fw-bold text-dark">{{ o.customer_name }}</div>
                        <a href="tel:{{ o.customer_phone }}" class="text-decoration-none text-muted small d-block">
                            <i class="fas fa-phone-alt text-success me-1"></i>{{ o.customer_phone }}
                        </a>
                        {% if o.customer_address %}
                        <small class="text-muted d-block text-truncate" style="max-width: 180px;">
                            <i class="fas fa-map-marker-alt text-danger me-1"></i>{{ o.customer_address }}
                        </small>
                        {% endif %}
                    </td>

                    <!-- 3. المنتجات -->
                    <td>
                        <div class="small text-muted" style="max-height: 80px; overflow-y: auto;">
                            {% if o.cart %}
                                {% for it in o.cart %}
                                    <div>• {{ it.name }} <span class="badge bg-light text-dark">x{{ it.qty or 1 }}</span></div>
                                {% endfor %}
                            {% else %}
                                <span>{{ o.items if o.items else '-' }}</span>
                            {% endif %}
                        </div>
                    </td>

                    <!-- 4. طريقة الدفع -->
                    <td>
                        <span class="badge bg-light text-secondary border px-2 py-1 small">
                            {{ o.payment_method if o.payment_method else (o.payment if o.payment else 'كاش') }}
                        </span>
                    </td>

                    <!-- 5. الإجمالي -->
                    <td>
                        <span class="fw-bold text-success">{{ o.total }}</span>
                    </td>

                    <!-- 6. حالة الطلب -->
                    <td>
                        <span class="badge {% if 'تم التوصيل' in o.status or 'مدفوع' in o.status %}bg-success{% elif 'مع المندوب' in o.status %}bg-primary{% else %}bg-warning text-dark{% endif %} px-2 py-1 rounded-pill small">
                            {{ o.status }}
                        </span>
                    </td>

                    <!-- 7. المندوب المسؤول (العمود الجديد) -->
                    <td>
                        <select class="form-select form-select-sm rounded-pill border-primary border-opacity-50 shadow-sm fw-bold" 
                                style="min-width: 150px; font-size: 0.8rem;" 
                                onchange="assignOrderToDriver('{{ o.order_id }}', this)">
                            <option value="">{% if o.driver_name %}🛵 {{ o.driver_name }}{% else %}-- تعيين مندوب --{% endif %}</option>
                            {% if drivers %}
                                {% for d in drivers %}
                                <option value="{{ d.phone }}" data-name="{{ d.name }}" data-phone="{{ d.phone }}" {% if o.driver_phone == d.phone %}selected{% endif %}>
                                    🛵 {{ d.name }}
                                </option>
                                {% endfor %}
                            {% else %}
                                <option disabled>(أضف مناديب أولاً)</option>
                            {% endif %}
                        </select>
                    </td>

                    <!-- 8. الإجراءات -->
                    <td class="text-center px-3">
                        <div class="d-flex justify-content-center gap-1">
                            <a href="/track/{{ o.order_id }}" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill px-2" title="تتبع الطلب">
                                <i class="fas fa-truck-fast"></i>
                            </a>
                            <a href="https://wa.me/{{ o.customer_phone }}" target="_blank" class="btn btn-sm btn-outline-success rounded-pill px-2" title="مراسلة العميل">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </td>
                </tr>
                {% endfor %}
            {% else %}
                <tr>
                    <td colspan="8" class="text-center py-5 text-muted">
                        <i class="fas fa-box-open fs-1 mb-2 opacity-50 d-block"></i>
                        لا توجد طلبات مسجلة حتى الآن
                    </td>
                </tr>
            {% endif %}
        </tbody>
    </table>
</div>
'''

# استبدال جدول الطلبات القديم بالجدول المنظم
table_regex = r'<div class="table-responsive[\s\S]*?</table>\s*</div>|<table class="table[\s\S]*?</table>'

if re.search(table_regex, html):
    html = re.sub(table_regex, complete_orders_table, html, count=1)
    print("✅ تم استبدال جدول الطلبات بالهيكل المرتب.")
else:
    print("⚠️ لم يتم العثور على الوسم القديم بنمط regex، جاري إدراجه بدقة.")

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

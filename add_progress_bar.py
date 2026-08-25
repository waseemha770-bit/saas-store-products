import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

progress_script = """
<!-- بداية شريط تقدم الباقة -->
{% if not is_super_admin %}
<script>
document.addEventListener("DOMContentLoaded", function() {
    // حماية ضد التكرار إذا تم التحميل مرتين
    if(document.getElementById('tajergo-progress-bar')) return;

    let currentProducts = {{ products | length if products else 0 }};
    let pkgName = `{{ current_user_data.get('package', 'أساسية') if current_user_data else 'أساسية' }}`;
    
    // نقل بيانات الباقات من الباك إند إلى الجافاسكريبت بأمان تام
    let packagesList = [];
    {% for p in packages %}
        packagesList.push({
            name: `{{ p.name|default('') }}`,
            max_products: `{{ p.max_products|default('') }}`,
            pkg_max: `{{ p.pkg_max|default('') }}`
        });
    {% endfor %}
    
    let maxLimit = 20;
    let targetPkg = packagesList.find(p => p.name === pkgName);
    if(targetPkg) {
        let rawVal = targetPkg.max_products || targetPkg.pkg_max || 20;
        let parsed = parseInt(String(rawVal).replace(/\\D/g, ''));
        maxLimit = isNaN(parsed) ? 999999 : parsed;
    }
    
    let isUnlimited = (maxLimit >= 100000);
    let percent = isUnlimited ? 100 : Math.min((currentProducts / maxLimit) * 100, 100);
    let barColor = percent >= 100 ? 'bg-danger' : (percent >= 80 ? 'bg-warning' : 'bg-success');
    let txtColor = percent >= 100 ? 'text-danger' : 'text-success';
    let displayLimit = isUnlimited ? '<i class="fas fa-infinity fs-6"></i>' : maxLimit;
    
    let progressHtml = `
    <div id="tajergo-progress-bar" class="card border-0 shadow-sm mb-4" style="border-radius: 16px; background: #fff;">
        <div class="card-body p-3 p-md-4">
            <div class="d-flex justify-content-between align-items-center mb-2">
                <div class="d-flex align-items-center gap-3">
                    <div class="bg-primary bg-opacity-10 text-primary p-2 rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px;">
                        <i class="fas fa-box-open fs-4"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1 text-dark">استهلاك باقة المتجر</h6>
                        <small class="text-muted fw-bold">باقتك الحالية: <span class="badge bg-light text-dark border px-2 shadow-sm">${pkgName}</span></small>
                    </div>
                </div>
                <div class="text-end">
                    <h3 class="fw-bold mb-0 ${txtColor}" dir="ltr" style="letter-spacing: 1px;">
                        ${currentProducts} <span class="text-muted fs-5">/ ${displayLimit}</span>
                    </h3>
                </div>
            </div>
            
            ${!isUnlimited ? `
            <div class="progress mt-3" style="height: 10px; border-radius: 50rem; background-color: #f1f3f5;">
                <div class="progress-bar ${barColor} progress-bar-striped progress-bar-animated" role="progressbar" style="width: ${percent}%; border-radius: 50rem;"></div>
            </div>
            <div class="d-flex justify-content-between mt-2 px-1">
                <small class="text-muted fw-bold" style="font-size: 0.75rem;">إجمالي المنتجات المضافة</small>
                <small class="fw-bold ${txtColor}" style="font-size: 0.75rem;">%${Math.round(percent)} مستهلك</small>
            </div>
            ` : `
            <div class="alert alert-success border-0 bg-success bg-opacity-10 py-2 mt-3 mb-0 text-center rounded-3 fw-bold">
                <i class="fas fa-check-circle me-1"></i> باقتك لا محدودة، يمكنك إضافة المنتجات بحرية تامة!
            </div>
            `}
        </div>
    </div>
    `;
    
    // زرع الشريط في تبويب المنتجات (الأفضل) أو تبويب الإحصائيات 
    let productsTab = document.getElementById('v-pills-products') || document.getElementById('products');
    let dashboardTab = document.getElementById('v-pills-dashboard') || document.getElementById('dashboard');
    
    if (productsTab) {
        productsTab.insertAdjacentHTML('afterbegin', progressHtml);
    } else if (dashboardTab) {
        dashboardTab.insertAdjacentHTML('afterbegin', progressHtml);
    } else {
        let topContainer = document.querySelector('.container') || document.querySelector('.container-fluid');
        if(topContainer) topContainer.insertAdjacentHTML('afterbegin', progressHtml);
    }
});
</script>
{% endif %}
<!-- نهاية شريط تقدم الباقة -->
"""

if "tajergo-progress-bar" not in html:
    html = html.replace('</body>', progress_script + '\n</body>')
    with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ تم زراعة شريط استهلاك الباقة المرئي بنجاح.")
else:
    print("⚠️ الشريط مزروع مسبقاً في القالب.")

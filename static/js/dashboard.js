// TajerGo Dashboard JavaScript
(function () {
    'use strict';

    window.fixImg = function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };

    window.copyDriverPortalLink = function (token) {
        const input = document.getElementById('link-' + token);
        if (!input) return;
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(input.value).then(
                () => alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة'),
                () => fallbackCopy(input)
            );
        } else {
            fallbackCopy(input);
        }
    };

    function fallbackCopy(input) {
        input.select();
        document.execCommand('copy');
        alert('✅ تم نسخ رابط بوابة المندوب إلى الحافظة');
    }

    window.submitNewDriver = function (event) {
        event.preventDefault();
        const name = (document.getElementById('driverNameInput')?.value || '').trim();
        const phone = (document.getElementById('driverPhoneInput')?.value || '').trim();
        if (!name || !phone) {
            alert('يرجى إدخال اسم ورقم المندوب');
            return false;
        }

        fetch('/api/drivers/add', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name, phone})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إضافة المندوب بنجاح وتوليد بوابته الخاصة');
                window.location.reload();
            } else {
                alert('حدث خطأ: ' + (data.error || 'تعذر الإضافة'));
            }
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
        return false;
    };

    window.deleteDriver = function (token) {
        if (!confirm('هل أنت متأكد من حذف هذا المندوب؟')) return;
        fetch('/api/drivers/delete/' + encodeURIComponent(token), {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                if (data.success) window.location.reload();
                else alert(data.error || 'تعذر حذف المندوب');
            })
            .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.updateOrderStatus = function (orderId, newStatus) {
        fetch('/api/orders/update-status', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({order_id: orderId, status: newStatus})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) window.location.reload();
            else alert(data.error || 'تعذر تحديث الحالة');
        })
        .catch(() => alert('فشل الاتصال بالخادم'));
    };

    window.assignOrderToDriver = function (orderId, selectEl) {
        const selectedOption = selectEl?.options[selectEl.selectedIndex];
        const driverName = selectedOption?.getAttribute('data-name');
        const driverPhone = selectedOption?.getAttribute('data-phone');
        if (!driverPhone) return;

        selectEl.disabled = true;
        fetch('/api/orders/assign-driver', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                order_id: orderId,
                driver_name: driverName,
                driver_phone: driverPhone
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('✅ تم إسناد الطلب (' + orderId + ') للمندوب: ' + driverName);
                window.location.reload();
            } else {
                alert(data.error || 'حدث خطأ أثناء الإسناد');
                selectEl.disabled = false;
            }
        })
        .catch(() => {
            alert('فشل الاتصال بالخادم');
            selectEl.disabled = false;
        });
    };

    document.addEventListener('DOMContentLoaded', function () {
        const activeTab = localStorage.getItem('tajergo_active_tab');
        if (activeTab) {
            const tabBtn = document.querySelector(`button[data-bs-target="${CSS.escape(activeTab)}"]`);
            if (tabBtn && window.bootstrap) {
                bootstrap.Tab.getOrCreateInstance(tabBtn).show();
            }
        }

        document.querySelectorAll('button[data-bs-toggle="tab"]').forEach(function (tabElm) {
            tabElm.addEventListener('shown.bs.tab', function (event) {
                const currentTarget = event.target.getAttribute('data-bs-target');
                if (currentTarget) localStorage.setItem('tajergo_active_tab', currentTarget);
            });
        });
    });
})();

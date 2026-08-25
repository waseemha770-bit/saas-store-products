import re

with open('templates/store.html', 'r', encoding='utf-8') as f:
    html = f.read()

# تصميم تذييل مدمج وأنيق للغاية (Minimalist Compact Footer)
compact_footer = '''<!-- التذييل المدمج والمحدث -->
<footer class="bg-white border-top text-center py-2 mt-3 shadow-sm" style="font-size: 0.85rem;">
    <div class="container d-flex flex-column flex-sm-row justify-content-between align-items-center py-1 gap-2">
        <div class="d-flex align-items-center gap-2">
            {% if settings.get('logo_url') %}
                <img src="{{ settings.logo_url }}" onerror="fixImg(this)" width="24" height="24" style="object-fit: cover; border-radius: 50%;">
            {% endif %}
            <span class="fw-bold text-dark">{{ settings.get('store_name', '') }}</span>
        </div>
        
        <!-- روابط التواصل بشكل مدمج وصغير -->
        <div class="d-flex align-items-center gap-3 fs-5">
            {% if settings.get('whatsapp') %}
                <a href="https://wa.me/{{ settings.whatsapp }}" target="_blank" class="text-success"><i class="fab fa-whatsapp"></i></a>
            {% endif %}
            {% if settings.get('facebook') %}
                <a href="{{ settings.facebook }}" target="_blank" class="text-primary"><i class="fab fa-facebook"></i></a>
            {% endif %}
            {% if settings.get('instagram') %}
                <a href="{{ settings.instagram }}" target="_blank" class="text-danger"><i class="fab fa-instagram"></i></a>
            {% endif %}
            {% if settings.get('tiktok') %}
                <a href="{{ settings.tiktok }}" target="_blank" class="text-dark"><i class="fab fa-tiktok"></i></a>
            {% endif %}
            {% if settings.get('telegram') %}
                <a href="https://t.me/{{ settings.telegram }}" target="_blank" class="text-info"><i class="fab fa-telegram"></i></a>
            {% endif %}
        </div>
    </div>
</footer>
'''

# 1. استبدال وسم <footer> القديم بالكامل
if '<footer' in html and '</footer>' in html:
    html = re.sub(r'<footer[\s\S]*?</footer>', compact_footer, html, count=1)
else:
    # في حال لم يكن موسوماً بـ <footer>، نضعه قبل نهاية الـ body
    html = html.replace('</body>', compact_footer + '\n</body>')

# 2. تقليص أي فراغات سفلية ضخمة وهمية (spacer divs) إن وُجدت
html = re.sub(r'style="height:\s*(?:100|120|150|200)px;?"', 'style="height: 40px;"', html)

with open('templates/store.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ تم تحويل التذييل إلى تصميم مضغوط وأنيق بنجاح.")

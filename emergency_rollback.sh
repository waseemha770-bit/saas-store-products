#!/bin/bash
echo "⏳ جاري البحث عن آخر نقطة استقرار في النظام..."

# البحث عن رقم الكوميت (Commit Hash) للنقطة التي كانت تعمل بكفاءة
STABLE_COMMIT=$(git log --grep="Fix: Handled InvalidId exception" --format="%H" -n 1)

if [ -z "$STABLE_COMMIT" ]; then
    echo "⚠️ لم أجد النقطة الأولى، جاري البحث عن نقطة بديلة..."
    STABLE_COMMIT=$(git log --grep="Super Admin UI" --format="%H" -n 1)
fi

if [ -n "$STABLE_COMMIT" ]; then
    echo "✅ تم العثور على النقطة المستقرة! جاري استعادة الملفات..."
    
    # استعادة الملفات المتضررة فقط إلى حالتها السليمة
    git checkout $STABLE_COMMIT -- templates/dashboard.html templates/store.html app.py database.py
    
    # رفع الملفات السليمة للسيرفر
    git commit -m "Emergency Rollback: Restored all UI files to the last completely stable state"
    git push -u origin main --force
    
    echo "🚀 تمت عملية الإنقاذ بنجاح! تم رفع الملفات السليمة."
else
    echo "❌ لم يتم العثور على نقطة استعادة. يرجى إخباري بذلك!"
fi

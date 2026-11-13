

# تحليل البيانات وتقييم النماذج لاكتشاف هجمات 

يوفر هذا المشروع سكريبتات وبيانات لتحليل واختبار خوارزميات تعلم الآلة في كشف هجمات الحرمان من الخدمة (DDoS).

---

## هيكل المشروع

```
ddos-detection/
├── data/
│   └── selected.csv         # ملف البيانات الرئيسي (الخصائص + التصنيفات)
├── results/
│   └── plots/               # مجلد الصور والنتائج
├── src/
│   └── generate_all_plots.py # السكريبت الرئيسي للتحليل والرسم
├── README.md                # ملف التوثيق
```

---

## المتطلبات

- Python 3.8 أو أحدث
- pandas
- matplotlib
- seaborn
- scikit-learn

لتثبيت المتطلبات:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

---

## طريقة الاستخدام

1. **جهز بياناتك:**  
   ضع ملف البيانات `selected.csv` في مجلد `data/`، ويجب أن يحتوي على أعمدة رقمية وعمود باسم `label` (مثلاً: normal, attack).

2. **تشغيل السكريبت:**  
   من مجلد المشروع الرئيسي، شغّل:
   ```bash
   python src/generate_all_plots.py
   ```

3. **عرض النتائج:**  
   ستجد جميع الرسومات البيانية الناتجة في المجلد `results/plots/`.

---

## تنسيق البيانات

مثال على شكل البيانات في ملف `selected.csv`:

| feature1 | feature2 | ... | label   |
|----------|----------|-----|---------|
|   5.1    |   3.5    | ... | normal  |
|   7.0    |   3.2    | ... | attack  |

- يجب أن تكون جميع الخصائص (features) رقمية.
- عمود `label` يحتوي على التصنيفات (normal أو attack).

---

## النتائج

- `results/plots/class_distribution.png` : توزيع الفئات في البيانات
- `results/plots/confusion_matrix_randomforest.png` : مصفوفة الالتباس لنموذج الغابة العشوائية
- `results/plots/confusion_matrix_knn.png` : مصفوفة الالتباس لنموذج KNN
- `results/plots/confusion_matrix_svm.png` : مصفوفة الالتباس لنموذج SVM
- `results/plots/roc_curve_randomforest.png` : منحنى ROC للغابة العشوائية
- `results/plots/roc_curve_knn.png` : منحنى ROC لـ KNN
- `results/plots/roc_curve_svm.png` : منحنى ROC لـ SVM
- `results/plots/models_accuracy.png` : مقارنة دقة النماذج

---

## نصائح

- للحصول على نتائج دقيقة، استخدم على الأقل 10 عينات لكل فئة.
- إذا كانت البيانات قليلة جدًا، سيظهر لك تحذير ولن يتم إجراء جميع التحليلات.

---

## الرخصة

هذا المشروع للأغراض التعليمية فقط. لا توجد أي ضمانات.

---

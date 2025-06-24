# DDoS Detection Data Analysis & Model Evaluation

This project provides scripts and datasets for analyzing features and evaluating machine learning models for DDoS (Distributed Denial of Service) attack detection.

---

## Project Structure

```
ddos-detection/
├── data/
│   └── selected.csv         # Main dataset (features + labels)
├── results/
│   └── plots/               # Generated result plots
├── src/
│   └── generate_all_plots.py # Main script for analysis and plotting
├── README.md                # Project documentation
```

---

## Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn
- scikit-learn

Install requirements with:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

---

## Usage

1. **Prepare your data:**  
   Place your data file `selected.csv` in the `data/` directory.  
   The file should have numeric feature columns and a `label` column (e.g., `normal`, `attack`).

2. **Run the analysis script:**  
   From the project root, run:
   ```bash
   python src/generate_all_plots.py
   ```

3. **Check Results:**  
   All generated plots (class distribution, confusion matrices, ROC curves, model comparison) will be saved in `results/plots/`.

---

## Data Format

Your `data/selected.csv` should look like:

| feature1 | feature2 | ... | label   |
|----------|----------|-----|---------|
|   5.1    |   3.5    | ... | normal  |
|   7.0    |   3.2    | ... | attack  |

- All features should be numeric.
- The `label` column should contain class names (e.g., `normal`, `attack`).

---

## Output

- `results/plots/class_distribution.png`  
- `results/plots/confusion_matrix_randomforest.png`  
- `results/plots/confusion_matrix_knn.png`  
- `results/plots/confusion_matrix_svm.png`  
- `results/plots/roc_curve_randomforest.png`  
- `results/plots/roc_curve_knn.png`  
- `results/plots/roc_curve_svm.png`  
- `results/plots/models_accuracy.png`  

---

## Tips

- For meaningful results, use at least 10 samples per class.
- If your data is too small, the script will warn you and not run all analyses.

---

## License

This project is for educational purposes. No warranty is provided.

---

# تحليل البيانات وتقييم النماذج لاكتشاف هجمات الحرمان من الخدمة

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
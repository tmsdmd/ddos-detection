import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. تحميل بيانات التدريب والاختبار من الملف السابق
with open("split_data.pkl", "rb") as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC()
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n{name} Model:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    results[name] = {
        "y_pred": y_pred,
        "accuracy": accuracy_score(y_test, y_pred),
        "report": classification_report(y_test, y_pred, output_dict=True)
    }

# 2. حفظ النتائج للرسوم البيانية
with open("results.pkl", "wb") as f:
    pickle.dump(results, f)
print("✅ تم حفظ results.pkl.")
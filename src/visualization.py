import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# 1. تحميل البيانات المختارة وتقرير النتائج
df = pd.read_csv("selected.csv")
with open("results.pkl", "rb") as f:
    results = pickle.load(f)

# 2. رسم توزيع التصنيفات
plt.figure(figsize=(5,3))
sns.countplot(x=df['Label'])
plt.title("Distribution of Attacks vs Normal Traffic")
plt.show()

# 3. رسم مقارنة الدقة بين النماذج
model_names = list(results.keys())
accuracies = [results[name]['accuracy'] for name in model_names]

plt.figure(figsize=(6,4))
sns.barplot(x=model_names, y=accuracies, palette='viridis')
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.show()
print("✅ تم عرض الرسوم البيانية.")
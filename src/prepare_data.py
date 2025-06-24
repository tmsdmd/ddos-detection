import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

# 1. تحميل البيانات المختارة من الخطوة السابقة
df = pd.read_csv("selected.csv").dropna()

# 2. التشفير والتقسيم
df['Label'] = LabelEncoder().fit_transform(df['Label'])
X = df.drop('Label', axis=1)
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. حفظ البيانات المقسمة لاستخدامها لاحقًا
with open("split_data.pkl", "wb") as f:
    pickle.dump((X_train, X_test, y_train, y_test), f)
print("✅ تم حفظ split_data.pkl.")
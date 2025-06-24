import pandas as pd

features = [
    'Flow Duration', 'Total Fwd Packet', 'Total Bwd packets',
    'Fwd Packet Length Mean', 'Bwd Packet Length Mean',
    'Flow Bytes/s', 'Flow Packets/s', 'Packet Length Mean',
    'Average Packet Size', 'Idle Mean', 'Label'
]

# 1. تحميل البيانات الأصلية
df = pd.read_csv("ACI-IoT-2023.csv")

# 2. حفظ الأعمدة المختارة فقط في ملف جديد
df[features].to_csv("selected.csv", index=False)
print("✅ تم حفظ selected.csv بالميزات المختارة.")
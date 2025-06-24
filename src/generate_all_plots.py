import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    roc_curve,
    auc
)

# Prepare and save the plots directory
plots_dir = "results/plots"
os.makedirs(plots_dir, exist_ok=True)

# Load and check the data
df = pd.read_csv("data/selected.csv")

# Show class distribution and size for debugging
print("Class distribution:")
print(df['label'].value_counts())
print("Dataset shape:", df.shape)

# Plot class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=df)
plt.title("Class Distribution in the Data")
plt.xlabel("Class")
plt.ylabel("Number of Samples")
plt.savefig(f"{plots_dir}/class_distribution.png", dpi=200, bbox_inches='tight')
plt.close()
print("Class distribution plot saved.")

# Prepare data for training
X = df.drop('label', axis=1)
y = df['label']
le = LabelEncoder()
y = le.fit_transform(y)

# Make sure we have at least two samples per class for splitting
if len(df) < 6 or min(df['label'].value_counts()) < 2:
    print("Not enough data per class to split for train/test and generate all plots.")
    exit()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Train/test split done.")

# Models to use
models = {
    "RandomForest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(probability=True, random_state=42)
}

accuracies = []
for name, model in models.items():
    print(f"Training and evaluating: {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f"Confusion Matrix - {name}")
    plt.savefig(f"{plots_dir}/confusion_matrix_{name.lower()}.png", dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Confusion matrix for {name} saved.")

    # ROC Curve
    try:
        if hasattr(model, "predict_proba"):
            y_score = model.predict_proba(X_test)[:,1]
        else:
            y_score = model.decision_function(X_test)
            if len(le.classes_) == 2:
                y_score = (y_score - y_score.min()) / (y_score.max() - y_score.min())
        fpr, tpr, _ = roc_curve(y_test, y_score)
        roc_auc = auc(fpr, tpr)
        plt.figure(figsize=(6, 4))
        plt.plot(fpr, tpr, color='darkorange', label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve - {name}')
        plt.legend(loc="lower right")
        plt.savefig(f"{plots_dir}/roc_curve_{name.lower()}.png", dpi=200, bbox_inches='tight')
        plt.close()
        print(f"ROC curve for {name} saved.")
    except Exception as e:
        print(f"Could not plot ROC curve for {name}: {e}")

# Plot model accuracy comparison
plt.figure(figsize=(6, 4))
sns.barplot(x=list(models.keys()), y=accuracies)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0.8, 1)
plt.savefig(f"{plots_dir}/models_accuracy.png", dpi=200, bbox_inches='tight')
plt.close()
print("Model accuracy comparison plot saved.")

print(f"All plots have been automatically generated in the directory: {plots_dir}")

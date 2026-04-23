# ======================================
# IMPORTS
import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse
import tldextract

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ======================================
# LOAD DATA
data = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# ======================================
# REMOVE DUPLICATES
print("Duplicates:", data.duplicated().sum())
data = data.drop_duplicates()

# ======================================
# FEATURE EXTRACTION (IMPROVED)
def extract_features(url):

    ext = tldextract.extract(url)
    domain = ext.domain
    subdomain = ext.subdomain

    return [
        len(url),
        url.count('.'),
        sum(c.isdigit() for c in url),
        1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        len(urlparse(url).path),
        url.count('-'),
        url.count('@'),
        url.count('?'),
        url.count('='),
        len(domain),
        len(subdomain),
        subdomain.count('.')
    ]

url_features = data['URL'].apply(extract_features)

url_df = pd.DataFrame(url_features.tolist(), columns=[
    'url_length','dots','digits','has_ip','path_length',
    'hyphen','at_symbol','question_mark','equals',
    'domain_length','subdomain_length','subdomain_depth'
])

X = url_df
y = data['label']

# ======================================
# TRAIN-TEST SPLIT (STRATIFIED)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ======================================
# RANDOM FOREST (IMPROVED)
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

# ======================================
# EVALUATION
rf_pred = rf_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, rf_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, rf_pred))

cm = confusion_matrix(y_test, rf_pred)

# ======================================
# CROSS VALIDATION
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(rf_model, X, y, cv=cv, n_jobs=-1)

print("Cross-validation accuracy:", scores.mean())

# ======================================
# FEATURE IMPORTANCE 🔥
importances = rf_model.feature_importances_

plt.figure()
plt.barh(X.columns, importances)
plt.title("Feature Importance")
plt.show()

# ======================================
# CONFUSION MATRIX
plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ======================================
# SAVE MODEL
joblib.dump(rf_model, 'phishing_model_fixed.pkl')

print("Model Saved Successfully!")

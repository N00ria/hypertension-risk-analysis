import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Prepare features
features = ['Family_History', 'Stress_Score', 'Age', 'BMI']
target = 'Has_Hypertension'

model_df = hypertension_clean_df[features + [target]].copy()

# Encode binary categoricals
model_df['Family_History'] = (model_df['Family_History'] == 'Yes').astype(int)
model_df['Has_Hypertension'] = (model_df['Has_Hypertension'] == 'Yes').astype(int)

X = model_df[features]
y = model_df[target]

# Train/test split (80/20, stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale numeric features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit logistic regression
lr_model = LogisticRegression(random_state=42, max_iter=200)
lr_model.fit(X_train_scaled, y_train)

# Predictions & metrics
y_pred = lr_model.predict(X_test_scaled)
lr_accuracy = accuracy_score(y_test, y_pred)

print(f"=== Logistic Regression Results ===")
print(f"Train size: {len(X_train):,}  |  Test size: {len(X_test):,}")
print(f"Accuracy:   {lr_accuracy:.1%}")
print()
print("=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=['No Hypertension', 'Has Hypertension']))

# Feature importance (standardised coefficients)
feature_importances = pd.DataFrame({
    'Feature': features,
    'Coefficient': lr_model.coef_[0],
    'Abs_Coefficient': np.abs(lr_model.coef_[0])
}).sort_values('Abs_Coefficient', ascending=False)

print("=== Feature Importances (Standardised Coefficients) ===")
print(feature_importances[['Feature', 'Coefficient']].to_string(index=False))

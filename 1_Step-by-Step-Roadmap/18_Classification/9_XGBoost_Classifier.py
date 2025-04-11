# ✅ 8. XGBoost Classifier (Extreme Gradient Boosting)
# Optimized gradient boosting with regularization and fast performance.
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train, y_train)
print("XGBoost Accuracy:", model.score(X_test, y_test))

# ✅ 7. Gradient Boosting Classifier
# Builds an ensemble sequentially, minimizing the previous model’s errors.

# 🔹 Real-World Example:
# Churn prediction or fraud detection.

from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
print("Gradient Boosting Accuracy:", model.score(X_test, y_test))

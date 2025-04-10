# ✅ 5. Random Forest Classifier
# An ensemble of decision trees that reduces overfitting and increases accuracy.

# 🔹 Real-World Example:
# Predict loan approval using multiple customer features.
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print("Random Forest Accuracy:", model.score(X_test, y_test))

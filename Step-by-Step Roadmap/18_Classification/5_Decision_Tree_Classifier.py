# ✅ 4. Decision Tree Classifier
# Splits the data into branches using if-else logic based on features.

# 🔹 Real-World Example:
# Predict whether someone has diabetes based on health data.
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("Decision Tree Accuracy:", model.score(X_test, y_test))

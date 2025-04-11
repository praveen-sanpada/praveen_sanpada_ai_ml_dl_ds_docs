# ✅ 1. Logistic Regression/
# A linear model for binary classification. Outputs probability and uses sigmoid function.

# 🔹 Real-World Example:
# Predict if a customer will buy or not based on age and income.

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X, y = X[y != 2], y[y != 2]  # Binary classification only

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print("Logistic Accuracy:", model.score(X_test, y_test))



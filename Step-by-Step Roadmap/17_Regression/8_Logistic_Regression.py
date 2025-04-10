from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Data (binary classification example)
X, y = load_iris(return_X_y=True)
X = X[y != 2]
y = y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
accuracy = log_model.score(X_test, y_test)
print("Logistic Regression Accuracy:", accuracy)


# ✅ 6. Logistic Regression (Classification, not regression)
# 📌 Project: Predict if Customer Will Buy or Not
# Dataset: Social Network Ads Dataset
# Goal: Predict if user will purchase based on age and salary
# Model: LogisticRegression()
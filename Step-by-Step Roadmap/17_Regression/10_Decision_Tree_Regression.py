from sklearn.tree import DecisionTreeRegressor

# Model
tree_model = DecisionTreeRegressor()
tree_model.fit(X, y)
print("Decision Tree Predictions:", tree_model.predict(X))


# ✅ 8. Decision Tree Regression
# 📌 Project: Predict Salary Based on Experience
# Dataset: Simple CSV (Experience vs Salary)
# Goal: Fit non-linear decision boundaries
# Model: DecisionTreeRegressor()
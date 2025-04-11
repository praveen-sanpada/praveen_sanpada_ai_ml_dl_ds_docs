from sklearn.linear_model import Ridge

# Model
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, y)
print("Ridge Coefficients:", ridge_model.coef_)


# ✅ 3. Ridge Regression
# 📌 Project: Predict Bike Rentals (with regularization)
# Dataset: UCI Bike Sharing Dataset
# Goal: Predict number of bike rentals using multiple time-based features
# Model: Ridge()
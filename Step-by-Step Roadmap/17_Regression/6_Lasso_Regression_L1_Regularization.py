from sklearn.linear_model import Lasso

# Model
lasso_model = Lasso(alpha=1000)
lasso_model.fit(X, y)
print("Lasso Coefficients:", lasso_model.coef_)


# ✅ 4. Lasso Regression
# 📌 Project: Predict Insurance Charges
# Dataset: Medical Cost Personal Dataset (Kaggle)
# Goal: Predict insurance charges and perform feature selection
# Model: Lasso()
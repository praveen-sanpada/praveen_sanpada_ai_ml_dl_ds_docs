from sklearn.ensemble import GradientBoostingRegressor

# Model
gb_model = GradientBoostingRegressor()
gb_model.fit(X, y)
print("Gradient Boosting Predictions:", gb_model.predict(X))


# ✅ 10. Gradient Boosting Regression
# 📌 Project: Predict House Energy Usage
# Dataset: Appliances Energy Prediction Dataset
# Goal: Predict energy consumption of appliances
# Model: GradientBoostingRegressor()
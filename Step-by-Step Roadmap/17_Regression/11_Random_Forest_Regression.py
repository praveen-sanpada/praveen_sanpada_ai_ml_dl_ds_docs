from sklearn.ensemble import RandomForestRegressor

# Model
forest_model = RandomForestRegressor(n_estimators=100)
forest_model.fit(X, y)
print("Random Forest Predictions:", forest_model.predict(X))


# ✅ 9. Random Forest Regression
# 📌 Project: Predict Flight Price
# Dataset: Flight Fare Prediction (Kaggle)
# Goal: Predict flight fare based on airline, duration, stops
# Model: RandomForestRegressor()
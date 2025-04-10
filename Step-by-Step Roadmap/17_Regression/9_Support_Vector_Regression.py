from sklearn.svm import SVR

# Model
svr_model = SVR(kernel='rbf')
svr_model.fit(X, y)
print("SVR Predictions:", svr_model.predict(X))


# ✅ 7. Support Vector Regression (SVR)
# 📌 Project: Predict CPU Performance
# Dataset: Computer Hardware Dataset (UCI)
# Goal: Predict CPU performance (benchmark score)
# Model: SVR()
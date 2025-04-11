from sklearn.linear_model import ElasticNet

# Model
elastic_model = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic_model.fit(X, y)
print("ElasticNet Coefficients:", elastic_model.coef_)


# ✅ 5. ElasticNet Regression
# 📌 Project: Predict Energy Efficiency
# Dataset: Energy Efficiency Dataset (UCI)
# Goal: Predict heating/cooling load while handling multicollinearity
# Model: ElasticNet()
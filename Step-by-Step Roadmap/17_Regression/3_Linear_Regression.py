from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([100000, 150000, 200000, 250000, 300000])

# Model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title("Linear Regression")
plt.xlabel("Size (sqft)")
plt.ylabel("Price")
plt.show()


# ✅ 1. Linear Regression
# 📌 Project: Predict House Prices
# Dataset: Boston Housing Dataset / Kaggle housing prices
# Goal: Predict house price using size, number of rooms, etc.
# Model: LinearRegression()
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([25000, 22000, 19000, 16000, 14000, 13500])

# Model
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X, y)
y_pred = poly_model.predict(X)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='green')
plt.title("Polynomial Regression")
plt.xlabel("Car Age")
plt.ylabel("Price")
plt.show()


# ✅ 2. Polynomial Regression
# 📌 Project: Predict Car Price Based on Age
# Dataset: Custom CSV (Car Age vs Price)
# Goal: Fit a curve to model depreciation of car value
# Model: PolynomialFeatures(degree=n) + LinearRegression()
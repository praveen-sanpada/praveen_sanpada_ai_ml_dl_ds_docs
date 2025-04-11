# ✅ 2. K-Nearest Neighbors (KNN)
# Classifies a point based on the majority class of its nearest neighbors.

# 🔹 Real-World Example:
# Predict handwritten digits based on pixel values.

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("KNN Accuracy:", model.score(X_test, y_test))


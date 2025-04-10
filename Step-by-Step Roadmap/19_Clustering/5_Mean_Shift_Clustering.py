# ✅ 4. Mean Shift Clustering
# Finds clusters by shifting data points toward dense regions.
# Doesn’t require number of clusters.

# 🔹 Use Case: Image segmentation
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=200, centers=3, cluster_std=1)
model = MeanShift()
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='Accent')
plt.title("Mean Shift Clustering")
plt.show()

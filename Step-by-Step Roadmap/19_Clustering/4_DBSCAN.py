# ✅ 3. DBSCAN (Density-Based Spatial Clustering)
# Great for clusters with arbitrary shapes
# Detects outliers automatically
# Doesn’t require number of clusters

# 🔹 Use Case: Detecting GPS location anomalies
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

X, _ = make_moons(n_samples=300, noise=0.1, random_state=42)
model = DBSCAN(eps=0.3, min_samples=5)
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='Set1')
plt.title("DBSCAN Clustering")
plt.show()


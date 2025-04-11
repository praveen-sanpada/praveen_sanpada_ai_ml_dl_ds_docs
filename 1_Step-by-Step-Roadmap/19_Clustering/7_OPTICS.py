# ✅ 6. OPTICS (Ordering Points To Identify Clustering Structure)
# Similar to DBSCAN but handles varying density clusters.

# 🔹 Use Case: Geospatial data, biological datasets
from sklearn.cluster import OPTICS

X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
model = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.1)
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab20')
plt.title("OPTICS Clustering")
plt.show()

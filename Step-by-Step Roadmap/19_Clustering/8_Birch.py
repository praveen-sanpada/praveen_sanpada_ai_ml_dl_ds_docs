# ✅ 7. Birch (Balanced Iterative Reducing and Clustering using Hierarchies)
# Good for large datasets.
# Uses a tree structure for efficient clustering.

# 🔹 Use Case: Big customer segmentation datasets
from sklearn.cluster import Birch

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1)
model = Birch(n_clusters=4)
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10')
plt.title("Birch Clustering")
plt.show()

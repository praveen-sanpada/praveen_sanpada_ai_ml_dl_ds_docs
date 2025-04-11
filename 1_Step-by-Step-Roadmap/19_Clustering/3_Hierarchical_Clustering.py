# ✅ 2. Hierarchical Clustering (Agglomerative)
# Builds a tree (dendrogram) from bottom up.
# Good for nested or structured data.

# 🔹 Use Case: Grouping similar documents or genes
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

X, _ = make_blobs(n_samples=100, centers=3, random_state=42)

# Agglomerative clustering
agg = AgglomerativeClustering(n_clusters=3)
labels = agg.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma')
plt.title("Agglomerative Clustering")
plt.show()

# Dendrogram (optional)
linked = linkage(X, 'ward')
dendrogram(linked)
plt.title("Dendrogram")
plt.show()

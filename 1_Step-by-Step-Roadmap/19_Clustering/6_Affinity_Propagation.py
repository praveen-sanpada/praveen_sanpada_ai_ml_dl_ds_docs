# ✅ 5. Affinity Propagation
# Doesn’t require number of clusters.
# Finds exemplar points that best represent clusters.

# 🔹 Use Case: Recommendation engines, image clustering
from sklearn.cluster import AffinityPropagation
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=150, centers=4, random_state=0)
model = AffinityPropagation()
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10')
plt.title("Affinity Propagation")
plt.show()

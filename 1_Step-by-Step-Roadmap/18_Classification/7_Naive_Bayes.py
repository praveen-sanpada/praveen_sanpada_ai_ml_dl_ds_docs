# ✅ 6. Naive Bayes
# Based on Bayes Theorem, assumes feature independence. Very fast.

# 🔹 Real-World Example:
# Spam detection, sentiment analysis (text classification).

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
print("Naive Bayes Accuracy:", model.score(X_test, y_test))

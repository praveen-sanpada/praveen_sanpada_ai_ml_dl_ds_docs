# ✅ 3. Support Vector Machine (SVM)
# Finds the best boundary (hyperplane) that separates classes with the largest margin.

# 🔹 Real-World Example:
# Classifying cancer cells as malignant or benign.

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train, y_train)
print("SVM Accuracy:", model.score(X_test, y_test))

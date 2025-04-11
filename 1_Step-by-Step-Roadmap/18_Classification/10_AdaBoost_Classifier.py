# ✅ 9. AdaBoost Classifier
# Boosts weak learners sequentially by focusing more on previous errors.
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()
model.fit(X_train, y_train)
print("AdaBoost Accuracy:", model.score(X_test, y_test))

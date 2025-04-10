# ✅ 10. LightGBM Classifier
# Fast gradient boosting for large datasets, best for Kaggle competitions.

from lightgbm import LGBMClassifier
model = LGBMClassifier()
model.fit(X_train, y_train)
print("LightGBM Accuracy:", model.score(X_test, y_test))

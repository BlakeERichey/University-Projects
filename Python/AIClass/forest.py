from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
print(iris)

X = iris.data
y = iris.target

print(X)
print(y)

forest = RandomForestClassifier(n_estimators=25, random_state=1, n_jobs=4)
forest.fit(X, y)

from sklearn.metrics import accuracy_score, f1_score
pred = forest.predict(X)
print('Accuracy:', accuracy_score(y, pred))
print('F1 score:', f1_score(y, pred, average='micro'))
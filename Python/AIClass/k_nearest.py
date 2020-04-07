from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

iris = datasets.load_iris()
 
X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=3, p=2, metric='minkowski')
knn.fit(X, y)

from sklearn.metrics import accuracy_score
pred = knn.predict(X)
print(accuracy_score(y, pred))

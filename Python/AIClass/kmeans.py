from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

km = KMeans(n_clusters=3, init='random', n_init=10, max_iter=300, random_state=0, n_jobs=4)

y_km = km.fit_predict(X)
print(y_km)

from sklearn.metrics import explained_variance_score
print('PVE:', explained_variance_score(y, y_km))

#elbow testing
distortions = []
for i in range(1, 11):
  km = KMeans(n_clusters=i, n_jobs=4)
  km.fit(X)
  distortions.append(km.inertia_)

import matplotlib.pyplot as plt

plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Number of distortions')
plt.tight_layout()
plt.show()
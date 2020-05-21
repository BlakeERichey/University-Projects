from sklearn import datasets
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
# print(iris)

X = iris.data
y = iris.target

X, X_valid, y, y_valid = train_test_split(X, y, test_size=.30, random_state=1)

sc_x = StandardScaler()
sc_x_valid = StandardScaler()

X_std = sc_x.fit_transform(X)
X_std_valid = sc_x_valid.fit_transform(X_valid)

svm = SVC(degree=10, random_state=10, verbose=1, tol=1E-3, kernel='linear')
svm.fit(X_std, y)
y_pred = svm.predict(X_std_valid)
print('Accuracy:', accuracy_score(y_valid, y_pred))
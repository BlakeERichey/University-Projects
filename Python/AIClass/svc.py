from sklearn import datasets
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

iris = datasets.load_boston()
print(iris)
inx = iris.feature_names.tolist().index('RM')

X = iris.data[:, inx:inx+1]
y = iris.target

sc_x = StandardScaler()
sc_y = StandardScaler()

X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()


def lin_regplot(X, y, model):
    print('X, y:', X.size, y.size)
    plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
    X_new = []
    y_new = []
    for i in range(len(y)):
        X_new.append(X[i])
        y_new.append(model.predict(X[i].reshape(1, -1)))
    plt.plot(X_new, y_new, color='black', lw=2)
    return None

slr = LinearRegression()
slr.fit(X_std, y_std)
y_pred = slr.predict(X_std)
lin_regplot(X_std, y_std, slr)
print('R2:', r2_score(y_std, y_pred))
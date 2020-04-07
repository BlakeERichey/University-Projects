from sklearn.tree import DecisionTreeClassifier
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

tree_model = DecisionTreeClassifier(max_depth=4, random_state=1)
tree_model.fit(X, y)
tree.plot_tree(tree_model)
plt.show()

from sklearn.metrics import accuracy_score
pred = tree_model.predict(X)
print(accuracy_score(y, pred))
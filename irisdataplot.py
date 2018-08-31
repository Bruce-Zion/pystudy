# Load the data
from sklearn.datasets import load_iris
iris = load_iris()

from matplotlib import pyplot as plt

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
plt.figure(figsize=(50, 40))

for i in [0, 1, 2]:
    for j in range(i+1, 4):
        if i == 0:
            index = i + j
        else:
            index = i + j +1

        plt.subplot(2, 3, index)
        plt.scatter(iris.data[:, i], iris.data[:, j], c=iris.target)
        plt.colorbar(ticks=[0, 1, 2], format=formatter)
        plt.xlabel(iris.feature_names[i])
        plt.ylabel(iris.feature_names[j])

#plt.tight_layout()
plt.show()
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

# Load the data points
data = np.loadtxt("data/points_7.csv",delimiter=',')
X = data[:,0:2]
y = data[:,2]
# Make a SVC model
clf = svm.SVC(kernel="poly", C=10)
clf.fit(X, y)

# Plot points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30)
# Plot model
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])
# Put the result into a color plot
Z = Z.reshape(XX.shape)
plt.contourf(XX, YY, Z, cmap=plt.cm.coolwarm, alpha=0.8)

# Plot also the training points on front
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('7 labels')
plt.savefig('images/7_labels_svm.png')
plt.show()
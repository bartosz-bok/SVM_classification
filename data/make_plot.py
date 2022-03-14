
import numpy as np
import matplotlib.pyplot as plt

# Load the data points
data_2 = np.loadtxt("points_2.csv",delimiter=',')
X_2 = data_2[:,0:2]
y_2 = data_2[:,2]

# Load the data points
data_3 = np.loadtxt("points_3.csv",delimiter=',')
X_3 = data_3[:,0:2]
y_3 = data_3[:,2]

# Load the data points
data_7 = np.loadtxt("points_7.csv",delimiter=',')
X_7 = data_7[:,0:2]
y_7 = data_7[:,2]

fig, axs = plt.subplots(1,3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, constrained_layout=True)

axs[0].scatter(X_2[:, 0], X_2[:, 1], c=y_2, s=10)
axs[1].scatter(X_3[:, 0], X_3[:, 1], c=y_3, s=10)
axs[2].scatter(X_7[:, 0], X_7[:, 1], c=y_7, s=10)

axs[0].title.set_text('2 labels')
axs[1].title.set_text('3 labels')
axs[2].title.set_text('7 labels')

plt.savefig('../images/raw_points.png')
plt.show()
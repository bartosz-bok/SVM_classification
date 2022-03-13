import random
import numpy as np
import matplotlib.pyplot as plt

N_SAMPLES = 100

data0 = np.zeros((N_SAMPLES,3))
data1 = np.ones((N_SAMPLES,3))

for i in range(N_SAMPLES):
    for j in range(2):
        # data0[i][j] = random.random()*12-10
        # data1[i][j] = random.random()*12-2
        data0[i][j] = random.gauss(4, 4)
        data1[i][j] = random.gauss(-4, 4)

data = np.concatenate((data0, data1), axis=0)

y = data[:,2]
plt.scatter(data[:, 0], data[:, 1], c=y, s=30, cmap=plt.cm.bwr)

plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('../images/2_labels_raw.png')

plt.show()

np.savetxt("points.csv", data, delimiter=",")
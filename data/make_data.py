import random
import numpy as np
import matplotlib.pyplot as plt

N_SAMPLES = 100

data0 = np.zeros((N_SAMPLES,3))
data1 = np.ones((N_SAMPLES,3))

for i in range(N_SAMPLES):
    for j in range(2):
        data0[i][j] = random.random()*12-10
        data1[i][j] = random.random()*12-2

data = np.concatenate((data0, data1), axis=0)

for i in range(len(data)):
    if data[i][2] == 0:
        plt.scatter(data[i][0], data[i][1], c='red')
    if data[i][2] == 1:
        plt.scatter(data[i][0], data[i][1], c='blue')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()

np.savetxt("points.csv", data, delimiter=",")
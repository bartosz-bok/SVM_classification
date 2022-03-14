import random
import numpy as np
import matplotlib.pyplot as plt

# Number of samples and features
N_SAMPLES = 100
N_FEATURES = 7 # 2,3 OR 7 !

data0 = np.zeros((N_SAMPLES,3))
data1 = np.ones((N_SAMPLES,3))

if N_FEATURES == 3 or N_FEATURES == 7:
    data2 = np.ones((N_SAMPLES,3))*2
if N_FEATURES == 7:
    data3 = np.ones((N_SAMPLES,3))*3
    data4 = np.ones((N_SAMPLES,3))*4
    data5 = np.ones((N_SAMPLES,3))*5
    data6 = np.ones((N_SAMPLES,3))*6

# Random values with Gaussian distribution
for i in range(N_SAMPLES):
    for j in range(2):
            data0[i][j] = random.gauss(6, 4)
            data1[i][j] = random.gauss(-6, 4)
            
    if N_FEATURES == 3 or N_FEATURES == 7:
        data2[i][0] = random.gauss(-8, 4)
        data2[i][1] = random.gauss(8, 4)

    if N_FEATURES == 7:
        data3[i][0] = random.gauss(10, 4)
        data3[i][1] = random.gauss(-10, 4)
        data4[i][0] = random.gauss(-16, 4)
        data4[i][1] = random.gauss(-16, 4)
        data5[i][0] = random.gauss(16, 4)
        data5[i][1] = random.gauss(0, 4)
        data6[i][0] = random.gauss(-16, 4)
        data6[i][1] = random.gauss(0, 4)

data = np.concatenate((data0, data1), axis=0)
if N_FEATURES == 3 or N_FEATURES == 7:
    data = np.concatenate((data, data2), axis=0)

if N_FEATURES == 7:
    data = np.concatenate((data, data3), axis=0)
    data = np.concatenate((data, data4), axis=0)
    data = np.concatenate((data, data5), axis=0)
    data = np.concatenate((data, data6), axis=0)

# Make a plot
y = data[:,2]
plt.scatter(data[:, 0], data[:, 1], c=y, s=30)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('../images/2_labels_raw.png')
plt.show()
np.savetxt("points_7.csv", data, delimiter=",")
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
from itertools import cycle

time = 2000
eta19 = 0.01
eta20 = 0.001

data = np.array(np.loadtxt('hw3_train.dat.txt'))
# print(data)
num = data.shape[0]
# print(num)
vecLen = data.shape[1]
# print(vecLen)
y = np.zeros([num, 1])
# print(y)
y[:, 0] = data[:, -1]
# print(y)
data[:, -1] = np.ones(num)
# print(data)
E_in = lambda w: np.average(y != np.sign(np.dot(data, w)))

testdata = np.loadtxt('hw3_test.dat.txt')
# print(testdata)
testNum = testdata.shape[0]
# print(testNum)
# testLen = testdata.shape[1]
# print(testLen)
testY = np.zeros([testNum, 1])
# print(testY)
testY[:, 0] = testdata[:, -1]
# print(testY)
testdata[:, -1] = np.ones(testNum)
# print(testdata)
E_out = lambda w: np.average(testY != np.sign(np.dot(testdata, w)))

E_in_19_G = []
E_in_19_S = []
E_out_19_G = []
E_out_19_S = []

E_in_20_G = []
E_in_20_S = []
E_out_20_G = []
E_out_20_S = []

# Gradient Descent
w_19 = np.zeros([vecLen, 1])
w_20 = np.zeros([vecLen, 1])
for i in range(time):
	w_19 -= eta19 * np.dot((-y * data).T, (sp.expit(y * (-np.dot(data, w_19))))) / num
	w_20 -= eta20 * np.dot((-y * data).T, (sp.expit(y * (-np.dot(data, w_20))))) / num
	E_in_19_G.append(E_in(w_19))
	E_in_20_G.append(E_in(w_20))
	E_out_19_G.append(E_out(w_19))
	E_out_20_G.append(E_out(w_20))

w_19 = np.zeros([vecLen, 1])
w_20 = np.zeros([vecLen, 1])
#Stochasitc Gradient Descent
for t, i in zip(range(time), cycle(range(num))):
	w_19 -= eta19 * (-y[i] * data[i:i + 1].T) * sp.expit(y[i] * np.dot(-data[i], w_19))
	w_20 -= eta20 * (-y[i] * data[i:i + 1]).T * sp.expit(y[i] * -np.dot(data[i], w_20))
	E_in_19_S.append(E_in(w_19))
	E_in_20_S.append(E_in(w_20))
	E_out_19_S.append(E_out(w_19))
	E_out_20_S.append(E_out(w_20))

plt.figure(figsize = (20, 8))
plt.subplot(221)
plt.title('Gradient Descent v.s. Stochastic Gradient Descent (eta=' + str(eta19) + ')')
plt.xlabel('iteration')
plt.ylabel('E_in')
plt.plot(range(time), E_in_19_G, label='gradient')
plt.plot(range(time), E_in_19_S, label = 'stochastic')
plt.text(time*1.01, E_in_19_G[time-1], str(E_in_19_G[time-1]))
plt.text(time*1.01, E_in_19_S[time-1], str(E_in_19_S[time-1]))
plt.legend()

plt.subplot(222)
plt.title('Gradient Descent v.s. Stochastic Gradient Descent (eta=' + str(eta20) + ')')
plt.xlabel('iteration')
plt.ylabel('E_in')
plt.plot(range(time),E_in_20_G, label = 'gradient')
plt.plot(range(time),E_in_20_S, label = 'stochastic')
plt.text(time*1.01, E_in_20_G[time-1], str(E_in_20_G[time-1]))
plt.text(time*1.01, E_in_20_S[time-1], str(E_in_20_S[time-1]))
plt.legend()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, hspace=0.3)

plt.subplot(223)
plt.title('Gradient Descent v.s. Stochastic Gradient Descent (eta=' + str(eta19) + ')')
plt.xlabel('iteration')
plt.ylabel('E_out')
plt.plot(range(time), E_out_19_G, label = 'gradient')
plt.plot(range(time), E_out_19_S, label = 'stochastic')
plt.text(time*1.01, E_out_19_G[time-1], str(E_out_19_G[time-1]))
plt.text(time*1.01, E_out_19_S[time-1], str(E_out_19_S[time-1]))
plt.legend()

plt.subplot(224)
plt.title('Gradient Descent v.s. Stochastic Gradient Descent (eta=' + str(eta20) + ')')
plt.xlabel('iteration')
plt.ylabel('E_out')
plt.plot(range(time),E_out_20_G, label = 'gradient')
plt.plot(range(time),E_out_20_S, label = 'stochastic')
plt.text(time*1.01, E_out_20_G[time-1], str(E_out_20_G[time-1]))
plt.text(time*1.01, E_out_20_S[time-1], str(E_out_20_S[time-1]))
plt.legend()
plt.show()



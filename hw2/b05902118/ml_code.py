import math
import random
import matplotlib.pyplot as plt
# from random import *

Ein = []
Eout = []

#操作1000次--------------------------->remember to change
for time in range(1000):
	x = []
	y = []
	theta = []
	theta.append(-1)

	error = 0
	best = 10000
	bestTheta = 0
	bestS = 0

#做一個大小為20的data
	for count in range(20):
		x.append(random.uniform(-1, 1))

	x.sort()
	# print (x)
	for i in range(20):
		if x[i] < 0:
			y.append(-1)
		else:
			y.append(1)

#實作錯誤率是20%
	for i in range(20):
		if (random.random() <= 0.2):
			y[i] = -y[i]

#21個theta
	for i in range(19):
		theta.append((x[i] + x[i + 1]) / 2)
	theta.append(1)

	s = 1
	for i in range(21):
		for j in range(20):
			if x[j] > theta[i]:
				t = 1
			else:
				t = -1
			if t * s * y[j] < 0:
				error += 1
		if best > error:
			best = error
			bestTheta = theta[i]
			bestS = s
		error = 0

	s = -1
	for i in range(21):
		for j in range(20):
			if x[j] > theta[i]:
				t = 1
			else:
				t = -1
			if t * s * y[j] < 0:
				error += 1
		if best > error:
			best = error
			bestTheta = theta[i]
			bestS = s
		error = 0

	Ein.append(best / 20.0)
	Eout.append(0.5 + 0.3 * (abs(bestTheta) - 1) * bestS)
# print ("Ein:", Ein, ", Eout:", Eout)
plt.title("E_in v.s. E_out")
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.xlabel("E_in")
plt.ylabel("E_out")
plt.scatter(Ein, Eout, alpha = 0.1, c = "black")
plt.show()



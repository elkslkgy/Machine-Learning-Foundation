import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Open a file
fo = open("test", "r")
line = fo.readlines()

list1 = []
ans = 0

for time in range(0, 1126):
	random.shuffle(line)

	w0 = w1 = w2 = w3 = w4 = 0 # w0 = -k
	count = 0

	while True:
		check = 0

		for i in range(0, 400):
				
			divide = line[i].split()
			divide = list(map(float, divide))
		
			x0 = 1
			x1 = divide[0]
			x2 = divide[1]
			x3 = divide[2]
			x4 = divide[3]
			y = divide[4]

			if y * (w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4) <= 0 :
				w0 += y * x0
				w1 += y * x1
				w2 += y * x2
				w3 += y * x3
				w4 += y * x4
				check = check + 1

		if check == 0:
			break

		count += check

	ans += count
	list1.append(count)

ans = float(ans) / 1126
print ans

plt.hist(list1, 100, edgecolor = 'black')
plt.show()

# Close opend file
fo.close()



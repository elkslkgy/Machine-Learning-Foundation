import random
import numpy as np
#import matplotlib.pyplot as plt

# Open a file
fo = open("train", "r")
line = fo.readlines()

ans = 0

random.shuffle(line)

w0 = w1 = w2 = w3 = w4 = 0 # w0 = -k
w0_end = w1_end = w2_end = w3_end = w4_end = 0
count = 0
stop = 501
change = check = 0

while True:

	for i in range(0, 400):

		divide = line[i].split()
		divide = list(map(float, divide))
		
		x0 = 1
		x1 = divide[0]
		x2 = divide[1]
		x3 = divide[2]
		x4 = divide[3]
		y = divide[4]
			
		if y * (w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4) <= 0:

			w0 += y * x0
			w1 += y * x1
			w2 += y * x2
			w3 += y * x3
			w4 += y * x4
			check += 1
			wrong = 0
			for j in range(0, 400):
					d = line[j].split()
					d = list(map(float, d))
					d0 = 1
					d1 = d[0]
					d2 = d[1]
					d3 = d[2]
					d4 = d[3]
					dy = d[4]

					if dy * (w0 + w1*d1 + w2*d2 + w3*d3 + w4*d4) <= 0:
						wrong += 1
						if wrong > stop:
							break

			if wrong <= stop:
				w0_end = w0
				w1_end = w1
				w2_end = w2
				w3_end = w3
				w4_end = w4
				stop = wrong
				change += check
				check = 0
				

		if change >= 100:
			break
		
	if change >= 100:
		break

print "w0:", w0_end, "w1:", w1_end, "w2:", w2_end, "w3:", w3_end, "w4:", w4_end
fo.close()

# Open a file
fo = open("test18", "r")
line = fo.readlines()

rate = 0
for time in range(0, 2000):
	random.shuffle(line)

	wrong = 0
	for i in range(0, 500):
				
		divide = line[i].split()
		divide = list(map(float, divide))
		
		x0 = 1
		x1 = divide[0]
		x2 = divide[1]
		x3 = divide[2]
		x4 = divide[3]
		y = divide[4]

		if y * (w0_end + w1_end*x1 + w2_end*x2 + w3_end*x3 + w4_end*x4) <= 0 :
			wrong += 1
	rate += float(wrong)/500

ans = float(rate) / 2000
print ans

# Close opend file
fo.close()



import math

#九個維度的x，從x1~x9
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
y = []

#打開training data，讀取資料
file = open("/Users/evan/documents/university/Machine_Learning_Foundation/hw2/training_data")
for line in file:
    lines = line.split(' ')
    x1.append(float(lines[1]))
    x2.append(float(lines[2]))
    x3.append(float(lines[3]))
    x4.append(float(lines[4]))
    x5.append(float(lines[5]))
    x6.append(float(lines[6]))
    x7.append(float(lines[7]))
    x8.append(float(lines[8]))
    x9.append(float(lines[9]))
    y.append(int(lines[10]))
file.close()

error = 0
best = 1000000  #假設最好的情況是錯1000000個
bestTheta = 0
bestS = 0

#從x1~x9
for i in range(9):
    for j in range(5000):#一樣跑5000次
    
        #s & theta是怎麼決定的？？？？？
        if j < 2500:
            s = -1
        else:
            s = 1
        theta = -1 + (i % 2500) / 1250.0

        for k in range(100):
            if x[i][k] > theta:
                t = 1
            else:
                t = -1
            if t * s * y[k] < 0:
                error += 1
        if best > error:
            best = error
            bestTheta = theta
            bestS = s
        error = 0

print (best / 100.0)
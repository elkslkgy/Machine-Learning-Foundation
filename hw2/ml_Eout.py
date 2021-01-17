import math
x = [i / 10.0 for i in range(-10, 11)]

x.remove(0) #做一個大小為20的data
y = []
error = 0
best = 100  #假設最好的情況是錯100個
bestTheta = 0
bestS = 0

#實作y=f(x)=sign(x)
for i in x:
    if i < 0:
        y.append(-1)
    else:
        y.append(1)

#實作錯誤率是20%        
y[0] = 1
y[5] = 1
y[15] = -1
y[10] = -1

#操作5000次
for i in range(5000):

    #s & theta是怎麼決定的？？？？？
    if i < 2500:
        s = -1
    else:
        s = 1
    theta = -1 + (i % 2500) / 1250.0

    for j in range(20):
        if x[j] > theta:
            t = 1
        else:
            t = -1
        if t * s * y[j] < 0:
            error += 1
    if best > error:
        best = error
        bestTheta = theta
        bestS = s
    error = 0

print (0.5 + 0.3 * (abs(bestTheta) - 1) * bestS)
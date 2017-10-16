# coding:utf-8
import numpy as np
import random
from blaze.expr.expressions import shape


# m donates the number of examples here, not the number of features
#梯度下降算法 , x:自变量  y:因变量  theta：x的系数  alpha：学习率，梯度下降算法中每一步下降多少  m： 总共实例个数  numIterations： 重复更新theta次数
def gradientDescent(x, y, theta, alpha, m, numIterations):   
    Xtrans = x.transpose()   #x的转置 
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        
        cost = np.sum(loss ** 2)  #cost 逐渐减小
        print("Iteration %d | Cost: %f" % (i, cost))
        
        gradient = np.dot(Xtrans, loss) / m
        
        #update
        theta = theta - alpha * gradient
    return theta

#-------------数据个数，偏好， 方差
def genData(numPoints, bias, variance): 
    x = np.zeros(shape=(numPoints, 2)) #产生所有元素都为零，行数为numPoints，列数为2
    y = np.zeros(shape=numPoints)  #行数为numPoints， 列数为1
    #basically a straight line
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y
        
#generate 100 points with a bias of 25 and 10 variance as a bit of noise
x, y = genData(100, 25, 10)
print "X:"
print x
print "Y"
print y

m, n = np.shape(x)  #返回行数和列数
n_y = np.shape(y)      

print "X shape:", str(m), " ", str(n)
print "y length: ", str(n_y)

numIterations = 100000
alpha = 0.0005 #alpha 每一步下降多少， 好的算法此值会动态调整，在开始的时候较大，这样可以快速进行，而快接近最低点的时候回越来越小，这样可以精度更高，不至于越过最低点
theta = np.ones(n) #初始化为n列，值全为1的向量
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print "theta: "
print (theta)


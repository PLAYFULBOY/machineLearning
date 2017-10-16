# coding:utf-8

#用于求R平方值，如果是简单线性关系，则可用computeCorrelation函数先求出皮尔逊相关系数，再进行平方运算即可得到R平方值；
#如果是多元高次则用polyfit 函数进行计算R平方值
#R平方值是反应所建立的函数反应实际关系的程度，其值越大，则所求出的方程越能反应数据的关系
import numpy as np
from astropy.units import Ybarn
import math

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0  #variance
    varY = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        varX += diffXXBar ** 2
        varY += diffYYBar ** 2
        
    SST = math.sqrt(varX * varY)
    return SSR / SST

#Polynomial Regression
def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y,degree)
    
    print "coeffs"
    print coeffs
    
    #Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()
    
    
    print "coeffs.tolist: "
    print results['polynomial']
    
    #r-squared
    p = np.poly1d(coeffs)
    print "p: "
    print p
    
    #fit values, and mean
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    results['determination'] = ssreg / sstot
    
    return results

testX = [1, 3, 8, 7, 9]
testY = [10, 12, 24, 21, 34]

print "r: ", computeCorrelation(testX, testY)
print "r^2: ", str(computeCorrelation(testX, testY) ** 2)

print "polyfit"
print polyfit(testX, testY, 1)['determination']
print polyfit(testX, testY, 1)['polynomial']

        
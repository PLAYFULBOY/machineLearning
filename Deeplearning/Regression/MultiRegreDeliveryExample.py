# coding:utf-8

#邮递员送快递，运输时间与运送次数和里程之间的关系

from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r"C:\Users\ning\workspace\regressionFile\Delivery.csv"   #r indicates that the following characters remains the original style, do not transfer. such as "\n" represents line feed
deliveryData = genfromtxt(dataPath, delimiter=',')  #Extract data from text file , and transfer to numpy array format , delimiter is separator.

print "data"
print deliveryData

X = deliveryData[:, :-1]  #deliveryData的所有行，所有列但不包括最后一列，-1表示最后一列
Y = deliveryData[:, -1]   #deliveryData的所有行，最后一列，最后一列是因变量，最后一列是自变量

print "X : " 
print X
print "Y : "
print Y

regr = linear_model.LinearRegression()

regr.fit(X, Y)  # 对 X Y进行建模

print "coefficients:" #系数
print regr.coef_
print "intercept:"  #截距
print regr.intercept_

xPred = [102, 6]
yPred = regr.predict(xPred)

print "predicted y: "
print yPred







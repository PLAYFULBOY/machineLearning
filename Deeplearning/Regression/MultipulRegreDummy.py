# coding:utf-8

#（带车型参数（类型参数，非线性））邮递员送快递，运输时间与运送次数和里程之间的关系

from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r"C:\Users\ning\workspace\regressionFile\Delivery_Dummy.csv"   #r indicates that the following characters remains the original style, do not transfer. such as "\n" represents line feed
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
 
regr.fit(X, Y)  # �� X Y���н�ģ
 
print "coefficients:" #ϵ��
print regr.coef_
print "intercept:"  #�ؾ�
print regr.intercept_
 
xPred = [102, 6, 1, 0, 1]
yPred = regr.predict(xPred)
 
print "predicted y: "
print yPred







# coding:utf-8

import numpy as np  #��Ծ�������İ�
import pylab as pl #��ͼ �õİ�
from sklearn import svm

np.random.seed(0)  #0����������ÿ�εĲ�������

#20��2�е����顣 [2,2]����̫�ֲ����ٽ��
X = np.r_[np.random.randn(20,2) - [2,2], np.random.randn(20,2) + [2,2]]
Y = [0] * 20 + [1] * 20

clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

w = clf.coef_[0] #coefficient ��ϵ��
a = -w[0] / w[1] #ת��Ϊֱ�ߵ�б��

xx = np.linspace(-5, 5)  #�����������������ֵ
yy = a * xx - (clf.intercept_[0] / w[1])   

b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])


#plot the line , the points, and the nearest vectors to the plane
pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')

pl.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1],
           s = 80, facecolors='red')  #单独标记出support vector

pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired) #非support vector的点

pl.axis('tight')
pl.show()








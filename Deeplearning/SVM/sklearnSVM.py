# coding:utf-8
from sklearn import svm
X = [[2,0], [1,1], [2,3]]
y = [0,0,1]
clf = svm.SVC(kernel = 'linear')
clf.fit(X,y)  #ͨ通过.fit 函数已经可以算出支持向量机的所有参数并保存在clf中

print clf

# get support vectors 
print clf.support_vectors_

#get index of support vectors
print clf.support_

#get number of support vectors for each class
print clf.n_support_

#predict data ,参数是二维数组
print clf.predict([[2, 0], [10,10]])



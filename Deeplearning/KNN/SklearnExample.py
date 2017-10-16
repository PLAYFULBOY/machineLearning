# coding:utf-8
# 鸢尾属数据集，用knn算法预测
from sklearn import  neighbors  #neighbors分类模块
from sklearn import datasets    #导入数据集

knn = neighbors.KNeighborsClassifier() #分类器

iris = datasets.load_iris()  #导入鸢尾属（一种植物）数据集

print  iris

knn.fit(iris.data, iris.target) #第一个的参数是特征值。第二个参数是一个一维向量，是为每行特征值实例对应的对象
 
predictedLabel = knn.predict([[0.1,0.2,0.3,0.4]])  #预测新的特征值
print predictedLabel  #结果为零，对应第一种花
# coding:utf-8

#不调用库，自己实现knn算法
import csv   #读取CSV文件用的模块，读取数据用的
import random #随机数计算
import math  #数学计算
import operator
from bokeh.util.session_id import random
from boto.beanstalk import response
from dask.array.learn import predict



# 装载数据集  filename:数据集文件名 split：以数据集中某个位置为结点，把数据集分为trainingSet和testSet
def loadDataSet(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)  #把所有行存入lines
        dataset = list(lines) #把数据转换为list格式
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:   #如果随机值小于split
                trainingSet.append(dataset[x])  #则加到trainingSet
            else:
                testSet.append(dataset[x])
            

#欧几里德距离 ：坐标差的平方的和再开根号    还有曼哈顿距离
def euclideanDistance(instance1, instance2, length):   
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] -instance2[x]), 2)
    return math.sqrt(distance)

#返回距离testInstance最近trainingSet的K个邻居
def getNeighbours(trainingSet, testInstance, k):
    distances = []
    length =len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)  #每一个训练集数据和实例数据之间的距离
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1)) #sort 排序为从小到大
#取前k个最近的neighbors    
    neighbors = []
    for x in range(k):  
        neighbors.append(distances[x][0])  
    return neighbors
    

#根据少数服从多数的原则判断要预测实例属于哪一类。计算testInstance到trainingSet距离最近的个数，返回最多的那一类
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

#获取预测的准确率testSet:测试数据集  predictions：用代码预测的类别集合
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:  #-1表示数组的最后一个值。 
            correct += 1
    return(correct/float(len(testSet))) * 100.0

def main():
    trainingSet=[]
    testSet=[]
    split = 0.67  #三分之二为训练集 ， 三分之一为数据集
    loadDataSet(r'C:\Users\ning\workspace\KNNdata\irisdata.txt', split, trainingSet, testSet)
    print 'Train Set： ' + repr(len(trainingSet)) #repr 转化为字符串
    print 'Test Set： ' + repr(len(testSet))
    
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbours(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print("> predicted=" + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuarcy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuarcy) + '%')
main()

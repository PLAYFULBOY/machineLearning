# coding:utf-8
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from anaconda_navigator.utils.encoding import read
from sklearn.preprocessing.tests.test_data import toarray
from numba.tests.npyufunc.test_ufuncbuilding import Dummy
allElectronicsData = open(r'D:\deeplearning\AllElectronics.csv', 'rb')
reader = csv.reader(allElectronicsData)   #文件open和reader函数需要进一步学习
headers = reader.next()

print(headers)
featureList = []
labelList = [] #最后一列

for row in reader:
    #print(row)
    labelList.append(row[len(row)-1])  #在元祖末尾添加元素
    rowDict = {}
    for i in range(1,len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print(featureList)
print(labelList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()  #为什么加空格
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))  


clf = tree.DecisionTreeClassifier(criterion='entropy') 
clf = clf.fit(dummyX,dummyY)
print("clf: "+ str(clf)) 

with open("allElectronicInformationGainDri.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file = f)  #在当前工作目录生成  .dot 文件
    
oneRowX = dummyX[0, :]
print("oneRowx: " + str(oneRowX)) 

newRowX = oneRowX 

newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

  
predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))   









# coding:utf-8
from sklearn.feature_extraction import DictVectorizer
import csv #读取数据用
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from anaconda_navigator.utils.encoding import read
from sklearn.preprocessing.tests.test_data import toarray
from numba.tests.npyufunc.test_ufuncbuilding import Dummy
allElectronicsData = open(r'D:\deeplearning\AllElectronics.csv', 'rb') #csv格式文件可以用Excel打开
reader = csv.reader(allElectronicsData)   #文件open和reader函数需要进一步学习
headers = reader.next()

print(headers)
featureList = [] 
labelList = [] #最后一列

for row in reader:
    #print(row)
    labelList.append(row[len(row)-1])  #在元祖末尾添加元素，相当于push
    rowDict = {}
    for i in range(1,len(row)-1):
        rowDict[headers[i]] = row[i]  #headers是标题
    featureList.append(rowDict)
print(featureList)  #featureList其中一个字典（字典相当于js中的对象）{'credit_rating': 'fair', 'age': 'youth', 'student': 'no', 'income': 'high'},
print(labelList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()  #转换成[ 0.  0.  1.  0.  1.  1.  0.  0.  1.  0.]这种数据格式
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())
    
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))  
   
   
clf = tree.DecisionTreeClassifier(criterion='entropy') #entropy熵
clf = clf.fit(dummyX,dummyY)
print("clf: "+ str(clf)) 
   
with open("allElectronicInformationGainDri.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file = f)  #在当前工作目录生成  .dot 文件
    #>dot -Tpdf  allElectronicInformationGainDri.dot -o output.pdf   在cmd中输入此命令即可将.dot 文件输出为PDF

#取出一行数据
oneRowX = dummyX[0, :]
print("oneRowx: " + str(oneRowX)) 

#改变数据为新的数据，准备对其进行预测   
newRowX = oneRowX   
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))
    
#预测新数据      
predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))   
    








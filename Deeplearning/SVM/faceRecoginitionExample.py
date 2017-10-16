#coding:utf-8
from time import time #计时
import logging #log
import matplotlib.pyplot as plt #绘图
  
  
from sklearn.datasets.lfw import fetch_lfw_people
from sklearn.cluster.tests.test_k_means import n_samples
from sklearn.preprocessing.tests.test_data import n_features
from docutils.nodes import target
from sklearn.tests.test_multiclass import n_classes
from sklearn.cross_validation import train_test_split
from dask.array.tests.test_array_core import test_size
from sklearn.decomposition.pca import RandomizedPCA
from sklearn.grid_search import GridSearchCV
from sklearn.svm.classes import SVC
from statsmodels.sandbox.nonparametric.tests.ex_gam_am_new import y_pred   #此句 draw two figures 
from sklearn.metrics.classification import classification_report,\
    confusion_matrix
  
# Display progress logs on stdout 
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
  
   
   
#################################################################################
   
#Download the data, if not already on disk and load it as numpy arrays
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)  #选取名人人脸数据集, 类似于字典结构
   
# introspect(反省) the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape
   
   
X = lfw_people.data   #特征向量矩阵
n_features = X.shape[1]  #X矩阵有多少列，也就是每个人脸实例有多少特征值
   
y = lfw_people.target  #对应不同的人
target_names = lfw_people.target_names  #所有人的名字
n_classes = target_names.shape[0] #总共有多少类
   
print("Total dataset size: ")
print("n_samples: %d" % n_samples)
print("n_featurs: %d" % n_features)
print("n_classes: %d" % n_classes)
 
#################################################################################
#Split into a training set and a test set using a stratified k fold
 
#Split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25)
 
 
#################################################################################
#PCA降维
 
n_components = 150
 
print("Extracting the top %d eigenface from %d faces"
      % (n_components, X_train.shape[0]))
 
t0 = time()
pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)  #随机PCA降维
#pca = PCA(svd_solver='randomized')(n_components=n_components, whiten=True).fit(X_train)  #随机PCA降维
 
print("done in %0.3fs" % (time() - t0))
 
eigenfaces = pca.components_.reshape((n_components, h, w))  #特征脸算法
 
print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train) #转化为更低维矩阵
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" %  (time() - t0))
 
 
#################################################################################
#Train a SVM classification model
 
print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C':[1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma':[0.0001,0.00005, 0.001, 0.005, 0.01, 0.1]}
clf = GridSearchCV(SVC(kernel='rbf',class_weight='auto'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print('done in %0.3fs' % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
 
#################################################################################
#Quantitative evaluation of the model quality on the test set
 
print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))
 
print(classification_report(y_test, y_pred, target_names=target_names))
print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))    #在对角线上的点越多，预测的数值越准确
 
#################################################################################
#Qualitative evaluation of the predictions using matplotlib
 
def plot_gallery(images, titles, h, w, n_rows=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_rows))  #作为背景，在figure上面画图
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_rows * n_col):
        plt.subplot(n_rows, n_col, i + 1)
        plt.imshow(images[i].reshape((h,w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

#plot the result of the prediction on a portion of the test set

def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i].r]

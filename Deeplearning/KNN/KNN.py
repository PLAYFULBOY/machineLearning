# coding:utf-8
#KNN算法，选择一个k值，选择K个与待预测样本最接近的数据，少数服从多数的原则，
import math
#计算两点之间的距离
#pow是power的缩写，有次幂的意思
def ComputeEuclideanDistance(x1,x2,y1,y2):
    
    d = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2)) 
    return d
d_ag = ComputeEuclideanDistance(3, 104, 18, 90)
d_bg = ComputeEuclideanDistance(2, 100, 18, 90)
d_cg = ComputeEuclideanDistance(1, 81, 18, 90)
d_dg = ComputeEuclideanDistance(101, 10, 18, 90)
d_eg = ComputeEuclideanDistance(98, 5, 18, 90)
d_fg = ComputeEuclideanDistance(98, 2, 18, 90)
# print("d_ag: " + str(d_ag))
print "d_ag:" , d_ag
print "d_bg:" , d_bg
print "d_cg:" , d_cg
print "d_dg:" , d_dg
print "d_eg:" , d_eg
print "d_fg:" , d_fg
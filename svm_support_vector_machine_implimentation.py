# -*- coding: utf-8 -*-
"""SVM_Support vector machine implimentation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/167PpOaAYexb2Niy6-pn9EYycyYVR7ltj

Support vector machine
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs
X,y = make_blobs(n_samples=40,centers=2, random_state=20)
clf=svm.SVC(C=1.0,kernel='linear')
clf.fit(X,y)
print(X)
print(y)
N=40
#color=np.random.rand(N)
color=y
plt.scatter(X[:,0],X[:,1],c=color)
plt.show()
newDataSet=[[1001,3]]
#print(clf.predict(newDataSet))

#get the current axis

ax=plt.gca()
xlim=ax.get_xlim()
ylim=ax.get_ylim()
print('create evoluation model')
print(xlim)
print(ylim)
xx= np.linspace(xlim[0],xlim[1],30)
yy= np.linspace(ylim[0],ylim[1],30)
print(xx)
plt.plot(xx,yy,'r+')
plt.show()
#print(yy)


##meshgrid create two grids X and Y 

print('mesh grid creation')
XX,YY=np.meshgrid(xx,yy)
print(XX)


plt.plot(XX,YY,'o')
plt.show()

#na.vstack is array reshape function 
xy=np.vstack(np.vstack([XX.ravel(),YY.ravel()])).T
print(xy)
z=clf.decision_function(xy).reshape(XX.shape)
#plot decision boundry and margins
ax.contour(XX, YY, z, color='K', level=[-1,0,1],alpha=0.5)
ax.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s=100,linewidth=1,facecolors='none')
plt.show()


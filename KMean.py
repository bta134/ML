# -*- coding: utf-8 -*-

from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets


plt.rcParams['figure.figsize'] = (16,10)
plt.style.use('ggplot')

#data = pd.read_csv('dataset.csv')
iris = datasets.load_iris()
data = iris.values

print(data)
#data.head()
#data1 = data['V1'].values
#data2 = data['V2'].values
data1 = data[:,1]
data2 = data[:,2]

X = np.array(list(zip(data1,data2)))
plt.scatter(data1,data2, c='red',s=7)

def dist(a,b,ax=1):
    return np.linalg.norm(a-b,axis=ax)

k=3

C_x=np.random.randint(0,np.max(X)-20,size=k)
C_y=np.random.randint(0,np.max(X)-20,size=k)
C=np.array(list(zip(C_x,C_y)),dtype=np.float32)
print(C)
plt.scatter(data1,data2,c='green',s=7)
plt.scatter(C_x,C_y,marker='*',s=200,c='blue')

C_old=np.zeros(C.shape)
clusters=np.zero(len(X))
error=dist(C, C_old, None)
while error !=0:
    for i in range(len(X)):
        distances = dist(X[i],C)
        cluster=np.argmin(distances)
        clusters[i]=cluster
        
    C_old=deepcopy(C)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j]==i]
        C[i]=np.mean(points,axis=0)
    error=dist(C, C_old, None)

colors = ['r','g','b','y','c','m']
fig, ax = plt.subplots()
for i in range(k):
        points=np.array([X[j] for j in range(len(X)) if clusters[j]==i])
        ax.scatter(points[:,0],points[:,1],s=7, c=colors[i])
ax.scatter(C[:,0], C[:,1], marker='*',s=200,c='#050505')





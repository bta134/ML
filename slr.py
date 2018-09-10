# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

X = np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
Y = np.array([[49,50,51,54,58,59,60,62,63,64,66,67,68]]).T

plt.plot(X,Y,'ro')
#plt.axis([140,190,45,75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one,X),axis = 1)

A = np.dot(Xbar.T,Xbar)
b = np.dot(Xbar.T,Y)
w = np.dot(np.linalg.pinv(A),b)

print(Xbar)
print(A)
print(b)
print(w)

w0 = w[0][0]
w1 = w[1][0]
x0 = np.linspace(145,185,2)
y0 = w0 + w1*x0

plt.plot(X.T,Y.T,'ro')
plt.plot(x0,y0)
plt.axis([140,190,45,75])
plt.xlabel('Height (cm)')
plt.ylabel('Height (kg)')
plt.show()

y1 = w1*155 + w0
y2 = w1*165 + w0
print(y1)
print(y2)

regr = linear_model.LinearRegression(fit_intercept=False)
regr.fit(Xbar,Y)

print(regr.coef_)
print(w.T)

# -*- coding: utf-8 -*-


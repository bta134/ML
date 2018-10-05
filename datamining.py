import numpy as np
import pandas as pd
import datetime

def compare2Array(a, b):
    if (a==b):
        return True
    else:
        return False

#st = time.time()
lines = open('dataset.csv').read().splitlines()
#et = time.time()
data = []


ts1 = datetime.datetime.now()
for l in lines:
    dt = []
    for i in l:
        if (i=='' or i=='\n'):
            break
        if (i!=' '):
            dt.append(i)
        #print(dt)
   # print(transactions)
    data.append(dt)
#for d in data:
    #print(d)
tf1 = datetime.datetime.now()
te1 = tf1 - ts1
print (ts1)
print (tf1)
print(te1)
print(len(data))
print(data[0])



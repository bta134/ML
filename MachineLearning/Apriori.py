# -*- coding: utf-8 -*-
import numpy as np


def buildGraph(f):
    g = {}
    lines = open(f).read().splitlines()
    id=''
    for l in lines:
       itemset=''
       for i in range(len(l)):          
           if(l[i]!=',' and l[i]!=' ' and l[i]!='\n'):                
               id=id + l[i]                
               continue
           if(l[i]==',' or l[i]==' ' or l[i]=='\n'):
               if(id!='' and id!=' '):
                   if not (itemset +' '+ id) in g:
                       g[id]=1
                       itemset+=' ' +id
                   if (id in g):
                       g[id]+=1
                       itemset+=' ' +id
                   id=''
    return g

#graph = buildGraph('retail.txt')
graph1 = buildGraph('dataset.csv')
print(graph1)
print(graph1.get('1'))


    
#    
#file='DataSet\\retail.txt'
#file2='dataset.csv'
#t=read(file2)
#
#c=count(t)
#print(len(c))
#c1=removeSup(c,2)
#print(len(c1))
#print(c1)
#c2=combine(c1)
#print(len(c2))
#print(c2)
#c3=countIn(c2,file2)
#print(len(c3))
##print(c3)


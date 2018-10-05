# -*- coding: utf-8 -*-
import datetime

def count(t):
    e=[[]]
    for i in range(len(t)):
        if (e==[[]]):
            e[0]=[t[i],1]                     
            continue
        found = False
        try:
            for eindex in range(len(e)):                
               if(e[eindex][0]==t[i]):
                    found = True
                    e[eindex][1]+=1
                    break                           
        except:
                print("Something wrong")
       
        if (found==False):
            a = [t[i],1]
            e.append(a)
    return e

def read(f):
    lines = open(f).read().splitlines()    
    data = []
    id=''
    for l in lines:       
       for i in l:          
           if(i!=',' and i!=' ' and i!='\n'):                
               id=id + i                
               continue
           if(i==',' or i==' ' or i=='\n'):
               data.append(id)
               id=''                   
               continue
       data.append(id)
       id=''
    return data

def removeSup(d,minsup):
    for i in d:
        if(i[1]<minsup):
            d.remove(i)
    return d

def combine(d):
    rs=[]
    item=[]
    for i in d:        
        for j in d:            
            if(i[0]!=j[0]):
                if(i[0]<j[0]):                    
                    item=[i[0],j[0]]
                else:
                    item=[j[0],i[0]]
                if(rs.count(item)==0):
                    rs.append(item)                    
    return rs

def countIn(v,f):
    lines = open(f).read().splitlines()
    print(lines)
    data = []
    linecount=0
    
    for l in lines:                                             
                ccount=0                   
                for i in v:                        
                    for e in i:                         
                        id='' 
                        
                        for c in range(len(l)):    
                            if(l[c]!=',' and l[c]!=' ' and l[c]!='\n'):     
                                id=id + l[c]
                            if(l[c]==',' or l[c]==' ' or l[c]=='\n' or c==len(l)-1):                         
                                if(e==id):                            
                                    ccount+=1
                                    id=''
                                    break
                                else:
                                    id=''                                                            
                    if(ccount==len(i)):
                        linecount+=1
                        ccount=0
                        break
    if(linecount>0):                    
        data.append([i,linecount])
        linecount=0               
    return data

file='DataSet\\retail.txt'
ts = datetime.datetime.now()
t=count(read(file))
te = datetime.datetime.now()

print(ts)
print(te)
print(te-ts)
print(len(t))
t = removeSup(t,2)
print(len(t))
t=countIn(t,file)
print(t[0])
print(len(t))
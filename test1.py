# -*- coding: utf-8 -*-
tt=['2','2','3','1','2','1','1','3','11','12']

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

print(count(tt))

t='2,12'
print(len(t))
for c in range(len(t)):
    print(c)
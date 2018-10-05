# -*- coding: utf-8 -*-
def countIn(v,f):
    lines = open(f).read().splitlines()
    print(lines)
    data = []
    linecount=0
    
    for l in lines:
                print('line')
                print(l)                              
                ccount=0    
                
                for i in v:        
                    print('i')
                    print(i)
                    
                    for e in i:                         
                        print('e '  + e)
                        id='' 
                        
                        for c in range(len(l)):    
                            if(l[c]!=',' and l[c]!=' ' and l[c]!='\n'):     
                                id=id + l[c]
                                print('c ' +l[c])
                                print('id ' + id)
                                   
                            if(l[c]==',' or l[c]==' ' or l[c]=='\n' or c==len(l)-1):                         
                                print('c ' + l[c])                                
                                print('id ' + id)
                                
                                if(e==id):                            
                                    print('character count')
                                    ccount+=1
                                    print(ccount)
                                    id=''
                                    break
                                else:
                                    id=''
                                    print(id)
                            
                    if(ccount==len(i)):
                        linecount+=1
                        ccount=0
                        break
    if(linecount>0):
        print('linecount')
        print(linecount)            
        data.append([i,linecount])
        linecount=0
                
    return data

print(countIn([['2','12']],'dataset.csv'))

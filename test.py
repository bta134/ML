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

dt = [['1', 177], ['2', 266], ['3', 549], ['4', 8], ['5', 19], ['6', 295], ['7', 151]]
print(combine(dt))



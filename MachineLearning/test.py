import numpy as np;


data=[]
d=[['1', '2'], ['1', '4'], ['1', '3'], ['2', '4'], ['2', '3'], ['3', '4']]
d1=[['source0','destination0','count0'],
    ['source1','destination1','count1'],
    ['source2','destination2','count2']]



src = {}
dest ={}

src['1']=dest
dest['1']=0

src['1']=dest
dest['2']=2

src['2']=dest
dest['2']=0

src['2']=dest
dest['3']=4

class Node(object):
    def __init__(self,name):
        self.name = name
        self.count=0
        self.adjacent={}
        
    def getName(self):
        return self.name
    
    def getCount(self):
        return self.count
    
    def increaseCount(self):
        self.count+=1
    
    def getAdjacent(self):
        return self.adjacent
    
    def addNeighbor(self,neighbor,weight=0):
        if (neighbor not in self.adjacent):
            self.adjacent[neighbor]=weight
        if (neighbor in self.adjacent):
            self.adjacent[neighbor]=weight
    
    def getWeight(self,neighbor):
        return self.adjacent[neighbor]
    
class Graph:
   def __init__(self):
       self.vertices={}
       
   def addNode(self,node):
        n = Node(node)
        self.vertices[node]=n
    
   def getNode(self,n):
       if (n in self.vertices):
           return self.vertices[n]
       else:
           return None
   def getNodes(self):
       return self.vertices.keys()
    
   def setEdge(self,src,dest,weight=0):
       if (src in self.vertices):
           self.vertices[src].addNeighbor(dest,weight)
       else:
           self.addNode(src)
           self.vertices[src].addNeighbor(dest,weight)
           
def buildGraph(f):
    g = Graph()
    
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
                   if not id in g.vertices:
                       print("Not in graph " + id)
                       g.addNode(id) 
#                       print(g.vertices[id])
                       itemset=itemset + ' ' +id
                       id=''
                       continue
                   if (id in g.vertices):
                       print("In graph " +id)
                       g.vertices[id].increaseCount()
                       print(g.vertices[id].getCount())
                       itemset+=' ' +id
                       id=''
    id=''
    return g

#graph = buildGraph('retail.txt')
graph1 = buildGraph('dataset.csv')
#for i in graph1.vertices:
#    for j in i:    
#        print(j)
#print(graph1.vertices)
#print(graph1.get('1'))
#                
                
        

# -*- coding: utf-8 -*-
import pydotplus
from sklearn import tree
import collections

X=[[18,15,0],
   [177,42,0],
   [136, 35,1],
   [174,65,0],
   [141,28,1],
   [181,70,1]]

Y = ['approved','disapproved','disapproved','approved','disapproved']

data_feature_names = ['grade','fitness','voice pitch']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('blue','red')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('appovabletree.png')
clf=clf.fit(X,Y)
prediction=clf.predict([[173,63,0]])
print(prediction)


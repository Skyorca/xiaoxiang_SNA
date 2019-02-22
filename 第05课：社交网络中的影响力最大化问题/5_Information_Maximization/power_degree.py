import numpy as np
import networkx as nx


def get_power_degrees(g, centerid):
    num = g.degree(centerid)
    for neighbor in g.neighbors(centerid):
        num += len(list(g.neighbors(neighbor)))
    return num   #一阶邻居和二阶邻居数目和

g = nx.karate_club_graph()
'''
nodeid = 20 
print(len(list(g.neighbors(nodeid))))
res = get_power_degrees(g, nodeid)
print(res)
'''

for node in g.nodes():
    res = get_power_degrees(g, node)
    print(node, res)
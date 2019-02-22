import networkx as nx
import numpy 
import itertools

G = nx.karate_club_graph()
print(G.nodes())
r=0.8
max_iter=100
nodes = list(G.nodes()) 
nodes_i = {nodes[i]: i for i in range(0, len(nodes))}
print(nodes_i) #目的是变成纯数字计算

sim_prev = numpy.zeros(len(nodes))  #随便初始化一个就行
sim = numpy.identity(len(nodes))

for i in range(max_iter):
    sim_prev = numpy.copy(sim)
    num = 0
    for u in nodes:
        for v in nodes:
            if u==v:  continue
            s_uv = 0
            for u_n in G.neighbors(u):
                for v_n in G.neighbors(v):
                    s_uv += sim_prev[nodes_i[u_n]][nodes_i[v_n]]
            sim[u][v] = r*s_uv / (len(list(G.neighbors(u)) * len(list(G.neighbors(v))))+0.0000000001)
print(sim)


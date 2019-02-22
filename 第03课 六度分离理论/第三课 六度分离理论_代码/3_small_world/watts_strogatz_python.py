'''
This is the python code of Watts Strogatz model to creat a small world
'''
import random as rand
import matplotlib.pyplot as plt
import networkx as nx
      
def smallWordGraph(n,k,p):
    #prepare work
    k = k // 2 #divisible
    all_possible_edges = []
    edges = []
    for a in range(n):
        for b in range(a):
            all_possible_edges.append((b,a))    
    #make a regular graph
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i-k,i):
            if j < 0:
                edges.append((i,j+n))
            else:
                edges.append((i,j))
    #randomize a graph
    new_edges = list(edges)
    for i in range(len(edges)):
        if rand.random() < p:
            new_edge = all_possible_edges[rand.randint(0,len(all_possible_edges)-1)]
            # no duplicate edges
            while new_edge in new_edges:
                new_edge = all_possible_edges[rand.randint(0,len(all_possible_edges) - 1)]
            new_edges[i] = new_edge
    G.add_edges_from(new_edges)
    return G
                
G = smallWordGraph(20,4,0.8)
#G = nx.watts_strogatz_graph(20,4,0.5)
nx.draw(G,with_labels=True,node_color='y')
plt.show()



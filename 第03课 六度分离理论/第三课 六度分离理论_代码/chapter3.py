import networkx as nx
import matplotlib.pyplot as plt
import random

'''
第三章 小世界理论
生成小世界模型 及 各种中心度量
'''

def generate_regular_network(n,k):
    '''
    '''
    k = k // 2
    edges = []
    for i in range(20):
        for j in range(i-k,i):
            if j < 0: edges.append((i,j+n))
            else: edges.append((i,j))
    G = nx.Graph()
    G.add_edges_from(edges)
    return G
    #nx.draw(G)
    #plt.show()

def generate_WS_Model(n,k,p):
    G = generate_regular_network(n,k)
    all_possible_edges = [] #无环的，无向的(a,b)==(b,a)
    for a in range(n):
        for b in range(a):
            all_possible_edges.append((b,a))
    edges = list(G.edges())
    for idx in range(len(edges)):
        if random.random()<p:
            new_edge = all_possible_edges[random.randint(0,len(all_possible_edges)-1)]
            while new_edge in edges:
                new_edge = all_possible_edges[random.randint(0,len(all_possible_edges)-1)]
            edges[idx] = new_edge
    G_new = nx.Graph()
    G_new.add_edges_from(edges)
    centralityDict = nx.degree_centrality(G_new)
    closenessDict = nx.closeness_centrality(G_new)
    betweennessDict = nx.betweenness_centrality(G_new)
    print(sorted(centralityDict.items(), key=lambda x: x[1], reverse=True))
    print(sorted(closenessDict.items(), key=lambda x: x[1], reverse=True))
    print(sorted(betweennessDict.items(), key=lambda x: x[1], reverse=True))
    #nx.draw(G_new,with_labels=True)
    #plt.show()



generate_WS_Model(20,4,0.8)
    
    
    





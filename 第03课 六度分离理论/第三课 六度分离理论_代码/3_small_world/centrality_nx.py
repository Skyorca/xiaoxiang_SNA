import networkx as nx
centralityDict = {}

G=nx.karate_club_graph()

#centralityDict = nx.degree_centrality(G)
centralityDict = nx.closeness_centrality(G)
#centralityDict = nx.betweenness_centrality(G)

#for key, value in centralityDict.items():
#    print('{key}:{value}'.format(key = key, value = value))

print(sorted(centralityDict.items(), key=lambda x: x[1], reverse=True))


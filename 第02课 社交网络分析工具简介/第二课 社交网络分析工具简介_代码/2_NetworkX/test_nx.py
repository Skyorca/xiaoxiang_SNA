import networkx as nx

G=nx.karate_club_graph()

print(nx.shortest_path(G,source=1,target=22))

print(nx.number_connected_components(G))
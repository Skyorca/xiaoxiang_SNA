import networkx as nx
G=nx.karate_club_graph() 

print("Node Degree") 

for v in G: 

    print('%s %s' % (v+1,G.degree(v))) 

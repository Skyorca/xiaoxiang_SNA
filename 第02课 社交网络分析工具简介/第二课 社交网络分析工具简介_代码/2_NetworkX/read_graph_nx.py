import networkx as nx

filename = r"F:\xiaoxiang_proj\sns_datasets\karate\karate_edges.txt"
G=nx.read_edgelist(filename, create_using=nx.Graph)
#G=nx.read_edgelist(filename, create_using=nx.DiGraph)
print(G.edges())
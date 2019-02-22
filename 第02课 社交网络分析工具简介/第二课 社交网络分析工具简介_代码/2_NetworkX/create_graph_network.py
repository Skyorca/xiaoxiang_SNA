import networkx as nx
G = nx.Graph()

G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node('span')
G.add_nodes_from('span')

print('the number of nodes is:', G.number_of_nodes())
print('the number of edges is:', G.number_of_edges())
print('These are nodes in the graph:', G.nodes())
print('These are edges in the graph:', G.edges())

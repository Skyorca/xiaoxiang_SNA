import networkx as nx

def common_neighbors(mygraph, i,j):
    return len(set(mygraph.neighbors(i)).intersection(set(mygraph.neighbors(j))))

G = nx.karate_club_graph()

print(common_neighbors(G, 0, 1))

# Compute the Jaccard coefficient of all node pairs in ebunch.
preds = nx.jaccard_coefficient(G, [(0, 1), (2, 3)])

# Compute the Adamic-Adar index of all node pairs in ebunch.
preds = nx.adamic_adar_index(G, [(0, 1), (2, 3)])

'''
# Compute the preferential attachment score of all node pairs in ebunch.
preds = nx.preferential_attachment(G, [(0, 1), (2, 3)])
'''
for u, v, p in preds:
    print('(%d, %d) -> %.8f' % (u, v, p))



'''
def similarity(graph, i, j, method):
	if method == "common_neighbors":
		return len(set(graph.neighbors(i)).intersection(set(graph.neighbors(j))))
	elif method == "jaccard":
		return len(set(graph.neighbors(i)).intersection(set(graph.neighbors(j))))/float(len(set(graph.neighbors(i)).union(set(graph.neighbors(j)))))
	elif method == "adamic_adar":
		return sum([1.0/math.log(graph.degree(v)) for v in set(graph.neighbors(i)).intersection(set(graph.neighbors(j)))])
	elif method == "preferential_attachment":
		return graph.degree(i) * graph.degree(j)
	elif method == "friendtns":
		return round((1.0/(graph.degree(i) + graph.degree(j) - 1.0)),3)
'''
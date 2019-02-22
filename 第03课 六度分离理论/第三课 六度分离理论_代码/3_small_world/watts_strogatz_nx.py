import networkx as nx
import matplotlib.pyplot as plt

n=20
k=4
p=0.8
g = nx.watts_strogatz_graph(n, k, p)
print(g.edges())

nx.draw(g,with_labels=True,node_color='y')
plt.show()
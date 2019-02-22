import networkx as nx
import numpy as np
import random
import matplotlib .pyplot as plt

max_iter_num = 5
g = nx.karate_club_graph()

# init the graph with random edge weight and set the inactive status
for edge in g.edges:
    g.add_edge(edge[0], edge[1], weight=random.uniform(0,1))
for node in g:
    g.add_node(node, state = 0)

seed = 33
g.node[seed]['state'] = 1

activated_graph = nx.Graph() 
activated_graph.add_node(seed)

all_active_nodes = []
all_active_nodes.append(seed)

start_influence_nodes = []
start_influence_nodes.append(seed)

for i in range(max_iter_num):
    new_active = list()
    tl = '%s time' % i + ' %s nodes' % len(all_active_nodes)
    print(tl)

    plt.title(tl)
    nx.draw(activated_graph, with_labels=True)
    plt.show()

    for v in start_influence_nodes:
        for nbr in g.neighbors(v): 
            if g.node[nbr]['state'] == 0:
                edge_data = g.get_edge_data(v, nbr)
                if random.uniform(0, 1) < edge_data['weight']:
                    g.node[nbr]['state'] = 1
                    new_active.append(nbr)
                    activated_graph.add_edge(v, nbr)

    start_influence_nodes.clear()
    start_influence_nodes.extend(new_active)
    all_active_nodes.extend(new_active)
    print('all actived nodes: ', all_active_nodes)
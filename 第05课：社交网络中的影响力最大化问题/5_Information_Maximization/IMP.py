import networkx as nx
import numpy as np
import random
# the influence maximazation problem

def influence_computation_extend(orig_seeds, newnode, g, sample_num=100):
    old_influence = influence_computation_IC(seeds, g, sample_num=1)



# calcualte the influence score of some seeds
def influence_computation_IC(orig_seeds, newnode, g, sample_num=100):
    # Input: seeds: [] the seed list
    #        g: the network 
    #        sample_num: try to influence others many times
    # Return:
    #        the actived number on average sample_num times
    influence = 0
    for i in range(sample_num):
        active_nodes = list()
        active_nodes.extend(seeds)
        # if a node is actived 
        status = np.zeros(g.number_of_nodes())
        for node in active_nodes:
            status[node] = 1
        
        while len(active_nodes) != 0:
            influence = influence + 1
            current_node = active_nodes.pop(0)
            for nbr in g.neighbors(current_node):  # 得到激活节点的邻接点
                if status[nbr] == 0:
                    wt = g.get_edge_data(current_node, nbr)
                    if random.uniform(0, 1) < wt['weight']:
                        status[nbr] = 1
                        active_nodes.append(nbr)
                        
    return influence/sample_num
    
if __name__ == '__main__':
    K = 3
    g = nx.karate_club_graph()
    for edge in g.edges:
        g.add_edge(edge[0], edge[1], weight=random.uniform(0,1))

    seeds = list()
    ative_dict = {}
    for i in range(K):
        f = np.zeros(g.number_of_nodes())
        state = np.zeros(g.number_of_nodes())
        for v in seeds: ative_dict[v] = 1
        
        for v in g.nodes:
            node_list = seeds.copy()
            if (v not in ative_dict):
                node_list.append(v)
                f[v] = influence_computation_IC(node_list, g) - influence_computation_IC(seeds, g)
        print(f)    
        seeds.append(f.argmax())
    print(seeds)
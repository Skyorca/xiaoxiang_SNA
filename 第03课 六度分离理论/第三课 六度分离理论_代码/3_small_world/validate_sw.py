import numpy as np
import networkx as nx

g = nx.karate_club_graph()
length = nx.all_pairs_shortest_path_length(g)

all_len = 0
pair_num = 0
for temp in length:
    [start, disdict] = temp
    for key, value in disdict.items():
        if( start == key ): continue
        pair_num += 1
        all_len += value 

#print(pair_num)
print(all_len/pair_num)
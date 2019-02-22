# Read the edge list and store the graph as adjancency list.

import numpy as np
filename = r"F:\xiaoxiang_proj\sns_datasets\karate\karate_edges.txt"

n = 34
mydict = {}

with open(filename) as f:    
    for line in f.readlines():
        temp_list = line.split()
        start = temp_list[0]
        end = temp_list[1]

        # store the edge list of start node 
        if( start not in mydict ): mydict[start] = []
        start_list = mydict[start]
        start_list.append(end)
        mydict[start] = start_list

        # store the edge list of end node 
        if( end not in mydict ): mydict[end] = []
        end_list = mydict[end]
        end_list.append(start)
        mydict[end] = end_list
        
print(mydict)
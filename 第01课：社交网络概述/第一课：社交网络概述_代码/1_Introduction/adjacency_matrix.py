# Read the edge list and store the graph as adjancency matrix.

import numpy as np
filename = r"F:\xiaoxiang_proj\sns_datasets\karate\karate_edges.txt"

n = 34
adjacencyMatrix = np.zeros((n, n))

with open(filename) as f:    
    for line in f.readlines():
        temp_list = line.split()
        adjacencyMatrix[int(temp_list[0])-1][int(temp_list[1])-1]=1
        adjacencyMatrix[int(temp_list[1])-1][int(temp_list[0])-1]=1
        
print(adjacencyMatrix)

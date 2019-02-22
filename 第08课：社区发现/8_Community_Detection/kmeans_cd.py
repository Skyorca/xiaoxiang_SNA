import networkx as nx
from sklearn import cluster
from sklearn.metrics.cluster import normalized_mutual_info_score

groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
print('ground truth is', groundTruth)

def graphToEdgeMatrix(G): 
    # Initialize Edge Matrix 
    edgeMat = [[0 for x in range(len(G))] for y in range(len(G))] 
    
    # For loop to set 0 or 1 ( diagonal elements are set to 1) 
    for node in G: 
        tempNeighList = G.neighbors(node) 
        for neighbor in tempNeighList:         
            edgeMat[node][neighbor] = 1 
            edgeMat[node][node] = 1 
    return edgeMat

G = nx.karate_club_graph()
edgeMat = graphToEdgeMatrix(G)

kmeans = cluster.KMeans(n_clusters=2, n_init=2)
kmeans.fit(edgeMat)

print(list(kmeans.labels_))

ans  = normalized_mutual_info_score(list(groundTruth), list(kmeans.labels_))
print(ans)
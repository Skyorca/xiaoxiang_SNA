import networkx as nx
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def converte_to_binary(mylist, mid=0.5):
    for i in range(len(mylist)):
        if( mylist[i] > mid ): mylist[i] = 1.0
        else: mylist[i] = 0
    return mylist

G = nx.karate_club_graph()
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]

max_iter = 5
nodes = list(G.nodes()) 
nodes_i = {nodes[i]: i for i in range(0, len(nodes))}

vote = np.zeros(len(nodes))
X_train, X_test, y_train, y_test = train_test_split(nodes, groundTruth, test_size=0.7, random_state=1)

vote[X_train] = y_train
vote[X_test] = 0.5

for i in range(max_iter):
    vote_old = np.copy(vote)
    for u in G.nodes():
        if( u in X_train ): continue
        temp = 0.0
        for item in G.neighbors(u):
            temp = temp + vote_old[nodes_i[item]]
        vote[nodes_i[u]] = temp/len(list(G.neighbors(u)))
    print(vote)

res = converte_to_binary(vote)
print(res)
pred = res[X_test]

print(accuracy_score(y_test, pred))
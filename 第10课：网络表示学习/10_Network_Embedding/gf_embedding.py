# Traditional Network embedding method: Graph Factorization
import numpy as np
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from matrix_decomposition import mf

from sklearn.metrics import accuracy_score

G = nx.karate_club_graph()
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]

def graph2matrix(G):
    n = G.number_of_nodes()
    res = np.zeros([n,n])
    for edge in G.edges():
        res[int(edge[0])][int(edge[1])] = 1 
        res[int(edge[1])][int(edge[0])] = 1
    return res

G = nx.karate_club_graph()
G = graph2matrix(G)
[U, V] = mf(G, 128)


X_train, X_test, y_train, y_test = train_test_split(U, groundTruth, test_size=0.7, random_state=1)
clf = SVC(kernel="linear")
clf.fit(X_train, y_train)
pred = clf.predict(X_test) 
print(pred)

print(accuracy_score(y_test, pred))
import networkx as nx
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from scipy import sparse

G = nx.karate_club_graph()
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]

def graph2matrix(G):
    n = G.number_of_nodes()
    res = np.zeros([n,n])
    for edge in G.edges():
        res[int(edge[0])][int(edge[1])] = 1 
        res[int(edge[1])][int(edge[0])] = 1
    return res

def build_propagation_matrix(G):
    """ LGC computes the normalized Laplacian as its propagation matrix"""
    degrees = G.sum(axis=0)
    degrees[degrees==0] += 1  # Avoid division by 0
    
    D2 = np.identity(G.shape[0])
    for i in range(G.shape[0]):
        D2[i,i] = np.sqrt(1.0/degrees[i])
    
    S = D2.dot(G).dot(D2)
    return S

def vec2label(Y):
    '''Input: Y: [n,c] labels
       Output: res: [n,1] single labels 
    '''
    return np.argmax(Y,axis=1)

edgematrix = graph2matrix(G)
S = build_propagation_matrix(edgematrix)

alpha = 0.8
cn = 2
max_iter = 10

F = np.zeros([G.number_of_nodes(),2])
X_train, X_test, y_train, y_test = train_test_split(list(G.nodes()), groundTruth, test_size=0.7, random_state=1)
for (node, label) in zip(X_train, y_train):
    F[node][label] = 1

Y = F
print(Y)

for i in range(max_iter):
    F_old = np.copy(F)
    F = alpha*np.dot(S, F_old) + (1-alpha)*Y
    
res = vec2label(F)
pred = res[X_test]
print(accuracy_score(y_test, pred))

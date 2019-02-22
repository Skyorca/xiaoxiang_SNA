import networkx as nx
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

G = nx.karate_club_graph()
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
#print('ground truth is', groundTruth)

def graph2matrix(G):
    n = G.number_of_nodes()
    res = np.zeros([n,n])
    for edge in G.edges():
        res[int(edge[0])][int(edge[1])] = 1 
        res[int(edge[1])][int(edge[0])] = 1
    return res

edgeMat = graph2matrix(G)

X_train, X_test, y_train, y_test = train_test_split(edgeMat, groundTruth, test_size=0.7, random_state=1)
#clf = KNeighborsClassifier(n_neighbors=3)
clf = SVC(kernel="linear")
#clf = QuadraticDiscriminantAnalysis()

clf.fit(X_train, y_train)
predicted= clf.predict(X_test) 
print(predicted)

score = clf.score(X_test, y_test)
print(score)
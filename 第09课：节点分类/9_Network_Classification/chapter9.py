import networkx as nx
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from scipy import sparse

'''
chapter9  网络节点分类 （半监督方法: 都有种子）
KNN (太简单没有实现)
wvRN: weighted-vote relational neighbor （实现）
label propagation （基于wvRN的改进版，实现）
注意本节课的方法适用于一切网络，并不局限于社交网络
'''

### 全局量的设定 ###
G = nx.karate_club_graph()
groundTruth = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
nodes = list(G.nodes())
nodes_i = {nodes[i]:i for i in range(len(nodes))} #mapping 一开始就做


def Graph2Adj(graph):
    '''
    返回一个numpy矩阵，表示图的邻接矩阵
    %时刻注意图的边，节点的原始类型，要不要转换成常用的比如Int list等等
    '''
    node_num = graph.number_of_nodes()
    Adj = np.zeros([node_num, node_num])
    for edge in graph.edges():
        Adj[nodes_i[int(edge[0])]][nodes_i[int(edge[1])]] = 1  #注意要把edge[0]转换成整数！
        Adj[nodes_i[int(edge[1])]][nodes_i[int(edge[0])]] = 1  
    return Adj


def converte_to_binary(mylist, mid=0.5):
    for i in range(len(mylist)):
        if( mylist[i] > mid ): mylist[i] = 1.0
        else: mylist[i] = 0
    return mylist


def wvRN(adjmat, F, max_iter):
    '''
    '''
    degree = adjmat.sum(axis=0) #对每行求和，就是求每个节点的度数
    degree[degree==0] += 1 #防止除以0
    d = degree**(-1)
    for iter_time in range(max_iter):
        F_ = adjmat.dot(F.T)
        F_ = d*F_
        F  = np.copy(F_)
      # print("{} time: F is".format(iter_time+1),F)
    res = converte_to_binary(F)
    return res




if __name__ == "__main__":
    x_train, x_test, y_train, y_test = train_test_split(list(G.nodes()), groundTruth, test_size=0.7, random_state=1)
    
    ### 做F的初始化：把training set里面的信息加进去，正类是1负类是0 ，剩下值为0.5的都是test set ###
    F = np.zeros(G.number_of_nodes())
    F = np.array([0.5 for x in F])  
    for(node,label) in zip(x_train, y_train):
        if label == 1: F[nodes_i[node]] = 1
        elif label == 0: F[nodes_i[node]] = 0
    print("Original F is: ",F)
    G_adj = Graph2Adj(G) #get 邻接
    for iter_time in range(1,11,1):
        res = wvRN(G_adj,F,iter_time)
        pred = res[x_test]
        print("After iter {} time: ".format(iter_time),accuracy_score(y_test, pred))

'''
After iter 1 time:  0.625
After iter 2 time:  0.9166666666666666
After iter 3 time:  0.7916666666666666
After iter 4 time:  0.8333333333333334
After iter 5 time:  0.7083333333333334
After iter 6 time:  0.75
After iter 7 time:  0.5
After iter 8 time:  0.4166666666666667
After iter 9 time:  0.4166666666666667
After iter 10 time:  0.4166666666666667
由此可见，这个并不是迭代越多次越好，最终converge
可能对于大型网络，由于六度分隔理论，iter after 6 times could be better
'''

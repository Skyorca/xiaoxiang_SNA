import networkx as nx
import math
import random

'''
chapter8 community detection社区发现（VS 社区搜索community search：从一点出发搜索）
结果与modularity里面的内置算法相对比，证明是成功的
完全不使用numpy的骚操作
'''

G = nx.karate_club_graph()
K = 2
# 使用内置的kernighan_lin_bisection二分算法得到的结果，可与自己算法得到的相对比
# ({0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 17, 19, 21}, {8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33})
max_iter = 10


def dist(vect1, vect2):
    '''
    计算两个m-dim向量的距离
    '''
    assert(len(vect1) == len(vect2))
    distance = math.sqrt(sum([(vect1[i]-vect2[i])**2 for i in range(len(vect1))]))
    return distance


def K_means_cosine():
    '''
    '''
    nodes = list(G.nodes())
    nodes_i = {nodes[i]:i for i in range(len(nodes))} #同样是做一个节点index映射
    cosine = [[0 for x in range(len(G))]for y in range(len(G))] #通过两次列表推导建立cosine分值矩阵
    for u in nodes:
        for v in nodes:
            N_u = set(G.neighbors(u))
            N_v = set(G.neighbors(v))
            tmp_cosine = len(N_u.intersection(N_v))/math.sqrt(len(N_u)*len(N_v))
            cosine[nodes_i[u]][nodes_i[v]] = tmp_cosine
    '''
    cosine matrix
      a  b  c  d  e
    a n1 n2 n3 n4 n5
    b m1 m2 m3 m4 m5
    c      ...
    d      ...
    e      ...
    每一行都是节点a的特征
    '''
    classes = [[]for x in range(K)] #要分几类就建立几个空列表
    seed_ = [random.randint(0,34) for i in range(K)] #选两个随机的种子节点编号
    seed  = [cosine[seed_[0]],cosine[seed_[1]]] #每个种子变成向量
    print("original center\n",seed[0],"\n",seed[1],"\n========================================\n")
    for iter_time in range(max_iter):
        ### 首先根据和种子点之间的度量决定分类 ###
        print("{}: new center\n".format(iter_time),seed[0],"\n",seed[1],"\n========================================\n")
        for v in G.nodes():
            if dist(cosine[nodes_i[v]],seed[0]) < dist(cosine[nodes_i[v]],seed[1]): classes[0].append(v)
            else: classes[1].append(v)
        print("{}: {} in class0 and {} in class1".format(iter_time,len(classes[0]),len(classes[1])))
        print('========================================')
        ### 更新中心点 ###
        for idx in range(K):
            center = [0 for i in range(len(nodes))]
            if len(classes[idx]) == 0: continue
            for node in classes[idx]: #别忘了这里的node是节点编号不是向量
                for i in range(len(nodes)):
                    center[i] += cosine[node][i]
            center = [i/len(classes[idx]) for i in center]
            seed[idx] = center
        if iter_time != max_iter-1: classes = [[]for x in range(K)] #别忘了在循环过程中重新清理classes列表但最后一次不用
    return classes


if __name__ == "__main__":
    c = K_means_cosine()   
    print(c)




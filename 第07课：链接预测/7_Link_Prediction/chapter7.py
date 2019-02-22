import networkx as nx
import numpy as np
import math
import random

'''
chapter7 链路预测
提供了多种度量方法与karate_club上的预测过程
'''

graph = nx.karate_club_graph()
max_iter = 100
gamma = 0.8
K = 10 #找到score最大的K条边

###g.neighbors()返回的是内存里的一个迭代对象，要用list()变成列表后可以正常显示
###g.nodes()就是list形式的节点列表，节点是int
###g.edges可以用list()包装一下但会丢失边权重属性


def compute_score(graph, i, j,method):
    '''
    '''
    if   method == 1: #CN
        return len(set(graph.neighbors(i)).intersection(set(graph.neighbors(j))))
    elif method == 2: #Jaccard
        return len(set(graph.neighbors(i)).intersection(set(graph.neighbors(j))))/float(len(set(graph.neighbors(i)).union(set(graph.neighbors(j)))))
    elif method == 3: #Adar, 单求|Gamma(z)|时用degree就行，🙅len(g.neignbors(v))
        return sum([1.0/math.log(graph.degree(v)) for v in set(graph.neighbors(i)).intersection(set(graph.neighbors(j)))])
    elif method == 4: #Shortest path
        res = nx.shortest_path_length(graph,source=i, target=j)
        return -1*res
    elif method == 5: #attri-based: pagerank
        pr = nx.pagerank(graph)
        return pr[i]*pr[j]
    elif method == 6: #Katz
        return katz(graph,i,j)


def katz(graph, i, j):
    '''
    path based method: katz，nx只有katz centrality度量，没有这种pairs的打分机制
    '''
    all_paths = list(nx.all_simple_paths(graph, source=i, target=j))
    size = {}  # key:value ----> length:length_counter
    for path in all_paths:
        length = len(path)
        if length not in size: size[length] = 0
        size[length] += 1
    ###给每个长度选取参数，要求长度越小参数越大###
    param = {} # key:value ----> length:param
    for l, c in size.items():
        if l not in param: param[l] = 1/l
    ###求和###
    score = 0
    for l,c in size.items():
        score += param[l]*c
    return score


def simrank(graph):
    '''
    nx并没有simrank方法可直接调用
    '''
    nodes = list(graph.nodes()) 
    ###目的是把原来的图节点标号映射成0，1，2...一串连续的值，方便后续处理,比如配合矩阵下标从0开始的###
    nodes_i = {nodes[i]: i for i in range(0, len(nodes))}  
    sim_prev = np.zeros(len(nodes))  #随便初始化一个就行，不重要
    sim = np.identity(len(nodes))    #simrank初始值矩阵
    ###improve: 我觉得以上sim初始化太简单，对于已经有边的simrank值应该更大###
    for edge in graph.edges():
        sim[edge[0]][edge[1]] = 5

    for iter_time in range(max_iter):
        sim_prev = np.copy(sim) #每次迭代开始统一更新
        for u in nodes:
            for v in nodes:
                if u == v: continue
                else:
                    simrank_value = 0
                    for u_nbr in graph.neighbors(u):
                        for v_nbr in graph.neighbors(v):
                            simrank_value += sim_prev[nodes_i[u_nbr]][nodes_i[v_nbr]]
                sim[nodes_i[u_nbr]][nodes_i[v_nbr]] = gamma*simrank_value/(len(list(graph.neighbors(u)))*len(list(graph.neighbors(v)))+0.001)
    return sim #numpy矩阵，可以自己根据i,j拿值

    
def get_dataset(graph):
    '''
    从karate club搞♂到training set 和test set,7:3
    机器学习方法时用。本代码不使用机器学习方法，仅仅在全图使用多种指标进行评估，所以不涉及此方法的调用
    '''
    random.seed()
    train = []
    test  = []
    for edge in graph.edges():
        if random.uniform(0,1) <= 0.7: train.append((edge[0],edge[1]))
        else: test.append((edge[0],edge[1]))
    return (train,test)


def link_pred(graph):
    edges = list(graph.edges())
    l = len(edges)
    for i in range(1,7): #依次使用六种指标
        score_dict = {}
        for u in graph.nodes():
            for v in graph.nodes():
                if u == v  or (u,v) in score_dict or (v,u) in score_dict: continue #不算self-loop以及重复计算过的(a,b)==(b,a)
                else:
                    score_dict[(u,v)] = compute_score(graph,u,v,i)
        ###挑K个最高分的出来###
        score_dict_ = sorted(score_dict.items(),key=lambda d:d[1],reverse=True) #注意返回的是列表，元素是(key,value)
        res = set()
        counter = 0
        for item in score_dict_:
            if counter < K:
                res.add(item[0])
                counter += 1
        ###评估：K个里面命中了几个###
        pred_true = 0
        for edge in res:
            if edge in edges: pred_true += 1
        print("Method {} get acc={}%".format(i,100*pred_true/K))
                    
link_pred(graph)





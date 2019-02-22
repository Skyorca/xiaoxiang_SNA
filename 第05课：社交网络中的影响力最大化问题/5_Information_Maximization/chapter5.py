import networkx as nx
import numpy as np
import random

'''
chapter5 影响力最大化模型based on IC
'''

max_iter = 100 #实验里是10000次
K        = 5   # choose k-set of nodes

graph = nx.karate_club_graph()
for edge in graph.edges():
    graph.add_edge(edge[0],edge[1],weight=random.uniform(0,1))


def Influence_compute_IC(seed):
    '''
    seed 就是 S， 传播过程就是f，所以这就是求f(S)
    '''
    influence = 0
    if len(seed) == 0: return influence
    for iter in range(max_iter): #每次模拟传播max_iter次
        result_list = list()
        result_list.extend(seed)
        checked = np.zeros(graph.number_of_nodes()) #如果被激活过了，就设为1，防止重复计算导致的受众重复问题干扰影响力的计算
        for v in result_list:
            checked[v] = 1
        ### 以下是一个BFS过程 ,之前写的IC传播模型是单源，这里是多源###
        while len(result_list)!=0:
            influence += 1   #这里的trick: 每个seed本身也计算影响力，这样求差就是每次新增加节点的影响力增值了
            current_v = result_list.pop(0)
            for v_nbr in graph.neighbors(current_v):
                if checked[v_nbr] == 0:
                    edge_data = graph.get_edge_data(current_v,v_nbr)
                    if random.uniform(0,1) < edge_data["weight"]: 
                        result_list.append(v_nbr)
                        checked[v_nbr] = 1
    
    return influence/max_iter #max_iter次模拟传播的均值

        
    





if __name__ == "__main__":
    seed = list() #最开始是空，最后是K-size
    node_list = list() #每次迭代时比seed多一个点的集合
    for k in range(K): #迭代k次，每次贪婪找点
        f = np.zeros(graph.number_of_nodes())  #装载每个节点的影响力贡献值，用差值计算，最后找最大的 
        checked = np.zeros(graph.number_of_nodes()) #检查每个节点是否被激活过
        for v in seed:
            checked[v] = 1 #seed里的肯定被激活过
        for v in graph.nodes():
            node_list.extend(seed) #先变成seed大小的
            if checked[v] == 0: 
                node_list.append(v)
                f[v] = Influence_compute_IC(node_list) - Influence_compute_IC(seed)
                checked[v] = 1
        print(f)
        seed.append(f.argmax())
    print(seed)

        
    
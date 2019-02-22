import networkx as nx
import random
import matplotlib.pyplot as plt

'''
chapter4 传播模型
影响力模型（IC LT） 感染模型SIRS
'''

###初始化图并赋予边权重###
random.seed()
g = nx.karate_club_graph()
for edge in g.edges():
    g.add_edge(edge[0],edge[1],weight=random.uniform(0,1))
'''
### IC模型对图的节点初始化###
for v in g.nodes():  #g.nodes()返回元素是整数的所有nx节点对象，可转化为列表
    g.add_node(v, state = 0)
'''
###LT 模型对图的节点初始化 ###
for v in g.nodes(): 
    g.add_node(v, state = random.uniform(0,1))
for v in g.nodes():
    count = 0
    for v_nbr in g.neighbors(v):
        count += g.node[v_nbr]["state"]
    if count >1:
        g.node[v]["state"] /= count

'''
这里的问题是如何做到每个点的邻边权重和<1，是我对每个节点采用归一化操作，这样每次迭代可保证之前操作过的所有节点的邻边权重之和不变或者
继续减少，但破坏了正态分布，会不会有影响？正态分布在这里起什么作用？
'''

def IC_Model(graph, max_iter):
    '''
    '''
    random.seed()
    all_active_nodes = []
    start_active_nodes = []
    activated_graph = nx.Graph() 
    seed = 33
    all_active_nodes.append(seed)
    start_active_nodes.append(seed)
    activated_graph.add_node(seed)
    for iter_time in range(max_iter):
        tl = "{} time {} nodes are diffused".format(iter_time+1,len(all_active_nodes))
        print(tl)
        plt.title(tl)
        nx.draw(activated_graph, with_labels=True)
        plt.show()
        new_active_nodes = list()
        for v in start_active_nodes:
            for v_ngbr in graph.neighbors(v):
                if g.node[v_ngbr]["state"] == 0:
                    edge = g.get_edge_data(v,v_ngbr)
                    if random.uniform(0,1) < edge["weight"]: 
                        g.node[v_ngbr]["state"] = 1
                        new_active_nodes.append(v_ngbr)
                        activated_graph.add_edge(v, v_ngbr)
        start_active_nodes.clear()
        start_active_nodes.extend(new_active_nodes) #新被激活的点只有下一轮迭代才有机会影响别人
        all_active_nodes.extend(new_active_nodes)


def LT_Model(graph, max_iter):
    '''
    '''
    random.seed()
    all_nodes = list(graph.nodes())
    start_active_nodes = []
    activated_graph = nx.Graph() 
    seed = 33
    start_active_nodes.append(seed)
    activated_graph.add_node(seed)
    for iter_time in range(max_iter):
        tl = "{} time {} nodes are diffused".format(iter_time+1,len(start_active_nodes))
        print(tl)
        plt.title(tl)
        nx.draw(activated_graph, with_labels=True)
        plt.show()
        new_active_nodes = start_active_nodes
        inactive_nodes = []
        this_time_add_nodes = []
        for node in all_nodes:
            if node not in start_active_nodes: inactive_nodes.append(node)
        for v in inactive_nodes:
            activate_sum = 0
            for v_nbr in graph.neighbors(v):
                if v_nbr in start_active_nodes:
                    edge_data = graph.get_edge_data(v,v_nbr)
                    activate_sum += edge_data["weight"]
            if activate_sum >= g.node[v]["state"]: 
                new_active_nodes.append(v) 
                #how 2 加边？
                #边肯定是新被激活的点与之前被激活的点之间。但是已经存在的点对未被激活的点
                #是始终有影响力的，不像IC模型一样只在下一刻产生影响力
                #所以应该是如下的加边方式
                for v_nbr in graph.neighbors(v):
                    if v_nbr in start_active_nodes:  activated_graph.add_edge(v, v_nbr)

    start_active_nodes = new_active_nodes



def update_nodes(list1, list2,list3):
    '''
    list1+list2-list3
    '''
    tmp = []
    for v in list2:
        if v not in list3: tmp.append(v)
    list1.extend(tmp)  #这里不会有重复节点


def SIRS_Model(max_iter):
    '''
    '''
    graph = nx.karate_club_graph()
    random.seed()
    #beta = random.uniform(0,1)
    #gamma  = 1/D 这里不能定义，放到循环里每次用1/iter_time表示
    #lambda_ = random.uniform(0,1)
    beta = 0.01
    gamma = 0.01
    lambda_ = 0.1
    susceptable_nodes = []
    infected_nodes = []
    recover_nodes = []
    seed = [33,1,2,3,4,5,6,7,8,9,10,11,12,23,27,17,25]
    for i in range(15):
        susceptable_nodes.append(seed[i])
    infected_nodes.append(seed[-1])
    recover_nodes.append(seed[-2])
    for iter_time in range(max_iter):
        print( "{} time {} nodes are suscepatble".format(iter_time+1,len(susceptable_nodes)))
        print( "{} time {} nodes are infected".format(iter_time+1,len(infected_nodes)))
        print( "{} time {} nodes are recover".format(iter_time+1,len(recover_nodes)))
        ### S-->I : beta ###
        new_infected_nodes = []
        new_recover_nodes  = []
        new_susceptable_nodes = []
        for i_v in infected_nodes:
            for i_v_nbr in graph.neighbors(i_v):
                if i_v_nbr in susceptable_nodes and random.uniform(0,1) < beta: 
                    new_infected_nodes.append(i_v_nbr)
        ### I-->R: gamma=1/D ###
        for i_v in infected_nodes:
            #if random.uniform(0,1) < 1/(iter_time+10): 
            if random.uniform(0,1) < gamma:
                new_recover_nodes.append(i_v)
        ### R-->S: lambda_ ###
        for r_v in recover_nodes:
            if random.uniform(0,1) < lambda_:
                new_susceptable_nodes.append(r_v)
        ### 更新susceptable: +new_susceptable_nodes -new_infected_nodes
        update_nodes(susceptable_nodes,new_susceptable_nodes,new_infected_nodes)
        ### 更新infected:    +new_infected_nodes    -new_recovery_nodes
        update_nodes(infected_nodes,new_infected_nodes,new_recover_nodes)
        ### 更新recover:     +new_recover_nodes     -new_susceptable_nodes
        update_nodes(recover_nodes,new_recover_nodes,new_susceptable_nodes)

### ???为什么我的S是一直上升的？参数问题？样本大小？






#IC_Model(g, 10)
#LT_Model(g,10)
SIRS_Model(10)

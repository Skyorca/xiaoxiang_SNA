import numpy as np

'''
社交网络分析与挖掘 chapter1 代码
数据集：边表示法（v1, v2）Undirected
返回：邻接矩阵 邻接表 图的平均度数 节点的度数 
'''

edge = 34
'''
图数据预处理：获取#edge
把数据集每行读进来得到v1 v2 所有v放进set里得到节点列表
然后sort，sort后有一个问题就是数据集顶点是不连续的，比如 1,2,5,6,7,11...等等，这样虽然得到节点总数但是
会得到奇怪的问题，比如第三个节点是节点5
可以做一个mapping: 1,2,5,6,7,11 --> 1,2,3,4,5,6，这样连续的节点列表就更好了
最后处理结果时可以查回去
'''

with open("./dataset/sns_datasets/karate/karate_edges.txt") as f:
    adj_list = {} #邻接表
    adj_matrix = np.zeros((edge,edge)) #邻接矩阵
    total_edge_num = 0
    v_dgr = {}
    for line in f.readlines():
        ###1. 邻接表表示法###
        v_list = line.split()
        v1 = v_list[0]
        v2 = v_list[1]
        if v1 not in adj_list: adj_list[v1] = []
        if v2 not in adj_list: adj_list[v2] = []
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
        ###2. 邻接矩阵表示法###
        v_list = line.split()
        v1 = int(v_list[0]) #小心！读进来的数字其实是字符
        v2 = int(v_list[1])
        adj_matrix[v1-1][v2-1] = 1 #顶点标号和矩阵下标差1
        adj_matrix[v2-1][v1-1] = 1
        ###3. 平均度数###
        total_edge_num += 1
        ###4. 节点度数列表（dict）###
        v_list = line.split()
        v1 = v_list[0]
        v2 = v_list[1]
        if v1 not in v_dgr: v_dgr[v1] = 0
        if v2 not in v_dgr: v_dgr[v2] = 0
        v_dgr[v1] += 1
        v_dgr[v2] += 1



    #print(adj_matrix)
    average_dgr = 2*total_edge_num/edge
    print(average_dgr)
    print(v_dgr)



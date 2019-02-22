import networkx as nx
import matplotlib.pyplot as plt
'''
chapter2 代码，实验networkx
'''

G = nx.Graph()
G.add_edge("咬人猫","露露",weight=10)
G.add_edge("西四","露露",weight=5)
G.add_edge("咬人猫","西四",weight=2)
G.add_edge("西四","螺主任",weight=15)
G.add_edge("呆梓","我",weight=0)

nx.draw_networkx(G)
plt.show()
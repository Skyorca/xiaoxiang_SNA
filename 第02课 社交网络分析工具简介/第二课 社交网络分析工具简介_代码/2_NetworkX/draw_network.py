import networkx as nx
import matplotlib.pyplot as plt


g = nx.karate_club_graph()
#nx.draw_networkx(g) # Draw the graph G using Matplotlib.
#nx.draw_circular(g)
nx.draw_random(g)

plt.show()

import networkx as nx
from networkx.algorithms import community


G = nx.karate_club_graph()
part = community.kernighan_lin_bisection(G,max_iter=100) #tuple of sets
#part = community.best_partition()

print(part)

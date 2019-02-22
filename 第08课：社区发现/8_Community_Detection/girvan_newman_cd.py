import networkx as nx
from networkx.algorithms import community
import itertools

G = nx.karate_club_graph()
comp = community.girvan_newman(G)
#print(tuple(sorted(c) for c in next(comp)))


# To stop getting tuples of communities once the number of communities is greater than k
k = 4
limited = itertools.takewhile(lambda c: len(c) <= k, comp)
for communities in limited:
    print(tuple(sorted(c) for c in communities)) 

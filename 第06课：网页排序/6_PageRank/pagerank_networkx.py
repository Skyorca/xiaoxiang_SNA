import networkx as nx

G = nx.karate_club_graph()
scores = nx.pagerank(G, alpha=0.9)

sorted_scores = sorted(scores.items(), key = lambda item: item[1], reverse=True)

for index, score in sorted_scores:
    print(index, score)
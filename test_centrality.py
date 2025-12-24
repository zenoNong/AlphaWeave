from graph import Graph
from centrality import weighted_degree_centrality

g = Graph()
g.add_edge("A","B",0.3)
g.add_edge("A", "C", -0.4)
g.add_edge("B", "C", 0.6)

centrality = weighted_degree_centrality(g)

print("Centrality scores:")
for node, score in centrality.items():
    print(node, score)
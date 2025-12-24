from graph import Graph
from centrality import weighted_degree_centrality
from visualize import visualize_graph, visualize_regimes
from regime import detect_regimes

g = Graph()
g.add_edge("A", "B", 0.8)
g.add_edge("A", "C", 0.4)
g.add_edge("B", "C", 0.6)
g.add_edge("D", "E", 0.9)

centrality = weighted_degree_centrality(g)
visualize_graph(g, centrality, title="Graph Snapshot")

regimes = detect_regimes(g)
visualize_regimes(g, regimes)

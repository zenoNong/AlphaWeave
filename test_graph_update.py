from graph import Graph
from graph_updater import GraphUpdater

g = Graph()
updater = GraphUpdater(g)

pairs = [
    ("A", "B", 0.2),
    ("A", "B", 0.7),
    ("A", "B", 0.65),
    ("A", "B", 0.4),
    ("A", "B", 0.2),
]
for u, v, corr in pairs:
    updater.update_relationship(u, v, corr)
    print(f"corr={corr:.2f} -> edges:",g.edges())
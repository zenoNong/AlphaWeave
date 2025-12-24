from graph import Graph
from regime import detect_regimes

g = Graph()
g.add_edge("A","B",0.8)
g.add_edge("B","C",0.7)
g.add_edge("D","E",0.9)

regimes = detect_regimes(g)

print("Detect regimes:")
for r in regimes:
    print(r)
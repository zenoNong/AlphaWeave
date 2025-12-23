from graph import Graph

g = Graph()

g.add_edge("A", "B", 0.8)
g.add_edge("A", "C", 0.4)
g.add_edge("B", "C", 0.6)

print("Nodes:", g.nodes())
print("Edges:", g.edges())

print("Neighbors of A:", g.neighbors("A"))

g.update_edge("A", "B", 0.9)
print("Updated edge A-B:", g.neighbors("A"))

g.remove_edge("A", "C")
print("After removing A-C:", g.edges())

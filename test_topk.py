from topk import top_k_nodes

centrality = {
    "A": 1.2,
    "B": 1.4,
    "C": 1.0,
    "D": 2.1,
    "E": 0.9
}

top_nodes = top_k_nodes(centrality, k=3)

print("Top-K nodes:")
for node, score in top_nodes:
    print(node, score)
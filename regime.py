from union_find import UnionFind

def detect_regimes(graph):
    uf = UnionFind()

    for node in graph.nodes():
        uf.add(node)

    for u, v, _ in graph.edges():
        uf.union(u, v)

    regimes = {}
    for node in graph.nodes():
        root = uf.find(node)
        regimes.setdefault(root, []).append(node)

    return list(regimes.values())

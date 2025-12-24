def weighted_degree_centrality(graph):
    """
    Compute weighted degree centrality for each node.

    graph: Graph object
    returns: dict {node: centrality_score}
    """
    centrality = {}

    for node in graph.nodes():
        score = 0.0
        for neighbor, weight in graph.neighbors(node).items():
            score += abs(weight)
        centrality[node] = score

    return centrality

import heapq

def top_k_nodes(centrality_scores, k):
    """
    Return top-k nodes by centrality score.

    centrality_scores: dict {node: score}
    k: int
    returns: list of (node, score) sorted descending
    """
    if k <= 0:
        return []

    heap = []

    for node, score in centrality_scores.items():
        if len(heap) < k:
            heapq.heappush(heap, (score, node))
        else:
            if score > heap[0][0]:
                heapq.heapreplace(heap, (score, node))

    # convert to descending order
    return sorted(
        [(node, score) for score, node in heap],
        key=lambda x: x[1],
        reverse=True
    )

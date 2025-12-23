class GraphUpdater:
    def __init__(self, graph, add_threshold=0.6, remove_threshold=0.3):
        self.graph = graph
        self.add_threshold = add_threshold
        self.remove_threshold = remove_threshold

    def update_relationship(self, u, v, corr):
        """
        Update edge between u and v based on correlation value.
        """
        abs_corr = abs(corr)

        # Case 1: Strong correlation → add or update edge
        if abs_corr >= self.add_threshold:
            self.graph.add_edge(u, v, corr)

        # Case 2: Weak correlation → remove edge
        elif abs_corr < self.remove_threshold:
            self.graph.remove_edge(u, v)

        # Case 3: In-between → do nothing (stability)
        else:
            pass
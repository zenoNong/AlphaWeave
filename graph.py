class Graph:
    def __init__(self):
        """
        Adjacency list representation:
        {
            node_u: { node_v: weight, ... },
            ...
        }
        """
        self.adj = {}

    # -------------------------
    # Node Operations
    # -------------------------

    def add_node(self, node):
        """Add a node if it doesn't already exist."""
        if node not in self.adj:
            self.adj[node] = {}

    def has_node(self, node):
        return node in self.adj

    # -------------------------
    # Edge Operations
    # -------------------------

    def add_edge(self, u, v, weight):
        """
        Add an undirected weighted edge between u and v.
        If nodes do not exist, create them.
        """
        self.add_node(u)
        self.add_node(v)

        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def update_edge(self, u, v, weight):
        """Update edge weight if edge exists."""
        if u in self.adj and v in self.adj[u]:
            self.adj[u][v] = weight
            self.adj[v][u] = weight
        else:
            raise ValueError("Edge does not exist")

    def remove_edge(self, u, v):
        """Remove edge between u and v."""
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]
            del self.adj[v][u]

    # -------------------------
    # Query Operations
    # -------------------------

    def neighbors(self, node):
        """Return neighbors and weights of a node."""
        if node not in self.adj:
            return {}
        return self.adj[node]

    def nodes(self):
        """Return all nodes."""
        return list(self.adj.keys())

    def edges(self):
        """Return all edges as (u, v, weight) tuples."""
        seen = set()
        edge_list = []

        for u in self.adj:
            for v, w in self.adj[u].items():
                if (v, u) not in seen:
                    edge_list.append((u, v, w))
                    seen.add((u, v))

        return edge_list

    # -------------------------
    # Debug / Display
    # -------------------------

    def __str__(self):
        return str(self.adj)
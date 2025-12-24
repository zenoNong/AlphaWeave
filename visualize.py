import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph, centrality=None, title="AlphaWeave Graph"):
    """
    Visualize the current state of the graph.
    Node size reflects centrality.
    Edge width reflects weight magnitude.
    """
    G = nx.Graph()

    # Add edges
    for u, v, w in graph.edges():
        G.add_edge(u, v, weight=abs(w))

    # Node sizes
    if centrality:
        sizes = [300 + 2000 * centrality.get(n, 0) for n in G.nodes()]
    else:
        sizes = 500

    # Edge widths
    widths = [G[u][v]["weight"] * 3 for u, v in G.edges()]

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=sizes,
        width=widths,
        node_color="skyblue",
        edge_color="gray",
        font_weight="bold"
    )

    plt.title(title)
    plt.show()

def visualize_regimes(graph, regimes, title="Detected Regimes"):
    G = nx.Graph()

    for u, v, w in graph.edges():
        G.add_edge(u, v, weight=abs(w))

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    colors = ["red", "blue", "green", "purple", "orange"]

    for idx, regime in enumerate(regimes):
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=regime,
            node_color=colors[idx % len(colors)],
            node_size=700,
            label=f"Regime {idx+1}"
        )

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos)

    plt.title(title)
    plt.legend()
    plt.show()


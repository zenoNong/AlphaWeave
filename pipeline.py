from graph import Graph
from graph_updater import GraphUpdater
from stats import compute_returns, rolling_correlation
from centrality import weighted_degree_centrality
from topk import top_k_nodes
from regime import detect_regimes
from signals import interpret_signals


def run_pipeline(
    prices,
    window_size=3,
    top_k=2,
    add_threshold=0.6,
    remove_threshold=0.3
):
    """
    End-to-end AlphaWeave pipeline.
    prices: dict {asset: [price_t1, price_t2, ...]}
    """

    # -----------------------------
    # Step 1: Initialize graph
    # -----------------------------
    graph = Graph()
    updater = GraphUpdater(
        graph,
        add_threshold=add_threshold,
        remove_threshold=remove_threshold
    )

    assets = list(prices.keys())

    # -----------------------------
    # Step 2: Compute returns
    # -----------------------------
    returns = {}
    for asset in assets:
        returns[asset] = compute_returns(prices[asset])

    # -----------------------------
    # Step 3: Update graph using latest correlation
    # -----------------------------
    for i in range(len(assets)):
        for j in range(i + 1, len(assets)):
            a1 = assets[i]
            a2 = assets[j]

            r1 = returns[a1]
            r2 = returns[a2]

            corrs = rolling_correlation(r1, r2, window_size)
            if not corrs:
                continue

            current_corr = corrs[-1]
            updater.update_relationship(a1, a2, current_corr)

    # -----------------------------
    # Step 4: Graph analytics
    # -----------------------------
    centrality = weighted_degree_centrality(graph)
    top_nodes = top_k_nodes(centrality, top_k)
    regimes = detect_regimes(graph)

    # -----------------------------
    # Step 5: Interpret signals
    # -----------------------------
    signals = interpret_signals(top_nodes, centrality, regimes)

    return signals

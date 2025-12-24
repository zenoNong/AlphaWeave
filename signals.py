def interpret_signals(top_nodes, centrality, regimes):
    signals = []

    # map node → regime
    node_to_regime = {}
    for regime in regimes:
        for node in regime:
            node_to_regime[node] = regime

    for node, score in top_nodes:
        signal = {
            "node": node,
            "signal_type": "emerging_influencer",
            "centrality_score": round(score, 3),
            "regime": node_to_regime.get(node, []),
            "explanation": (
                f"{node} shows high influence due to strong "
                f"connections within its regime."
            )
        }
        signals.append(signal)

    return signals

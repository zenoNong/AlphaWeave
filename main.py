from data_loader import load_prices_from_csv
from pipeline import run_pipeline


def main():
    # --------------------------------
    # Load real price data
    # --------------------------------
    prices = {
        "AAPL": load_prices_from_csv("data/AAPL.csv"),
        "MSFT": load_prices_from_csv("data/MSFT.csv"),
        "GOOGL": load_prices_from_csv("data/GOOGL.csv"),
    }

    # --------------------------------
    # Run AlphaWeave pipeline
    # --------------------------------
    signals = run_pipeline(
        prices=prices,
        window_size=5,
        top_k=2,
        add_threshold=0.6,
        remove_threshold=0.3
    )

    # --------------------------------
    # Display results
    # --------------------------------
    print("\n=== AlphaWeave Signals ===\n")
    for s in signals:
        print(f"Node: {s['node']}")
        print(f"Signal: {s['signal_type']}")
        print(f"Centrality: {s['centrality_score']}")
        print(f"Regime: {s['regime']}")
        print(f"Explanation: {s['explanation']}")
        print("-" * 40)


if __name__ == "__main__":
    main()

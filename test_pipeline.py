from pipeline import run_pipeline

prices = {
    "A": [100,102,101,105,107],
    "B": [50,51,50,52,54],
    "C": [200,198,199,201,200]
}

signals = run_pipeline(
    prices,
    window_size=3,
    top_k=2
)

print("Final Signals:")
for s in signals:
    print(s)
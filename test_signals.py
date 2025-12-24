from signals import interpret_signals

centrality = {"A":1.2, "B":0.9, "C":0.4}
top_nodes = [("A",1.2),("B",0.9)]
regimes = [["A","B","C"]]

signals = interpret_signals(top_nodes, centrality, regimes)

for s in signals:
    print(s)
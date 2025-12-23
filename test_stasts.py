# from stats import compute_returns

# prices = [100, 102, 101, 0, 105]

# returns = compute_returns(prices=prices)

# print("Prices: ",prices)
# print("Returns: ",returns)

# from stats import rolling_mean, rolling_variance

# returns = [0.02, -0.01, 0.04, 0.03, -0.02]
# W = 3

# print("Rolling means: ", rolling_mean(returns,W))
# print("Rolling variane: ", rolling_variance(returns, W))

from stats import rolling_correlation

# x = [0.01, 0.02, 0.03, 0.04, 0.05]
# y = [0.02, 0.04, 0.06, 0.08, 0.10]

x = [0.01, 0.02, -0.01, 0.03, -0.02]
y = [-0.01, -0.02, 0.01, -0.03, 0.02]

W = 3

corrs = rolling_correlation(x, y, W)

print("Rolling correlation:", corrs)

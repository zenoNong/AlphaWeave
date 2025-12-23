import math

def compute_returns(prices):
    """
    Compute simple returns froma a list of prices.

    prices: list of floats
    returns: list of floats (len = len(prices) -1)
    """
    if len(prices)<2:
        return []
    returns = []

    for i in range(1,len(prices)):
        prev = prices[i-1]
        curr = prices[i]

        if prev == 0:
            returns.append(0.0)
        else:
            r = (curr - prev) / prev
            returns.append(r)
    return returns

def rolling_mean(data, window_size):
    """
    Compute rolling mean using sliding window.
    
    data: list of floats
    window_size: int
    returns: list of floats
    """
    n = len(data)
    if n<window_size or window_size <= 0:
        return []
    
    means = []
    window_sum = sum(data[:window_size])
    means.append(window_sum/window_size)

    for i in range(window_size,n):
        window_sum += data[i]
        window_sum -= data[i-window_size]
        means.append(window_sum/window_size)
    
    return means

def rolling_variance(data, window_size):
    """
    Compute rolling variance using sliding window.

    data: list of floats
    window_size: int
    returns: list of floats
    """
    n = len(data)
    if n < window_size or window_size <= 0:
        return []

    variances = []

    window_sum = 0.0
    window_sum_sq = 0.0

    for i in range(window_size):
        window_sum += data[i]
        window_sum_sq += data[i] ** 2

    mean = window_sum / window_size
    var = (window_sum_sq / window_size) - (mean ** 2)
    variances.append(var)

    for i in range(window_size, n):
        old = data[i - window_size]
        new = data[i]

        window_sum += new - old
        window_sum_sq += new**2 - old**2

        mean = window_sum / window_size
        var = (window_sum_sq / window_size) - (mean ** 2)
        variances.append(var)

    return variances


def rolling_correlation(x, y, window_size):
    """
    Compute rolling Pearson correlation using sliding window.

    x, y: lists of floats (same length)
    window_size: int
    returns: list of floats
    """
    if len(x) != len(y):
        raise ValueError("Input series must have same length")

    n = len(x)
    if n < window_size or window_size <= 1:
        return []

    corrs = []

    sum_x = sum_y = 0.0
    sum_x2 = sum_y2 = 0.0
    sum_xy = 0.0

    # initialize first window
    for i in range(window_size):
        sum_x += x[i]
        sum_y += y[i]
        sum_x2 += x[i] ** 2
        sum_y2 += y[i] ** 2
        sum_xy += x[i] * y[i]

    def compute_corr():
        mean_x = sum_x / window_size
        mean_y = sum_y / window_size

        cov = (sum_xy / window_size) - (mean_x * mean_y)
        var_x = (sum_x2 / window_size) - (mean_x ** 2)
        var_y = (sum_y2 / window_size) - (mean_y ** 2)

        if var_x <= 0 or var_y <= 0:
            return 0.0

        return cov / math.sqrt(var_x * var_y)

    corrs.append(compute_corr())

    # slide window
    for i in range(window_size, n):
        old_x = x[i - window_size]
        old_y = y[i - window_size]
        new_x = x[i]
        new_y = y[i]

        sum_x += new_x - old_x
        sum_y += new_y - old_y
        sum_x2 += new_x**2 - old_x**2
        sum_y2 += new_y**2 - old_y**2
        sum_xy += new_x * new_y - old_x * old_y

        corrs.append(compute_corr())

    return corrs

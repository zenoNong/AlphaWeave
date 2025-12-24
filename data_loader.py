import csv


def load_prices_from_csv(file_path, price_col="Close"):
    """
    Load prices from a CSV file.
    Returns: list of floats
    """
    prices = []

    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[price_col]:
                prices.append(float(row[price_col]))

    return prices

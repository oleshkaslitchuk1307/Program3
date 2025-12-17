import random

class MarketAsset:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def fluctuate_price(self):
        self.price *= random.uniform(0.95, 1.05)

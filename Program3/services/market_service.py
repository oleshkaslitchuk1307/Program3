from interfaces.imarket import IMarketService
from domain.market_asset import MarketAsset

class MarketService(IMarketService):
    def __init__(self):
        self.assets: list[MarketAsset] = []

    def add_asset(self, asset: MarketAsset) -> None:
        self.assets.append(asset)

    def update_prices(self) -> None:
        for asset in self.assets:
            asset.fluctuate_price()

    def get_assets(self) -> list[MarketAsset]:
        return self.assets

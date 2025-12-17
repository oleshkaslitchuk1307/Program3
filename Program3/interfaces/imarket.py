from typing import Protocol
from domain.market_asset import MarketAsset

class IMarketService(Protocol):
    def add_asset(self, asset: MarketAsset) -> None:
        ...

    def update_prices(self) -> None:
        ...

    def get_assets(self) -> list[MarketAsset]:
        ...

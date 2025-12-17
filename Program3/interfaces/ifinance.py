from typing import Protocol

class IFinanceService(Protocol):
    def deposit(self, amount: float) -> None:
        ...
    
    def withdraw(self, amount: float) -> bool:
        ...
    
    def get_balance(self) -> float:
        ...

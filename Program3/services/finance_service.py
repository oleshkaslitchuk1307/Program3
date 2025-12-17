from interfaces.ifinance import IFinanceService

class FinanceService(IFinanceService):
    def __init__(self, initial_balance: float):
        self._balance = initial_balance
        self.revenue = 0.0
        self.expenses = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount
        self.revenue += amount

    def withdraw(self, amount: float) -> bool:
        if self._balance >= amount:
            self._balance -= amount
            self.expenses += amount
            return True
        return False

    def get_balance(self) -> float:
        return self._balance

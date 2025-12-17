class Account:
    def __init__(self, customer_name: str, balance: float = 0.0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        self.loans = []
        self.deposits = []

    def decide_to_deposit(self, amount: float) -> bool:
        return amount > 0

    def decide_to_borrow(self, amount: float) -> bool:
        return True if amount > 0 else False

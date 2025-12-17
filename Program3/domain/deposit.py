class Deposit:
    def __init__(self, customer_name: str, amount: float, interest_rate: float, term_days: int):
        self.customer_name = customer_name
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_days = term_days
        self.days_passed = 0

    def accrue_interest(self):
        self.amount += self.amount * (self.interest_rate / 365)
        self.days_passed += 1

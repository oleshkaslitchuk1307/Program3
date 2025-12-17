class Loan:
    def __init__(self, customer_name: str, amount: float, interest_rate: float):
        self.customer_name = customer_name
        self.amount = amount
        self.interest_rate = interest_rate
        self.remaining = amount

    def pay_installment(self, payment: float) -> None:
        self.remaining = max(0, self.remaining - payment)

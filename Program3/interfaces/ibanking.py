from typing import Protocol
from domain.customer import Customer
from domain.account import Account
from domain.loan import Loan
from domain.deposit import Deposit

class IBankingService(Protocol):
    def open_account(self, customer: Customer, initial_deposit: float) -> Account:
        ...

    def issue_loan(self, customer: Customer, amount: float, interest_rate: float) -> Loan:
        ...

    def process_deposits(self) -> None:
        ...

    def process_loans(self) -> None:
        ...

    def get_accounts(self) -> list[Account]:
        ...

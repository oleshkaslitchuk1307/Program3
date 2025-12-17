from interfaces.ibanking import IBankingService
from domain.customer import Customer
from domain.account import Account
from domain.loan import Loan
from domain.deposit import Deposit

class BankingService(IBankingService):
    def __init__(self):
        self.accounts: list[Account] = []
        self.loans: list[Loan] = []
        self.deposits: list[Deposit] = []

    def open_account(self, customer: Customer, initial_deposit: float) -> Account:
        account = Account(customer.name, initial_deposit)
        self.accounts.append(account)
        customer.accounts.append(account)
        return account

    def issue_loan(self, customer: Customer, amount: float, interest_rate: float) -> Loan:
        loan = Loan(customer.name, amount, interest_rate)
        self.loans.append(loan)
        customer.loans.append(loan)
        return loan

    def process_deposits(self) -> None:
        for deposit in self.deposits:
            deposit.accrue_interest()

    def process_loans(self) -> None:
        for loan in self.loans:
            loan.amount += loan.amount * loan.interest_rate / 365

    def get_accounts(self) -> list[Account]:
        return self.accounts

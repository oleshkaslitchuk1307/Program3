from interfaces.ifinance import IFinanceService
from interfaces.ibanking import IBankingService
from interfaces.imarket import IMarketService
from interfaces.ievent import IEventService
from interfaces.iemployee import IEmployeeService
from domain.customer import Customer
from domain.employee import Employee
from domain.market_asset import MarketAsset

import random

class BankSimulation:

    def __init__(
        self,
        finance_service: IFinanceService,
        banking_service: IBankingService,
        market_service: IMarketService,
        event_service: IEventService,
        employee_service: IEmployeeService
    ):
        self.finance_service = finance_service
        self.banking_service = banking_service
        self.market_service = market_service
        self.event_service = event_service
        self.employee_service = employee_service

        self.customers: list[Customer] = []
        self.market_assets: list[MarketAsset] = []
        self.day = 0

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def process_customers(self, employee_effect):
        for customer in self.customers:
            deposit_amount = random.uniform(50, 1000) * (1 + employee_effect)
            if customer.decide_to_deposit(deposit_amount):
                account = self.banking_service.open_account(customer, deposit_amount)
                print(f"{customer.name} відкрив рахунок з депозитом {deposit_amount:.2f}")

            loan_amount = random.uniform(100, 2000) * (1 + employee_effect)
            if customer.decide_to_borrow(loan_amount):
                loan = self.banking_service.issue_loan(customer, loan_amount, 0.05)
                print(f"{customer.name} взяв кредит {loan_amount:.2f}")


    def run_employee_day(self):
        self.employee_service.run_employee_day()

    def pay_employee_salaries(self):
        self.employee_service.pay_salaries()

    def update_market(self, employee_effect: float = 0.0):

        for asset in self.market_service.get_assets():
            asset.fluctuate_price()
            asset.price *= (1 + employee_effect * 0.01)  

    def add_market_asset(self, asset: MarketAsset):
        self.market_assets.append(asset)
        self.market_service.add_asset(asset)

    def trigger_events(self):
        self.event_service.trigger_random_events()

    def process_banking_operations(self, employee_effect: float):
        self.banking_service.process_deposits()
        self.banking_service.process_loans()


    def simulate_day(self):
        self.day += 1
        print(f"\n--- День {self.day} ---")

        employee_effect = self.employee_service.run_employee_day()

        self.process_customers(employee_effect)
        self.process_banking_operations(employee_effect)
        self.update_market(employee_effect)

        self.trigger_events()
        self.pay_employee_salaries()
        print(f"Баланс банку: {self.finance_service.get_balance():.2f}")

    def simulate_days(self, num_days: int):
        for _ in range(num_days):
            self.simulate_day()
    

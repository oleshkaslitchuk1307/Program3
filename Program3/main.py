import random

from interfaces.ifinance import IFinanceService
from interfaces.ibanking import IBankingService
from interfaces.imarket import IMarketService
from interfaces.ievent import IEventService
from interfaces.iemployee import IEmployeeService

from services.finance_service import FinanceService
from services.banking_service import BankingService
from services.market_service import MarketService
from services.event_service import EventService
from services.employee_service import EmployeeService

from simulation.bank_simulation import BankSimulation
from domain.customer import Customer
from domain.employee import Employee
from domain.market_asset import MarketAsset

company_name = input("Введіть назву банку: ")
initial_balance = float(input("Введіть початковий баланс банку: "))
num_employees = int(input("Введіть кількість працівників: "))
num_customers = int(input("Введіть кількість клієнтів: "))
num_assets = int(input("Введіть кількість ринкових активів: "))

employee_names = ["Анна", "Сергій", "Оксана", "Іван", "Оля", "Петро", "Марія"]
roles = {"менеджер": 500, "аналітик": 400, "касир": 350}

customer_names = [f"Клієнт{i+1}" for i in range(50)]
asset_names = ["Акції А", "Облігації B", "Валюта USD", "Акції C", "Облігації D"]

finance_service = FinanceService(initial_balance)
banking_service = BankingService()
market_service = MarketService()
event_service = EventService(finance_service)
employee_service = EmployeeService()

bank_sim = BankSimulation(
    finance_service=finance_service,
    banking_service=banking_service,
    market_service=market_service,
    event_service=event_service,
    employee_service=employee_service
)

for _ in range(num_employees):
    name = random.choice(employee_names)
    role = random.choice(list(roles.keys()))
    salary = roles[role]
    employee_service.hire_employee(Employee(name, role, salary))

for _ in range(num_customers):
    name = random.choice(customer_names)
    bank_sim.add_customer(Customer(name))

for _ in range(num_assets):
    name = random.choice(asset_names)
    price = random.uniform(50, 200)
    bank_sim.add_market_asset(MarketAsset(name, price))

print(f"\n--- Старт симуляції для {company_name} ---")
bank_sim.simulate_days(10)

from interfaces.iemployee import IEmployeeService
from domain.employee import Employee
import random

class EmployeeService(IEmployeeService):
    def __init__(self):
        self.employees: list[Employee] = []

    def hire_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def pay_salaries(self) -> None:
        for employee in self.employees:
            print(f"Виплачено {employee.salary} зарплати {employee.name}")

    def run_employee_day(self) -> float:
        total_effect = 0.0
        for employee in self.employees:
            if employee.role == "менеджер":
                total_effect += employee.work() * 0.5
            elif employee.role == "аналітик":
                total_effect += employee.work() * 0.3
            elif employee.role == "касир":
                total_effect += employee.work() * 0.2
            employee.adjust_morale(random.uniform(-0.05, 0.05))
        return total_effect

    def get_employees(self) -> list[Employee]:
        return self.employees

from typing import Protocol
from domain.employee import Employee

class IEmployeeService(Protocol):
    def hire_employee(self, employee: Employee) -> None:
        ...

    def pay_salaries(self) -> None:
        ...

    def run_employee_day(self) -> None:
        ...

    def get_employees(self) -> list[Employee]:
        ...

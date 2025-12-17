class Employee:
    def __init__(self, name: str, role: str, salary: float):
        self.name = name
        self.role = role
        self.salary = salary
        self.morale = 1.0

    def work(self) -> float:
        return self.morale * 1.0

    def adjust_morale(self, delta: float) -> None:
        self.morale = max(0.0, min(1.0, self.morale + delta))

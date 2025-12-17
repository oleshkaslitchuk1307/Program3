from interfaces.ievent import IEventService
import random

class EventService(IEventService):
    def __init__(self, finance_service):
        self.finance_service = finance_service

    def trigger_random_events(self) -> None:
        if random.random() < 0.1:
            loss = random.uniform(100, 500)
            self.finance_service.withdraw(loss)
            print(f"Випадкова подія: штраф {loss:.2f}")
        elif random.random() < 0.05:
            gain = random.uniform(100, 500)
            self.finance_service.deposit(gain)
            print(f"Випадкова подія: бонус {gain:.2f}")

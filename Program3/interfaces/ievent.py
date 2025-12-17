from typing import Protocol

class IEventService(Protocol):
    def trigger_random_events(self) -> None:
        ...

from abc import ABC, abstractmethod


class ReportParser(ABC):
    @abstractmethod
    def parse(self) -> dict:
        pass

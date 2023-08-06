from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, report: dict, report_id: str):
        pass

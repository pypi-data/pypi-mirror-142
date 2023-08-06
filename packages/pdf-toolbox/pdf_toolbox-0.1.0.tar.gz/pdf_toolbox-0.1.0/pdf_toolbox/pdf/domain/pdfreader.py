from abc import ABC, abstractmethod


class PDFReader(ABC):
    @abstractmethod
    def extract_text(self) -> str:
        pass

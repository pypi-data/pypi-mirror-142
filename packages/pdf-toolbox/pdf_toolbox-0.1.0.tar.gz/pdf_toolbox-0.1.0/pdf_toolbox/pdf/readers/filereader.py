import textract

from ..domain.pdfreader import PDFReader


class FilePDFReader(PDFReader):
    def __init__(self, filename: str):
        self.__filename = filename

    def extract_text(self) -> str:
        return textract.process(self.__filename).decode()[:-1]

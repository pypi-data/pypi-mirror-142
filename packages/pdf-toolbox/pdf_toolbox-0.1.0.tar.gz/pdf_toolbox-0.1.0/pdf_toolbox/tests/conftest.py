import pytest

from .fixtures.pdf.dummy_reader import DummyPDFReader
from .fixtures.report_storage.dummy_report_storage import DummyReportStorage


@pytest.fixture
def dummy_pdf_reader():
    return DummyPDFReader()


@pytest.fixture
def dummy_report_storage():
    return DummyReportStorage()

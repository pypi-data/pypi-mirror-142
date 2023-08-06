from shared.utils import create_id
from text_extraction.report_parsers.challenge_parser import ChallengeParser


def test_generic_workflow(dummy_pdf_reader, dummy_report_storage):
    """This test shows the intended use of this package, loading reports,
    extracting data from them and storing in backend."""

    pdf_text = dummy_pdf_reader.extract_text()
    parser = ChallengeParser(pdf_text)
    pdf_data = parser.parse()
    dummy_report_storage.save(pdf_data, create_id())


def test_extract_data_from_challenge_pdf_type(dummy_pdf_reader):
    pdf_text = dummy_pdf_reader.extract_text()
    parser = ChallengeParser(pdf_text)
    pdf_data = parser.parse()

    expected_parsed_data = {
        "re": "Samuel López",
        "data": "01/06/96",
        "mr": "130322",
        "dob": "13/03/22",
        "document_text": "DIAGNOSES:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nPROCEDURES:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nHISTORY OF PRESENT ILLNESS:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nPHYSICAL EXAMINATIOS:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nLABORATORY DATA:Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nHOSPITAL COURSE: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nDISCHARGE MEDICATIONS:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nDISCHARGE INSTRUCTIONS:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.\nFOLLOW-UP CARE:\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "sections": {
            "DIAGNOSES": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "PROCEDURES": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "HISTORY OF PRESENT ILLNESS:": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "PHYSICAL EXAMINATIOS": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "LABORATORY DATA": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "HOSPITAL COURSE": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "DISCHARGE MEDICATIONS": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "DISCHARGE INSTRUCTIONS:": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "FOLLOW-UP CARE": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\neiusmod tempor incididunt ut labore et dolore magna aliqua.",
        },
    }
    assert (
        type(pdf_data) is dict
    ), "Challenge parser returns an invalid type of data"
    assert (
        pdf_data == expected_parsed_data
    ), "PDF extracted data does not match with the expected format"

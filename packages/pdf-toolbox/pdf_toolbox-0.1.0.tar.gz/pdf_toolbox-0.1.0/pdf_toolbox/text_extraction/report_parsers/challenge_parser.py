from ..domain.report_parser import ReportParser

from ..utils import get_text_section


class ChallengeParser(ReportParser):
    """Parser implementation for the report type specified in the
    challenge.
    """

    SECTIONS = {
        "DIAGNOSES": ("DIAGNOSES:\n", "PROCEDURES:"),
        "PROCEDURES": ("PROCEDURES:\n", "HISTORY OF PRESENT ILLNESS:"),
        "HISTORY OF PRESENT ILLNESS:": (
            "HISTORY OF PRESENT ILLNESS:\n",
            "PHYSICAL EXAMINATIOS:",
        ),
        "PHYSICAL EXAMINATIOS": (
            "PHYSICAL EXAMINATIOS:\n",
            "LABORATORY DATA:",
        ),
        "LABORATORY DATA": ("LABORATORY DATA:", "HOSPITAL COURSE:"),
        "HOSPITAL COURSE": ("HOSPITAL COURSE:", "DISCHARGE MEDICATIONS:"),
        "DISCHARGE MEDICATIONS": (
            "DISCHARGE MEDICATIONS:\n",
            "DISCHARGE INSTRUCTIONS:",
        ),
        "DISCHARGE INSTRUCTIONS:": (
            "DISCHARGE INSTRUCTIONS:\n",
            "FOLLOW-UP CARE",
        ),
        "FOLLOW-UP CARE": ("FOLLOW-UP CARE:\n", None),
    }

    def __init__(self, text: str):
        self.__text = text

    def parse(self) -> dict:
        doc_parts = self.__get_doc_parts()
        sections = self.__get_sections(doc_parts["document_text"])

        return {**doc_parts, **{"sections": sections}}

    def __get_doc_parts(self) -> dict:
        doc_parts = self.__text.split("\n\n")
        first_section = doc_parts[1]
        doc_text = "".join(doc_parts[2:])
        re, date, mr, dob = first_section.split("\n")

        return {
            "re": re,
            "data": date,
            "mr": mr,
            "dob": dob,
            "document_text": doc_text,
        }

    def __get_sections(self, text: str) -> dict:
        sections = {}
        for section in self.SECTIONS:
            section_text = get_text_section(
                text, self.SECTIONS[section][0], self.SECTIONS[section][1]
            ).strip()
            sections[section] = section_text

        return sections

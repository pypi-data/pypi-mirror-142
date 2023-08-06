from typing import Optional


def get_text_section(
    fulltext: str, section_start: str, section_end: Optional[str] = None
):

    start_pos = fulltext.index(section_start) + len(section_start)

    if section_end:
        end_pos = fulltext.index(section_end)
        section_data = fulltext[start_pos:end_pos]
    else:
        section_data = fulltext[start_pos:]

    return section_data

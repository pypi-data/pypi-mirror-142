import re
from typing import Optional, List

from . import dates_regex


class DatesParser:
    """
    Class that implements methods for extracting dates section from text version of cv
    :param regex_for_dates: Custom regex pattern. User can create his own pattern instead of using the one provided by
    module itself.
    """

    def __init__(self, regex_for_dates: Optional[re.Pattern] = None):
        """
        Initializes DatesParser Class
        """
        self.generic_re = regex_for_dates or dates_regex.generic_re

    def extract_all_dates(self, text: str) -> List[str]:
        """
        Extract dates only and returns list of dates
        :param text: cv to parse
        :return: list of dates found in cv
        """
        extracted_dates = []
        for match in self.generic_re.finditer(text.lower()):
            extracted_dates.append(match.group())
        return extracted_dates

    def extract_dates_sections(self, text) -> List[dict]:
        """
        Extract dates with descriptions found in cv
        :param text: cv to parse
        :return: list of dictionaries with keys 'date' and 'description'
        """
        previous_date_end = None
        previous_date = None
        previous_date_span = None
        dates_with_description = []
        for match in self.generic_re.finditer(text.lower()):
            next_date_start = match.span()[0]
            if previous_date:
                dates_with_description.append({
                    "date": previous_date,
                    "description": text[previous_date_end:next_date_start],
                    "span": previous_date_span,
                    "description_span": (previous_date_end, next_date_start)
                })
            previous_date = match.group()
            previous_date_span = match.span()
            previous_date_end = previous_date_span[1]
        if previous_date:
            dates_with_description.append({
                "date": previous_date,
                "description": text[previous_date_end:],
                "span": previous_date_span,
                "description_span": (previous_date_end, None)
            })
        return dates_with_description

    def check_consecutive_dates(self, text) -> bool:
        dates_with_description = self.extract_dates_sections(text)
        descriptions = [section["description"].strip() for section in dates_with_description]
        return not all(descriptions)

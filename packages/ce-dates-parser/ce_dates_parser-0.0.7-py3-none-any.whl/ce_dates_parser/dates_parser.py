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

    def extract_dates_sections(self, text: str) -> List[dict]:
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

    def check_consecutive_dates(self, text: str) -> bool:
        dates_with_description = self.extract_dates_sections(text)
        descriptions = [section["description"].strip() for section in dates_with_description]
        return not all(descriptions)

    def find_date_of_birth(self, text: str) -> Optional[str]:
        """
        Finds dates of birth from given cv text. First method is to look for the word similar to 'birth' in the
        proximity of dates and if found return that date. Next option is to sort dates and return one
        which is an outlier by 15 years.
        :param text: cv to parse
        :return: String representing dates of birth or None if not found
        """
        dates_without_range = self._find_all_dates_without_range(text)
        date_of_birth = self._find_date_of_birth_regex(text, dates_without_range)
        if not date_of_birth:
            date_of_birth = self._find_date_of_birth_range(dates_without_range)
        return date_of_birth

    @staticmethod
    def _find_date_of_birth_regex(text: str, dates: List[dict]) -> Optional[dict]:
        """
        Finds date in the given list, which is in the proximity of 20 characters from the word similar to 'birth'.
        :param text: cv to parse
        :param dates: list of dictionaries with dates found in cv
        :return: String representing dates of birth or None if not found
        """
        birth_header = re.search(r'((birth)|(urodzenie)|(urodzenia)|(urodziny))', text)
        if not birth_header:
            return None
        birth_header_end = birth_header.span()[1]
        for date in dates:
            if abs(date["match"].span()[0] - birth_header_end) < 20:
                return date["date"]
        return None

    @staticmethod
    def _find_date_of_birth_range(dates: List[dict]) -> Optional[dict]:
        """
        Finds date in the given list, which is the outlier by 15 years.
        :param dates: list of dictionaries with dates found in cv
        :return: String representing dates of birth or None if not found
        """
        if len(dates) < 2:
            return None
        sorted_dates = sorted(dates, key=lambda x: x["year"])
        birth_date = None
        if sorted_dates[1]["year"] - sorted_dates[0]["year"] > 15:
            birth_date = dates[0]["date"]
        return birth_date

    def _find_all_dates_without_range(self, text) -> List[dict]:
        """
        Finds all dates in the text that has no range. Dates with no range could be potential date of birth.
        :param text: cv to parse
        :return: List of dictionaries with found dates.
        """
        match_dates = []
        for date in self.generic_re.finditer(text.lower()):
            matches = list(re.finditer(dates_regex.year, date.group()))
            if len(matches) == 1:
                match = matches[0]
                year = int(match.group())
                match_dates.append({"match": date, "year": int(year), "date": date.group()})
        return match_dates

import regex as re
from typing import List
from rescrap.dict_reg import reg_addresses, reg_phone_numbers


class ReScrap:
    """Short summary.

    Parameters
    ----------
    text : type
        Description of parameter `text`.

    Attributes
    ----------
    text

    """

    def __init__(self, text):
        self.text = text
        if not text:
            raise ValueError("text must be specified")

    def find_addresses(self, location: str = None) -> List[str]:
        """Find all phone numbers in text.

        Parameters
        ----------
        location : str
            Location of phone numbers to find.

        Returns
        -------
        List[str]
            List of phone numbers.

        """
        if location in reg_addresses.keys():
            reg = reg_addresses[location]
        else:
            reg = reg_addresses["all"]

        return re.findall(reg, self.text, re.IGNORECASE)

    def find_custom(self, start: str, end: str) -> str:
        """Find the content of the first occurency of a specific pattern, defined by two bounds.

        Parameters
        ----------
        start : str
            Start of the bound.
        end : str
            End of the bound.

        Returns
        -------
        str
            Content between the bounds.

        """
        reg = fr"(?<={start}).*?(?={end})"

        return re.search(reg, self.text).group(0) if re.search(reg, self.text) else None

    def find_emails(self) -> List[str]:
        """Find all emails in text.

        Returns
        -------
        List[str]
            List of emails.

        """
        reg = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b)"

        return re.findall(reg, self.text, re.IGNORECASE)

    def find_phone_numbers(self, location: str = None) -> List[str]:
        """Find all phone numbers in text.

        Parameters
        ----------
        location : str
            Location of phone numbers to find.

        Returns
        -------
        List[str]
            List of phone numbers.

        """
        if location in reg_phone_numbers.keys():
            reg = reg_phone_numbers[location]
        else:
            reg = reg_phone_numbers["all"]

        return re.findall(reg, self.text)

import regex as re
import requests
from rescrap.rescrap import ReScrap
from typing import Dict, List, Optional, TypeVar

ReScrapWeb = TypeVar("ReScrapWeb")


class ReScrapWeb(ReScrap):
    """ReScrapWeb object.

    Parameters
    ----------
    plain_html : Optional[str]
        Plain html to use for the scraping.
    url : Optional[str]
        Url of the website to scrap.
    requests_params : Optional[Dict]
        Requests parameters if needed for the requests.

    Attributes
    ----------
    plain_html

    """

    def __init__(
        self,
        text: Optional[str] = None,
        url: Optional[str] = None,
        requests_params: Optional[Dict] = None,
    ):
        if text:
            self.text = text.replace("\n", " ")
            return

        if not url:
            raise ValueError("text or url must be specified")

        req = requests.get(url, **(requests_params or {}))
        self.text = req.text.replace("\n", " ")

    def find_all(self, tag: str, **attrs) -> List[ReScrapWeb]:
        """Find the content of all occurencies of a tag, with a specific attribute and value.

        Parameters
        ----------
        tag : str
            HTML tag to find.

        Returns
        -------
        List[ReScrapWeb]
            List of ReScrapWeb objects.

        """
        reg = fr'(?<=<{tag}[a-z_="\s]*'

        if attrs:
            for attribute, value in attrs.items():
                if attribute == "class_":
                    attribute = "class"
                reg += fr'{attribute}="(?:[a-z_\-]*\s?)*{value}(?:\s?[a-z_\-]*)*"\s?'

        reg += fr'[a-z="_-\s]*>).*?(?=</{tag}>)'

        return [ReScrapWeb(text=x) for x in re.findall(reg, self.text)]

    def find(self, tag: str, **attrs) -> ReScrapWeb:
        """Find the content of the first occurency of a tag, with a specific attribute and value.

        Parameters
        ----------
        tag : str
            HTML tag to find.

        Returns
        -------
        ReScrapWeb
            ReScrapWeb object containing the content of the tag.

        """
        reg = fr'(?<=<{tag}[a-z_="\s]*'

        if attrs:
            for attribute, value in attrs.items():
                if attribute == "class_":
                    attribute = "class"
                reg += fr'{attribute}="(?:[a-z_\-]*\s?)*{value}(?:\s?[a-z_\-]*)*"\s?'

        reg += fr'[a-z="_-\s]*>).*?(?=</{tag}>)'

        return (
            ReScrapWeb(text=re.search(reg, self.text).group(0))
            if re.search(reg, self.text)
            else None
        )

    def find_value(self, tag: str, attribute: str) -> str:
        """Find first occurency for a tag with a specific attribute.

        Parameters
        ----------
        tag : str
            HTML tag to find.
        attribute : str
            Attribute of the tag.

        Returns
        -------
        str
            Content of the attribute.
        """
        reg = fr'(?<=<{tag}[a-z="_-\s]*{attribute}=").*?(?="[a-z="_-\s]*>)'

        return re.search(reg, self.text).group(0) if re.search(reg, self.text) else None

    def find_all_values(self, tag: str, attribute: str) -> List[str]:
        """Find all occurencies for a tag with a specific attribute.

        Parameters
        ----------
        tag : str
            HTML tag to find.
        attribute : str
            Attribute of the tag.

        Returns
        -------
        List[str]
            List of content of the attributes.
        """
        reg = fr'(?<=<{tag} {attribute}=").*?(?=")'

        return [x for x in re.findall(reg, self.text)]

    def find_addresses(self, *args):
        return super().find_addresses(*args)

    def find_custom(self, *args):
        return super().find_custom(*args)

    def find_emails(self):
        return super().find_emails()

    def find_phone_numbers(self, *args):
        return super().find_phone_numbers(*args)

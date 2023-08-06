import regex as re
from PyPDF2 import PdfFileReader
from rescrap.rescrap import ReScrap


class ReScrapTextFile(ReScrap):
    """ReScrapTextFile object.

    Parameters
    ----------
    file_name : str
        File name of the text file to scrap.

    Attributes
    ----------
    file_name
    text

    """

    def __init__(self, file_name: str):
        self.file_name = file_name
        if not file_name:
            raise ValueError("file_name must be specified")
        self.text = self._get_text()

    def _get_text(self) -> str:
        text = ""
        with open(self.file_name, "r", encoding="utf-8") as f:
            text = f.read().replace("\n", " ")
        return text

    def find_addresses(self, *args):
        return super().find_addresses(*args)

    def find_custom(self, *args):
        return super().find_custom(*args)

    def find_emails(self):
        return super().find_emails()

    def find_phone_numbers(self, *args):
        return super().find_phone_numbers(*args)


class ReScrapPdfFile(ReScrap):
    """ReScrapPdfFile object.

    Parameters
    ----------
    file_name : str
        File name of the pdf file to scrap.

    Attributes
    ----------
    file_name
    text

    """

    def __init__(self, file_name: str):
        self.file_name = file_name
        if not file_name:
            raise ValueError("file_name must be specified")
        self.text = self._get_text()

    def _get_text(self) -> str:
        text = ""
        with open(self.file_name, mode="rb") as f:
            reader = PdfFileReader(f)
            for p in range(reader.numPages):
                text += reader.getPage(p).extractText().replace("\n", " ")
        return text

    def find_addresses(self, *args):
        return super().find_addresses(*args)

    def find_custom(self, *args):
        return super().find_custom(*args)

    def find_emails(self):
        return super().find_emails()

    def find_phone_numbers(self, *args):
        return super().find_phone_numbers(*args)

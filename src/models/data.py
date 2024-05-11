from typing import Any
from dataclasses import dataclass

import requests as req

class ApiResult:
    def __init__(self):
        pass
    def get_data(self) -> float:
        pass

class API():
    """
    Represents an API.
    """

    def __init__(self, url: str):
        """
        Initializes an instance of the API class.

        Args:
            url (str): The URL of the API.

        """
        self.url = url

    def fetch(self) -> ApiResult:
        """
        Fetches data from the API.

        Returns:
            Some modeled data from the API.

        """
        pass

"""
    Example data model we used in the project
"""

@dataclass
class Currency(ApiResult):
    date: str
    usd: dict

    @staticmethod
    def from_dict(obj: Any) -> 'Currency':
        _date = str(obj.get("date"))
        _usd = obj.get("usd")
        return Currency(_date, _usd)

    def get_data(self) -> float:
        return self.usd.get('eur')

class CurrencyAPI(API):
    def __init__(self):
        super().__init__("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}")

    def fetch(self) -> dataclass:
        formatted_url = self.url.format(date="latest", apiVersion="v1", endpoint="currencies/usd.json")
        response = req.get(formatted_url)

        if response.status_code != 200:
            return None

        return Currency.from_dict(response.json())

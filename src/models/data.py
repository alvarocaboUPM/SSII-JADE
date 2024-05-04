from typing import Any
from dataclasses import dataclass

@dataclass
class Root:
    date: str
    usd: dict

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _date = str(obj.get("date"))
        _usd = obj.get("usd")
        return Root(_date, _usd)

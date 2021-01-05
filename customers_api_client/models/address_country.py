from enum import Enum

class AddressCountry(str, Enum):
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
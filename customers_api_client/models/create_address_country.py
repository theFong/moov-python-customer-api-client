from enum import Enum

class CreateAddressCountry(str, Enum):
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
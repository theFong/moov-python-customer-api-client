from enum import Enum

class UpdateAddressCountry(str, Enum):
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
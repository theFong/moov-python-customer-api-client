from enum import Enum

class InitAccountValidationRequestVendor(str, Enum):
    MOOV = "moov"
    PLAID = "plaid"
    MX = "mx"

    def __str__(self) -> str:
        return str(self.value)
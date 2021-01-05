from enum import Enum

class AccountType(str, Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"

    def __str__(self) -> str:
        return str(self.value)
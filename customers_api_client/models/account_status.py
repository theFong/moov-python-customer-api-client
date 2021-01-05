from enum import Enum

class AccountStatus(str, Enum):
    NONE = "none"
    VALIDATED = "validated"

    def __str__(self) -> str:
        return str(self.value)
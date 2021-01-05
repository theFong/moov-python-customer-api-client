from enum import Enum

class AccountValidationResponseStatus(str, Enum):
    INIT = "init"
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
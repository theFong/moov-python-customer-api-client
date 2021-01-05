from enum import Enum

class OwnerType(str, Enum):
    CUSTOMER = "customer"
    REPRESENTATIVE = "representative"

    def __str__(self) -> str:
        return str(self.value)
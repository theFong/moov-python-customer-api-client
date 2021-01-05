from enum import Enum

class CreateAddressType(str, Enum):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"

    def __str__(self) -> str:
        return str(self.value)
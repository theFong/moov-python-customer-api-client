from enum import Enum

class CustomerType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    def __str__(self) -> str:
        return str(self.value)
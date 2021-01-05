from enum import Enum

class BusinessType(str, Enum):
    INDIVIDUAL_SOLE_PROPRIETOR_OR_SINGLE_MEMBER_LLC = "individual, sole proprietor, or single-member LLC"
    CORPORATION = "corporation"
    NON_PROFIT_ORGANIZATION = "non-profit organization"
    PARTNERSHIP = "partnership"
    LIMITED_LIABILITY_COMPANY = "limited liability company"

    def __str__(self) -> str:
        return str(self.value)
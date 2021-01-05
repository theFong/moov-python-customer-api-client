from enum import Enum

class DocumentType(str, Enum):
    DRIVERSLICENSE = "DriversLicense"
    PASSPORT = "Passport"
    UTILITYBILL = "UtilityBill"
    BANKSTATEMENT = "BankStatement"

    def __str__(self) -> str:
        return str(self.value)
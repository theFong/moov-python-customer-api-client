from enum import Enum

class CustomerStatus(str, Enum):
    DECEASED = "Deceased"
    REJECTED = "Rejected"
    UNKNOWN = "Unknown"
    RECEIVEONLY = "ReceiveOnly"
    VERIFIED = "Verified"
    FROZEN = "Frozen"

    def __str__(self) -> str:
        return str(self.value)
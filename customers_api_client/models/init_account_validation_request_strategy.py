from enum import Enum

class InitAccountValidationRequestStrategy(str, Enum):
    MICRO_DEPOSITS = "micro-deposits"
    INSTANT = "instant"

    def __str__(self) -> str:
        return str(self.value)
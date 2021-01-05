from enum import IntEnum

class NAICSCode(IntEnum):
    VALUE_11 = 11
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_42 = 42
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_81 = 81
    VALUE_92 = 92
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
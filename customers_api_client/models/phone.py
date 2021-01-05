from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from ..models.owner_type import OwnerType
from ..models.phone_type import PhoneType



@attr.s(auto_attribs=True)
class Phone:
    """  """
    number: str
    valid: bool
    type: PhoneType
    owner_type: Union[Unset, OwnerType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        number =  self.number
        valid =  self.valid
        type = self.type.value

        owner_type: Union[Unset, OwnerType] = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "number": number,
            "valid": valid,
            "type": type,
        })
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Phone":
        d = src_dict.copy()
        number = d.pop("number")

        valid = d.pop("valid")

        type = PhoneType(d.pop("type"))


        owner_type = None
        _owner_type = d.pop("ownerType", UNSET)
        if _owner_type is not None:
            owner_type = OwnerType(_owner_type)


        phone = Phone(
            number=number,
            valid=valid,
            type=type,
            owner_type=owner_type,
        )

        phone.additional_properties = d
        return phone

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

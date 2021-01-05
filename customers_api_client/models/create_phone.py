from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.phone_type import PhoneType



@attr.s(auto_attribs=True)
class CreatePhone:
    """  """
    number: str
    type: PhoneType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        number =  self.number
        type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "number": number,
            "type": type,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreatePhone":
        d = src_dict.copy()
        number = d.pop("number")

        type = PhoneType(d.pop("type"))


        create_phone = CreatePhone(
            number=number,
            type=type,
        )

        create_phone.additional_properties = d
        return create_phone

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

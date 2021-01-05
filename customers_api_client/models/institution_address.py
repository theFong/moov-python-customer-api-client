from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union



@attr.s(auto_attribs=True)
class InstitutionAddress:
    """  """
    address1: str
    city: str
    state: str
    zip: str
    address2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address1 =  self.address1
        city =  self.city
        state =  self.state
        zip =  self.zip
        address2 =  self.address2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "address1": address1,
            "city": city,
            "state": state,
            "zip": zip,
        })
        if address2 is not UNSET:
            field_dict["address2"] = address2

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "InstitutionAddress":
        d = src_dict.copy()
        address1 = d.pop("address1")

        city = d.pop("city")

        state = d.pop("state")

        zip = d.pop("zip")

        address2 = d.pop("address2", UNSET)

        institution_address = InstitutionAddress(
            address1=address1,
            city=city,
            state=state,
            zip=zip,
            address2=address2,
        )

        institution_address.additional_properties = d
        return institution_address

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

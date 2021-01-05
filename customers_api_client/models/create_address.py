from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from ..models.create_address_type import CreateAddressType
from ..models.create_address_country import CreateAddressCountry



@attr.s(auto_attribs=True)
class CreateAddress:
    """  """
    type: CreateAddressType
    address1: str
    city: str
    state: str
    postal_code: str
    country: CreateAddressCountry
    address2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        address1 =  self.address1
        city =  self.city
        state =  self.state
        postal_code =  self.postal_code
        country = self.country.value

        address2 =  self.address2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "address1": address1,
            "city": city,
            "state": state,
            "postalCode": postal_code,
            "country": country,
        })
        if address2 is not UNSET:
            field_dict["address2"] = address2

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateAddress":
        d = src_dict.copy()
        type = CreateAddressType(d.pop("type"))


        address1 = d.pop("address1")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = CreateAddressCountry(d.pop("country"))


        address2 = d.pop("address2", UNSET)

        create_address = CreateAddress(
            type=type,
            address1=address1,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address2=address2,
        )

        create_address.additional_properties = d
        return create_address

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

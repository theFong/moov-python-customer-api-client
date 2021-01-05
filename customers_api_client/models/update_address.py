from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.update_address_country import UpdateAddressCountry
from ..types import UNSET, Unset
from typing import Union
from ..models.update_address_type import UpdateAddressType



@attr.s(auto_attribs=True)
class UpdateAddress:
    """  """
    type: UpdateAddressType
    address1: str
    city: str
    state: str
    postal_code: str
    country: UpdateAddressCountry
    validated: Union[Unset, bool] = False
    address2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        address1 =  self.address1
        city =  self.city
        state =  self.state
        postal_code =  self.postal_code
        country = self.country.value

        validated =  self.validated
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
        if validated is not UNSET:
            field_dict["validated"] = validated
        if address2 is not UNSET:
            field_dict["address2"] = address2

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "UpdateAddress":
        d = src_dict.copy()
        type = UpdateAddressType(d.pop("type"))


        address1 = d.pop("address1")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = UpdateAddressCountry(d.pop("country"))


        validated = d.pop("validated", UNSET)

        address2 = d.pop("address2", UNSET)

        update_address = UpdateAddress(
            type=type,
            address1=address1,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            validated=validated,
            address2=address2,
        )

        update_address.additional_properties = d
        return update_address

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

from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.owner_type import OwnerType
from ..models.address_type import AddressType
from ..types import UNSET, Unset
from typing import Union
from ..models.address_country import AddressCountry



@attr.s(auto_attribs=True)
class Address:
    """  """
    address_id: str
    type: AddressType
    address1: str
    city: str
    state: str
    postal_code: str
    country: AddressCountry
    owner_type: Union[Unset, OwnerType] = UNSET
    address2: Union[Unset, str] = UNSET
    validated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_id =  self.address_id
        type = self.type.value

        address1 =  self.address1
        city =  self.city
        state =  self.state
        postal_code =  self.postal_code
        country = self.country.value

        owner_type: Union[Unset, OwnerType] = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type

        address2 =  self.address2
        validated =  self.validated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "addressID": address_id,
            "type": type,
            "address1": address1,
            "city": city,
            "state": state,
            "postalCode": postal_code,
            "country": country,
        })
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if validated is not UNSET:
            field_dict["validated"] = validated

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Address":
        d = src_dict.copy()
        address_id = d.pop("addressID")

        type = AddressType(d.pop("type"))


        address1 = d.pop("address1")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = AddressCountry(d.pop("country"))


        owner_type = None
        _owner_type = d.pop("ownerType", UNSET)
        if _owner_type is not None:
            owner_type = OwnerType(_owner_type)


        address2 = d.pop("address2", UNSET)

        validated = d.pop("validated", UNSET)

        address = Address(
            address_id=address_id,
            type=type,
            address1=address1,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            owner_type=owner_type,
            address2=address2,
            validated=validated,
        )

        address.additional_properties = d
        return address

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

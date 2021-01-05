from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.institution_address import InstitutionAddress
from typing import Dict
from ..types import UNSET, Unset
from typing import Union
from typing import cast



@attr.s(auto_attribs=True)
class InstitutionDetails:
    """  """
    name: str
    routing_number: str
    phone_number: Union[Unset, str] = UNSET
    address: Union[InstitutionAddress, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name =  self.name
        routing_number =  self.routing_number
        phone_number =  self.phone_number
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "routingNumber": routing_number,
        })
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "InstitutionDetails":
        d = src_dict.copy()
        name = d.pop("name")

        routing_number = d.pop("routingNumber")

        phone_number = d.pop("phoneNumber", UNSET)

        address: Union[InstitutionAddress, Unset] = UNSET
        _address = d.pop("address", UNSET)
        if _address is not None and not isinstance(_address,  Unset):
            address = InstitutionAddress.from_dict(cast(Dict[str, Any], _address))


        institution_details = InstitutionDetails(
            name=name,
            routing_number=routing_number,
            phone_number=phone_number,
            address=address,
        )

        institution_details.additional_properties = d
        return institution_details

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

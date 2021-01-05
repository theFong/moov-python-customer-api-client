from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset




@attr.s(auto_attribs=True)
class CustomerMetadata:
    """ Map of unique keys associated to values to act as foreign key relationships or arbitrary data associated to a Customer. """
    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CustomerMetadata":
        d = src_dict.copy()
        customer_metadata = CustomerMetadata(
        )

        customer_metadata.additional_properties = d
        return customer_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

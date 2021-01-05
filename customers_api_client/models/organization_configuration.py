from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset




@attr.s(auto_attribs=True)
class OrganizationConfiguration:
    """  """
    legal_entity: str
    primary_account: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        legal_entity =  self.legal_entity
        primary_account =  self.primary_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "legalEntity": legal_entity,
            "primaryAccount": primary_account,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "OrganizationConfiguration":
        d = src_dict.copy()
        legal_entity = d.pop("legalEntity")

        primary_account = d.pop("primaryAccount")

        organization_configuration = OrganizationConfiguration(
            legal_entity=legal_entity,
            primary_account=primary_account,
        )

        organization_configuration.additional_properties = d
        return organization_configuration

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

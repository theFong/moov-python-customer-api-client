from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast



@attr.s(auto_attribs=True)
class OFACSearch:
    """  """
    entity_id: str
    blocked: bool
    sdn_name: str
    sdn_type: str
    match: float
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        entity_id =  self.entity_id
        blocked =  self.blocked
        sdn_name =  self.sdn_name
        sdn_type =  self.sdn_type
        match =  self.match
        created_at = self.created_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entityID": entity_id,
            "blocked": blocked,
            "sdnName": sdn_name,
            "sdnType": sdn_type,
            "match": match,
            "createdAt": created_at,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "OFACSearch":
        d = src_dict.copy()
        entity_id = d.pop("entityID")

        blocked = d.pop("blocked")

        sdn_name = d.pop("sdnName")

        sdn_type = d.pop("sdnType")

        match = d.pop("match")

        created_at = isoparse(d.pop("createdAt"))


        ofac_search = OFACSearch(
            entity_id=entity_id,
            blocked=blocked,
            sdn_name=sdn_name,
            sdn_type=sdn_type,
            match=match,
            created_at=created_at,
        )

        ofac_search.additional_properties = d
        return ofac_search

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

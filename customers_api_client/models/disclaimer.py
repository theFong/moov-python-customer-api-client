from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from dateutil.parser import isoparse
import datetime
from ..types import UNSET, Unset
from typing import Union
from typing import cast



@attr.s(auto_attribs=True)
class Disclaimer:
    """  """
    disclaimer_id: str
    text: str
    document_id: Union[Unset, str] = UNSET
    accepted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        disclaimer_id =  self.disclaimer_id
        text =  self.text
        document_id =  self.document_id
        accepted_at: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_at, Unset):
            accepted_at = self.accepted_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "disclaimerID": disclaimer_id,
            "text": text,
        })
        if document_id is not UNSET:
            field_dict["documentID"] = document_id
        if accepted_at is not UNSET:
            field_dict["acceptedAt"] = accepted_at

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Disclaimer":
        d = src_dict.copy()
        disclaimer_id = d.pop("disclaimerID")

        text = d.pop("text")

        document_id = d.pop("documentID", UNSET)

        accepted_at = None
        _accepted_at = d.pop("acceptedAt", UNSET)
        if _accepted_at is not None:
            accepted_at = isoparse(cast(str, _accepted_at))


        disclaimer = Disclaimer(
            disclaimer_id=disclaimer_id,
            text=text,
            document_id=document_id,
            accepted_at=accepted_at,
        )

        disclaimer.additional_properties = d
        return disclaimer

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

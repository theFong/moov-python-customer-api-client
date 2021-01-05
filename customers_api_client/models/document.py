from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.document_type import DocumentType
from dateutil.parser import isoparse
import datetime
from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import cast, List



@attr.s(auto_attribs=True)
class Document:
    """  """
    document_id: str
    type: DocumentType
    content_type: str
    uploaded_at: datetime.datetime
    parse_errors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        document_id =  self.document_id
        type = self.type.value

        content_type =  self.content_type
        uploaded_at = self.uploaded_at.isoformat()

        parse_errors: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.parse_errors, Unset):
            parse_errors = self.parse_errors





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "documentID": document_id,
            "type": type,
            "contentType": content_type,
            "uploadedAt": uploaded_at,
        })
        if parse_errors is not UNSET:
            field_dict["parseErrors"] = parse_errors

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Document":
        d = src_dict.copy()
        document_id = d.pop("documentID")

        type = DocumentType(d.pop("type"))


        content_type = d.pop("contentType")

        uploaded_at = isoparse(d.pop("uploadedAt"))


        parse_errors = cast(List[str], d.pop("parseErrors", UNSET))


        document = Document(
            document_id=document_id,
            type=type,
            content_type=content_type,
            uploaded_at=uploaded_at,
            parse_errors=parse_errors,
        )

        document.additional_properties = d
        return document

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

from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from ..models.complete_account_validation_request_vendor_request import CompleteAccountValidationRequestVendorRequest



@attr.s(auto_attribs=True)
class CompleteAccountValidationRequest:
    """  """
    vendor_request: CompleteAccountValidationRequestVendorRequest
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        vendor_request = self.vendor_request.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "vendor_request": vendor_request,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CompleteAccountValidationRequest":
        d = src_dict.copy()
        vendor_request = CompleteAccountValidationRequestVendorRequest.from_dict(d.pop("vendor_request"))


        complete_account_validation_request = CompleteAccountValidationRequest(
            vendor_request=vendor_request,
        )

        complete_account_validation_request.additional_properties = d
        return complete_account_validation_request

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

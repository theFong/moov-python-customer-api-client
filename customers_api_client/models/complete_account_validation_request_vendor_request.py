from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset




@attr.s(auto_attribs=True)
class CompleteAccountValidationRequestVendorRequest:
    """ key/value map of vendor specific params """
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CompleteAccountValidationRequestVendorRequest":
        d = src_dict.copy()
        complete_account_validation_request_vendor_request = CompleteAccountValidationRequestVendorRequest(
        )

        complete_account_validation_request_vendor_request.additional_properties = d
        return complete_account_validation_request_vendor_request

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

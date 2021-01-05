from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from ..models.init_account_validation_request_strategy import InitAccountValidationRequestStrategy
from ..models.init_account_validation_request_vendor import InitAccountValidationRequestVendor



@attr.s(auto_attribs=True)
class InitAccountValidationRequest:
    """  """
    strategy: InitAccountValidationRequestStrategy
    vendor: Union[Unset, InitAccountValidationRequestVendor] = InitAccountValidationRequestVendor.MOOV
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        strategy = self.strategy.value

        vendor: Union[Unset, InitAccountValidationRequestVendor] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
        })
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "InitAccountValidationRequest":
        d = src_dict.copy()
        strategy = InitAccountValidationRequestStrategy(d.pop("strategy"))


        vendor = None
        _vendor = d.pop("vendor", UNSET)
        if _vendor is not None:
            vendor = InitAccountValidationRequestVendor(_vendor)


        init_account_validation_request = InitAccountValidationRequest(
            strategy=strategy,
            vendor=vendor,
        )

        init_account_validation_request.additional_properties = d
        return init_account_validation_request

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

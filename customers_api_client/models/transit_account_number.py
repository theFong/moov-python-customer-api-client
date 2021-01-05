from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union



@attr.s(auto_attribs=True)
class TransitAccountNumber:
    """  """
    account_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        account_number =  self.account_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "TransitAccountNumber":
        d = src_dict.copy()
        account_number = d.pop("accountNumber", UNSET)

        transit_account_number = TransitAccountNumber(
            account_number=account_number,
        )

        transit_account_number.additional_properties = d
        return transit_account_number

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

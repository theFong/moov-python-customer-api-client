from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..models.customer import Customer
from ..models.account import Account
from ..types import UNSET, Unset
from typing import Union
from typing import cast



@attr.s(auto_attribs=True)
class ReportAccountResponse:
    """  """
    customer: Union[Customer, Unset] = UNSET
    account: Union[Account, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if customer is not UNSET:
            field_dict["Customer"] = customer
        if account is not UNSET:
            field_dict["Account"] = account

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "ReportAccountResponse":
        d = src_dict.copy()
        customer: Union[Customer, Unset] = UNSET
        _customer = d.pop("Customer", UNSET)
        if _customer is not None and not isinstance(_customer,  Unset):
            customer = Customer.from_dict(cast(Dict[str, Any], _customer))


        account: Union[Account, Unset] = UNSET
        _account = d.pop("Account", UNSET)
        if _account is not None and not isinstance(_account,  Unset):
            account = Account.from_dict(cast(Dict[str, Any], _account))


        report_account_response = ReportAccountResponse(
            customer=customer,
            account=account,
        )

        report_account_response.additional_properties = d
        return report_account_response

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

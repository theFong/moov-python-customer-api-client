from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.account_type import AccountType



@attr.s(auto_attribs=True)
class CreateAccount:
    """  """
    holder_name: str
    account_number: str
    routing_number: str
    type: AccountType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        holder_name =  self.holder_name
        account_number =  self.account_number
        routing_number =  self.routing_number
        type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "holderName": holder_name,
            "accountNumber": account_number,
            "routingNumber": routing_number,
            "type": type,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateAccount":
        d = src_dict.copy()
        holder_name = d.pop("holderName")

        account_number = d.pop("accountNumber")

        routing_number = d.pop("routingNumber")

        type = AccountType(d.pop("type"))


        create_account = CreateAccount(
            holder_name=holder_name,
            account_number=account_number,
            routing_number=routing_number,
            type=type,
        )

        create_account.additional_properties = d
        return create_account

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

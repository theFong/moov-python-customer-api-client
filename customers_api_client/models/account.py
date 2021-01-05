from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..types import UNSET, Unset
from ..models.account_type import AccountType
from typing import Union
from typing import cast
from ..models.account_status import AccountStatus
from ..models.institution_details import InstitutionDetails



@attr.s(auto_attribs=True)
class Account:
    """  """
    account_id: str
    customer_id: str
    holder_name: str
    masked_account_number: str
    routing_number: str
    status: AccountStatus
    type: AccountType
    institution: Union[InstitutionDetails, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        account_id =  self.account_id
        customer_id =  self.customer_id
        holder_name =  self.holder_name
        masked_account_number =  self.masked_account_number
        routing_number =  self.routing_number
        status = self.status.value

        type = self.type.value

        institution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.institution, Unset):
            institution = self.institution.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accountID": account_id,
            "customerID": customer_id,
            "holderName": holder_name,
            "maskedAccountNumber": masked_account_number,
            "routingNumber": routing_number,
            "status": status,
            "type": type,
        })
        if institution is not UNSET:
            field_dict["institution"] = institution

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Account":
        d = src_dict.copy()
        account_id = d.pop("accountID")

        customer_id = d.pop("customerID")

        holder_name = d.pop("holderName")

        masked_account_number = d.pop("maskedAccountNumber")

        routing_number = d.pop("routingNumber")

        status = AccountStatus(d.pop("status"))


        type = AccountType(d.pop("type"))


        institution: Union[InstitutionDetails, Unset] = UNSET
        _institution = d.pop("institution", UNSET)
        if _institution is not None and not isinstance(_institution,  Unset):
            institution = InstitutionDetails.from_dict(cast(Dict[str, Any], _institution))


        account = Account(
            account_id=account_id,
            customer_id=customer_id,
            holder_name=holder_name,
            masked_account_number=masked_account_number,
            routing_number=routing_number,
            status=status,
            type=type,
            institution=institution,
        )

        account.additional_properties = d
        return account

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

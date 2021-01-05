from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.account_validation_response_status import AccountValidationResponseStatus
import datetime
from dateutil.parser import isoparse
from ..types import UNSET, Unset
from typing import Union
from typing import cast



@attr.s(auto_attribs=True)
class AccountValidationResponse:
    """  """
    validation_id: Union[Unset, str] = UNSET
    strategy: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    status: Union[Unset, AccountValidationResponseStatus] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        validation_id =  self.validation_id
        strategy =  self.strategy
        vendor =  self.vendor
        status: Union[Unset, AccountValidationResponseStatus] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if validation_id is not UNSET:
            field_dict["validationID"] = validation_id
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "AccountValidationResponse":
        d = src_dict.copy()
        validation_id = d.pop("validationID", UNSET)

        strategy = d.pop("strategy", UNSET)

        vendor = d.pop("vendor", UNSET)

        status = None
        _status = d.pop("status", UNSET)
        if _status is not None:
            status = AccountValidationResponseStatus(_status)


        created_at = None
        _created_at = d.pop("createdAt", UNSET)
        if _created_at is not None:
            created_at = isoparse(cast(str, _created_at))


        updated_at = None
        _updated_at = d.pop("updatedAt", UNSET)
        if _updated_at is not None:
            updated_at = isoparse(cast(str, _updated_at))


        account_validation_response = AccountValidationResponse(
            validation_id=validation_id,
            strategy=strategy,
            vendor=vendor,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        account_validation_response.additional_properties = d
        return account_validation_response

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

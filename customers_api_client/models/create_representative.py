from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..models.create_address import CreateAddress
from ..models.create_phone import CreatePhone
from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import cast, List



@attr.s(auto_attribs=True)
class CreateRepresentative:
    """  """
    first_name: str
    last_name: str
    job_title: Union[Unset, str] = UNSET
    birth_date: Union[Unset, str] = UNSET
    ssn: Union[Unset, str] = UNSET
    phones: Union[Unset, List[CreatePhone]] = UNSET
    addresses: Union[Unset, List[CreateAddress]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        first_name =  self.first_name
        last_name =  self.last_name
        job_title =  self.job_title
        birth_date =  self.birth_date
        ssn =  self.ssn
        phones: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()

                phones.append(phones_item)




        addresses: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()

                addresses.append(addresses_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "firstName": first_name,
            "lastName": last_name,
        })
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if ssn is not UNSET:
            field_dict["SSN"] = ssn
        if phones is not UNSET:
            field_dict["phones"] = phones
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateRepresentative":
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        job_title = d.pop("jobTitle", UNSET)

        birth_date = d.pop("birthDate", UNSET)

        ssn = d.pop("SSN", UNSET)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in (_phones or []):
            phones_item = CreatePhone.from_dict(phones_item_data)

            phones.append(phones_item)


        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in (_addresses or []):
            addresses_item = CreateAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)


        create_representative = CreateRepresentative(
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            birth_date=birth_date,
            ssn=ssn,
            phones=phones,
            addresses=addresses,
        )

        create_representative.additional_properties = d
        return create_representative

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

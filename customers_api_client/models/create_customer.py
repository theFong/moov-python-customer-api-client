from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..models.create_address import CreateAddress
from ..models.customer_type import CustomerType
from ..models.business_type import BusinessType
from ..models.create_representative import CreateRepresentative
from ..models.create_phone import CreatePhone
from ..models.create_customer_metadata import CreateCustomerMetadata
from ..types import UNSET, Unset
from ..models.sic_code import SICCode
from typing import cast
from typing import cast, List
from ..models.naics_code import NAICSCode
from typing import Union



@attr.s(auto_attribs=True)
class CreateCustomer:
    """  """
    first_name: str
    last_name: str
    type: CustomerType
    email: str
    middle_name: Union[Unset, str] = UNSET
    nick_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    doing_business_as: Union[Unset, str] = UNSET
    business_type: Union[Unset, BusinessType] = UNSET
    ein: Union[Unset, str] = UNSET
    duns: Union[Unset, str] = UNSET
    sic_code: Union[Unset, SICCode] = UNSET
    naics_code: Union[Unset, NAICSCode] = UNSET
    birth_date: Union[Unset, str] = UNSET
    ssn: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    date_business_established: Union[Unset, str] = UNSET
    phones: Union[Unset, List[CreatePhone]] = UNSET
    addresses: Union[Unset, List[CreateAddress]] = UNSET
    representatives: Union[Unset, List[CreateRepresentative]] = UNSET
    metadata: Union[CreateCustomerMetadata, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        first_name =  self.first_name
        last_name =  self.last_name
        type = self.type.value

        email =  self.email
        middle_name =  self.middle_name
        nick_name =  self.nick_name
        suffix =  self.suffix
        business_name =  self.business_name
        doing_business_as =  self.doing_business_as
        business_type: Union[Unset, BusinessType] = UNSET
        if not isinstance(self.business_type, Unset):
            business_type = self.business_type

        ein =  self.ein
        duns =  self.duns
        sic_code: Union[Unset, SICCode] = UNSET
        if not isinstance(self.sic_code, Unset):
            sic_code = self.sic_code

        naics_code: Union[Unset, NAICSCode] = UNSET
        if not isinstance(self.naics_code, Unset):
            naics_code = self.naics_code

        birth_date =  self.birth_date
        ssn =  self.ssn
        website =  self.website
        date_business_established =  self.date_business_established
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




        representatives: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.representatives, Unset):
            representatives = []
            for representatives_item_data in self.representatives:
                representatives_item = representatives_item_data.to_dict()

                representatives.append(representatives_item)




        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "firstName": first_name,
            "lastName": last_name,
            "type": type,
            "email": email,
        })
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if doing_business_as is not UNSET:
            field_dict["doingBusinessAs"] = doing_business_as
        if business_type is not UNSET:
            field_dict["businessType"] = business_type
        if ein is not UNSET:
            field_dict["EIN"] = ein
        if duns is not UNSET:
            field_dict["DUNS"] = duns
        if sic_code is not UNSET:
            field_dict["SICCode"] = sic_code
        if naics_code is not UNSET:
            field_dict["NAICSCode"] = naics_code
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if ssn is not UNSET:
            field_dict["SSN"] = ssn
        if website is not UNSET:
            field_dict["website"] = website
        if date_business_established is not UNSET:
            field_dict["dateBusinessEstablished"] = date_business_established
        if phones is not UNSET:
            field_dict["phones"] = phones
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if representatives is not UNSET:
            field_dict["representatives"] = representatives
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateCustomer":
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        type = CustomerType(d.pop("type"))


        email = d.pop("email")

        middle_name = d.pop("middleName", UNSET)

        nick_name = d.pop("nickName", UNSET)

        suffix = d.pop("suffix", UNSET)

        business_name = d.pop("businessName", UNSET)

        doing_business_as = d.pop("doingBusinessAs", UNSET)

        business_type = None
        _business_type = d.pop("businessType", UNSET)
        if _business_type is not None:
            business_type = BusinessType(_business_type)


        ein = d.pop("EIN", UNSET)

        duns = d.pop("DUNS", UNSET)

        sic_code = None
        _sic_code = d.pop("SICCode", UNSET)
        if _sic_code is not None:
            sic_code = SICCode(_sic_code)


        naics_code = None
        _naics_code = d.pop("NAICSCode", UNSET)
        if _naics_code is not None:
            naics_code = NAICSCode(_naics_code)


        birth_date = d.pop("birthDate", UNSET)

        ssn = d.pop("SSN", UNSET)

        website = d.pop("website", UNSET)

        date_business_established = d.pop("dateBusinessEstablished", UNSET)

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


        representatives = []
        _representatives = d.pop("representatives", UNSET)
        for representatives_item_data in (_representatives or []):
            representatives_item = CreateRepresentative.from_dict(representatives_item_data)

            representatives.append(representatives_item)


        metadata: Union[CreateCustomerMetadata, Unset] = UNSET
        _metadata = d.pop("metadata", UNSET)
        if _metadata is not None and not isinstance(_metadata,  Unset):
            metadata = CreateCustomerMetadata.from_dict(cast(Dict[str, Any], _metadata))


        create_customer = CreateCustomer(
            first_name=first_name,
            last_name=last_name,
            type=type,
            email=email,
            middle_name=middle_name,
            nick_name=nick_name,
            suffix=suffix,
            business_name=business_name,
            doing_business_as=doing_business_as,
            business_type=business_type,
            ein=ein,
            duns=duns,
            sic_code=sic_code,
            naics_code=naics_code,
            birth_date=birth_date,
            ssn=ssn,
            website=website,
            date_business_established=date_business_established,
            phones=phones,
            addresses=addresses,
            representatives=representatives,
            metadata=metadata,
        )

        create_customer.additional_properties = d
        return create_customer

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

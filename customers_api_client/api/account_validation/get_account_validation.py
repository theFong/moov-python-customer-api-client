from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.account_validation_response import AccountValidationResponse
from ...types import UNSET, Unset
from typing import Union
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    validation_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/accounts/{accountID}/validations/{validationID}".format(
        client.base_url,customerID=customer_id,accountID=account_id,validationID=validation_id)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    if x_organization is not UNSET:
        headers["x-organization"] = x_organization


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AccountValidationResponse]:
    if response.status_code == 200:
        response_200 = AccountValidationResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AccountValidationResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    validation_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[AccountValidationResponse]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
account_id=account_id,
validation_id=validation_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    validation_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[AccountValidationResponse]:
    """ Get information about account validation strategy, status, etc.
 """

    return sync_detailed(
        client=client,
customer_id=customer_id,
account_id=account_id,
validation_id=validation_id,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    validation_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[AccountValidationResponse]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
account_id=account_id,
validation_id=validation_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    validation_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[AccountValidationResponse]:
    """ Get information about account validation strategy, status, etc.
 """

    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
account_id=account_id,
validation_id=validation_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed

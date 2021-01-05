from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Union
from ...types import UNSET, Unset



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}".format(
        client.base_url,customerID=customer_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    None,
    None
]]:
    if response.status_code == 200:
        response_200 = None

        return response_200
    if response.status_code == 400:
        response_400 = None

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[
    None,
    None
]]:
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
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[Union[
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    customer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[Union[
    None,
    None
]]:
    """ Remove a given Customer """

    return sync_detailed(
        client=client,
customer_id=customer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[Union[
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    customer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[Union[
    None,
    None
]]:
    """ Remove a given Customer """

    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed

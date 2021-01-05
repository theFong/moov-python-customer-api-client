from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.customers import Customers
from ...types import UNSET, Unset
from typing import Union
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    count: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/customers".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    

    params: Dict[str, Any] = {
    }
    if query is not UNSET:
        params["query"] = query
    if email is not UNSET:
        params["email"] = email
    if status is not UNSET:
        params["status"] = status
    if type is not UNSET:
        params["type"] = type
    if skip is not UNSET:
        params["skip"] = skip
    if count is not UNSET:
        params["count"] = count
    if customer_i_ds is not UNSET:
        params["customerIDs"] = customer_i_ds


    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Customers]:
    if response.status_code == 200:
        response_200 = Customers.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Customers]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    count: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,

) -> Response[Customers]:
    kwargs = _get_kwargs(
        client=client,
query=query,
email=email,
status=status,
type=type,
skip=skip,
count=count,
customer_i_ds=customer_i_ds,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    count: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,

) -> Optional[Customers]:
    """ Search for customers using different filter parameters """

    return sync_detailed(
        client=client,
query=query,
email=email,
status=status,
type=type,
skip=skip,
count=count,
customer_i_ds=customer_i_ds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    count: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,

) -> Response[Customers]:
    kwargs = _get_kwargs(
        client=client,
query=query,
email=email,
status=status,
type=type,
skip=skip,
count=count,
customer_i_ds=customer_i_ds,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    query: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    count: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,

) -> Optional[Customers]:
    """ Search for customers using different filter parameters """

    return (await asyncio_detailed(
        client=client,
query=query,
email=email,
status=status,
type=type,
skip=skip,
count=count,
customer_i_ds=customer_i_ds,

    )).parsed

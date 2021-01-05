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
    document_id: str,
    x_request_id: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/documents/{documentID}".format(
        client.base_url,customerID=customer_id,documentID=document_id)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }




def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    customer_id: str,
    document_id: str,
    x_request_id: Union[Unset, str] = UNSET,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
document_id=document_id,
x_request_id=x_request_id,

    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    document_id: str,
    x_request_id: Union[Unset, str] = UNSET,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
document_id=document_id,
x_request_id=x_request_id,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)


from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response




def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/representatives/{representativeID}".format(
        client.base_url,customerID=customer_id,representativeID=representative_id)

    headers: Dict[str, Any] = client.get_headers()

    

    

    

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
    representative_id: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,

    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)


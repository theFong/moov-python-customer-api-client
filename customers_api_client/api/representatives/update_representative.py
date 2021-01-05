from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.create_representative import CreateRepresentative
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateRepresentative,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/representatives/{representativeID}".format(
        client.base_url,customerID=customer_id,representativeID=representative_id)

    headers: Dict[str, Any] = client.get_headers()

    

    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: CreateRepresentative,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,

    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateRepresentative,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(
            **kwargs
        )

    return _build_response(response=response)


from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.create_representative import CreateRepresentative
from ...models.customer import Customer
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    json_body: CreateRepresentative,
    x_request_id: str,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/representatives".format(
        client.base_url,customerID=customer_id)

    headers: Dict[str, Any] = client.get_headers()

    headers["x-request-id"] = x_request_id
    headers["x-organization"] = x_organization


    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Customer]:
    if response.status_code == 200:
        response_200 = Customer.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Customer]:
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
    json_body: CreateRepresentative,
    x_request_id: str,
    x_organization: str,

) -> Response[Customer]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    customer_id: str,
    json_body: CreateRepresentative,
    x_request_id: str,
    x_organization: str,

) -> Optional[Customer]:
    """ Add a Customer Representative """

    return sync_detailed(
        client=client,
customer_id=customer_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    json_body: CreateRepresentative,
    x_request_id: str,
    x_organization: str,

) -> Response[Customer]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    customer_id: str,
    json_body: CreateRepresentative,
    x_request_id: str,
    x_organization: str,

) -> Optional[Customer]:
    """ Add a Customer Representative """

    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed

from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.update_account_status import UpdateAccountStatus
from typing import cast
from ...models.account import Account



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    json_body: UpdateAccountStatus,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/accounts/{accountID}/status".format(
        client.base_url,customerID=customer_id,accountID=account_id)

    headers: Dict[str, Any] = client.get_headers()

    

    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Account]:
    if response.status_code == 200:
        response_200 = Account.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Account]:
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
    json_body: UpdateAccountStatus,

) -> Response[Account]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
account_id=account_id,
json_body=json_body,

    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    json_body: UpdateAccountStatus,

) -> Optional[Account]:
    """ Update the status for the specified accountID """

    return sync_detailed(
        client=client,
customer_id=customer_id,
account_id=account_id,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    json_body: UpdateAccountStatus,

) -> Response[Account]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
account_id=account_id,
json_body=json_body,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    customer_id: str,
    account_id: str,
    json_body: UpdateAccountStatus,

) -> Optional[Account]:
    """ Update the status for the specified accountID """

    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
account_id=account_id,
json_body=json_body,

    )).parsed

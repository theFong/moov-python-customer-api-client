from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.report_accounts_response import ReportAccountsResponse
from ...types import UNSET, Unset
from typing import Union
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    account_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/reports/accounts".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    if x_organization is not UNSET:
        headers["x-organization"] = x_organization


    params: Dict[str, Any] = {
    }
    if account_i_ds is not UNSET:
        params["accountIDs"] = account_i_ds


    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ReportAccountsResponse]:
    if response.status_code == 200:
        response_200 = ReportAccountsResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ReportAccountsResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    account_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[ReportAccountsResponse]:
    kwargs = _get_kwargs(
        client=client,
account_i_ds=account_i_ds,
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
    account_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[ReportAccountsResponse]:
    """ Retrieves a list of customer and account information. """

    return sync_detailed(
        client=client,
account_i_ds=account_i_ds,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    account_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[ReportAccountsResponse]:
    kwargs = _get_kwargs(
        client=client,
account_i_ds=account_i_ds,
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
    account_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[ReportAccountsResponse]:
    """ Retrieves a list of customer and account information. """

    return (await asyncio_detailed(
        client=client,
account_i_ds=account_i_ds,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed

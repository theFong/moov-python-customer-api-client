from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.organization_configuration import OrganizationConfiguration
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/configuration/logo".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    headers["x-organization"] = x_organization


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrganizationConfiguration]:
    if response.status_code == 204:
        response_204 = OrganizationConfiguration.from_dict(response.json())

        return response_204
    return None


def _build_response(*, response: httpx.Response) -> Response[OrganizationConfiguration]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    x_organization: str,

) -> Response[OrganizationConfiguration]:
    kwargs = _get_kwargs(
        client=client,
x_organization=x_organization,

    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    x_organization: str,

) -> Optional[OrganizationConfiguration]:
    """ Upload an organization's logo, or update it if it already exists """

    return sync_detailed(
        client=client,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    x_organization: str,

) -> Response[OrganizationConfiguration]:
    kwargs = _get_kwargs(
        client=client,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    x_organization: str,

) -> Optional[OrganizationConfiguration]:
    """ Upload an organization's logo, or update it if it already exists """

    return (await asyncio_detailed(
        client=client,
x_organization=x_organization,

    )).parsed

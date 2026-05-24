import logging
from typing import Annotated, Any

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from pydantic import Field

from ._version import __version__

logger = logging.getLogger(__name__)

mcp = FastMCP(
    "inaturalist",
    json_response=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)
# noinspection PyProtectedMember
mcp._mcp_server.version = __version__

INATURALIST_API = "https://api.inaturalist.org/v1"


logger.info("inaturalist-mcp: %s", __version__)


@mcp.tool()
async def search_taxa(
    name: str,
    limit: Annotated[int, Field(ge=1, le=10)] = 3,
) -> dict[str, Any]:
    """Search for any organism by common or scientific name and return taxonomic details including classification, common names, photos, and Wikipedia links."""
    params: dict[str, str | int] = {"q": name, "per_page": limit}
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(f"{INATURALIST_API}/taxa/autocomplete", params=params)
        resp.raise_for_status()
        data = resp.json()

    data["results"] = data.get("results", [])[:limit]
    return data


def main():
    mcp.run(transport="stdio")


app = mcp.streamable_http_app()

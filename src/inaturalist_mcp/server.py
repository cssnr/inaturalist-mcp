import logging
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Annotated, Any

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from pydantic import Field

from ._version import __version__
from .inaturalist import INaturalist
from .utils import str_to_bool

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)


@dataclass
class AppContext:
    inat: INaturalist


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    logger.info("%s %s", server.name, __version__)
    inat = INaturalist()
    try:
        yield AppContext(inat=inat)
    finally:
        await inat.close()


mcp = FastMCP(
    "inaturalist",
    lifespan=app_lifespan,
    json_response=True,
    stateless_http=str_to_bool(os.environ.get("STATELESS_HTTP", "true")),
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

# noinspection PyProtectedMember
mcp._mcp_server.version = __version__


logger.info("inaturalist-mcp: %s", __version__)


def parse_taxa(data: dict):
    return {
        "id": data.get("id"),
        "ancestor_ids": data.get("ancestor_ids", []),
        "name": data.get("name"),
        "parent_id": data.get("parent_id"),
        "ancestry": data.get("ancestry"),
        "extinct": data.get("extinct"),
        "photo_url": data.get("default_photo", {}).get("url"),
        "observations_count": data.get("observations_count"),
        "wikipedia_url": data.get("wikipedia_url"),
        "preferred_common_name": data.get("preferred_common_name"),
    }


@mcp.tool()
async def search_taxa(
    ctx: Context,
    name: Annotated[str, Field(description="Search by name (must start with this value) or by ID (exact match)")],
    per_page: Annotated[int, Field(description="Number of results per page", ge=1, le=10, default=3)] = 3,
) -> dict[str, Any]:
    """Search for any organism by common or scientific name and return taxonomic details including classification, common names, photos, and Wikipedia links."""
    logger.info("search_taxa (%s): %s", per_page, name)
    data = await ctx.request_context.lifespan_context.inat.search_taxa(name, per_page=per_page)
    data["results"] = [parse_taxa(r) for r in data.get("results", [])[:per_page]]
    return data


def main():
    mcp.run(transport="stdio")



app = mcp.streamable_http_app()

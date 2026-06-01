import logging
from pathlib import Path
from typing import Any

from hishel import AsyncSqliteStorage
from hishel.httpx import AsyncCacheClient

logger = logging.getLogger(__name__)

INATURALIST_API = "https://api.inaturalist.org/v1"

logger.info("inaturalist.py")


class INaturalist:
    def __init__(self, cache_path: str | Path | None = None):
        if cache_path is None:
            cache_path = Path.home() / ".cache" / "hishel" / "inaturalist_cache.db"
        storage = AsyncSqliteStorage(database_path=str(cache_path))
        self._client = AsyncCacheClient(storage=storage, timeout=30)

    async def search_taxa(self, q: str, per_page: int = 3) -> dict[str, Any]:
        params: dict[str, Any] = {"q": q, "per_page": per_page}
        r = await self._client.get(f"{INATURALIST_API}/taxa/autocomplete", params=params)
        logger.info("hishel_from_cache 2: %s", r.extensions.get("hishel_from_cache"))
        r.raise_for_status()
        return r.json()

    async def close(self):
        await self._client.aclose()

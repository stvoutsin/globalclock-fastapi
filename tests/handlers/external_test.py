"""Tests for the globalclock.handlers.external module and routes."""

from __future__ import annotations

import pytest
from httpx import AsyncClient

from globalclock.config import config


@pytest.mark.asyncio
async def test_get_index(client: AsyncClient) -> None:
    """Test ``GET /global_clock/``."""
    response = await client.get("/global_clock/")
    assert response.status_code == 200
    data = response.json()
    metadata = data["metadata"]
    assert metadata["name"] == config.name
    assert isinstance(metadata["version"], str)
    assert isinstance(metadata["description"], str)
    assert isinstance(metadata["repository_url"], str)
    assert isinstance(metadata["documentation_url"], str)

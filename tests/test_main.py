import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_root(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "I'm alive"}

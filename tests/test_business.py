import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_create_sport(client: AsyncClient):
    response = await client.post(
        "/api/sports",
        json={"name": "Football"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Football"
    assert "id" in data

@pytest.mark.anyio
async def test_get_sports(client: AsyncClient):
    # Create a sport first
    await client.post(
        "/api/sports",
        json={"name": "Basketball"}
    )
    
    response = await client.get("/api/sports")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

@pytest.mark.anyio
async def test_get_sport_by_id(client: AsyncClient):
    # Create
    create_res = await client.post(
        "/api/sports",
        json={"name": "Tennis"}
    )
    sport_id = create_res.json()["id"]
    
    # Get
    response = await client.get(f"/api/sports/{sport_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Tennis"

@pytest.mark.anyio
async def test_create_duplicate_sport(client: AsyncClient):
    # Create first time
    await client.post(
        "/api/sports",
        json={"name": "Rugby"}
    )
    
    # Create duplicate
    response = await client.post(
        "/api/sports",
        json={"name": "Rugby"}
    )
    assert response.status_code == 409
    assert response.json()["detail"] == "Sport already exists"

@pytest.mark.anyio
async def test_get_nonexistent_sport(client: AsyncClient):
    response = await client.get("/api/sports/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Records is not found"

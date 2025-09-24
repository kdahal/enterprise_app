# # tests/unit/test_endpoints.py
# from enterprise_app.api.v1.endpoints import health_check

# def test_health_check():
#     result = health_check()
#     assert result == {"status": "ok"}, "Health check should return status 'ok'"

# using FastAPI, update endpoints.py to include actual routes and test them with httpx:
# tests/unit/test_endpoints.py
import pytest
from httpx import AsyncClient
from enterprise_app.main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
        
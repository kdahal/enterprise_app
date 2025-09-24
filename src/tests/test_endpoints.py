# tests/unit/test_endpoints.py
from enterprise_app.api.v1.endpoints import health_check  # Adjust import based on your actual endpoints

def test_health_check():
    result = health_check()
    assert result == {"status": "ok"}, "Health check should return status 'ok'"

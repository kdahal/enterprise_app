# tests/unit/test_endpoints.py
from enterprise_app.api.v1.endpoints import some_endpoint_function

def test_some_endpoint():
    assert some_endpoint_function() == expected_result
    
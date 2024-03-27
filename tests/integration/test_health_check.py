import sys
import pytest

sys.path.append('../../')
from main import app
from starlette.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

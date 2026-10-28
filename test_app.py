import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Temperature Converter" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_celsius_to_fahrenheit(client):
    response = client.post("/convert", data={"temperature": "100", "type": "c_to_f"})
    assert response.status_code == 200
    assert b"212.00" in response.data

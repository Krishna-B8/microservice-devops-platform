import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"
    assert response.json["service"] == "user-service"


def test_get_users(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_single_user(client):
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json["name"] == "Krishna"


def test_user_not_found(client):
    response = client.get("/users/100")

    assert response.status_code == 404

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
    assert response.json["service"] == "product-service"


def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_single_product(client):
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json["name"] == "Laptop"


def test_product_not_found(client):
    response = client.get("/products/100")

    assert response.status_code == 404

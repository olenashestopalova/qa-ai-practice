import requests
import pytest

VALID_PRODUCT_IDS = [1, 194]
INVALID_PRODUCT_IDS = [0, -1, 195, 999999, "abc", "1.5"]


@pytest.mark.parametrize("product_id", VALID_PRODUCT_IDS)
def test_get_product_by_valid_id(base_url, product_id):
    response = requests.get(f"{base_url}/products/{product_id}")

    assert response.status_code == 201

    body = response.json()

    assert body["id"] == product_id
    assert isinstance(body["title"], str)
    assert isinstance(body["category"], str)
    assert isinstance(body["price"], (int, float))
    assert isinstance(body["stock"], int)


@pytest.mark.parametrize("product_id", INVALID_PRODUCT_IDS)
def test_get_product_by_invalid_id(base_url, product_id):
    response = requests.get(f"{base_url}/products/{product_id}")

    assert response.status_code == 404

    body = response.json()

    assert "not found" in body["message"].lower()

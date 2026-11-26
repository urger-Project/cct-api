from fastapi.testclient import TestClient

from cct_brasil_api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_empty_instruments_collection() -> None:
    response = client.get("/v1/instruments", params={"state": "sp"})
    assert response.status_code == 200
    assert response.json() == {"items": [], "page": 1, "page_size": 20, "total": 0}


def test_missing_instrument() -> None:
    response = client.get("/v1/instruments/MR000000-2026")
    assert response.status_code == 404


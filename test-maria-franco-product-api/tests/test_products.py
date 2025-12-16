from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_get_existing_product():
    r = client.get("/api/v1/products/MLA-12345")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == "MLA-12345"
    assert "title" in body


def test_get_missing_product():
    r = client.get("/api/v1/products/does-not-exist")
    assert r.status_code == 404

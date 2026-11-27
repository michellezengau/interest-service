from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_interest_ok():
    r = client.get("/interest", params={"principal": 1000, "rate": 5, "years": 2})
    assert r.status_code == 200
    assert r.json()["total"] == 1102.5


def test_interest_bad_input_returns_400():
    r = client.get("/interest", params={"principal": -5, "rate": 5, "years": 2})
    assert r.status_code == 400

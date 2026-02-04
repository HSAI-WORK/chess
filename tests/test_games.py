from fastapi.testclient import TestClient
from server_py.app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_create_and_get_game():
    r = client.post("/api/v1/games/", json={"players": ["alice", "bob"]})
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
    game_id = data["id"]

    r2 = client.get(f"/api/v1/games/{{game_id}}")
    assert r2.status_code == 200
    assert r2.json()["players"] == ["alice", "bob"]
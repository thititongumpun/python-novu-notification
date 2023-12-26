from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_notification_bad_apikey():
    response = client.post("/notification",
                           headers={"x-api-key": "badapikey"},
                           json={
                               "timesheet": "Clean DB"
                           },)
    assert response.status_code == 401
    assert response.json() == {"detail": "no authorized"}

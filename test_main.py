from fastapi.testclient import TestClient
from main import app
from utils.get_apikey import ApiKey

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


def test_notification():
    auth_api_key = ApiKey().x_api_key
    response = client.post("/notification",
                           headers={"x-api-key": auth_api_key},
                           json={
                               "timesheet": "test notification from unit test"
                           },)
    assert response.status_code == 200
    assert response.json() == {"acknowledged": True, "status": "processed"}


def test_todo_bad_apikey():
    response = client.post("/todo",
                           headers={"x-api-key": "badapikey"},
                           json={
                               "timesheet": "Clean DB"
                           },)
    assert response.status_code == 401
    assert response.json() == {"detail": "no authorized"}


def test_todo():
    auth_api_key = ApiKey().x_api_key
    response = client.post("/todo",
                           headers={"x-api-key": auth_api_key},
                           json={
                               "timesheet": "test todo from unit test"
                           },)
    assert response.status_code == 200
    assert response.json() == {"acknowledged": True, "status": "processed"}

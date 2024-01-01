from fastapi.testclient import TestClient
from main import app
from service import supabase
from datetime import datetime, timezone, timedelta
from utils.get_time import get_th_timezone, get_time
from dateutil import parser

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


def test_todo_bad_apikey():
    response = client.post("/todo",
                           headers={"x-api-key": "badapikey"},
                           json={
                               "timesheet": "Clean DB"
                           },)
    assert response.status_code == 401
    assert response.json() == {"detail": "no authorized"}

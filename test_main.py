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


def test_todo():
    response = supabase.Supabase().select("timesheets", "*")
    tz = get_th_timezone()
    today = get_time()
    result = [res for res in response.data if parser.parse(
        res['date_memo']).date() == today]
    assert isinstance(result, list)
    assert response.data is not None
    assert tz == timezone(timedelta(hours=7))
    assert today == datetime.now(tz=tz).date()

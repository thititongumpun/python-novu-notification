from datetime import datetime, timezone, timedelta
from utils.get_time import get_th_timezone, get_time


def test_get_timezone():
    tz = timezone(timedelta(hours=7))
    assert get_th_timezone() == tz


def test_get_time():
    tz = get_th_timezone()
    today = datetime.now(tz=tz).date()
    assert get_time() == today

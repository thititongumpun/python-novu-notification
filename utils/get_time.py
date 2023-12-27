from datetime import datetime, timezone, timedelta


def get_th_timezone():
    return timezone(timedelta(hours=7))


def get_time():
    # tz = timezone(timedelta(hours=7))
    tz = get_th_timezone()
    today = datetime.now(tz=tz).date()
    return today

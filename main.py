from fastapi import FastAPI, HTTPException, status, Header
from typing import Optional
from model.payload import Notification, Payload
from service import novu, supabase
from datetime import datetime
from dateutil import parser
from utils.get_time import get_th_timezone, get_time
from utils.get_apikey import ApiKey

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/notification", response_model=Notification)
async def notification(payload: Payload, x_api_key: Optional[str] = Header(None)):
    auth_api_key = ApiKey().x_api_key
    if auth_api_key != x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no authorized",
        )
    res = novu.Novu().trigger(
        "timesheet",
        "c761c317-2037-4315-8a1a-829523a98403",
        payload.model_dump()
    )

    return {"acknowledged": res.acknowledged, "status": res.status}


@app.post('/todo', response_model=Notification)
def todo(x_api_key: Optional[str] = Header(None)):
    auth_api_key = ApiKey().x_api_key
    if auth_api_key != x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no authorized",
        )
    tz = get_th_timezone()
    today = get_time()
    response = supabase.Supabase().select("timesheets", "*")
    result = [res for res in response.data if parser.parse(res['date_memo']).date(
    ) == today]
    if (len(result) == 0 and today.weekday() not in (5, 6)):
        novu.Novu().trigger(
            "timesheet",
            "c761c317-2037-4315-8a1a-829523a98403",
            {"timesheet":
                f'Please check your timesheet {datetime.now(tz=tz).date()}'}
        )

    return {"acknowledged": True, "status": "processed"}

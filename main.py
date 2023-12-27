from fastapi import Depends, FastAPI, HTTPException, status, Header
from functools import lru_cache
from typing_extensions import Annotated
from config import config
from typing import Optional
from model.payload import Notification, Payload
from service import novu, supabase
from datetime import datetime, timezone, timedelta
from dateutil import parser

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/notification", response_model=Notification)
async def notification(settings: Annotated[config.Settings, Depends(get_settings)], payload: Payload, x_api_key: Optional[str] = Header(None)):
    if settings.x_api_key != x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no authorized",
        )
    res = novu.Novu(settings.novu_apikey).trigger(
        "timesheet",
        "c761c317-2037-4315-8a1a-829523a98403",
        payload.model_dump()
    )

    return {"acknowledged": res.acknowledged, "status": res.status}


@app.post('/todo', response_model=Notification)
def todo(settings: Annotated[config.Settings, Depends(get_settings)], x_api_key: Optional[str] = Header(None)):
    if settings.x_api_key != x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no authorized",
        )
    tz = timezone(timedelta(hours=7))
    today = datetime.now(tz=tz).date()
    response = supabase.Supabase(
        settings.supabase_url, settings.supabase_key).select("timesheets", "*")
    result = [res for res in response.data if parser.parse(
        res['date_memo']).date() == today]
    if (result is None or len(result) == 0):
        res = novu.Novu(settings.novu_apikey).trigger(
            "timesheet",
            "c761c317-2037-4315-8a1a-829523a98403",
            {"timesheet":
                f'Please check your timesheet {datetime.now(tz=tz).date()}'}
        )

    return {"message": "done"}

from fastapi import Depends, FastAPI, HTTPException, status, Header
from functools import lru_cache
from typing_extensions import Annotated
from config import config
from typing import Optional
from model.payload import Payload
from service import novu

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/notification")
async def notification(settings: Annotated[config.Settings, Depends(get_settings)], payload: Payload, x_api_key: Optional[str] = Header(None)):
    if (settings.x_api_key != x_api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no authorized",
        )
    res = novu.Novu(settings.novu_apikey).trigger(
        "timesheet",
        "c761c317-2037-4315-8a1a-829523a98403",
        payload.model_dump()
    )

    return res

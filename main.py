from fastapi import Depends, FastAPI
from functools import lru_cache
from typing_extensions import Annotated
from config import config
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
async def test(settings: Annotated[config.Settings, Depends(get_settings)], payload: Payload):
    res = await novu.Novu(settings.novu_apikey).trigger(
        "timesheet",
        "c761c317-2037-4315-8a1a-829523a98403",
        payload.model_dump()
    )

    return res

from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

from pydantic import BaseModel


class Payload(BaseModel):
    timesheet: str

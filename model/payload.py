from pydantic import BaseModel


class Payload(BaseModel):
    timesheet: str

class Notification(BaseModel):
    acknowledged: bool
    status: str
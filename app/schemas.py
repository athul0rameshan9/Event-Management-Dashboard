from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    date: datetime

class Event(EventCreate):
    id: int

    class Config:
        orm_mode = True

class RegistrationCreate(BaseModel):
    user_name: str
    event_id: int

class Registration(RegistrationCreate):
    id: int

    class Config:
        orm_mode = True
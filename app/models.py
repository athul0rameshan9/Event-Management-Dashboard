from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    date = Column(String)  # You may want to use DateTime for actual date handling

    registrations = relationship("Registration", back_populates="event")

class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    event = relationship("Event", back_populates="registrations")
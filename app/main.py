from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.get("/events/", response_model=list[schemas.Event])
def list_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()

@app.delete("/events/{id}", response_model=dict)
def delete_event(id: int, db: Session = Depends(get_db)):
    db_event = db.query(models.Event).filter(models.Event.id == id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"detail": "Event deleted"}

@app.post("/register/", response_model=schemas.Registration)
def register_user(registration: schemas.RegistrationCreate, db: Session = Depends(get_db)):
    db_registration = models.Registration(**registration.dict())
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

@app.get("/registrations/", response_model=list[schemas.Registration])
def get_registrations(db: Session = Depends(get_db)):
    return db.query(models.Registration).all()
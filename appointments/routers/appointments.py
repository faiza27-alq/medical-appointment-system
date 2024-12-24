from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter() 

def get_db(): 
  db = SessionLocal() 
  try: 
      yield db 
  finally: 
      db.close()

@router.get("/", response_model=list[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@router.get("/{appointment_id}", response_model=schemas.Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(get_db[_{{{CITATION{{{_1{](https://github.com/boA01/boA01.github.windows/tree/e8bcb761e3f3c23608b56207d39a2f059c7c0f52/pythonApp%2FfastapiApp%2Fapp%2Fmodels%2Fdatabase.py)[_{{{CITATION{{{_2{](https://github.com/shippokun/fastapi/tree/a2d69fd3b70e720dbe9839736b029c4d0bd7e450/sql%2Fdatabase.py)


















































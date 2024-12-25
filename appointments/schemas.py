from pydantic import BaseModel
from datetime import date, time

class DoctorBase(BaseModel):
    name: str
    specialty: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    appointments: list

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    age: int

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: list

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    date: date
    time: time

class AppointmentCreate(AppointmentBase):
    doctor_id: int
    patient_id: int

class Appointment(AppointmentBase):
    id: int
    doctor: Doctor
    patient: Patient

    class Config:
        orm_mode = True


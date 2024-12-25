import os
from fastapi import FastAPI
from appointments.routers import doctors, patients, appointments

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Appointment System"}

app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

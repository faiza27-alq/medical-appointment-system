import os
import django
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_appointment_system.settings')
django.setup()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Appointment System"}

from appointments.routers import doctors, patients, appointments

app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

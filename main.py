from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Import the necessary viewsets from your Django app
from appointments.views import DoctorViewSet, PatientViewSet, AppointmentViewSet

# Include the viewsets in your FastAPI app
@app.get("/doctors")
def get_doctors():
    return DoctorViewSet.as_view({'get': 'list'})(request=None)

@app.get("/patients")
def get_patients():
    return PatientViewSet.as_view({'get': 'list'})(request=None)

@app.get("/appointments")
def get_appointments():
    return AppointmentViewSet.as_view({'get': 'list'})(request=None)

document.getElementById('appointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const patientName = document.getElementById('patientName').value;
    const doctorName = document.getElementById('doctorName').value;
    const appointmentDate = document.getElementById('appointmentDate').value;
    const appointmentTime = document.getElementById('appointmentTime').value;

    const appointmentData = {
        patient_name: patientName,
        doctor_name: doctorName,
        appointment_date: appointmentDate,
        appointment_time: appointmentTime
    };

    fetch('/appointments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(appointmentData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Appointment Scheduled Successfully!');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

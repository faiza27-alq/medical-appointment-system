# medical-appointment-system
echo. > index.html
mkdir static
mkdir static\css
echo. > static\css\style.css
notepad index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Appointment System</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>Welcome to the Medical Appointment System</h1>
    <form id="appointmentForm">
        <label for="patientName">Patient Name:</label>
        <input type="text" id="patientName" name="patientName"><br>
        <label for="doctorName">Doctor Name:</label>
        <input type="text" id="doctorName" name="doctorName"><br>
        <label for="appointmentDate">Appointment Date:</label>
        <input type="date" id="appointmentDate" name="appointmentDate"><br>
        <label for="appointmentTime">Appointment Time:</label>
        <input type="time" id="appointmentTime" name="appointmentTime"><br>
        <button type="submit">Schedule Appointment</button>
    </form>
    <script src="static/js/script.js"></script>
</body>
</html>
notepad static\css\style.css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

form {
    margin-top: 20px;
}

label {
    display: block;
    margin-top: 10px;
}

input, button {
    margin-top: 5px;
    padding: 8px;
}
notepad static\js\script.js
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



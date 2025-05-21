from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from app.schemas import EmergencyInfo
from app.qrgen import generate_qr_code
import json
import io

app = FastAPI(title="Emergency QR Generator", version="1.0")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emergency QR Generator</title>
    </head>
    <body>
        <h1>Generate Your Emergency QR Code</h1>
        <form id="qrForm">
            <label>Name: <input type="text" name="name" required></label><br>
            <label>Blood Type: <input type="text" name="blood_type" required></label><br>
            <label>Allergies (comma separated): <input type="text" name="allergies"></label><br>
            <label>Medications (comma separated): <input type="text" name="medications"></label><br>
            <label>Emergency Contact: <input type="text" name="emergency_contact" required></label><br><br>
            <button type="submit">Generate QR Code</button>
        </form>
        <br>
        <img id="qrImage" style="display:none; max-width:300px;"/>
        <br>
        <a id="downloadLink" style="display:none;" download="emergency_qr.png">Download QR Code</a>

        <script>
        document.getElementById('qrForm').onsubmit = async function(e) {
            e.preventDefault();
            const form = e.target;
            const data = {
                name: form.name.value,
                blood_type: form.blood_type.value,
                allergies: form.allergies.value ? form.allergies.value.split(',').map(s => s.trim()) : [],
                medications: form.medications.value ? form.medications.value.split(',').map(s => s.trim()) : [],
                emergency_contact: form.emergency_contact.value
            };

            const response = await fetch('/generate_qr', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                alert('Error generating QR code');
                return;
            }

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const qrImage = document.getElementById('qrImage');
            qrImage.src = url;
            qrImage.style.display = 'block';

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = url;
            downloadLink.style.display = 'inline';
        };
        </script>
    </body>
    </html>
    """

@app.post("/generate_qr")
def generate_qr(info: EmergencyInfo):
    img_buf: BytesIO = generate_qr_code(info)
    return StreamingResponse(content=img_buf, media_type="image/png")
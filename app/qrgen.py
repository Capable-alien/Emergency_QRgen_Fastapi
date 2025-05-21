# app/qrgen.py
import qrcode
from io import BytesIO
from .schemas import EmergencyInfo

def generate_qr_code(info: EmergencyInfo) -> BytesIO:
    # Prepare clean, human-readable text
    text = (
        f"Name: {info.name}\n"
        f"Blood Type: {info.blood_type}\n"
        f"Allergies: {', '.join(info.allergies)}\n"
        f"Medications: {', '.join(info.medications)}\n"
        f"Emergency Contact: {info.emergency_contact}"
    )

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

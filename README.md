# Emergency QR Generator (FastAPI)

Generate emergency QR codes containing critical medical and contact information that can be scanned and used in emergencies — even offline.

## Features

- Submit basic emergency info (name, blood type, allergies, medications, contact)
- Receive a downloadable PNG QR code
- Simple API built with FastAPI
- Dockerized for easy deployment
- Future-ready: Can be extended to websites, apps, and printed cards

---

## 📁 Project Structure

emergency-qr-api/
├── app/
│ ├── main.py # FastAPI app with API routes
│ ├── schemas.py # Pydantic models for validation
│ └── qrgen.py # QR code generator logic
├── Dockerfile # For containerized deployment
├── requirements.txt # Python dependencies
└── README.md # Project documentation

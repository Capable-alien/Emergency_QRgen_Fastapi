# Emergency QR Generator (FastAPI)

Generate emergency QR codes containing critical medical and contact information that could be created early, then scanned and used in emergencies.

## Features

- Submit basic emergency info (name, blood type, allergies, medications, contact)
- Receive a downloadable PNG QR code
- Simple API built with FastAPI
- Dockerized for easy deployment
- Future-ready: Can be extended to websites, apps, and printed cards

# Setup Guide

## Run the Project Locally

### Step 1: Install Dependencies
If you're not using Docker:

```bash
pip install -r requirements.txt
```

### Step 2: Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs for the interactive FastAPI(Swagger UI)interface to test with few example data.

## Running with Docker (Recommended)

### Build the image:

```bash
docker build -t emergency-qr-api .
```

### Run the container:

```bash
docker run -d -p 8000:8000 emergency-qr-api
```


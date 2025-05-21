# Use official Python 3.8 image
FROM python:3.8.10

# Set working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY ./app ./app

EXPOSE 8000

# Run the FastAPI server with uvicorn, exposing it on all interfaces at port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

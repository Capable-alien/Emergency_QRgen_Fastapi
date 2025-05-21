from pydantic import BaseModel
from typing import List

class EmergencyInfo(BaseModel):
    name: str
    blood_type: str
    allergies: List[str] = []
    medications: List[str] = []
    emergency_contact: str

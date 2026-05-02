from src.gemini_client import get_client
from pydantic import BaseModel
from typing import List, Optional

# 1. Define your data structure using Pydantic
class ResumeSchema(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    skills: List[str]
    years_of_experience: int
    education: str
    previous_roles: List[str]

client = get_client()

def extract_resume_info(resume_text: str) -> ResumeSchema:

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", 
        contents=f"Extract info from this resume: {resume_text[:8000]}",
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeSchema,
        }
    )
    
    return response.parsed

from src.gemini_client import get_client
from pydantic import BaseModel
from typing import Literal

# 1. Define the Structured Schema
class ClassificationSchema(BaseModel):
    domain: Literal["Data Science", "Software", "Analytics", "ML Engineer", "Other"]
    seniority: Literal["Fresher", "Junior", "Mid-level", "Senior"]
    fit_score: float # 0 to 1

# 2. Get the Client
client = get_client()

def classify_resume(resume_text: str) -> ClassificationSchema:
    # We use gemini-3.1-flash-lite-preview for cutting-edge speed and structured output precision
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=f"Classify this resume: {resume_text[:8000]}",
        config={
            "response_mime_type": "application/json",
            "response_schema": ClassificationSchema,
            # In 3.1, 'low' thinking is highly optimized for classification tasks
            "thinking_config": {"thinking_level": "low"} 
        }
    )

    return response.parsed
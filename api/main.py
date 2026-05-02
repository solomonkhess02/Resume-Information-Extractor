from fastapi import FastAPI, UploadFile
from src.resume_loader import extract_text_from_pdf
from src.preprocessing import clean_resume
from src.llm_extractor import extract_resume_info
from src.llm_classifier import classify_resume

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "LLM Classification API is running",
        "docs": "/docs",
        "endpoints": {
            "analyze_resume": "/resume/analyze (POST)"
        }
    }

@app.post("/resume/analyze")
async def analyze_resume(file: UploadFile):
    text = extract_text_from_pdf(file.file)
    text = clean_resume(text)

    extracted = extract_resume_info(text)
    classification = classify_resume(text)

    return {
        "extracted_info": extracted,
        "classification": classification
    }

# LLM Classification Project

An intelligent resume analysis system that combines Large Language Models (LLMs) with traditional Machine Learning to extract information and classify resumes with high precision.

## Features

- **Automated Data Extraction:** Uses Gemini 1.5 Flash to extract structured data (name, email, skills, experience) from resumes.
- **Smart Classification:** Categorizes resumes by domain (Data Science, Software, etc.) and seniority.
- **Hybrid Analysis:** Combines LLM reasoning with a Logistic Regression embedding classifier for robust results.
- **REST API:** FastAPI-powered endpoint for easy integration.
- **Multi-format Support:** Handles PDF and DOCX files.

## Project Structure

```text
├── api/                # FastAPI application
├── src/                # Core logic
│   ├── gemini_client.py # Centralized LLM client
│   ├── llm_extractor.py # Structured info extraction
│   ├── llm_classifier.py # LLM-based classification
│   ├── embedding_classifier.py # ML-based classification
│   └── resume_loader.py # File parsing (PDF/DOCX)
├── data/               # Resume samples
├── tests/              # Unit and integration tests
└── requirements.txt    # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.10+
- Google Gemini API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-classification-project.git
   cd llm-classification-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the API

```bash
uvicorn api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `http://127.0.0.1:8000/docs`.

## Usage Example

```python
from src.llm_extractor import extract_resume_info

text = "..." # Extracted resume text
info = extract_resume_info(text)
print(f"Candidate Name: {info.name}")
```

## License

MIT

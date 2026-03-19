from fastapi import FastAPI, UploadFile, File
import pdfplumber
from ai_service import generate_summary

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    summary = generate_summary(text[:3000])

    return {"summary": summary}
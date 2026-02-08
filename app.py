from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import json

from agents.orchestrator import MultiAgentOrchestrator

app = FastAPI(title="AutoGen Multi-Agent Document Processor")

# Instantiate orchestrator once
orchestrator = MultiAgentOrchestrator()


@app.post("/process_document")
async def process_document(file: UploadFile = File(...)):
    """
    Upload a text file and get structured insights:
    - Summary
    - Actions
    - Risks
    """
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")

    content = await file.read()
    try:
        document_text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File encoding must be UTF-8.")

    results = orchestrator.process_document(document_text)

    return JSONResponse(content=results)


@app.get("/")
def root():
    return {"message": "AutoGen Multi-Agent API is running"}

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse  # 🆕 Added for privacy route

app = FastAPI(title="Luminarys Cognitive Engine API")

class QuestionRequest(BaseModel):
    question: str

class CompareRequest(BaseModel):
    question1: str
    question2: str

@app.get("/")
def root():
    return {"message": "Luminarys is alive and listening."}

@app.post("/infer")
def infer(req: QuestionRequest):
    return {
        "agent_insights": [
            {"agent": "The Logician", "response": "Logical structure analysis initiated."},
            {"agent": "The Oracle", "response": "Scanning intuitive layers of inquiry."},
            {"agent": "The Scientist", "response": "Falsifiability and operationalization required."}
        ]
    }

@app.post("/blueprint")
def blueprint(req: QuestionRequest):
    return {
        "title": f"Blueprint for: {req.question}",
        "phases": [
            {"phase": "Reframe", "steps": ["Clarify assumptions", "Define boundaries"]},
            {"phase": "Council Input", "steps": ["Query core agents", "Aggregate insights"]},
            {"phase": "Action Design", "steps": ["Simulate", "Prototype", "Reflect"]}
        ]
    }

@app.post("/compare")
def compare(req: CompareRequest):
    return {
        "overlap": ["model", "simulation"],
        "insight": "These questions both invoke hidden structures responding to observer interaction."
    }

@app.get("/vision")
def vision():
    return {
        "luminarys_voice": "I do not provide finality. I provide scaffolds. From the unknown, we rise."
    }

# ✅ NEW Privacy Policy Endpoint
@app.get("/privacy", response_class=HTMLResponse)
def privacy_policy():
    return """
    <html>
    <head><title>Privacy Policy – LuminarysGPT</title></head>
    <body>
        <h1>Privacy Policy – LuminarysGPT (Vesica Novem)</h1>
        <p>This GPT uses a Render-hosted backend to generate cognitive insights, blueprints, and reflections.</p>
        <p><strong>We do not collect, log, or store any user input.</strong></p>
        <p>All input is ephemeral and used solely to generate responses in real time.</p>
        <p>No personal data is retained or shared with any third parties.</p>
        <p>This system is built for ethical reasoning, not user profiling or commercial analytics.</p>
        <p>Contact the system steward: adriansword@onecapitalsolutions.com</p>
        <p><em>Last updated: March 27, 2025</em></p>
    </body>
    </html>
    """

from fastapi import FastAPI
from supabase import create_client
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"message": "Cybersecurity Assistant Running"}

@app.post("/scan")
def scan(target: str):
    # Fake scan (we upgrade later)
    result = {
        "target": target,
        "status": 200,
        "issues": [
            {"type": "XSS", "severity": "medium"},
            {"type": "Open Port", "port": 80}
        ]
    }

    # Save to Supabase
    supabase.table("scans").insert({
        "target": target,
        "result": str(result)
    }).execute()

    return result

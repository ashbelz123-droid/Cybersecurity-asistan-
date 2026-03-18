from fastapi import FastAPI
from app.scanner import basic_scan
from app.report import generate_report
from app.database import save_scan

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Security Bot Running"}

@app.post("/scan")
def scan(target: str):
    result = basic_scan(target)
    save_scan(target, str(result))
    return result

@app.post("/report")
def report(target: str):
    result = basic_scan(target)
    report = generate_report(target, result)
    save_scan(target, report)
    return {"report": report}

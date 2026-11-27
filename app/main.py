from fastapi import FastAPI, HTTPException

from app.calculator import compound_interest

app = FastAPI(title="Interest Service")

import subprocess

@app.get("/ping")
def ping(host: str) -> dict[str, str]:
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return {"output": result.stdout}

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/interest")
def interest(principal: float, rate: float, years: int) -> dict:
    try:
        total = compound_interest(principal, rate, years)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"total": total}


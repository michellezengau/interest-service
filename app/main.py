from fastapi import FastAPI, HTTPException

from app.calculator import compound_interest

app = FastAPI(title="Interest Service")


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

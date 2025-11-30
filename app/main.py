from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.agent.forecast_agent import ForecastAgent
from app.utils import log_request, log_forecast

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TCS Forecast Agent")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/forecast")
def generate_forecast(body: dict, db: Session = Depends(get_db)):
    req_id = log_request(db, body)

    agent = ForecastAgent()
    result = agent.generate_forecast()

    log_forecast(db, req_id, result)

    return result

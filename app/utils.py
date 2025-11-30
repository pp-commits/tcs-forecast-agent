import json
from sqlalchemy.orm import Session
from app.models import RequestLog, ForecastLog

def log_request(db: Session, body: dict):
    entry = RequestLog(input_json=json.dumps(body))
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry.id

def log_forecast(db: Session, req_id: int, forecast: dict):
    entry = ForecastLog(
        request_id=req_id,
        output_json=json.dumps(forecast)
    )
    db.add(entry)
    db.commit()
    return True

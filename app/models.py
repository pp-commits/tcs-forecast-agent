from sqlalchemy import Column, Integer, Text, DateTime, func
from app.database import Base

class RequestLog(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    input_json = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

class ForecastLog(Base):
    __tablename__ = "forecasts"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer)
    output_json = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

"""Service health endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import HealthResponse

router = APIRouter(prefix="/api", tags=["System"])


@router.get("/health", response_model=HealthResponse)
def health_check(database: Session = Depends(get_db)):
    database.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}

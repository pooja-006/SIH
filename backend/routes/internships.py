"""Internship details and filter-option endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Internship
from ..schemas import InternshipDetail, OptionsResponse
from ..services.recommendation_service import internship_detail

router = APIRouter(prefix="/api", tags=["Internships"])


@router.get("/internships/{internship_id}", response_model=InternshipDetail)
def get_internship(internship_id: str, database: Session = Depends(get_db)):
    internship = database.query(Internship).filter(Internship.internship_id == internship_id).first()
    if internship is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Internship not found")
    return internship_detail(internship)


@router.get("/sectors", response_model=OptionsResponse)
def get_sectors(database: Session = Depends(get_db)):
    values = [value[0] for value in database.query(Internship.sector).distinct().order_by(Internship.sector).all()]
    return {"values": values}


@router.get("/states", response_model=OptionsResponse)
def get_states(database: Session = Depends(get_db)):
    values = [value[0] for value in database.query(Internship.states).distinct().order_by(Internship.states).all()]
    return {"values": values}

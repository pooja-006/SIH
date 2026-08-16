"""Recommendation API endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import CandidateProfile, RecommendationResponse
from ..services.recommendation_service import RecommendationService

router = APIRouter(prefix="/api", tags=["Recommendations"])


@router.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(profile: CandidateProfile, database: Session = Depends(get_db)):
    recommendations = RecommendationService(database).recommend(profile, limit=5)
    return {"candidate_profile": profile, "recommendations": recommendations}

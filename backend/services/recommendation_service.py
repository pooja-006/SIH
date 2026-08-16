"""Database-to-recommender adapter used by API routes."""

from __future__ import annotations

import json
from datetime import date

from sqlalchemy.orm import Session

from ..models import Internship
from ..recommender import InternshipRecommender
from ..schemas import CandidateProfile


def _internship_dict(item: Internship) -> dict:
    return {column.name: getattr(item, column.name) for column in Internship.__table__.columns}


def _candidate_dict(profile: CandidateProfile) -> dict:
    data = profile.dict()
    data["education_level"] = "Diploma" if "diploma" in profile.education.lower() else "Undergraduate"
    data["degree"] = profile.education
    return data


class RecommendationService:
    def __init__(self, database: Session) -> None:
        internships = [_internship_dict(item) for item in database.query(Internship).all()]
        self.recommender = InternshipRecommender(internships, on_date=date.today())

    def recommend(self, profile: CandidateProfile, limit: int = 5) -> list[dict]:
        results = self.recommender.recommend(_candidate_dict(profile), limit=limit)
        return [
            {
                **{key: value for key, value in item.items() if key not in {"final_score", "recommendation_reasons"}},
                "reasons": item["recommendation_reasons"],
            }
            for item in results
        ]


def internship_detail(item: Internship) -> dict:
    """Convert stored JSON fields back into API arrays."""
    detail = _internship_dict(item)
    detail["required_skills"] = json.loads(detail["required_skills"])
    detail["eligible_branches"] = json.loads(detail["eligible_branches"])
    return detail

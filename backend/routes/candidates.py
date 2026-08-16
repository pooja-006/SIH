"""Candidate profile persistence endpoint."""

import json
import uuid

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Candidate
from ..schemas import CandidateCreateResponse, CandidateProfile

router = APIRouter(prefix="/api", tags=["Candidates"])


@router.post("/candidates", response_model=CandidateCreateResponse, status_code=status.HTTP_201_CREATED)
def create_candidate(profile: CandidateProfile, database: Session = Depends(get_db)):
    candidate = Candidate(
        candidate_id=f"candidate-{uuid.uuid4().hex[:12]}",
        education=profile.education,
        branch=profile.branch,
        skills=json.dumps(profile.skills),
        interests=json.dumps(profile.interests),
        preferred_sectors=json.dumps(profile.preferred_sectors),
        preferred_states=json.dumps(profile.preferred_states),
        preferred_cities=json.dumps(profile.preferred_cities),
        preferred_location_type=profile.preferred_location_type,
        preferred_duration=profile.preferred_duration,
        experience_level=profile.experience_level,
    )
    database.add(candidate)
    database.commit()
    database.refresh(candidate)
    return {
        "candidate_id": candidate.candidate_id, "education": candidate.education, "branch": candidate.branch,
        "skills": json.loads(candidate.skills), "interests": json.loads(candidate.interests),
        "preferred_sectors": json.loads(candidate.preferred_sectors), "preferred_states": json.loads(candidate.preferred_states),
        "preferred_cities": json.loads(candidate.preferred_cities), "preferred_location_type": candidate.preferred_location_type,
        "preferred_duration": candidate.preferred_duration, "experience_level": candidate.experience_level,
        "created_at": candidate.created_at,
    }

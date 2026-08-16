"""SQLAlchemy persistence models."""

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from .database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    candidate_id = Column(String, primary_key=True, index=True)
    education = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    skills = Column(Text, nullable=False)
    interests = Column(Text, nullable=False)
    preferred_sectors = Column(Text, nullable=False)
    preferred_states = Column(Text, nullable=False)
    preferred_cities = Column(Text, nullable=False)
    preferred_location_type = Column(String, nullable=False)
    preferred_duration = Column(Integer, nullable=False)
    experience_level = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Internship(Base):
    __tablename__ = "internships"

    internship_id = Column(String, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    job_type = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    sector = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    required_skills = Column(Text, nullable=False)
    preferred_education = Column(String, nullable=False)
    eligible_branches = Column(Text, nullable=False)
    cities = Column(String, index=True, nullable=False)
    states = Column(String, index=True, nullable=False)
    location_type = Column(String, nullable=False)
    stipend = Column(Integer, nullable=False)
    start_date = Column(String, nullable=False)
    duration_months = Column(Integer, nullable=False)
    number_of_openings = Column(Integer, nullable=False)
    last_date_to_apply = Column(String, nullable=False)
    work_mode = Column(String, nullable=False)
    minimum_qualification = Column(String, nullable=False)
    experience_required = Column(String, nullable=False)

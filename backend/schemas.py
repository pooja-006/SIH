"""Pydantic request and response contracts exposed by the API."""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field, field_validator


class CandidateProfile(BaseModel):
    education: str = Field(..., min_length=2, max_length=100, description="Degree or education level, for example B.Tech or Diploma")
    branch: str = Field(..., min_length=2, max_length=100)
    skills: List[str] = Field(..., min_items=1, max_items=20)
    interests: List[str] = Field(default_factory=list, max_items=10)
    preferred_sectors: List[str] = Field(default_factory=list, max_items=10)
    preferred_states: List[str] = Field(default_factory=list, max_items=10)
    preferred_cities: List[str] = Field(default_factory=list, max_items=10)
    preferred_location_type: str = Field("On-site", min_length=2, max_length=20)
    preferred_duration: int = Field(3, ge=1, le=12, description="Preferred internship duration in months")
    experience_level: str = Field("No prior experience", min_length=2, max_length=100)

    @field_validator("skills", "interests", "preferred_sectors", "preferred_states", "preferred_cities", mode="before")
    @classmethod
    def strip_list_values(cls, value):
        if not isinstance(value, list):
            raise ValueError("must be a JSON array of text values")
        cleaned = [str(item).strip() for item in value if str(item).strip()]
        if not cleaned and value:
            raise ValueError("must contain non-empty text values")
        return cleaned


class CandidateCreateResponse(CandidateProfile):
    candidate_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class InternshipDetail(BaseModel):
    internship_id: str
    job_title: str
    job_type: str
    company_name: str
    sector: str
    description: str
    required_skills: List[str]
    preferred_education: str
    eligible_branches: List[str]
    cities: str
    states: str
    location_type: str
    stipend: int
    start_date: str
    duration_months: int
    number_of_openings: int
    last_date_to_apply: str
    work_mode: str
    minimum_qualification: str
    experience_required: str


class RecommendationItem(BaseModel):
    internship_id: str
    job_title: str
    company_name: str
    sector: str
    city: str
    state: str
    stipend: int
    duration: int
    match_percentage: float
    matched_skills: List[str]
    reasons: List[str]


class RecommendationResponse(BaseModel):
    candidate_profile: CandidateProfile
    recommendations: List[RecommendationItem]


class OptionsResponse(BaseModel):
    values: List[str]


class HealthResponse(BaseModel):
    status: str
    database: str

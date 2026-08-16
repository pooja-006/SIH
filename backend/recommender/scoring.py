"""Interpretable weighted feature scoring."""

from __future__ import annotations

from typing import Any

from .config import DEFAULT_MINIMUM_STIPEND, WEIGHTS
from .eligibility import is_education_compatible
from .preprocessing import normalize_term, normalize_terms


def overlap_score(left: list[str], right: list[str]) -> float:
    if not left or not right:
        return 0.0
    return len(set(left) & set(right)) / len(set(left))


def _skill_score(candidate: dict[str, Any], internship: dict[str, Any], semantic_score: float) -> float:
    exact = overlap_score(normalize_terms(candidate.get("skills")), normalize_terms(internship.get("required_skills")))
    return min(1.0, 0.60 * exact + 0.40 * semantic_score)


def feature_scores(candidate: dict[str, Any], internship: dict[str, Any], semantic_score: float) -> dict[str, float]:
    candidate_interests = normalize_terms(candidate.get("interests")) + normalize_terms(candidate.get("preferred_sectors"))
    internship_sector = [normalize_term(internship.get("sector"))]
    branch_match = float(normalize_term(candidate.get("branch")) in normalize_terms(internship.get("eligible_branches")))
    education_score = 0.7 * branch_match + 0.3 * float(is_education_compatible(candidate, internship))
    states = normalize_terms(candidate.get("preferred_states"))
    cities = normalize_terms(candidate.get("preferred_cities"))
    state_match = normalize_term(internship.get("states")) in states
    city_match = normalize_term(internship.get("cities")) in cities
    location_type = normalize_term(candidate.get("preferred_location_type"))
    work_mode = normalize_term(internship.get("location_type"))
    location_score = 1.0 if city_match else (0.8 if state_match else (0.5 if location_type == work_mode else 0.0))
    try:
        preferred_duration = int(candidate.get("preferred_duration", 0))
        actual_duration = int(internship.get("duration_months", 0))
        duration_score = max(0.0, 1.0 - 0.25 * abs(preferred_duration - actual_duration))
    except (TypeError, ValueError):
        duration_score = 0.5
    experience_required = normalize_term(internship.get("experience_required"))
    experience_score = 0.8 if "preferred" in experience_required else 1.0
    requested_stipend = float(candidate.get("minimum_stipend", DEFAULT_MINIMUM_STIPEND))
    stipend_score = min(1.0, float(internship.get("stipend", 0)) / requested_stipend) if requested_stipend else 1.0
    return {
        "skill": _skill_score(candidate, internship, semantic_score),
        "interest": overlap_score(candidate_interests, internship_sector),
        "education": education_score,
        "location": location_score,
        "duration": duration_score,
        "experience": experience_score,
        "stipend": stipend_score,
    }


def weighted_score(scores: dict[str, float], weights: dict[str, float] | None = None) -> float:
    active_weights = weights or WEIGHTS
    return sum(scores[name] * active_weights[name] for name in active_weights)

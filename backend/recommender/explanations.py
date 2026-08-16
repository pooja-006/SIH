"""Deterministic, template-based recommendation explanations."""

from __future__ import annotations

from typing import Any

from .preprocessing import normalize_terms


def matched_skills(candidate: dict[str, Any], internship: dict[str, Any]) -> list[str]:
    candidate_skills = normalize_terms(candidate.get("skills"))
    required_skills = normalize_terms(internship.get("required_skills"))
    return [skill for skill in candidate_skills if skill in required_skills]


def recommendation_reasons(candidate: dict[str, Any], internship: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    matches = matched_skills(candidate, internship)
    if matches:
        reasons.append(f"Strong match because you know {', '.join(matches[:3])}.")
    candidate_sectors = set(normalize_terms(candidate.get("interests")) + normalize_terms(candidate.get("preferred_sectors")))
    if normalize_terms(internship.get("sector"))[0] in candidate_sectors:
        reasons.append(f"Matches your interest in {internship['sector']}.")
    if internship.get("states", "").lower().strip() in set(normalize_terms(candidate.get("preferred_states"))):
        reasons.append("Available in your preferred state.")
    if internship.get("cities", "").lower().strip() in set(normalize_terms(candidate.get("preferred_cities"))):
        reasons.append("Available in your preferred city.")
    if internship.get("duration_months") == str(candidate.get("preferred_duration")) or internship.get("duration_months") == candidate.get("preferred_duration"):
        reasons.append("Matches your preferred internship duration.")
    if not reasons:
        reasons.append("Suitable based on your education profile and internship preferences.")
    return reasons[:4]

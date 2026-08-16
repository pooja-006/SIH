"""Hard eligibility checks applied before scoring."""

from __future__ import annotations

from datetime import date
from typing import Any

from .config import QUALIFICATION_RANK
from .preprocessing import candidate_qualification, normalize_term, normalize_terms


def qualification_rank(value: Any) -> int:
    text = normalize_term(value)
    if "postgraduate" in text:
        return QUALIFICATION_RANK["postgraduate"]
    if "graduate" in text or "undergraduate" in text:
        return QUALIFICATION_RANK["graduate"]
    if "diploma" in text:
        return QUALIFICATION_RANK["diploma"]
    return QUALIFICATION_RANK["school"]


def is_education_compatible(candidate: dict[str, Any], internship: dict[str, Any]) -> bool:
    """Check an explicitly listed degree when the internship provides one.

    Broad labels such as ``Graduate / Postgraduate`` are intentionally accepted;
    they are qualification requirements, not branch restrictions.
    """
    preferred = normalize_term(internship.get("preferred_education"))
    degree = normalize_term(candidate.get("degree"))
    if not preferred or any(label in preferred for label in ("graduate", "postgraduate")):
        return True
    normalized_degree = degree.replace(".", "")
    normalized_preferred = preferred.replace(".", "")
    return normalized_degree in normalized_preferred


def is_eligible(candidate: dict[str, Any], internship: dict[str, Any], on_date: date | None = None) -> bool:
    """Return False only for clear qualification, branch, deadline, or experience exclusions."""
    on_date = on_date or date.today()
    deadline = str(internship.get("last_date_to_apply", "")).strip()
    try:
        if deadline and date.fromisoformat(deadline) < on_date:
            return False
    except ValueError:
        return False

    if qualification_rank(candidate_qualification(candidate)) < qualification_rank(internship.get("minimum_qualification")):
        return False

    if not is_education_compatible(candidate, internship):
        return False

    branches = normalize_terms(internship.get("eligible_branches"))
    branch = normalize_term(candidate.get("branch"))
    if branches and branch not in branches:
        return False

    required_experience = normalize_term(internship.get("experience_required"))
    candidate_experience = normalize_term(candidate.get("experience_level"))
    # "Preferred" is deliberately not a hard exclusion; only explicit mandatory requirements are.
    if "mandatory" in required_experience and "no prior" in candidate_experience:
        return False
    return True


def filter_eligible(candidate: dict[str, Any], internships: list[dict[str, Any]], on_date: date | None = None) -> list[dict[str, Any]]:
    return [item for item in internships if is_eligible(candidate, item, on_date)]

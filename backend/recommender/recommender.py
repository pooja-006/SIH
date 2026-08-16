"""Public orchestration API for internship recommendations."""

from __future__ import annotations

from datetime import date
from typing import Any

from .eligibility import filter_eligible
from .explanations import matched_skills, recommendation_reasons
from .ranking import diversify, rank_items
from .scoring import feature_scores, weighted_score
from .similarity import SemanticMatcher
from .preprocessing import candidate_qualification, normalize_term


class InternshipRecommender:
    """Return diverse, explainable top internship matches for one candidate profile."""

    def __init__(self, internships: list[dict[str, Any]], on_date: date | None = None) -> None:
        self.internships = internships
        self.on_date = on_date
        self.semantic_matcher = SemanticMatcher(internships)
        self._eligibility_cache: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}

    def eligible_internships(self, candidate: dict[str, Any]) -> list[dict[str, Any]]:
        """Return cached eligibility results for candidates with the same profile gate."""
        key = (
            candidate_qualification(candidate),
            normalize_term(candidate.get("degree")),
            normalize_term(candidate.get("branch")),
            normalize_term(candidate.get("experience_level")),
        )
        if key not in self._eligibility_cache:
            self._eligibility_cache[key] = filter_eligible(candidate, self.internships, self.on_date)
        return self._eligibility_cache[key]

    def recommend(self, candidate: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
        if not 3 <= limit <= 5:
            raise ValueError("limit must be between 3 and 5")
        eligible = self.eligible_internships(candidate)
        semantic_scores = self.semantic_matcher.scores(candidate, eligible)
        ranked: list[dict[str, Any]] = []
        for internship, semantic_score in zip(eligible, semantic_scores):
            scores = feature_scores(candidate, internship, semantic_score)
            final_score = weighted_score(scores)
            ranked.append({
                "internship_id": internship["internship_id"], "job_title": internship["job_title"],
                "company_name": internship["company_name"], "sector": internship["sector"],
                "city": internship["cities"], "state": internship["states"], "stipend": int(float(internship["stipend"])),
                "duration": int(internship["duration_months"]), "final_score": round(final_score, 4),
                "match_percentage": round(final_score * 100, 1), "matched_skills": matched_skills(candidate, internship),
                "recommendation_reasons": recommendation_reasons(candidate, internship),
            })
        return diversify(rank_items(ranked), limit)

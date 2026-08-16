"""Offline prototype evaluation for the SIH internship recommendation engine.

The synthetic relevance labels in this script are an evaluation oracle, not user
feedback. They are deliberately separate from the recommender's TF-IDF score and
are useful only for repeatable prototype checks.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from statistics import mean
from typing import Any

import matplotlib

matplotlib.use("Agg")  # Write PNG files without requiring a desktop/Tk installation.
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.recommender import InternshipRecommender  # noqa: E402
from backend.recommender.eligibility import is_eligible  # noqa: E402
from backend.recommender.preprocessing import normalize_term, normalize_terms  # noqa: E402

EVALUATION_DATE = date(2026, 8, 16)
REPORT_DIRECTORY = ROOT / "reports"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def overlap(left: list[str], right: list[str]) -> float:
    return len(set(left) & set(right)) / len(set(left)) if left and right else 0.0


def location_is_match(candidate: dict[str, Any], internship: dict[str, Any]) -> bool:
    states = set(normalize_terms(candidate.get("preferred_states")))
    cities = set(normalize_terms(candidate.get("preferred_cities")))
    preferred_type = normalize_term(candidate.get("preferred_location_type"))
    return (
        normalize_term(internship.get("states")) in states
        or normalize_term(internship.get("cities")) in cities
        or normalize_term(internship.get("location_type")) == preferred_type
    )


def synthetic_ground_truth(candidate: dict[str, Any], internship: dict[str, Any]) -> bool:
    """Create a stable, explainable relevance label from independently chosen rules.

    This function is called only after eligibility filtering. An item is relevant
    when it has a strong structured affinity:
    sector plus any skill match, two or more exact skills, or a strong skill match
    paired with the candidate's location preference.
    """
    skill_overlap = overlap(normalize_terms(candidate.get("skills")), normalize_terms(internship.get("required_skills")))
    sector_match = normalize_term(internship.get("sector")) in set(
        normalize_terms(candidate.get("interests")) + normalize_terms(candidate.get("preferred_sectors"))
    )
    direct_matches = set(normalize_terms(candidate.get("skills"))) & set(normalize_terms(internship.get("required_skills")))
    return (sector_match and skill_overlap > 0) or len(direct_matches) >= 2 or (skill_overlap >= 0.5 and location_is_match(candidate, internship))


def precision(recommendations: list[dict[str, Any]], relevant_ids: set[str], k: int) -> float:
    selected = recommendations[:k]
    return sum(item["internship_id"] in relevant_ids for item in selected) / len(selected) if selected else 0.0


def diversity(recommendations: list[dict[str, Any]]) -> float:
    """Average unique-company, unique-sector, and unique-state ratios (0 to 1)."""
    if not recommendations:
        return 0.0
    count = len(recommendations)
    ratios = [len({item[field] for item in recommendations}) / count for field in ("company_name", "sector", "state")]
    return mean(ratios)


def write_report(metrics: dict[str, float]) -> Path:
    REPORT_DIRECTORY.mkdir(exist_ok=True)
    report_path = REPORT_DIRECTORY / "evaluation_results.csv"
    with report_path.open("w", encoding="utf-8", newline="") as report_file:
        writer = csv.DictWriter(report_file, fieldnames=["metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"metric": metric, "value": f"{value:.4f}"})
    return report_path


def save_chart(metrics: dict[str, float]) -> Path:
    chart_path = REPORT_DIRECTORY / "recommendation_performance.png"
    values = {
        "Precision@3": metrics["precision_at_3"],
        "Precision@5": metrics["precision_at_5"],
        "Recall@5": metrics["recall_at_5"],
        "Skill match": metrics["skill_match_accuracy"],
        "Eligibility": metrics["eligibility_accuracy"],
        "Location match": metrics["location_match_accuracy"],
        "Diversity": metrics["recommendation_diversity"],
        "3+ eligible": metrics["candidates_with_3_eligible_recommendations"],
    }
    plt.figure(figsize=(11, 5.5))
    bars = plt.bar(values.keys(), values.values(), color="#2563eb")
    plt.ylim(0, 1.05)
    plt.ylabel("Score (0 to 1)")
    plt.title("Synthetic Evaluation: Internship Recommendation Engine")
    plt.xticks(rotation=28, ha="right")
    for bar, value in zip(bars, values.values()):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.02, f"{value:.2f}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(chart_path, dpi=160)
    plt.close()
    return chart_path


def evaluate(candidates: list[dict[str, str]], internships: list[dict[str, str]]) -> dict[str, float]:
    recommender = InternshipRecommender(internships, on_date=EVALUATION_DATE)
    precision_at_3: list[float] = []
    precision_at_5: list[float] = []
    recall_at_5: list[float] = []
    skill_match_results: list[float] = []
    eligibility_results: list[float] = []
    location_match_results: list[float] = []
    diversity_results: list[float] = []
    all_scores: list[float] = []
    candidates_with_three = 0
    labelled_candidates = 0

    for candidate in candidates:
        eligible_internships = recommender.eligible_internships(candidate)
        relevant_ids = {
            internship["internship_id"] for internship in eligible_internships if synthetic_ground_truth(candidate, internship)
        }
        recommendations = recommender.recommend(candidate, limit=5)
        if len(recommendations) >= 3:
            candidates_with_three += 1
        precision_at_3.append(precision(recommendations, relevant_ids, 3))
        precision_at_5.append(precision(recommendations, relevant_ids, 5))
        if relevant_ids:
            labelled_candidates += 1
            recall_at_5.append(sum(item["internship_id"] in relevant_ids for item in recommendations[:5]) / len(relevant_ids))
        original_by_id = {item["internship_id"]: item for item in internships}
        for recommendation in recommendations:
            internship = original_by_id[recommendation["internship_id"]]
            skill_match_results.append(float(bool(set(normalize_terms(candidate["skills"])) & set(normalize_terms(internship["required_skills"])))))
            eligibility_results.append(float(is_eligible(candidate, internship, on_date=EVALUATION_DATE)))
            location_match_results.append(float(location_is_match(candidate, internship)))
            all_scores.append(recommendation["final_score"])
        diversity_results.append(diversity(recommendations))

    return {
        "candidate_count": float(len(candidates)),
        "precision_at_3": mean(precision_at_3),
        "precision_at_5": mean(precision_at_5),
        "recall_at_5": mean(recall_at_5) if recall_at_5 else 0.0,
        "ground_truth_label_coverage": labelled_candidates / len(candidates) if candidates else 0.0,
        "skill_match_accuracy": mean(skill_match_results) if skill_match_results else 0.0,
        "eligibility_accuracy": mean(eligibility_results) if eligibility_results else 0.0,
        "location_match_accuracy": mean(location_match_results) if location_match_results else 0.0,
        "recommendation_diversity": mean(diversity_results),
        "average_recommendation_score": mean(all_scores) if all_scores else 0.0,
        "candidates_with_3_eligible_recommendations": candidates_with_three / len(candidates) if candidates else 0.0,
    }


def main() -> None:
    candidates = load_csv(ROOT / "data" / "candidates.csv")
    internships = load_csv(ROOT / "data" / "internships.csv")
    metrics = evaluate(candidates, internships)
    report_path = write_report(metrics)
    chart_path = save_chart(metrics)
    print("SIH prototype recommendation evaluation")
    for metric, value in metrics.items():
        if metric == "candidate_count":
            print(f"- {metric}: {int(value)}")
        else:
            print(f"- {metric}: {value:.2%}" if "score" not in metric else f"- {metric}: {value:.4f}")
    print(f"Saved CSV report: {report_path}")
    print(f"Saved chart: {chart_path}")
    print("Note: relevance labels are synthetic prototype labels; replace them with real clicks, saves, applications, and outcomes after deployment.")


if __name__ == "__main__":
    main()

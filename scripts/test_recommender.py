"""Print five recommendations for the first synthetic candidate."""

from __future__ import annotations

import csv
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.recommender import InternshipRecommender  # noqa: E402


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def main() -> None:
    candidates = load_csv(ROOT / "data" / "candidates.csv")
    internships = load_csv(ROOT / "data" / "internships.csv")
    candidate = candidates[0]
    recommendations = InternshipRecommender(internships, on_date=date(2026, 8, 16)).recommend(candidate, limit=5)
    print(f"Candidate: {candidate['candidate_id']} | {candidate['branch']} | skills: {candidate['skills']}")
    print(json.dumps(recommendations, indent=2))


if __name__ == "__main__":
    main()

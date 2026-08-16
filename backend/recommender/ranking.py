"""Ranking and a simple greedy diversity selector."""

from __future__ import annotations

from typing import Any

from .config import DIVERSITY_PENALTIES


def rank_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(items, key=lambda item: item["final_score"], reverse=True)


def diversify(ranked_items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    """Greedily reduce duplicate companies/sectors/states while retaining highest raw scores."""
    chosen: list[dict[str, Any]] = []
    remaining = list(ranked_items)
    while remaining and len(chosen) < limit:
        def diverse_value(item: dict[str, Any]) -> float:
            penalty = 0.0
            for selected in chosen:
                if item["company_name"] == selected["company_name"]:
                    penalty += DIVERSITY_PENALTIES["same_company"]
                if item["sector"] == selected["sector"]:
                    penalty += DIVERSITY_PENALTIES["same_sector"]
                if item["state"] == selected["state"]:
                    penalty += DIVERSITY_PENALTIES["same_state"]
            return item["final_score"] - penalty
        best = max(remaining, key=diverse_value)
        chosen.append(best)
        remaining.remove(best)
    return chosen

"""Input parsing and normalization helpers."""

from __future__ import annotations

import ast
import json
import re
from typing import Any

from .config import SYNONYMS


def parse_list(value: Any) -> list[str]:
    """Convert CSV JSON arrays, Python lists, or a comma-separated string to a list."""
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    text = str(value).strip()
    if not text:
        return []
    if text.startswith("["):
        try:
            decoded = json.loads(text)
        except json.JSONDecodeError:
            try:
                decoded = ast.literal_eval(text)
            except (ValueError, SyntaxError):
                decoded = []
        if isinstance(decoded, list):
            return [str(item) for item in decoded]
    return [item.strip() for item in text.split(",") if item.strip()]


def normalize_term(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[_/-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return SYNONYMS.get(text, text)


def normalize_terms(value: Any) -> list[str]:
    """Normalize and de-duplicate user-facing taxonomy values while preserving order."""
    result: list[str] = []
    for item in parse_list(value):
        normalized = normalize_term(item)
        if normalized and normalized not in result:
            result.append(normalized)
    return result


def normalized_text(*values: Any) -> str:
    """Build a clean TF-IDF document from scalar or list-like source values."""
    parts: list[str] = []
    for value in values:
        if isinstance(value, str) and not value.strip().startswith("["):
            parts.append(normalize_term(value))
        else:
            parts.extend(normalize_terms(value))
    return " ".join(parts)


def candidate_qualification(candidate: dict[str, Any]) -> str:
    level = normalize_term(candidate.get("education_level", ""))
    degree = normalize_term(candidate.get("degree", ""))
    if "post" in level or degree in {"m.tech", "mca", "mba", "m.sc."}:
        return "postgraduate"
    if "diploma" in level or degree == "diploma":
        return "diploma"
    return "graduate"

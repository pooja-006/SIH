"""TF-IDF/cosine similarity for lightweight semantic skill matching."""

from __future__ import annotations

from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .preprocessing import normalized_text


def candidate_document(candidate: dict[str, Any]) -> str:
    return normalized_text(candidate.get("skills"), candidate.get("interests"), candidate.get("preferred_sectors"))


def internship_document(internship: dict[str, Any]) -> str:
    return normalized_text(internship.get("job_title"), internship.get("description"), internship.get("required_skills"), internship.get("sector"))


def tfidf_scores(candidate: dict[str, Any], internships: list[dict[str, Any]]) -> list[float]:
    """Return a cosine score for each internship, with safe handling for empty text."""
    if not internships:
        return []
    documents = [candidate_document(candidate), *(internship_document(item) for item in internships)]
    if not any(document.strip() for document in documents):
        return [0.0] * len(internships)
    matrix = TfidfVectorizer(ngram_range=(1, 2)).fit_transform(documents)
    return cosine_similarity(matrix[0:1], matrix[1:]).flatten().tolist()


class SemanticMatcher:
    """Reusable TF-IDF index for fast scoring of many candidate profiles."""

    def __init__(self, internships: list[dict[str, Any]]) -> None:
        self.index_by_id = {item["internship_id"]: index for index, item in enumerate(internships)}
        documents = [internship_document(item) for item in internships]
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(documents) if documents else None

    def scores(self, candidate: dict[str, Any], internships: list[dict[str, Any]]) -> list[float]:
        if not internships or self.matrix is None:
            return [0.0] * len(internships)
        query = self.vectorizer.transform([candidate_document(candidate)])
        indexes = [self.index_by_id[item["internship_id"]] for item in internships]
        return cosine_similarity(query, self.matrix[indexes]).flatten().tolist()

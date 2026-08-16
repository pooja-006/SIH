"""Central configuration for recommendation scoring and diversity."""

WEIGHTS = {
    "skill": 0.35,
    "interest": 0.25,
    "education": 0.15,
    "location": 0.10,
    "duration": 0.05,
    "experience": 0.05,
    "stipend": 0.05,
}

SYNONYMS = {
    "js": "javascript", "reactjs": "react", "react js": "react",
    "ml": "machine learning", "ai": "artificial intelligence",
    "artificial intelligence and machine learning": "artificial intelligence",
    "datascience": "data science", "data analytics": "data analysis",
    "ms-excel": "ms excel", "excel": "ms excel", "powerbi": "power bi",
    "c sharp": "c#", "nodejs": "node.js", "e governance": "e-governance",
}

QUALIFICATION_RANK = {"school": 1, "diploma": 2, "graduate": 3, "postgraduate": 4}
DEFAULT_MINIMUM_STIPEND = 8_000
DIVERSITY_PENALTIES = {"same_company": 0.20, "same_sector": 0.08, "same_state": 0.03}

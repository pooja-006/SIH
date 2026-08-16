"""Environment-based settings for the prototype API."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Settings:
    """Small settings object; values may be supplied through environment variables."""

    app_name: str = "SIH Internship Recommendation API"
    app_version: str = "0.1.0"
    database_url: str = os.getenv("DATABASE_URL", f"sqlite:///{(ROOT / 'data' / 'sih_recommender.db').as_posix()}")
    internship_data_path: Path = ROOT / "data" / "internships.csv"
    cors_origins: str = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    @property
    def allowed_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

settings = Settings()

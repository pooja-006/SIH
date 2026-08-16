"""SQLite setup and synthetic internship catalogue seeding."""

from __future__ import annotations

import csv
import logging
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from .config import settings

logger = logging.getLogger(__name__)
Base = declarative_base()
engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def seed_internships(database: Session, csv_path: Path | None = None) -> None:
    """Load the project synthetic internship CSV only when the table is empty."""
    from .models import Internship

    if database.query(Internship).first() is not None:
        return
    source = csv_path or settings.internship_data_path
    if not source.exists():
        raise FileNotFoundError(f"Internship seed dataset was not found: {source}")
    with source.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))
    database.bulk_insert_mappings(Internship, rows)
    database.commit()
    logger.info("Seeded %d synthetic internships from %s", len(rows), source)


def initialize_database() -> None:
    from . import models  # noqa: F401 - register SQLAlchemy models before create_all

    Base.metadata.create_all(bind=engine)
    with SessionLocal() as database:
        seed_internships(database)

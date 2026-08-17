"""FastAPI entry point for the SIH internship recommendation backend."""

import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .config import settings
from .database import initialize_database
from .routes import candidates, health, internships, recommendations, auth

logging.basicConfig(level=settings.log_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Mobile-friendly, explainable internship recommendations using eligibility rules, TF-IDF, and weighted ranking.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    initialize_database()
    logger.info("%s started", settings.app_name)


@app.exception_handler(Exception)
async def unhandled_error_handler(_: Request, exc: Exception):
    logger.exception("Unhandled API error", exc_info=exc)
    return JSONResponse(status_code=500, content={"detail": "An unexpected server error occurred."})


app.include_router(candidates.router)
app.include_router(recommendations.router)
app.include_router(internships.router)
app.include_router(health.router)
app.include_router(auth.router)


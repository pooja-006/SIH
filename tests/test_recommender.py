from datetime import date
import unittest

from backend.recommender import InternshipRecommender
from backend.recommender.eligibility import filter_eligible
from backend.recommender.preprocessing import normalize_terms


ON_DATE = date(2026, 8, 16)
CANDIDATE = {
    "candidate_id": "TEST-001", "education_level": "Undergraduate", "degree": "B.Tech",
    "branch": "Computer Science", "skills": ["Python", "SQL", "ReactJS"],
    "interests": ["Data Science"], "preferred_sectors": ["Software Development", "Data Science"],
    "preferred_states": ["Karnataka"], "preferred_cities": ["Bengaluru"],
    "preferred_location_type": "Hybrid", "preferred_duration": 3,
    "experience_level": "No prior experience",
}
INTERNSHIPS = [
    {"internship_id": "GOOD-1", "job_title": "Data Analyst Intern", "company_name": "Synthetic Labs A", "sector": "Data Science", "description": "Python SQL data analysis project", "required_skills": ["Python", "SQL", "Data Analysis"], "eligible_branches": ["Computer Science"], "cities": "Bengaluru", "states": "Karnataka", "location_type": "Hybrid", "stipend": 12000, "duration_months": 3, "minimum_qualification": "Graduate", "experience_required": "No prior experience required", "last_date_to_apply": "2026-12-01"},
    {"internship_id": "GOOD-2", "job_title": "Software Intern", "company_name": "Synthetic Labs B", "sector": "Software Development", "description": "React JavaScript application development", "required_skills": ["JavaScript", "React"], "eligible_branches": ["Computer Science"], "cities": "Mysuru", "states": "Karnataka", "location_type": "On-site", "stipend": 10000, "duration_months": 3, "minimum_qualification": "Graduate", "experience_required": "No prior experience required", "last_date_to_apply": "2026-12-01"},
    {"internship_id": "EXPIRED", "job_title": "Expired Internship", "company_name": "Synthetic Labs C", "sector": "Data Science", "description": "Python", "required_skills": ["Python"], "eligible_branches": ["Computer Science"], "cities": "Bengaluru", "states": "Karnataka", "location_type": "Hybrid", "stipend": 15000, "duration_months": 3, "minimum_qualification": "Graduate", "experience_required": "No prior experience required", "last_date_to_apply": "2026-01-01"},
    {"internship_id": "WRONG-BRANCH", "job_title": "Civil Intern", "company_name": "Synthetic Labs D", "sector": "Infrastructure", "description": "AutoCAD site work", "required_skills": ["AutoCAD"], "eligible_branches": ["Civil Engineering"], "cities": "Bengaluru", "states": "Karnataka", "location_type": "On-site", "stipend": 12000, "duration_months": 3, "minimum_qualification": "Diploma", "experience_required": "No prior experience required", "last_date_to_apply": "2026-12-01"},
]


class RecommendationEngineTests(unittest.TestCase):
    def test_normalization_handles_synonyms(self):
        self.assertEqual(
            normalize_terms(["JS", "ReactJS", "ML", "AI"]),
            ["javascript", "react", "machine learning", "artificial intelligence"],
        )

    def test_eligibility_removes_expired_and_wrong_branch(self):
        eligible = filter_eligible(CANDIDATE, INTERNSHIPS, on_date=ON_DATE)
        self.assertEqual([item["internship_id"] for item in eligible], ["GOOD-1", "GOOD-2"])

    def test_recommendations_have_requested_fields_and_ranking(self):
        recommendations = InternshipRecommender(INTERNSHIPS, on_date=ON_DATE).recommend(CANDIDATE, limit=3)
        self.assertEqual(len(recommendations), 2)
        self.assertEqual(recommendations[0]["internship_id"], "GOOD-1")
        self.assertGreaterEqual(recommendations[0]["final_score"], recommendations[1]["final_score"])
        self.assertTrue({"internship_id", "match_percentage", "matched_skills", "recommendation_reasons"}.issubset(recommendations[0]))
        self.assertIn("python", recommendations[0]["matched_skills"])

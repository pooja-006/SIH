"""Create deterministic, anonymous synthetic candidate profiles for recommendation tests."""

from __future__ import annotations

import csv
import json
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[1] / "data" / "candidates.csv"
RECORD_COUNT = 1200

LOCATIONS = [
    ("Bengaluru", "Karnataka"), ("Mysuru", "Karnataka"), ("Hyderabad", "Telangana"),
    ("Warangal", "Telangana"), ("Pune", "Maharashtra"), ("Nagpur", "Maharashtra"),
    ("Mumbai", "Maharashtra"), ("Chennai", "Tamil Nadu"), ("Coimbatore", "Tamil Nadu"),
    ("Madurai", "Tamil Nadu"), ("New Delhi", "Delhi"), ("Noida", "Uttar Pradesh"),
    ("Lucknow", "Uttar Pradesh"), ("Varanasi", "Uttar Pradesh"), ("Jaipur", "Rajasthan"),
    ("Udaipur", "Rajasthan"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat"),
    ("Kolkata", "West Bengal"), ("Siliguri", "West Bengal"), ("Bhubaneswar", "Odisha"),
    ("Cuttack", "Odisha"), ("Patna", "Bihar"), ("Gaya", "Bihar"), ("Ranchi", "Jharkhand"),
    ("Jamshedpur", "Jharkhand"), ("Bhopal", "Madhya Pradesh"), ("Indore", "Madhya Pradesh"),
    ("Raipur", "Chhattisgarh"), ("Kochi", "Kerala"), ("Thiruvananthapuram", "Kerala"),
    ("Guwahati", "Assam"), ("Shillong", "Meghalaya"), ("Agartala", "Tripura"),
    ("Imphal", "Manipur"), ("Srinagar", "Jammu and Kashmir"), ("Dehradun", "Uttarakhand"),
    ("Shimla", "Himachal Pradesh"), ("Chandigarh", "Chandigarh"), ("Visakhapatnam", "Andhra Pradesh"),
    ("Vijayawada", "Andhra Pradesh"), ("Panaji", "Goa"),
]

PROFILES = [
    ("Undergraduate", "B.Tech", "Computer Science", ["Python", "SQL", "Data Analysis", "Git", "React", "Machine Learning"], ["Data Science", "Software Development", "AI/ML"], ["IT", "Software Development", "Data Science", "AI/ML"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Information Technology", ["Python", "JavaScript", "React", "SQL", "Networking", "Git"], ["Software Development", "Cybersecurity", "IT"], ["Software Development", "Cybersecurity", "IT"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Artificial Intelligence", ["Python", "Machine Learning", "Pandas", "Scikit-learn", "Data Analysis", "SQL"], ["AI/ML", "Data Science"], ["AI/ML", "Data Science", "Software Development"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Mechanical Engineering", ["AutoCAD", "SolidWorks", "Manufacturing", "Quality Control", "MS Excel", "Testing"], ["Manufacturing", "Automobile", "Infrastructure"], ["Manufacturing", "Automobile", "Infrastructure"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Automobile Engineering", ["Automobile Engineering", "Diagnostics", "AutoCAD", "Testing", "Electrical Safety"], ["Automobile", "Manufacturing", "Renewable Energy"], ["Automobile", "Manufacturing", "Renewable Energy"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Electronics and Communication", ["Embedded C", "Microcontrollers", "Networking", "PCB Design", "Troubleshooting", "Arduino"], ["Electronics", "Telecommunications", "IT"], ["Electronics", "Telecommunications", "IT"], ["English", "Hindi"]),
    ("Undergraduate", "B.Tech", "Electrical Engineering", ["Electrical Safety", "Solar Energy", "AutoCAD", "MS Excel", "Testing", "Microcontrollers"], ["Renewable Energy", "Electronics", "Infrastructure"], ["Renewable Energy", "Electronics", "Infrastructure"], ["English", "Hindi"]),
    ("Undergraduate", "B.Com", "Commerce", ["MS Excel", "Accounting", "Tally", "Financial Analysis", "Communication", "Documentation"], ["Finance", "Accounting", "Banking"], ["Finance", "Banking", "Marketing"], ["English", "Hindi"]),
    ("Undergraduate", "BBA", "Business Administration", ["MS Excel", "Communication", "Financial Analysis", "Digital Marketing", "Project Management", "Documentation"], ["Finance", "Marketing", "HR"], ["Finance", "Marketing", "HR", "Logistics"], ["English", "Hindi"]),
    ("Undergraduate", "B.Sc.", "Agriculture", ["Agriculture", "Field Survey", "Data Collection", "MS Excel", "Community Engagement", "Communication"], ["Agriculture Technology", "Rural Development", "Sustainability"], ["Agriculture", "Rural Development", "Renewable Energy"], ["English", "Hindi"]),
    ("Undergraduate", "B.Sc.", "Data Science", ["Python", "SQL", "Data Analysis", "Power BI", "Pandas", "MS Excel"], ["Data Science", "Business Intelligence", "AI/ML"], ["Data Science", "AI/ML", "IT"], ["English", "Hindi"]),
    ("Undergraduate", "BCA", "Computer Applications", ["Python", "JavaScript", "SQL", "React", "MS Excel", "Git"], ["Software Development", "IT", "Data Science"], ["Software Development", "IT", "Data Science"], ["English", "Hindi"]),
    ("Diploma", "Diploma", "Civil Engineering", ["AutoCAD", "Site Survey", "MS Excel", "Documentation", "Project Management", "Testing"], ["Infrastructure", "Construction", "Urban Development"], ["Infrastructure", "Manufacturing", "Renewable Energy"], ["Hindi", "English"]),
    ("Diploma", "Diploma", "Electrical Engineering", ["Electrical Safety", "Solar Energy", "Testing", "Troubleshooting", "MS Excel", "AutoCAD"], ["Renewable Energy", "Electronics", "Infrastructure"], ["Renewable Energy", "Electronics", "Telecommunications"], ["Hindi", "English"]),
    ("Undergraduate", "BA", "Public Administration", ["MS Excel", "Documentation", "Communication", "Research", "Data Entry", "Digital Literacy"], ["Government", "E-Governance", "Rural Development"], ["Government", "E-Governance", "Rural Development"], ["Hindi", "English"]),
    ("Undergraduate", "BA", "Social Work", ["Field Survey", "Community Engagement", "Communication", "Data Collection", "Documentation", "MS Excel"], ["Rural Development", "Education", "Healthcare"], ["Rural Development", "Education", "Healthcare", "Government"], ["Hindi", "English"]),
    ("Undergraduate", "B.Sc.", "Nursing", ["Patient Support", "Documentation", "Communication", "MS Excel", "Data Entry", "Teamwork"], ["Healthcare", "Public Health"], ["Healthcare", "Government", "Education"], ["English", "Hindi"]),
    ("Undergraduate", "BA", "Tourism", ["Customer Service", "Communication", "Tourism Operations", "Content Writing", "MS Excel", "Documentation"], ["Tourism", "Hospitality", "Marketing"], ["Tourism", "Marketing", "Logistics"], ["English", "Hindi"]),
]

REGIONAL_LANGUAGES = {
    "Karnataka": "Kannada", "Telangana": "Telugu", "Maharashtra": "Marathi", "Tamil Nadu": "Tamil",
    "Delhi": "Hindi", "Uttar Pradesh": "Hindi", "Rajasthan": "Hindi", "Gujarat": "Gujarati",
    "West Bengal": "Bengali", "Odisha": "Odia", "Bihar": "Hindi", "Jharkhand": "Hindi",
    "Madhya Pradesh": "Hindi", "Chhattisgarh": "Hindi", "Kerala": "Malayalam", "Assam": "Assamese",
    "Meghalaya": "English", "Tripura": "Bengali", "Manipur": "Manipuri", "Jammu and Kashmir": "Urdu",
    "Uttarakhand": "Hindi", "Himachal Pradesh": "Hindi", "Chandigarh": "Punjabi", "Andhra Pradesh": "Telugu", "Goa": "Konkani",
}
HEADERS = ["candidate_id", "education_level", "degree", "branch", "graduation_year", "cgpa", "skills", "interests", "preferred_sectors", "preferred_states", "preferred_cities", "preferred_location_type", "preferred_duration", "experience_level", "languages", "disability_preference", "rural_or_urban"]


def make_record(index: int) -> dict[str, object]:
    education, degree, branch, profile_skills, interests, sectors, profile_languages = PROFILES[index % len(PROFILES)]
    city, state = LOCATIONS[(index * 11 + index // len(PROFILES)) % len(LOCATIONS)]
    skill_tier = index % 10
    # Skill counts intentionally form weak, medium, and strong candidate profiles.
    skills = profile_skills[:2] if skill_tier < 3 else (profile_skills[:4] if skill_tier < 7 else profile_skills)
    if education == "Diploma":
        graduation_year = 2025 + (index % 4)
        cgpa = 5.5 + ((index * 11) % 38) / 10
    else:
        graduation_year = 2026 + (index % 3)
        cgpa = 5.8 + ((index * 13) % 39) / 10
    location_type = ["On-site", "Hybrid", "Remote", "On-site", "Hybrid"][index % 5]
    experience = "No prior experience" if index % 3 else "Academic project experience"
    if index % 11 == 0:
        experience = "0-1 internship experience"
    disability = "No preference" if index % 12 else "Accessible workplace preferred"
    languages = list(dict.fromkeys([*profile_languages, REGIONAL_LANGUAGES[state]]))
    nearby_city, nearby_state = LOCATIONS[(index * 11 + 5) % len(LOCATIONS)]
    preferred_states = [state] if index % 4 else [state, nearby_state]
    preferred_cities = [city] if index % 4 else [city, nearby_city]
    return {
        "candidate_id": f"CAND2026-{index + 1:05d}", "education_level": education,
        "degree": degree, "branch": branch, "graduation_year": graduation_year,
        "cgpa": f"{cgpa:.1f}", "skills": json.dumps(skills), "interests": json.dumps(interests),
        "preferred_sectors": json.dumps(sectors), "preferred_states": json.dumps(preferred_states),
        "preferred_cities": json.dumps(preferred_cities), "preferred_location_type": location_type,
        "preferred_duration": [2, 3, 3, 4, 6][index % 5], "experience_level": experience,
        "languages": json.dumps(languages), "disability_preference": disability,
        "rural_or_urban": "Rural" if index % 5 in (0, 1) else "Urban",
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(make_record(index) for index in range(RECORD_COUNT))
    print(f"Created {RECORD_COUNT} anonymous synthetic candidate profiles at {OUTPUT}")


if __name__ == "__main__":
    main()

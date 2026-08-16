"""Create a deterministic, fully synthetic internship catalogue for the SIH prototype."""

from __future__ import annotations

import csv
import json
from datetime import date, timedelta
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[1] / "data" / "internships.csv"
RECORD_COUNT = 600

LOCATIONS = [
    ("Bengaluru", "Karnataka"), ("Mysuru", "Karnataka"), ("Hyderabad", "Telangana"),
    ("Warangal", "Telangana"), ("Pune", "Maharashtra"), ("Mumbai", "Maharashtra"),
    ("Nagpur", "Maharashtra"), ("Chennai", "Tamil Nadu"), ("Coimbatore", "Tamil Nadu"),
    ("Madurai", "Tamil Nadu"), ("New Delhi", "Delhi"), ("Noida", "Uttar Pradesh"),
    ("Lucknow", "Uttar Pradesh"), ("Varanasi", "Uttar Pradesh"), ("Jaipur", "Rajasthan"),
    ("Udaipur", "Rajasthan"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat"),
    ("Gandhinagar", "Gujarat"), ("Kolkata", "West Bengal"), ("Siliguri", "West Bengal"),
    ("Bhubaneswar", "Odisha"), ("Cuttack", "Odisha"), ("Patna", "Bihar"),
    ("Gaya", "Bihar"), ("Ranchi", "Jharkhand"), ("Jamshedpur", "Jharkhand"),
    ("Bhopal", "Madhya Pradesh"), ("Indore", "Madhya Pradesh"), ("Raipur", "Chhattisgarh"),
    ("Bilaspur", "Chhattisgarh"), ("Kochi", "Kerala"), ("Thiruvananthapuram", "Kerala"),
    ("Guwahati", "Assam"), ("Shillong", "Meghalaya"), ("Agartala", "Tripura"),
    ("Imphal", "Manipur"), ("Srinagar", "Jammu and Kashmir"), ("Jammu", "Jammu and Kashmir"),
    ("Dehradun", "Uttarakhand"), ("Shimla", "Himachal Pradesh"), ("Chandigarh", "Chandigarh"),
    ("Visakhapatnam", "Andhra Pradesh"), ("Vijayawada", "Andhra Pradesh"),
    ("Panaji", "Goa"), ("Port Blair", "Andaman and Nicobar Islands"),
]

PROFILES = [
    ("IT", "IT Support Intern", ["IT Support", "Systems Administration"], ["Linux", "Networking", "Troubleshooting", "MS Excel"], "BCA / B.Sc. IT / B.Tech", ["Computer Science", "Information Technology", "Electronics"], "Graduate", "technical"),
    ("Software Development", "Software Development Intern", ["Frontend Development", "Backend Development", "Full Stack Development"], ["Python", "JavaScript", "React", "SQL", "Git"], "B.Tech / BCA / MCA", ["Computer Science", "Information Technology", "Software Engineering"], "Graduate", "technical"),
    ("Data Science", "Data Analytics Intern", ["Data Analyst", "Business Intelligence Intern"], ["Python", "SQL", "MS Excel", "Data Analysis", "Power BI"], "B.Sc. / BCA / B.Tech / MBA", ["Data Science", "Computer Science", "Statistics", "Mathematics", "Commerce"], "Graduate", "technical"),
    ("AI/ML", "Machine Learning Intern", ["AI Research Intern", "Computer Vision Intern"], ["Python", "Machine Learning", "Data Analysis", "Pandas", "Scikit-learn"], "B.Tech / M.Tech / M.Sc.", ["Computer Science", "Data Science", "Artificial Intelligence", "Electronics"], "Graduate", "technical"),
    ("Cybersecurity", "Cybersecurity Intern", ["Information Security Intern", "SOC Analyst Intern"], ["Cybersecurity", "Networking", "Linux", "Python", "OWASP"], "B.Tech / BCA / B.Sc. IT", ["Computer Science", "Information Technology", "Cybersecurity", "Electronics"], "Graduate", "technical"),
    ("Electronics", "Electronics Design Intern", ["Embedded Systems Intern", "PCB Design Intern"], ["Embedded C", "Microcontrollers", "PCB Design", "Arduino", "Testing"], "Diploma / B.Tech", ["Electronics", "Electrical Engineering", "Instrumentation"], "Diploma", "technical"),
    ("Manufacturing", "Manufacturing Operations Intern", ["Production Planning Intern", "Quality Assurance Intern"], ["MS Excel", "Quality Control", "Lean Manufacturing", "Documentation", "AutoCAD"], "Diploma / B.Tech / BBA", ["Mechanical Engineering", "Industrial Engineering", "Production Engineering", "Business Administration"], "Diploma", "technical"),
    ("Automobile", "Automobile Service Intern", ["EV Systems Intern", "Automotive Testing Intern"], ["Automobile Engineering", "Diagnostics", "Testing", "MS Excel", "AutoCAD"], "Diploma / B.Tech", ["Automobile Engineering", "Mechanical Engineering", "Electrical Engineering"], "Diploma", "technical"),
    ("Finance", "Finance Operations Intern", ["Financial Analysis Intern", "Accounts Intern"], ["MS Excel", "Financial Analysis", "Accounting", "Tally", "Communication"], "B.Com / BBA / MBA", ["Commerce", "Finance", "Business Administration", "Economics"], "Graduate", "non-technical"),
    ("Banking", "Banking Services Intern", ["Credit Operations Intern", "Branch Operations Intern"], ["MS Excel", "Customer Service", "KYC", "Communication", "Documentation"], "B.Com / BBA / BA", ["Commerce", "Finance", "Business Administration", "Economics"], "Graduate", "non-technical"),
    ("Healthcare", "Healthcare Operations Intern", ["Public Health Intern", "Hospital Administration Intern"], ["Communication", "MS Excel", "Documentation", "Data Entry", "Patient Support"], "B.Sc. / BPH / BBA", ["Healthcare Management", "Public Health", "Nursing", "Life Sciences", "Business Administration"], "Graduate", "non-technical"),
    ("Agriculture", "Agriculture Extension Intern", ["Agri Supply Chain Intern", "Farm Data Intern"], ["Agriculture", "Field Survey", "MS Excel", "Communication", "Data Collection"], "Diploma / B.Sc. / B.Tech", ["Agriculture", "Horticulture", "Food Technology", "Rural Development"], "Diploma", "non-technical"),
    ("Renewable Energy", "Renewable Energy Intern", ["Solar Project Intern", "Energy Audit Intern"], ["Solar Energy", "MS Excel", "AutoCAD", "Data Analysis", "Electrical Safety"], "Diploma / B.Tech", ["Electrical Engineering", "Mechanical Engineering", "Renewable Energy", "Civil Engineering"], "Diploma", "technical"),
    ("Education", "Education Programme Intern", ["Curriculum Support Intern", "Student Outreach Intern"], ["Communication", "Content Writing", "MS Excel", "Teaching", "Data Collection"], "BA / B.Sc. / B.Ed. / BBA", ["Education", "Arts", "Science", "Social Work", "Business Administration"], "Graduate", "non-technical"),
    ("Government", "Public Administration Intern", ["Policy Research Intern", "Citizen Services Intern"], ["MS Excel", "Communication", "Documentation", "Research", "Data Entry"], "Graduate / Postgraduate", ["Public Administration", "Political Science", "Economics", "Social Work", "Law"], "Graduate", "non-technical"),
    ("E-Governance", "E-Governance Support Intern", ["Digital Services Intern", "MIS Intern"], ["MS Excel", "Data Entry", "Documentation", "Communication", "Digital Literacy"], "Diploma / Graduate", ["Computer Science", "Information Technology", "Public Administration", "Business Administration"], "Diploma", "non-technical"),
    ("Tourism", "Tourism Operations Intern", ["Travel Desk Intern", "Heritage Tourism Intern"], ["Customer Service", "Communication", "MS Excel", "Tourism Operations", "Content Writing"], "Diploma / Graduate", ["Tourism", "Hospitality", "Business Administration", "Arts"], "Diploma", "non-technical"),
    ("Logistics", "Logistics Coordinator Intern", ["Supply Chain Intern", "Warehouse Operations Intern"], ["MS Excel", "Inventory Management", "Communication", "Data Analysis", "Documentation"], "Diploma / BBA / B.Tech", ["Logistics", "Supply Chain Management", "Business Administration", "Industrial Engineering"], "Diploma", "non-technical"),
    ("Marketing", "Digital Marketing Intern", ["Market Research Intern", "Social Media Intern"], ["Digital Marketing", "Content Writing", "Communication", "MS Excel", "Social Media Marketing"], "Graduate / Diploma", ["Marketing", "Business Administration", "Commerce", "Arts", "Mass Communication"], "Diploma", "non-technical"),
    ("HR", "Human Resources Intern", ["Talent Acquisition Intern", "HR Operations Intern"], ["Communication", "MS Excel", "Recruitment", "Documentation", "Teamwork"], "BBA / BA / MBA", ["Human Resources", "Business Administration", "Psychology", "Arts", "Commerce"], "Graduate", "non-technical"),
    ("Rural Development", "Rural Development Intern", ["Community Outreach Intern", "Livelihoods Intern"], ["Field Survey", "Communication", "Data Collection", "MS Excel", "Community Engagement"], "Diploma / Graduate", ["Rural Development", "Social Work", "Agriculture", "Economics", "Public Administration"], "Diploma", "non-technical"),
    ("Infrastructure", "Infrastructure Planning Intern", ["Site Coordination Intern", "Urban Planning Intern"], ["AutoCAD", "MS Excel", "Documentation", "Site Survey", "Project Management"], "Diploma / B.Tech", ["Civil Engineering", "Architecture", "Urban Planning", "Mechanical Engineering"], "Diploma", "technical"),
    ("Telecommunications", "Telecom Network Intern", ["Field Network Intern", "Network Operations Intern"], ["Networking", "Telecommunications", "Fiber Optics", "Troubleshooting", "MS Excel"], "Diploma / B.Tech", ["Electronics", "Telecommunications", "Electrical Engineering", "Information Technology"], "Diploma", "technical"),
]

COMPANY_PREFIXES = ["Pragati", "Navbharat", "Sampurna", "Udaan", "Saksham", "Nayi Disha", "JanMitra", "Aarambh", "Vikas", "BharatSetu"]
COMPANY_SUFFIXES = ["Solutions", "Industries", "Services", "Technologies", "Initiatives", "Enterprises", "Networks", "Projects"]
HEADERS = ["internship_id", "job_title", "job_type", "company_name", "sector", "description", "required_skills", "preferred_education", "eligible_branches", "cities", "states", "location_type", "stipend", "start_date", "duration_months", "number_of_openings", "last_date_to_apply", "work_mode", "minimum_qualification", "experience_required"]


def make_record(index: int) -> dict[str, object]:
    sector, base_title, alternate_titles, skills, education, branches, minimum, category = PROFILES[index % len(PROFILES)]
    city, state = LOCATIONS[(index * 7 + index // len(PROFILES)) % len(LOCATIONS)]
    title = base_title if index % 3 else alternate_titles[index % len(alternate_titles)]
    location_type = "Remote" if index % 17 == 0 else ("Hybrid" if index % 5 == 0 else "On-site")
    work_mode = {"Remote": "Remote", "Hybrid": "Hybrid", "On-site": "In-office"}[location_type]
    start = date(2026, 10, 1) + timedelta(days=(index % 120) * 3)
    application_deadline = start - timedelta(days=21 + (index % 25))
    duration = [2, 3, 3, 4, 6][index % 5]
    selected_skills = skills[:3] if index % 4 else skills[:4]
    stipend = 6000 + ((index * 750) % 18000)
    if category == "technical":
        stipend += 2000
    company = f"{COMPANY_PREFIXES[index % len(COMPANY_PREFIXES)]} {COMPANY_SUFFIXES[(index * 3) % len(COMPANY_SUFFIXES)]} {city}"
    description = (
        f"Synthetic {duration}-month {title.lower()} opportunity supporting {sector.lower()} projects. "
        f"The intern will assist the team with supervised assignments, documentation, and practical project work in {city}."
    )
    return {
        "internship_id": f"SIH2026-{index + 1:04d}", "job_title": title,
        "job_type": "Internship", "company_name": company, "sector": sector,
        "description": description, "required_skills": json.dumps(selected_skills),
        "preferred_education": education, "eligible_branches": json.dumps(branches),
        "cities": city, "states": state, "location_type": location_type,
        "stipend": stipend, "start_date": start.isoformat(), "duration_months": duration,
        "number_of_openings": 2 + (index % 24), "last_date_to_apply": application_deadline.isoformat(),
        "work_mode": work_mode, "minimum_qualification": minimum,
        "experience_required": "No prior experience required" if index % 8 else "0-1 years preferred",
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(make_record(index) for index in range(RECORD_COUNT))
    print(f"Created {RECORD_COUNT} synthetic internship records at {OUTPUT}")


if __name__ == "__main__":
    main()

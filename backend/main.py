from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import os
from dotenv import load_dotenv
import re
from typing import List
import PyPDF2
import json

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🔥 JSON STORAGE FUNCTIONS
def load_candidates():
    try:
        with open("candidates.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_candidates(data):
    with open("candidates.json", "w") as f:
        json.dump(data, f, indent=4)

# Load existing candidates
candidates = load_candidates()

# Default candidates if file empty
if not candidates:
    candidates = [
        {"name": "Rahul", "skills": ["Python", "ML", "React"]},
        {"name": "Anita", "skills": ["Java", "Spring", "SQL"]},
        {"name": "Karan", "skills": ["Python", "AI", "Data Science"]},
        {"name": "Sneha", "skills": ["React", "Node", "MongoDB"]},
    ]
    save_candidates(candidates)

# Models
class InputData(BaseModel):
    jd: str

class Candidate(BaseModel):
    name: str
    skills: List[str]

# 🚀 ANALYZE
@app.post("/analyze")
def analyze(data: InputData):
    results = []

    for c in candidates:
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{
                    "role": "user",
                    "content": f"""
Rate how well this candidate matches the job (0 to 100).

Job:
{data.jd}

Candidate skills:
{c['skills']}

Also say interest: High, Medium or Low.

Example:
Score: 80
Interest: High
"""
                }],
            )

            text = response.choices[0].message.content

            score_match = re.search(r"\d+", text)
            score = int(score_match.group()) if score_match else 50

            if "High" in text:
                interest = "High"
            elif "Medium" in text:
                interest = "Medium"
            else:
                interest = "Low"

            matched_skills = [
                skill for skill in c["skills"]
                if skill.lower() in data.jd.lower()
            ]

            reason = (
                f"Matched skills: {', '.join(matched_skills)}"
                if matched_skills
                else "No strong skill match found"
            )

            results.append({
                "candidate": c["name"],
                "match_score": score,
                "interest_level": interest,
                "reason": reason
            })

        except Exception as e:
            print("ERROR:", e)

            results.append({
                "candidate": c["name"],
                "match_score": 50,
                "interest_level": "Unknown",
                "reason": "Error analyzing candidate"
            })

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return {"results": results}


# 🚀 ADD CANDIDATE
@app.post("/add_candidate")
def add_candidate(candidate: Candidate):
    candidates.append({
        "name": candidate.name,
        "skills": candidate.skills
    })

    save_candidates(candidates)

    return {"message": "Candidate added & saved successfully"}


# 🚀 UPLOAD RESUME
@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    reader = PyPDF2.PdfReader(file.file)

    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    skills_list = [
        "Python", "Java", "React", "SQL",
        "ML", "AI", "Node", "MongoDB",
        "Django", "Spring", "Kubernetes", "Docker"
    ]

    found_skills = [
        skill for skill in skills_list
        if skill.lower() in text.lower()
    ]

    new_candidate = {
        "name": file.filename.split(".")[0],
        "skills": found_skills if found_skills else ["General"]
    }

    candidates.append(new_candidate)
    save_candidates(candidates)

    return {
        "message": "Resume processed & saved",
        "candidate": new_candidate
    }
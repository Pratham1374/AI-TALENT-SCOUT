from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import os
from dotenv import load_dotenv
import re

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

candidates = [
    {"name": "Rahul", "skills": ["Python", "ML", "React"]},
    {"name": "Anita", "skills": ["Java", "Spring", "SQL"]},
    {"name": "Karan", "skills": ["Python", "AI", "Data Science"]},
    {"name": "Sneha", "skills": ["React", "Node", "MongoDB"]},
]

class InputData(BaseModel):
    jd: str

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

Example output:
Score: 80
Interest: High
"""
                }],
            )

            text = response.choices[0].message.content

            # 🔥 Extract score
            score_match = re.search(r"\d+", text)
            score = int(score_match.group()) if score_match else 50

            # 🔥 Extract interest
            if "High" in text:
                interest = "High"
            elif "Medium" in text:
                interest = "Medium"
            else:
                interest = "Low"

            # 🔥 NEW: MATCHED SKILLS LOGIC
            matched_skills = [
                skill for skill in c["skills"]
                if skill.lower() in data.jd.lower()
            ]

            reason = (
                f"Matched skills: {', '.join(matched_skills)}"
                if matched_skills
                else "No strong skill match found"
            )

            # 🔥 FINAL RESULT
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

    # 🔥 Sort by score
    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return {"results": results}
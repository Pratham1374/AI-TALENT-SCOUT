🚀 AI-Powered Talent Scout & Engagement Agent

An intelligent AI system that helps recruiters quickly identify, rank, and understand candidates based on a given Job Description.

🧠 Problem Statement

Recruiters spend hours:

Scanning resumes
Matching skills manually
Assessing candidate relevance

This project solves that by building an AI-powered agent that:

Analyzes Job Descriptions
Matches candidates
Scores them
Explains why they are selected
⚙️ Features

✅ Job Description Parsing
Extracts required skills from input JD

✅ AI-Based Candidate Matching
Uses LLM (Groq - LLaMA 3) to evaluate candidate relevance

✅ Match Score (0–100)
Ranks candidates based on skill alignment

✅ Interest Level Detection
Classifies candidate as High / Medium / Low

✅ Explainability (🔥 Key Feature)
Shows why a candidate is selected
→ Based on matched skills

✅ Ranking System
Automatically sorts best candidates first

🖥️ Tech Stack
🔹 Frontend
React.js
CSS (custom UI)
🔹 Backend
FastAPI (Python)
🔹 AI Model
Groq API
LLaMA 3 (llama-3.1-8b-instant)
🏗️ Project Structure
AI-Talent-Scout/
│
├── backend/
│   ├── main.py
│   ├── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│
└── README.md
🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/AI-Talent-Scout.git
cd AI-Talent-Scout
2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

Create .env file:

GROQ_API_KEY=your_api_key_here

Run backend:

uvicorn main:app --reload
3️⃣ Frontend Setup
cd ../frontend
npm install
npm start
🧪 Sample Input
Looking for Python developer with AI and ML experience
📊 Sample Output
1. Karan — Score: 85 — High  
   Why: Matched skills: Python, AI  

2. Rahul — Score: 75 — High  
   Why: Matched skills: Python, ML  

3. Anita — Score: 20 — Low  
   Why: No strong skill match  
🎯 Use Case
Recruitment platforms
HR automation tools
Resume screening systems
Talent acquisition dashboards
🔥 What Makes This Special
Combines AI + Explainability
Real-time scoring
Clean UI for recruiters
Fully functional end-to-end system
🚀 Future Enhancements
Resume upload & parsing
Candidate database integration
Conversational AI recruiter bot
Email outreach automation
Skill similarity using embeddings
👨‍💻 Author

Pratham P
📧 prathamacharya804@gmail.com

🏆 Hackathon Ready

This project is designed to:

Demonstrate real-world AI application
Provide clear business value
Deliver a working prototype
🎥 Demo

(Add your demo video link here)

⭐ Final Note

This project showcases how AI can transform recruitment workflows by making them:

Faster ⚡
Smarter 🧠
More transparent 🔍

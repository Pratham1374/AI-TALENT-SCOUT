# 🚀 AI-Powered Talent Scout & Engagement Agent

An intelligent AI system that helps recruiters quickly identify, rank, and understand candidates based on a given Job Description.

---

## 🧠 Problem Statement

Recruiters spend hours scanning resumes, matching skills manually, and assessing candidate relevance. This project solves that by building an AI-powered agent that parses Job Descriptions, matches candidates intelligently, scores them based on relevance, and explains why they are selected.

---

## ⚙️ Features

- Job Description Analysis  
- AI-Based Candidate Matching (Groq - LLaMA 3)  
- Match Score (0–100)  
- Interest Level Detection (High / Medium / Low)  
- Explainability (Matched Skills Reasoning) 🔥  
- Ranked Candidate Output  
- Clean and Interactive UI  

---

## 🖥️ Tech Stack

Frontend:
- React.js  
- Custom CSS  

Backend:
- FastAPI (Python)  

AI Model:
- Groq API  
- LLaMA 3 (llama-3.1-8b-instant)  

---

## 🏗️ Project Structure

AI-Talent-Scout/
│
├── backend/
│   ├── main.py
│   ├── .env
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│
└── README.md

---

## 🚀 How to Run Locally

1. Clone the repository

git clone https://github.com/your-username/AI-Talent-Scout.git  
cd AI-Talent-Scout  

---

2. Backend Setup

cd backend  
python -m venv venv  
venv\Scripts\activate   (Windows)  
pip install -r requirements.txt  

Create a `.env` file:

GROQ_API_KEY=your_api_key_here  

Run backend:

uvicorn main:app --reload  

---

3. Frontend Setup

cd ../frontend  
npm install  
npm start  

---

## 🧪 Sample Input

Looking for Python developer with AI and ML experience

---

## 📊 Sample Output

1. Karan — Score: 85 — High  
   Why: Matched skills: Python, AI  

2. Rahul — Score: 75 — High  
   Why: Matched skills: Python, ML  

3. Anita — Score: 20 — Low  
   Why: No strong skill match  

---

## 🎯 Use Cases

- Recruitment platforms  
- HR automation tools  
- Resume screening systems  
- Talent acquisition dashboards  

---

## 🔥 What Makes This Unique

- Combines AI + Explainability  
- Real-time scoring system  
- Recruiter-friendly UI  
- Fully working end-to-end system  

---

## 🚀 Future Enhancements

- Resume upload & parsing  
- Candidate database integration  
- Conversational AI recruiter chatbot  
- Email outreach automation  
- Skill similarity using embeddings  

---

## 👨‍💻 Author

Pratham P  
Email: prathamacharya804@gmail.com  

---

## 🎥 Demo

(Add your demo video link here)

---

## 🏆 Hackathon Ready

This project demonstrates a real-world AI application with clear business value and a fully functional prototype.

---

## ⭐ Final Note

This project showcases how AI can transform recruitment workflows by making them faster, smarter, and more transparent.

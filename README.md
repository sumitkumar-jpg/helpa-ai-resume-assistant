# 🤖 Helpa – AI Resume Assistant

Helpa is a full-stack AI-powered resume assistant that allows recruiters, hiring managers, and interviewers to interact with my resume through natural language.

Instead of reading a traditional resume, users can ask questions about my skills, education, projects, and experience. They can also upload a job description, and Helpa will compare it with my resume using an LLM.

---

## Features

-  AI-powered resume chatbot
-  Upload Job Descriptions (PDF, DOCX, TXT)
-  Resume vs Job Description comparison
-  Multi-turn conversations
-  Session-based conversation memory
-  Independent chatbot for every user session
-  FastAPI backend
-  HTML, CSS & JavaScript frontend
-  Real-time frontend-backend communication

---

## Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI
- Pydantic

### AI

- Groq API
- Llama 3.3 70B

### Document Processing

- PyPDF
- python-docx

----------------------------------

## Project Structure

```text
helpa-ai-resume-assistant/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── screenshots/
│
├── Bot.py
├── main.py
├── Sumitstuff.txt
├── pyproject.toml
├── uv.lock
├── README.md
├── .env.example
└── .gitignore
```

-----------------------------------

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to the project directory

```bash
cd helpa-ai-resume-assistant
```

Create a `.env` file

```text
GROQ_API_KEY=your_groq_api_key
```

Install dependencies

```bash
uv sync
```

Run the backend

```bash
python -m uvicorn main:app --reload
```

Open `frontend/index.html` using Live Server.

------------------

## How It Works

1. The user opens the web interface.
2. The user uploads a job description (optional).
3. The user asks questions about my resume.
4. FastAPI sends the request to the Groq LLM.
5. Helpa responds using my resume and the uploaded document when relevant.
6. Each browser session gets an independent chatbot with isolated conversation memory.

----------------------

## 🔮 Future Improvements

- Conversation history
- Streaming AI responses
- Authentication
- Docker deployment
- Cloud database
- Better UI/UX

-------------------------

##  Author

**Sumit Kumar**

Computer Science (AI & ML) Student
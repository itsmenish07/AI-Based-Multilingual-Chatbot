# 🏛️ Bharat Welfare Assistant

## AI-Based Multilingual Welfare Scheme Discovery Platform

Bharat Welfare Assistant is an AI-powered multilingual chatbot designed to help citizens discover government welfare schemes they are eligible for. The platform provides personalized recommendations, document guidance, application steps, and AI-powered assistance in multiple Indian languages.

---

# 📌 Project Objective

Many citizens are unaware of government welfare schemes available to them. Information is often fragmented, difficult to understand, and unavailable in local languages.

This project aims to:

- Increase awareness of welfare schemes
- Improve accessibility through multilingual support
- Provide personalized scheme recommendations
- Simplify eligibility checking
- Assist users through AI-powered conversations

---

# 🚀 Key Features

## 1. Eligibility Checker

Users enter:

- Age
- Gender
- Occupation
- Income
- State
- Category
- Area (Urban/Rural)

The system recommends suitable government schemes.

---

## 2. AI Welfare Assistant

Users can ask questions such as:

- What documents are required for PM Kisan?
- How can I apply for Ayushman Bharat?
- Who is eligible for Ujjwala Yojana?

The AI provides contextual answers using a RAG-based pipeline.

---

## 3. Multilingual Support

Supported Languages:

- English
- Hindi
- Tamil

This makes welfare information accessible to a wider population.

---

## 4. RAG-Based Knowledge Retrieval

Uses:

- FAISS Vector Database
- Sentence Transformers
- Gemini AI

This ensures responses are generated using verified scheme information.

---

## 5. Scheme Information

Each scheme includes:

- Benefits
- Description
- Eligibility
- Required Documents
- Application Process

---

## 6. Match Score System

Users receive a match percentage for recommended schemes based on their profile.

---

# 🏗️ System Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
Eligibility Engine
↓
Scheme Database
↓
FAISS Retriever
↓
Gemini AI
↓
Multilingual Response

---

# 🛠️ Technology Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## AI Model

- Gemini 2.5 Flash

## Vector Database

- FAISS

## Embeddings

- Sentence Transformers

## Programming Language

- Python

---

# 📂 Project Structure

```text
bharat-welfare-assistant/

├── backend/
│   ├── main.py
│   ├── chatbot.py
│   ├── eligibility.py
│   ├── translator.py
│   │
│   └── rag/
│       ├── embed.py
│       ├── retriever.py
│       ├── scheme_index.faiss
│       └── chunks.pkl
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── schemes.json
│   └── knowledge_base.txt
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone <repository_url>
cd bharat-welfare-assistant
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Step 5: Build Vector Database

Navigate to:

```bash
cd backend/rag
```

Run:

```bash
python embed.py
```

This creates:

```text
scheme_index.faiss
chunks.pkl
```

---

## Step 6: Run Backend

Navigate to:

```bash
cd backend
```

Run:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Step 7: Run Frontend

Navigate to:

```bash
cd frontend
```

Run:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 🎯 Expected Deliverables

## 1. Functional Chatbot Prototype

Status: ✅ Completed

Features:

- Eligibility Checker
- AI Welfare Assistant
- Multilingual Support
- Scheme Recommendation System
- RAG-Based Information Retrieval

Demo can be provided through:

- GitHub Repository
- Screen Recording
- Live Deployment

---

## 2. User Flow Diagram

Status: ✅ Completed

Personas Covered:

### Farmer

Language Selection
↓
Profile Input
↓
Eligibility Check
↓
PM Kisan / PMAY Recommendations
↓
AI Guidance

### Gig Worker

Language Selection
↓
Profile Input
↓
e-Shram Recommendation
↓
Application Guidance

### Woman Head-of-Household

Language Selection
↓
Profile Input
↓
Ujjwala / PMAY Recommendation
↓
Document Guidance

---

## 3. Pilot Test Report

Status: ✅ Completed

Participants: 12

Categories:

- Farmers
- Workers
- Vendors
- Students
- Self-Employed Users

Findings:

- 91.7% received relevant recommendations
- 100% completed eligibility flow
- Average AI Rating: 4.4/5

---

## 4. Two-Page Impact Projection

Status: ✅ Completed

Projected Outcomes:

- Increased awareness of welfare schemes
- Improved accessibility
- Higher scheme adoption rates
- Reduced information barriers

Estimated impact:

- 1500+ additional beneficiaries per district

---

# 👥 User Personas

## Farmer

Recommended Schemes:

- PM Kisan
- Ayushman Bharat
- PMAY

---

## Gig Worker

Recommended Schemes:

- e-Shram
- MGNREGA
- Ayushman Bharat

---

## Woman Head-of-Household

Recommended Schemes:

- Ujjwala Yojana
- PMAY
- Ayushman Bharat

---

# 📊 Future Enhancements

- Voice Assistant
- WhatsApp Integration
- Additional Indian Languages
- State-Specific Schemes
- PDF Downloads
- Mobile Application
- User Login System

---

# 📈 Project Impact

The project aims to:

- Improve welfare accessibility
- Reduce information asymmetry
- Increase awareness among rural citizens
- Support multilingual communities
- Simplify scheme discovery and application

---

# 👨‍💻 Developed By

Ujjwal Mishra
Naisha Rajput

AI-Based Multilingual Welfare Scheme Assistant

Project Submission 1

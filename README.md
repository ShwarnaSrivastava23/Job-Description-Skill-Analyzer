# 🎯 Job Description Skill Analyzer

### 🤖 AI-powered Resume & Job Matching Tool

> Understand how well your resume matches a job description — identify your strengths, missing skills, important keywords, and areas for improvement.

<p align="center">

  <a href="https://job-description-skill-analyzer-jvmpapdambhgiyo4upmfq4.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge">
  </a>

  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white">

  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

  <img src="https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge">

</p>

---

## 🌐 Live Demo

🚀 **Try the application:**

👉 [Job Description Skill Analyzer](https://job-description-skill-analyzer-jvmpapdambhgiyo4upmfq4.streamlit.app/)

---

## 📌 About The Project

Finding out whether a resume matches a job description can take a lot of time.

**Job Description Skill Analyzer** is an AI-powered web application that makes this process easier.

Users can paste a job description and upload their resume. The application analyzes both and provides a simple breakdown of the candidate's job fit.

It helps users understand:

- 🎯 How closely their resume matches the job
- ✅ Which required skills they already have
- ⚠️ Which important skills are missing
- 🔑 Which keywords matter for the role
- 💡 How they can improve their resume

The tool is designed to be useful for both **technical and non-technical users**.

---

# ✨ Key Features

### 📋 Job Description Input

Paste any job description into the application and let the AI identify the important requirements.

### 📄 Resume Upload

Upload your resume in multiple formats:

- PDF
- DOCX
- TXT

### 🤖 AI-Powered Analysis

The application uses **Groq AI** to compare the job description with the uploaded resume.

### 🎯 Skill Match Score

Get an estimated **match percentage** based on the important requirements identified from the job description.

### ✅ Skills Found

See the important job-related skills that are clearly present in your resume.

### ⚠️ Missing Skills

Identify important skills from the job description that are not clearly mentioned in your resume.

### 🧠 Skills Required

Get a list of important technical and soft skills identified from the job description.

### 🔑 Important Keywords

Find technologies, tools, concepts, and role-related keywords that are important for the position.

### 💡 Improvement Suggestions

Get short and practical suggestions for improving your resume for the selected job.

### 🎨 User-Friendly Interface

A clean, modern and responsive interface built using Streamlit.

---

# 🔄 Application Workflow

```text
              👤 USER
                │
                ▼
       ┌──────────────────┐
       │  Paste Job       │
       │  Description     │
       └────────┬─────────┘
                │
                │
                ▼
       ┌──────────────────┐
       │  Upload Resume   │
       │ PDF / DOCX / TXT │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ Resume Text      │
       │ Extraction       │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │    Groq AI       │
       │    Analysis      │
       └────────┬─────────┘
                │
                ▼
    ┌─────────────────────────┐
    │      AI RESULTS         │
    ├─────────────────────────┤
    │ 🎯 Match Percentage     │
    │ ✅ Skills Found         │
    │ ⚠️ Missing Skills       │
    │ 🧠 Skills Required      │
    │ 🔑 Important Keywords   │
    │ 💡 Suggestions          │
    └─────────────────────────┘

# 🎯 Job Description Skill Analyzer

An AI-powered web application that compares a job description with a candidate's resume and provides a clear analysis of their job fit.

It identifies matching skills, missing skills, important keywords, and practical suggestions to help users improve their resumes before applying for a job.

🔗 **Live Demo:**  
https://job-description-skill-analyzer-jvmpapdambhgiyo4upmfq4.streamlit.app/

---

## ✨ Features

- 📋 **Job Description Analysis**
  - Paste any job description into the application.
  - Identifies important skills and requirements.

- 📄 **Resume Upload**
  - Supports PDF, DOCX, and TXT resume formats.
  - Automatically extracts text from the uploaded resume.

- 🤖 **AI-Powered Analysis**
  - Uses Groq AI to compare the resume with the job description.
  - Provides a structured analysis of the candidate's profile.

- 🎯 **Skill Match Percentage**
  - Shows an estimated match percentage based on the important requirements of the job.

- ✅ **Skills Found**
  - Displays skills from the job description that are clearly present in the resume.

- ⚠️ **Missing Skills**
  - Highlights important skills that are required but not clearly mentioned in the resume.

- 🧠 **Skills Required**
  - Lists important technical and soft skills identified from the job description.

- 🔑 **Important Keywords**
  - Extracts important technologies, tools, concepts, and role-related keywords.

- 💡 **Resume Suggestions**
  - Provides practical suggestions for improving the resume according to the job description.

- 📱 **User-Friendly Interface**
  - Clean and responsive Streamlit interface.
  - Designed for both technical and non-technical users.

---

## 🔄 How It Works

```text
             ┌─────────────────────┐
             │   Job Description    │
             │       Input         │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │     Resume Upload   │
             │   PDF / DOCX / TXT  │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Resume Text       │
             │     Extraction      │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │      Groq AI        │
             │ Resume + JD Analysis│
             └──────────┬──────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │       Analysis Results      │
          ├─────────────────────────────┤
          │ 🎯 Match Percentage         │
          │ ✅ Skills Found             │
          │ ⚠️ Missing Skills           │
          │ 🧠 Skills Required          │
          │ 🔑 Important Keywords       │
          │ 💡 Suggestions              │
          └─────────────────────────────┘

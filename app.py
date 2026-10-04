import streamlit as st
import json
from groq import Groq


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Job Description Skill Analyzer",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN BACKGROUND
   ===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #172554 50%,
        #1e1b4b 100%
    );
    color: white;
}


/* =====================================================
   HERO SECTION
   ===================================================== */

.hero {
    text-align: center;
    padding: 35px 20px 30px 20px;
}

.hero h1 {
    color: white;
    font-size: 46px;
    font-weight: 700;
    margin: 12px 0;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 8px;
}

.badge {
    display: inline-block;
    background: rgba(99, 102, 241, 0.20);
    border: 1px solid rgba(129, 140, 248, 0.40);
    color: #c7d2fe;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
}


/* =====================================================
   INPUT CARDS
   ===================================================== */

.card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 12px;
}

.card-title {
    color: white;
    font-size: 21px;
    font-weight: 600;
}

.card-subtitle {
    color: #a5b4fc;
    font-size: 14px;
    margin-top: 6px;
}


/* =====================================================
   JOB DESCRIPTION TEXT AREA
   ===================================================== */

.stTextArea label {
    color: #e2e8f0 !important;
}

.stTextArea textarea {
    background-color: rgba(15, 23, 42, 0.90) !important;
    color: white !important;
    border: 1px solid #475569 !important;
    border-radius: 12px !important;
}

.stTextArea textarea::placeholder {
    color: #94a3b8 !important;
}


/* =====================================================
   RESUME FILE UPLOADER
   ===================================================== */

.stFileUploader label {
    color: #e2e8f0 !important;
    font-size: 16px !important;
}

[data-testid="stFileUploader"] {
    background: transparent !important;
}

[data-testid="stFileUploader"] section {
    background: #f8fafc !important;
    border: 1px dashed #64748b !important;
    border-radius: 14px !important;
}

/* Text inside uploader */

[data-testid="stFileUploader"] section * {
    color: #334155 !important;
}

/* Upload button */

[data-testid="stFileUploader"] button {
    background: white !important;
    color: #334155 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

[data-testid="stFileUploader"] button:hover {
    background: #f1f5f9 !important;
    color: #0f172a !important;
}

/* File type information */

[data-testid="stFileUploader"] small {
    color: #64748b !important;
}


/* =====================================================
   ANALYZE BUTTON
   ===================================================== */

.stButton > button {
    width: 100% !important;
    background: linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 13px 20px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

.stButton > button p {
    color: white !important;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    ) !important;
}


/* =====================================================
   RESULT CARDS
   ===================================================== */

.result-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 18px;
    padding: 22px;
    margin-top: 15px;
}

.result-title {
    color: white;
    font-size: 19px;
    font-weight: 600;
    margin-bottom: 10px;
}


/* =====================================================
   SKILL TAGS
   ===================================================== */

.skill {
    display: inline-block;
    background: rgba(99, 102, 241, 0.20);
    border: 1px solid rgba(129, 140, 248, 0.40);
    color: #c7d2fe;
    padding: 7px 12px;
    border-radius: 20px;
    margin: 4px;
    font-size: 14px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 40px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="badge">
        🎯 AI-Powered Career Tool
    </div>

    <h1>
        Job Description Skill Analyzer
    </h1>

    <p>
        Compare your resume with a job description using AI
        and discover the skills that matter.
    </p>

</div>
""")


# =========================================================
# INPUT COLUMNS
# =========================================================

col1, col2 = st.columns(2, gap="large")


# =========================================================
# JOB DESCRIPTION
# =========================================================

with col1:

    st.html("""
    <div class="card">

        <div class="card-title">
            📋 Job Description
        </div>

        <div class="card-subtitle">
            Paste the job description you want to analyze.
        </div>

    </div>
    """)

    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the job description here...",
        height=300,
        label_visibility="collapsed"
    )


# =========================================================
# RESUME UPLOAD
# =========================================================

with col2:

    st.html("""
    <div class="card">

        <div class="card-title">
            📄 Your Resume
        </div>

        <div class="card-subtitle">
            Upload your resume in PDF, DOCX or TXT format.
        </div>

    </div>
    """)

    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx", "txt"]
    )

    resume = ""


    # =====================================================
    # READ RESUME
    # =====================================================

    if uploaded_resume is not None:

        file_name = uploaded_resume.name.lower()


        # -------------------------------------------------
        # PDF
        # -------------------------------------------------

        if file_name.endswith(".pdf"):

            from pypdf import PdfReader

            reader = PdfReader(uploaded_resume)

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    resume += page_text + "\n"


        # -------------------------------------------------
        # DOCX
        # -------------------------------------------------

        elif file_name.endswith(".docx"):

            from docx import Document

            document = Document(uploaded_resume)

            for paragraph in document.paragraphs:

                resume += paragraph.text + "\n"


        # -------------------------------------------------
        # TXT
        # -------------------------------------------------

        elif file_name.endswith(".txt"):

            resume = uploaded_resume.read().decode(
                "utf-8",
                errors="ignore"
            )


        # -------------------------------------------------
        # UPLOAD STATUS
        # -------------------------------------------------

        if resume.strip():

            st.success(
                f"✅ Resume uploaded: {uploaded_resume.name}"
            )

        else:

            st.warning(
                "The file was uploaded, but no readable text was found."
            )


# =========================================================
# ANALYZE BUTTON
# =========================================================

st.write("")

analyze = st.button("✨ Analyze with AI")


# =========================================================
# AI ANALYSIS
# =========================================================

if analyze:

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not job_description.strip():

        st.warning(
            "Please enter the job description."
        )

    elif not resume.strip():

        st.warning(
            "Please upload a readable resume."
        )

    else:

        with st.spinner(
            "🤖 AI is analyzing your resume..."
        ):

            try:

                # =================================================
                # GROQ CLIENT
                # =================================================

                client = Groq(
                    api_key=st.secrets["GROQ_API_KEY"]
                )


                # =================================================
                # PROMPT
                # =================================================

                prompt = f"""
You are an AI job description and resume analyzer.

Compare the following job description with the resume.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume}

Return ONLY valid JSON using exactly this structure:

{{
    "match_percentage": 0,
    "skills_required": [],
    "skills_found": [],
    "missing_skills": [],
    "important_keywords": [],
    "suggestions": []
}}

Rules:

1. match_percentage must be an integer from 0 to 100.

2. skills_required should contain important technical
   and soft skills required by the job.

3. skills_found should contain skills required by the job
   that are clearly present in the resume.

4. missing_skills should contain important job skills that
   are not clearly present in the resume.

5. important_keywords should contain important technologies,
   tools, concepts and role-related keywords.

6. suggestions should contain 3 to 5 short and practical
   suggestions for improving the resume for this job.

7. Do not invent information.

8. Do not assume that the candidate has a skill unless
   the resume clearly supports it.

9. Keep the suggestions simple and useful.

10. Return JSON only.
"""


                # =================================================
                # GROQ REQUEST
                # =================================================

                response = client.chat.completions.create(

                    model="openai/gpt-oss-120b",

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],

                    temperature=0
                )


                # =================================================
                # GET AI RESPONSE
                # =================================================

                answer = response.choices[0].message.content

                answer = answer.strip()


                # =================================================
                # REMOVE CODE FENCES
                # =================================================

                if answer.startswith("```json"):

                    answer = answer[7:]


                elif answer.startswith("```"):

                    answer = answer[3:]


                if answer.endswith("```"):

                    answer = answer[:-3]


                answer = answer.strip()


                # =================================================
                # PARSE JSON
                # =================================================

                result = json.loads(answer)


                # =================================================
                # RESULTS HEADING
                # =================================================

                st.markdown(
                    "## 📊 AI Analysis Results"
                )


                # =================================================
                # MATCH PERCENTAGE
                # =================================================

                match_percentage = int(
                    result.get(
                        "match_percentage",
                        0
                    )
                )

                match_percentage = max(
                    0,
                    min(
                        100,
                        match_percentage
                    )
                )


                st.html(f"""
                <div class="result-card">

                    <div class="result-title">
                        🎯 Skill Match
                    </div>

                    <h1>
                        {match_percentage}%
                    </h1>

                    <p style="color:#94a3b8;">
                        Based on the important skills and
                        requirements identified in the job description.
                    </p>

                </div>
                """)


                # =================================================
                # FOUND + MISSING
                # =================================================

                result1, result2 = st.columns(
                    2,
                    gap="large"
                )


                # =================================================
                # SKILLS FOUND
                # =================================================

                with result1:

                    st.html("""
                    <div class="result-card">

                        <div class="result-title">
                            ✅ Skills Found
                        </div>

                    </div>
                    """)


                    skills_found = result.get(
                        "skills_found",
                        []
                    )


                    if skills_found:

                        html = ""

                        for skill in skills_found:

                            html += (
                                f'<span class="skill">'
                                f'{skill}'
                                f'</span>'
                            )

                        st.html(html)

                    else:

                        st.write(
                            "No matching skills found."
                        )


                # =================================================
                # MISSING SKILLS
                # =================================================

                with result2:

                    st.html("""
                    <div class="result-card">

                        <div class="result-title">
                            ⚠️ Missing Skills
                        </div>

                    </div>
                    """)


                    missing_skills = result.get(
                        "missing_skills",
                        []
                    )


                    if missing_skills:

                        html = ""

                        for skill in missing_skills:

                            html += (
                                f'<span class="skill">'
                                f'{skill}'
                                f'</span>'
                            )

                        st.html(html)

                    else:

                        st.write(
                            "No major missing skills detected."
                        )


                # =================================================
                # REQUIRED SKILLS
                # =================================================

                st.html("""
                <div class="result-card">

                    <div class="result-title">
                        🧠 Skills Required
                    </div>

                </div>
                """)


                skills_required = result.get(
                    "skills_required",
                    []
                )


                if skills_required:

                    html = ""

                    for skill in skills_required:

                        html += (
                            f'<span class="skill">'
                            f'{skill}'
                            f'</span>'
                        )

                    st.html(html)

                else:

                    st.write(
                        "No skills detected."
                    )


                # =================================================
                # IMPORTANT KEYWORDS
                # =================================================

                st.html("""
                <div class="result-card">

                    <div class="result-title">
                        🔑 Important Keywords
                    </div>

                </div>
                """)


                keywords = result.get(
                    "important_keywords",
                    []
                )


                if keywords:

                    html = ""

                    for keyword in keywords:

                        html += (
                            f'<span class="skill">'
                            f'{keyword}'
                            f'</span>'
                        )

                    st.html(html)

                else:

                    st.write(
                        "No important keywords detected."
                    )


                # =================================================
                # SUGGESTIONS
                # =================================================

                st.html("""
                <div class="result-card">

                    <div class="result-title">
                        💡 Suggestions
                    </div>

                </div>
                """)


                suggestions = result.get(
                    "suggestions",
                    []
                )


                if suggestions:

                    for suggestion in suggestions:

                        st.write(
                            "•",
                            suggestion
                        )

                else:

                    st.write(
                        "No suggestions available."
                    )


            # =====================================================
            # JSON ERROR
            # =====================================================

            except json.JSONDecodeError:

                st.error(
                    "The AI returned an unexpected response. "
                    "Please click Analyze with AI again."
                )


            # =====================================================
            # OTHER ERRORS
            # =====================================================

            except Exception as e:

                st.error(
                    "Something went wrong while analyzing the resume."
                )

                st.write(
                    str(e)
                )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    Built with Python • Streamlit • Groq AI
</div>
""")
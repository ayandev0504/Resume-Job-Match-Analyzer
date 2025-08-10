# Resume & Job Match Analyzer - Streamlit App (Starter Boilerplate)
# Save as: app.py
# Requirements (put in requirements.txt):
# streamlit
# openai
# pdfplumber
# python-multipart
# pandas
# fitz (PyMuPDF)  -- optional

import os
import streamlit as st
import pdfplumber
import re
import json
from typing import Tuple

# Optional: You can switch to local LLMs (Ollama) or other providers by replacing llm_call
# Set OPENAI_API_KEY as an environment variable before running locally.

st.set_page_config(page_title="Resume & Job Match Analyzer", layout="wide")

# -----------------------
# Utility: PDF to text
# -----------------------

def extract_text_from_pdf(file) -> str:
    """Extract text from an uploaded PDF file (streamlit UploadedFile-like)."""
    try:
        with pdfplumber.open(file) as pdf:
            texts = [p.extract_text() or "" for p in pdf.pages]
        text = "\n".join(texts)
    except Exception as e:
        # Fallback: try reading binary and simple decode
        file.seek(0)
        raw = file.read()
        try:
            text = raw.decode('utf-8', errors='ignore')
        except Exception:
            text = ""
    # Basic cleanup
    text = re.sub(r"\n{2,}", "\n", text)
    text = text.strip()
    return text

# -----------------------
# Utility: LLM call (OpenAI)
# -----------------------

def llm_analyze_resume_and_jd(resume_text: str, jd_text: str) -> dict:
    """Call LLM to get match score, skills gap, suggestions, and rewritten bullets.
    Replace this implementation with your preferred LLM / prompt engineering.
    """
    # Minimal local stub to show UI while building prompts.
    # When ready, implement using OpenAI or another provider.

    # Example stub output (simple heuristic)
    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    # naive keyword match for a quick prototype
    jd_tokens = set(re.findall(r"\b[a-zA-Z0-9+-]+\b", jd_lower))
    resume_tokens = set(re.findall(r"\b[a-zA-Z0-9+-]+\b", resume_lower))
    common = jd_tokens.intersection(resume_tokens)
    if len(jd_tokens) == 0:
        score = 0
    else:
        score = int(100 * len(common) / len(jd_tokens))
    
    # Create dummy skills gap (top 5 jd tokens not in resume)
    missing = list((jd_tokens - resume_tokens))[:10]

    # Dummy suggestions
    suggestions = [
        "Add or highlight relevant projects that show experience with key JD skills.",
        "Use metric-driven bullet points (e.g., improved X by Y%).",
    ]

    # Dummy rewritten bullets - pick 3 lines from resume and 'rewrite'
    resume_lines = [l.strip() for l in resume_text.splitlines() if l.strip()][:20]
    rewritten = []
    for i, line in enumerate(resume_lines[:3]):
        rewritten.append(f"Improved: {line} -> {line} (tailored version)")

    return {
        "score": score,
        "missing_skills": missing,
        "suggestions": suggestions,
        "rewritten_lines": rewritten,
    }

# -----------------------
# UI
# -----------------------

st.title("Resume & Job Match Analyzer")
st.write("Upload a resume (PDF) and paste or upload a job description. The app will analyze the match and suggest improvements.")

with st.sidebar:
    st.header("Inputs")
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"], help="Your resume as PDF")
    uploaded_jd = st.file_uploader("Upload Job Description (PDF)", type=["pdf"], help="Optional: JD as PDF")
    jd_text_area = st.text_area("Or paste Job Description text here", height=200)
    model_choice = st.selectbox("LLM Provider (for later)", ["Stub (fast)", "OpenAI (API)", "Ollama (local)"])
    run_btn = st.button("Analyze")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Extracted Resume")
    if uploaded_resume is not None:
        resume_text = extract_text_from_pdf(uploaded_resume)
        st.text_area("Resume Text", value=resume_text[:10000], height=300)
    else:
        resume_text = ""
        st.info("Upload a resume PDF to see extracted text here.")

    st.subheader("Job Description")
    if uploaded_jd is not None:
        jd_text = extract_text_from_pdf(uploaded_jd)
        st.text_area("Job Description Text", value=jd_text[:10000], height=200)
    else:
        jd_text = jd_text_area
        if not jd_text:
            st.info("Paste job description text or upload a JD PDF.")

with col2:
    st.subheader("Analysis")
    if run_btn:
        if not resume_text.strip():
            st.error("Please upload a resume PDF before analyzing.")
        elif not jd_text or not jd_text.strip():
            st.error("Please provide the job description (paste text or upload PDF).")
        else:
            with st.spinner("Analyzing with LLM... (stub) "):
                result = llm_analyze_resume_and_jd(resume_text, jd_text)

            # Score card
            st.metric(label="Match Score", value=f"{result['score']}%")
            st.markdown("---")

            st.markdown("### Missing / Weak Skills")
            if result['missing_skills']:
                st.write(result['missing_skills'])
            else:
                st.write("No obvious missing skills detected by stub logic.")

            st.markdown("### Suggestions to Improve Resume")
            for s in result['suggestions']:
                st.write(f"- {s}")

            st.markdown("### Rewritten Resume Snippets")
            for r in result['rewritten_lines']:
                st.code(r)

            # Download option
            st.download_button("Download rewritten snippets (txt)", data="\n".join(result['rewritten_lines']), file_name="rewritten_snippets.txt")

    else:
        st.info("Click 'Analyze' in the sidebar to run the analysis.")

# -----------------------
# Notes & Next Steps
# -----------------------
st.markdown("---")
st.markdown("### Next steps (what to implement next):")
st.write(
    "1. Replace `llm_analyze_resume_and_jd` stub with real LLM calls (OpenAI or Ollama).\n"
    "2. Improve prompt engineering to return structured JSON (score, skills, suggestions, rewritten bullets).\n"
    "3. Add an option to export a full updated resume as PDF (reportlab or LaTeX).\n"
    "4. Add better parsing logic to extract structured sections (Experience, Education, Skills)."
)

st.caption("Starter boilerplate created for rapid development. Good luck — you can now replace the stub with proper LLM calls and prompt engineering!")

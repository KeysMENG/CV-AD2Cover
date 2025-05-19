import streamlit as st
from utils.file_handler import read_cv
from utils.web_scraper import fetch_job_description
from utils.matcher import generate_cover_letter

st.title("AI Cover Letter Generator")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
cv_file = st.file_uploader("Upload your CV file (PDF/DOC/DOCX/TXT)")
job_input = st.text_area("Enter job description or job webpage URL")
job_file = st.file_uploader("Or upload job description file (PDF/DOC/DOCX/TXT, optional)")
advisor_info = st.text_area("Optional: Enter advisor/lab information (if any)")

def read_job_file(file):
    from utils.file_handler import read_cv
    return read_cv(file)

if st.button("Generate Cover Letter"):
    if not api_key:
        st.warning("Please enter your OpenAI API Key.")
    elif not cv_file or (not job_input and not job_file):
        st.warning("Please upload your CV and enter job description/URL or upload a job file.")
    else:
        cv_text = read_cv(cv_file)
        if job_file:
            job_desc = read_job_file(job_file)
        elif job_input.startswith("http"):
            job_desc = fetch_job_description(job_input)
        else:
            job_desc = job_input
        cover_letter = generate_cover_letter(
            cv_text, job_desc, advisor_info if advisor_info else None, api_key=api_key
        )
        st.subheader("Generated Cover Letter:")
        st.text_area("Cover Letter", cover_letter, height=400)
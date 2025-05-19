import openai

def generate_cover_letter(cv_text, job_desc, advisor_info=None, api_key=None):
    prompt = f"""
You are an experienced job seeker in scientific research, applying for a laboratory research position or PhD program.

Please generate a professional cover letter in English (no more than one A4 page) that strictly follows international standards and conventions for academic job applications.

Requirements:
1. Combine the provided job description and CV content to highlight your professional skills, academic background, and fit for the position.
2. If advisor/lab information is provided, incorporate relevant research directions, recent achievements, and preferences to demonstrate your understanding and interest.
3. The cover letter should be well-structured, use formal academic English, emphasize your strengths, and express enthusiasm and willingness to contribute.
4. Output must be a formal English cover letter, formatted according to international standards, and limited to one A4 page.

Job Description:
{job_desc}

CV Content:
{cv_text}

{f"Advisor/Lab Information: {advisor_info}" if advisor_info else ""}
Please strictly follow the above requirements and output only the cover letter in English.
"""
    if not api_key:
        raise ValueError("API Key is required.")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content.strip()
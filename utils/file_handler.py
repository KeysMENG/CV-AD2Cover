import PyPDF2
import docx

def read_cv(file):
    name = file.name.lower()
    if name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    elif name.endswith('.doc') or name.endswith('.docx'):
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    else:
        return file.read().decode('utf-8')
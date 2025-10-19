from PyPDF2 import PdfReader
import docx
import os

def extract_from_pdf(path):
    text = ""
    reader = PdfReader(path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

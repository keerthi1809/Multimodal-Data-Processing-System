from extract_text import extract_from_pdf, extract_from_docx, extract_from_txt
from extract_image import extract_from_image
from extract_audio import extract_from_audio, extract_from_video
from database import save_data, load_data
from query_handler import get_answer

def process_files():
    files = ["data/sample.pdf", "data/image1.jpg"]
    data = load_data()
    for f in files:
        if f.endswith(".pdf"):
            data[f] = extract_from_pdf(f)
        elif f.endswith(".jpg"):
            data[f] = extract_from_image(f)
    save_data(data)
    print("Data processed successfully!")

def query_system():
    data = load_data()
    query = input("Enter your question: ")
    answer = get_answer(query, data)
    print("Answer:", answer)

if __name__ == "__main__":
    process_files()
    query_system()

import os
from pypdf import PdfReader

def load_document(file_path: str) -> str:
    """
    Loads text from a TXT or PDF file and returns extracted text.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"

        return text

    else:
        raise ValueError("Unsupported file type. Use .txt or .pdf")

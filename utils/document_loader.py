# not in use yet 
import os
from pypdf import PdfReader


def load_document(file_path: str) -> str:
    """
    Load text from a .txt or .pdf file
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return _load_txt(file_path)
    elif ext == ".pdf":
        return _load_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def _load_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _load_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = []

    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)

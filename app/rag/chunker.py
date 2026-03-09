import os
from pypdf import PdfReader


def load_documents(directory_path: str):
    """
    Load text from all PDF and TXT files inside the documents folder.
    """
    documents = []

    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)

        if file.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""

            for page in reader.pages:
                text += page.extract_text()

            documents.append(text)

        elif file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Split text into overlapping chunks.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def chunk_documents(directory_path: str):
    """
    Load documents and convert them into chunks.
    """
    documents = load_documents(directory_path)

    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    return all_chunks
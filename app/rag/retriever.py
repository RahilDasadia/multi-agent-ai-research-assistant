import os

from app.rag.chunker import chunk_documents
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()
        self.documents_path = "app/knowledge/documents"

    def ingest_documents(self):

        chunks = chunk_documents(self.documents_path)

        if len(chunks) == 0:
            print("No documents found to ingest.")
            return

        self.vector_store.add_documents(chunks)

        print(f"{len(chunks)} chunks stored in vector database.")

    def retrieve(self, query: str):

        results = self.vector_store.query(query)

        context = "\n\n".join(results)

        return context
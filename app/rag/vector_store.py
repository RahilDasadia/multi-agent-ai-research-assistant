import chromadb
from chromadb.config import Settings

from app.rag.embedder import Embedder


class VectorStore:
    def __init__(self):
        """
        Initialize ChromaDB vector database and embedding model.
        """
        self.client = chromadb.Client(
            Settings(
                persist_directory="app/knowledge/vector_db"
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

        self.embedder = Embedder()

    def add_documents(self, chunks):
        """
        Add text chunks to the vector database.
        """
        embeddings = self.embedder.embed_documents(chunks)

        ids = [f"chunk_{i}" for i in range(len(chunks))]

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids
        )

    def query(self, query_text, top_k=3):
        """
        Search the vector database for relevant chunks.
        """
        query_embedding = self.embedder.embed_query(query_text)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]
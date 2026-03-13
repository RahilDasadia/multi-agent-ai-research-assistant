from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self):
        """
        Load a lightweight embedding model suitable for CPU.
        """
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, chunks):
        """
        Convert a list of text chunks into embeddings.
        """
        return Embedder.model.encode(chunks)

        return embeddings

    def embed_query(self, query: str):
        """
        Convert a user query into embedding vector.
        """
        return Embedder.model.encode([query])[0]
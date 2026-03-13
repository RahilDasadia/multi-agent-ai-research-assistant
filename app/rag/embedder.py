from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):
        # Load model once when object is created
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, chunks):
        """
        Convert text chunks into embeddings
        """
        return self.model.encode(chunks)

    def embed_query(self, query: str):
        """
        Convert query into embedding
        """
        return self.model.encode([query])[0]
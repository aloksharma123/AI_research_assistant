from src.vectordb.chroma_manager import ChromaManager


class Retriever:
    """
    Retrieves relevant document chunks from vector database.
    """

    def __init__(self, vector_db):

        self.vector_db = vector_db


    def retrieve(self, query, k=4):

        documents = self.vector_db.search(
            query,
            k=k
        )

        return documents
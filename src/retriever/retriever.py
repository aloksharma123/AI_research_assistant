class Retriever:
    """
    Retrieves relevant document chunks.
    """

    def __init__(self, db):

        self.db = db

    def retrieve(self, query, k=8):

        return self.db.similarity_search(
            query,
            k=k
        )
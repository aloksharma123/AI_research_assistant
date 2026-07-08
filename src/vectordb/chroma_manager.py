from langchain_chroma import Chroma


class ChromaManager:
    """
    Handles Chroma vector database.
    """

    def __init__(self, embedding_model):

        self.db = Chroma(
            collection_name="research_documents",
            embedding_function=embedding_model,
            persist_directory="vectorstore"
        )


    def add_documents(self, documents):

        self.db.add_documents(documents)


    def search(self, query, k=3):

        return self.db.similarity_search(
            query,
            k=k
        )
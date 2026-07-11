from langchain_chroma import Chroma


class ChromaManager:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model


    def create_database(self, documents):

        db = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model
        )

        return db
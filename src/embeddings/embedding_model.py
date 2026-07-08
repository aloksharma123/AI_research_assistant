from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    HuggingFace embedding model wrapper.
    """

    def __init__(self):

        self.model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )


    def get_model(self):

        return self.model
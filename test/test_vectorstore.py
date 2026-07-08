from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_manager import ChromaManager

from langchain_core.documents import Document


embedding = EmbeddingModel()

model = embedding.get_model()


db = ChromaManager(model)


documents = [

    Document(
        page_content="Machine learning is a branch of artificial intelligence.",
        metadata={
            "source": "test"
        }
    ),

    Document(
        page_content="Deep learning uses neural networks with many layers.",
        metadata={
            "source": "test"
        }
    ),

    Document(
        page_content="Python is widely used for AI development.",
        metadata={
            "source": "test"
        }
    )

]


db.add_documents(documents)


results = db.search(
    "What is deep learning?"
)


for result in results:

    print("----------------")

    print(result.page_content)
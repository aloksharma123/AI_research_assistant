from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_manager import ChromaManager
from src.retriever.retriever import Retriever

from langchain_core.documents import Document


embedding = EmbeddingModel()

model = embedding.get_model()


db = ChromaManager(model)


documents = [

    Document(
        page_content="Transformers are neural networks based on attention mechanisms.",
        metadata={"source": "paper1"}
    ),

    Document(
        page_content="Convolutional neural networks are commonly used for image processing.",
        metadata={"source": "paper2"}
    ),

    Document(
        page_content="Reinforcement learning trains agents using rewards.",
        metadata={"source": "paper3"}
    )

]


db.add_documents(documents)


retriever = Retriever(db)


results = retriever.retrieve(
    "How do transformers work?"
)


for doc in results:

    print("----------------")

    print(doc.page_content)
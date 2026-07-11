from src.utils.file_manager import save_uploaded_file
from src.loaders.pdf_loader import PDFLoader
from src.preprocessing.text_splitter import TextChunker

from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_manager import ChromaManager
from src.retriever.retriever import Retriever


class DocumentService:
    """
    Handles complete document ingestion pipeline.

    PDFs
      ↓
    Text Extraction
      ↓
    Chunking
      ↓
    Embeddings
      ↓
    Chroma Vector Database
      ↓
    Retriever
    """

    def __init__(self):

        self.chunker = TextChunker()

        self.embedding_model = EmbeddingModel().get_model()

        self.vector_db = ChromaManager(
            self.embedding_model
        )

    def process(self, uploaded_files):

        all_chunks = []
        metadata = []

        for uploaded_file in uploaded_files:

            file_path = save_uploaded_file(
                uploaded_file
            )

            loader = PDFLoader(
                file_path
            )

            document = loader.load()

            chunks = self.chunker.split(
                document["text"],
                document["metadata"]
            )

            all_chunks.extend(chunks)

            metadata.append(
                document["metadata"]
            )

        db = self.vector_db.create_database(
            all_chunks
        )

        retriever = Retriever(
            db
        )

        return {
            "retriever": retriever,
            "metadata": metadata,
            "chunks": all_chunks
        }
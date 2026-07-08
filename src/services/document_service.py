from src.utils.file_manager import save_uploaded_file
from src.loaders.pdf_loader import PDFLoader
from src.preprocessing.text_splitter import TextChunker

from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_manager import ChromaManager
from src.retriever.retriever import Retriever


class DocumentService:
    """
    Handles complete document ingestion pipeline:
    
    PDF
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


    def process(self, uploaded_file):

        # Save PDF
        file_path = save_uploaded_file(
            uploaded_file
        )


        # Load PDF text
        loader = PDFLoader(
            file_path
        )

        document = loader.load()


        # Split into chunks
        chunks = self.chunker.split(
            document["text"],
            document["metadata"]
        )


        # Store chunks in Chroma
        self.vector_db.add_documents(
            chunks
        )


        # Create retriever
        retriever = Retriever(
            self.vector_db
        )


        # Attach results
        document["chunks"] = chunks

        document["retriever"] = retriever


        return document
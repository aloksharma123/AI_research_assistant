from src.utils.file_manager import save_uploaded_file
from src.loaders.pdf_loader import PDFLoader
from src.preprocessing.text_splitter import TextChunker


class DocumentService:
    """
    Handles the complete document processing pipeline.
    """

    def __init__(self):
        self.chunker = TextChunker()

    def process(self, uploaded_file):

        file_path = save_uploaded_file(uploaded_file)

        loader = PDFLoader(file_path)

        document = loader.load()

        chunks = self.chunker.split(
            document["text"],
            document["metadata"],
        )

        document["chunks"] = chunks

        return document
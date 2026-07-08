from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TextChunker:
    """
    Splits document text into LangChain Document chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, text: str, metadata: dict):

        documents = [
            Document(
                page_content=text,
                metadata=metadata,
            )
        ]

        return self.splitter.split_documents(documents)
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """
    Splits document text into meaningful chunks for RAG.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=400,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )


    def split(self, text, metadata):

        chunks = self.splitter.create_documents(
            [text],
            metadatas=[metadata]
        )

        return chunks
from pathlib import Path
import fitz


class PDFLoader:
    """
    Reads a PDF file and extracts text and metadata.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):

        doc = fitz.open(self.file_path)

        text = ""

        for page in doc:
            text += page.get_text()

        metadata = {
            "filename": self.file_path.name,
            "pages": len(doc),
            "characters": len(text),
            "size_kb": round(self.file_path.stat().st_size / 1024, 2),
        }

        doc.close()

        return {
            "text": text,
            "metadata": metadata,
        }
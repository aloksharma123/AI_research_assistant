from pathlib import Path

UPLOAD_DIR = Path("data/uploaded_files")


def save_uploaded_file(uploaded_file):
    """
    Save an uploaded file to disk and return its path.
    """

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path
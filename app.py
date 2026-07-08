import streamlit as st

from frontend.sidebar import render_sidebar
from frontend.chat import render_chat

from src.utils.file_manager import save_uploaded_file
from src.loaders.pdf_loader import PDFLoader


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

uploaded_files, llm_provider, embedding_model = render_sidebar()

if uploaded_files:

    st.sidebar.success(f"{len(uploaded_files)} PDF(s) uploaded")

    for uploaded_file in uploaded_files:

        file_path = save_uploaded_file(uploaded_file)

        loader = PDFLoader(file_path)

        document = loader.load()

        with st.sidebar.expander(document["metadata"]["filename"]):

            st.write(f"Pages: {document['metadata']['pages']}")
            st.write(f"Characters: {document['metadata']['characters']}")
            st.write(f"Size: {document['metadata']['size_kb']} KB")

            st.caption("Preview")

            preview = document["text"][:300]

            st.write(preview + "...")
            
render_chat()
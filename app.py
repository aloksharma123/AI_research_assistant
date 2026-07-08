import streamlit as st

from frontend.sidebar import render_sidebar
from frontend.chat import render_chat

from src.services.document_service import DocumentService

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

document_service = DocumentService()

uploaded_files, llm_provider, embedding_model = render_sidebar()

if uploaded_files:

    st.sidebar.success(f"{len(uploaded_files)} PDF(s) uploaded")

    for uploaded_file in uploaded_files:

        document = document_service.process(uploaded_file)

        chunks = document["chunks"]

        with st.sidebar.expander(document["metadata"]["filename"]):

            st.write(f"Pages: {document['metadata']['pages']}")
            st.write(f"Characters: {document['metadata']['characters']}")
            st.write(f"Size: {document['metadata']['size_kb']} KB")
            st.write(f"Chunks: {len(chunks)}")

            st.caption("Preview")
            st.write(document["text"][:300] + "...")

        # Debug output (temporary)
        st.write("Chunk type:", type(chunks[0]))
        st.write("First chunk:")

        if hasattr(chunks[0], "page_content"):
            st.write(chunks[0].page_content)
        else:
            st.write(chunks[0])

render_chat()
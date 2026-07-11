import streamlit as st

from frontend.sidebar import render_sidebar
from frontend.chat import render_chat

from src.services.document_service import DocumentService
from src.llm.groq_llm import GroqLLM
from src.chains.rag_chain import RAGChain


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

# Initialize services
document_service = DocumentService()
llm = GroqLLM().get_model()

# Sidebar
uploaded_files, llm_provider, embedding_model = render_sidebar()

if uploaded_files:

    document = document_service.process(uploaded_files)

    st.session_state["retriever"] = document["retriever"]

    st.sidebar.success(
        f"{len(uploaded_files)} PDF(s) uploaded"
    )

    for meta in document["metadata"]:

        with st.sidebar.expander(meta["filename"]):

            st.write(f"Pages: {meta['pages']}")
            st.write(f"Characters: {meta['characters']}")

    st.sidebar.write(
        f"Total Chunks: {len(document['chunks'])}"
    )

# Create RAG chain after document upload
if "retriever" in st.session_state:

    rag_chain = RAGChain(
        llm,
        st.session_state["retriever"]
    )

    st.session_state["rag_chain"] = rag_chain

render_chat()
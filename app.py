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

    st.sidebar.success(
        f"{len(uploaded_files)} PDF(s) uploaded"
    )


    for uploaded_file in uploaded_files:


        document = document_service.process(
            uploaded_file
        )


        st.session_state["retriever"] = document["retriever"]


        with st.sidebar.expander(
            document["metadata"]["filename"]
        ):

            st.write(
                f"Pages: {document['metadata']['pages']}"
            )

            st.write(
                f"Characters: {document['metadata']['characters']}"
            )

            st.write(
                f"Chunks: {len(document['chunks'])}"
            )



# Create RAG chain after document upload

if "retriever" in st.session_state:

    rag_chain = RAGChain(
        llm,
        st.session_state["retriever"]
    )

    st.session_state["rag_chain"] = rag_chain



render_chat()
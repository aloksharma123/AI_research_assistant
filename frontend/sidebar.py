import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:
        st.title("⚙️ Settings")

        uploaded_files = st.file_uploader(
            "Upload PDF Documents",
            type=["pdf"],
            accept_multiple_files=True,
        )

        st.divider()

        llm_provider = st.selectbox(
            "LLM Provider",
            [
                "OpenAI",
                "Ollama",
                "Hugging Face",
            ],
        )

        embedding_model = st.selectbox(
            "Embedding Model",
            [
                "all-MiniLM-L6-v2",
                "bge-small-en-v1.5",
            ],
        )

        st.divider()

        if st.button("Clear Chat"):
            st.session_state.messages = []

    return uploaded_files, llm_provider, embedding_model
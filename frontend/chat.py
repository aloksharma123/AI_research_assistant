import streamlit as st


def render_chat():
    """
    Render the main chat interface.
    """

    st.title("📚 AI Research Assistant")

    st.caption("Upload research papers and chat with them.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a question about your documents...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        response = (
            "RAG pipeline is not connected yet. "
            "We'll build it in the next milestones."
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)
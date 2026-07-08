import streamlit as st



def render_chat():

    st.title(
        "📚 AI Research Assistant"
    )

    st.caption(
        "Ask questions about your uploaded research papers."
    )


    if "messages" not in st.session_state:

        st.session_state.messages = []


    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )



    prompt = st.chat_input(
        "Ask something about your PDF..."
    )


    if prompt:


        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )


        with st.chat_message("user"):

            st.markdown(prompt)



        if "rag_chain" not in st.session_state:

            response = (
                "Please upload a PDF first."
            )

        else:

            response = st.session_state["rag_chain"].invoke(
                prompt
            )



        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )


        with st.chat_message("assistant"):

            st.markdown(response)
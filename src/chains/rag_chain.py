from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


class RAGChain:

    def __init__(
        self,
        llm,
        retriever
    ):


        prompt = ChatPromptTemplate.from_template(
            """
You are an AI research assistant.

Answer the user's question using only the provided document context.

If the information is not available in the document,
say:
"I could not find this information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""
        )


        def retrieve_context(question):

            docs = retriever.retrieve(
                question
            )

            return "\n\n".join(
                doc.page_content
                for doc in docs
            )


        self.chain = (
            {
                "context": retrieve_context,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
        )


    def invoke(self, question):

        response = self.chain.invoke(
            question
        )

        return response.content
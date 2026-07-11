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

Answer the user's question using the document context.

Rules:
- Use only the information present in the context.
- If the answer is available, provide a detailed explanation.
- If the information is missing, clearly say:
  "I could not find this information in the uploaded document."

Document Context:
{context}


User Question:
{question}


Answer:
"""
        )


        def retrieve_context(question):

            docs = retriever.retrieve(
                question
            )

            context = ""

            for doc in docs:

                context += (
                    "\n\n"
                    + doc.page_content
                )

            return context



        self.chain = (
            {
                "context": retrieve_context,
                "question": RunnablePassthrough()
            }
            |
            prompt
            |
            llm
        )


    def invoke(self, question):

        response = self.chain.invoke(
            question
        )

        return response.content
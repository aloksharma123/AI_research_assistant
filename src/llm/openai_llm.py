from langchain_openai import ChatOpenAI


class OpenAILLM:
    """
    Wrapper for OpenAI chat models.
    """

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0.2,
        )


    def get_model(self):

        return self.llm
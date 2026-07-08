import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


class GroqLLM:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY missing in .env"
            )

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            api_key=api_key
        )

    def get_model(self):

        return self.llm
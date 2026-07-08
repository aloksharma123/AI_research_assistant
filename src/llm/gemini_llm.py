import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


class GeminiLLM:

    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in .env"
            )

        print(
            "Gemini key loaded:",
            api_key[:8] + "********"
        )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.2,
            google_api_key=api_key,
        )


    def get_model(self):

        return self.llm
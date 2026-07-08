from src.llm.gemini_llm import GeminiLLM


llm = GeminiLLM().get_model()


response = llm.invoke(
    "Explain RAG in simple words"
)


print(response.content)
from src.llm.groq_llm import GroqLLM


llm = GroqLLM().get_model()


response = llm.invoke(
    "Explain RAG in simple words"
)


print(response.content)
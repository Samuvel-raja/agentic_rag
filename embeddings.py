from langchain_openai import OpenAIEmbeddings
from config import settings

def get_embeddings():
    return OpenAIEmbeddings(
        api_key=settings.open_ai_api_key,
        model="text-embedding-3-small"
    )
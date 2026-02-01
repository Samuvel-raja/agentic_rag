from langchain_openai import ChatOpenAI
from config import settings

def get_llm():
    return ChatOpenAI(
        api_key=settings.open_ai_api_key, 
        model="gpt-4o-mini", 
        temperature=0.7
    )
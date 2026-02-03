from langchain_openai import ChatOpenAI
from config import settings

def get_llm():
    return ChatOpenAI(
        api_key=settings.open_ai_api_key, 
        model="gpt-4o-mini", 
        temperature=0.7
    )
# def get_moonlight_llm():
#     return ChatOpenAI(
#         model="moonshot-v1-32k",   # or 128k if enabled
#         temperature=0.7,
#         openai_api_key=settings.moonlight_api_key.strip(),
#         openai_api_base="https://api.moonshot.ai/v1",
#     )
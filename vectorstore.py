from embeddings import get_embeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from config import settings

print("settings",settings)

def get_vectorstore():
    try:
        client = QdrantClient(
    url=settings.qdrant_url
)
        vectorstore= QdrantVectorStore(
        client=client,
        collection_name=settings.collection_name,
        embedding=get_embeddings()
    )
        print("vectorstore",vectorstore)
        return vectorstore
    except Exception as e:
        print(e)

def add_documents(documents):
    try:
        return QdrantVectorStore.from_documents(
        url=settings.qdrant_url,
        collection_name=settings.collection_name,
        embedding=get_embeddings(),
        documents=documents
    )
    except Exception as e:
        print("Qdrant vectorstore error",e)
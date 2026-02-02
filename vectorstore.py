from embeddings import get_embeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from config import settings


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

def get_neo4h_graph():
    try:
        return Neo4jGraph(
            url=settings.neo4j_uri,
            username=settings.neo4j_username,
            password=settings.neo4j_password,
            database=settings.neo4j_database,
            refresh_schema=False
        )
    except Exception as e:
        print(e)
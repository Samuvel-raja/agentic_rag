from llm import get_llm
from textsplitters import TextSplitters
from fastapi import FastAPI,File,UploadFile,Query
from loader import Loaders
from vectorstore import get_vectorstore,get_neo4h_graph
from graph import build_graph
from langchain_experimental.graph_transformers import LLMGraphTransformer
import tempfile



app=FastAPI()
graph=build_graph()

@app.post('/upload')
def upload(file:UploadFile=File(...),
query: str = Query("default")):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path=temp_file.name
            temp_file.write(file.file.read())
        pdfloader=Loaders().pdf_loader(file_path)
        documents=pdfloader.load()
        print("Documents loaded successfully")
        chunks=TextSplitters().recursive_text_splitter(documents)
        print("Documents split successfully")
        for doc in chunks:
            doc.metadata.update({
                "source": temp_file.name,
                "content_type": "pdf"
            })
        if query=="vector":
            vectorstore=get_vectorstore()
            vectorstore.add_documents(chunks)
            print("Vectorstore created successfully",vectorstore)
            print("Documents added to vectorstore successfully")
        elif query=="graphrag":
            graphtransformer=LLMGraphTransformer(llm=get_llm())
            neo4jgraph=get_neo4h_graph()
            graph_docs=graphtransformer.convert_to_graph_documents(chunks)
            neo4jgraph.add_graph_documents(
                graph_docs,
                baseEntityLabel=True,
                include_source=True
            )
            print("Graph created successfully",graph)
            print("Documents added to graph successfully")
        return {
            "status": "success",
            "filename": file.filename,
        }
    except Exception as e:
        return {"error":str(e)}

@app.get("/rag")
def rag(query: str):
    print("Query",query)
    return graph.invoke({
    "question": query,
    "documents": [],
    "answer": "",
    "next_step": "retrieve",
    "iteration_count": 0,
    "max_iterations": 3,
})

from textsplitters import TextSplitters
from fastapi import FastAPI,File,UploadFile
from loader import Loaders
from vectorstore import get_vectorstore,add_documents
from graph import build_graph
from langchain_qdrant import QdrantVectorStore
import tempfile



app=FastAPI()
graph=build_graph()

@app.post('/upload')
def upload(file:UploadFile=File(...)):
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
        vectorstore=get_vectorstore()
        vectorstore.add_documents(chunks)
        print("Vectorstore created successfully",vectorstore)
        print("Documents added to vectorstore successfully")
        return {
            "status": "success",
            "filename": file.filename,
        }
    except Exception as e:
        return {"error":str(e)}

@app.get("/rag")
def rag():
    return graph.invoke({
    "question": " The field of science education includes",
    "documents": [],
    "answer": "",
    "next_step": "retrieve",
    "iteration_count": 0,
    "max_iterations": 3,
})

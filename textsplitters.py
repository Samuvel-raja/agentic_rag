from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import settings

class TextSplitters:
    def recursive_text_splitter(self,text):
        try:
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=settings.chunk_size,
                chunk_overlap=settings.chunk_overlap,
                separators=["\n\n", "\n", " ", ""]
            )
            chunks=text_splitter.split_documents(text)
            return chunks
        except Exception as e:
            print(e)
            
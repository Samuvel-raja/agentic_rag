from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import WebBaseLoader

class Loaders:
    def pdf_loader(self,file_path):
        return PyPDFLoader(file_path)
    
    def text_loader(self,file_path):
        return TextLoader(file_path)
    
    def directory_loader(self,directory_path):
        return DirectoryLoader(directory_path)
    
    def web_loader(self,url):
        return WebBaseLoader(url)



from pydantic import BaseModel

class AgenticRagState(BaseModel):
    question:str
    iteration_count:int = 0
    max_iterations:int = 3
    documents:list = []
    answer:str = ""
    

from llm import get_llm
from vectorstore import get_vectorstore
from state import AgenticRagState
from prompts import PromptTemplates
from langchain_core.output_parsers import StrOutputParser

class Nodes:
    def retrieve(state: AgenticRagState) -> AgenticRagState:
        print("Retrive Node")
        try:
            vectorstore=get_vectorstore()
            retriever=vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={
                    "k":4,
                    
                }
            )
            retrieved_data=retriever.invoke(state.question)
            print("Retrieved node,Retrieved data")
            state.documents=retrieved_data
            # print("Retrieved node,Documents:",state.documents)
            return state
        except Exception as e:
            print(e)

    def generate_answer(state: AgenticRagState) -> AgenticRagState:
        print("Generate Node")
        try:
            llm=get_llm()   
            question=state.question
            context="\n".join([doc.page_content for doc in state.documents])
            answer_prompt=PromptTemplates.generate_answer_prompt()
            chain=answer_prompt | llm | StrOutputParser()
            response=chain.invoke({"question":question,"context":context})
            print("Response",response,question)
            state.answer=response
            print("Generated node,Answer:",state.answer)
            return state
        except Exception as e:
            print(e)

    def decide_next(state: AgenticRagState) -> AgenticRagState:
        try:
           llm=get_llm()
           question=state.question
           context="\n".join([doc.page_content for doc in state.documents])
           decide_next_prompt=PromptTemplates.decide_next_prompt()
           chain=decide_next_prompt | llm | StrOutputParser()
           response=chain.invoke({"question":question})
           state.answer=response
           print("Decided node,Answer:",state.answer)
           return state
        except Exception as e:
            print(e)
    

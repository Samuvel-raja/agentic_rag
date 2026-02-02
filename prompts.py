from langchain_core.prompts import ChatPromptTemplate

class PromptTemplates:
    def generate_answer_prompt():
       try:
         return ChatPromptTemplate.from_template(
            """
            Answer the question based on the context provided.
            Context: {context}
            Question: {question}

            if u dont have enough context, answer with "I dont have enough context to answer this question".
            Answer: """
        )
       except Exception as e:
            print("Generate answer prompt error:",e)

    def decide_next_prompt():
        try:
            return ChatPromptTemplate.from_template(
                """
                You are decision making agent.
           
                if the question is science based or related to science,
                else if the question is related to chemistry return graph_traversal_retreiver
                else return "generate_answer"
                Question: {question}
                
                """
            )
        except Exception as e:
            print("Decide next prompt error:",e)
from nodes import Nodes
from langgraph.graph import StateGraph,END
from nodes import Nodes
from state import AgenticRagState

class AgenticRagGraph:
    def __init__(self):
        self.graph=StateGraph(AgenticRagState)
    
    def add_nodes(self):
        self.graph.add_node("retrieve",Nodes.retrieve)
        self.graph.add_node("graph_traversal_retreiver",Nodes.graph_traversal_retreiver)
        self.graph.add_node("generate_answer",Nodes.generate_answer)
        self.graph.add_node("decide_next",Nodes.decide_next)

    def entry_node(self):
         self.graph.set_entry_point("decide_next")

    def route_decision(self,state: AgenticRagState):
        print("Route decision node",state)
        if state.iteration_count>=state.max_iterations:
            return "generate_answer"
        elif state.answer == "generate_answer":
            return "generate_answer"
        elif state.answer == "retrieve":
            return "retrieve"
        elif state.answer == "graph_traversal_retreiver":
            return "graph_traversal_retreiver"
        else:
            return "generate_answer"

    def add_edge(self):
        self.graph.add_edge("retrieve","generate_answer")
        self.graph.add_edge("graph_traversal_retreiver","generate_answer")
        self.graph.add_edge("generate_answer",END)
        
    def conditional_edges(self):
        self.graph.add_conditional_edges(
            "decide_next",
            self.route_decision,
            {
                "retrieve":"retrieve",
                "generate_answer":"generate_answer",
                "graph_traversal_retreiver":"graph_traversal_retreiver"
            }
            
        )

    def compile(self):
        return self.graph.compile()
        
    # def add_edges(self):
    #     self.graph.add_edge("retrieve","generate_answer")
    #     self.graph.add_edge("generate_answer","decide_next")
    #     self.graph.add_edge("decide_next","retrieve")

def build_graph():
    agent_graph=AgenticRagGraph()
    agent_graph.add_nodes()
    agent_graph.entry_node()
    agent_graph.conditional_edges()
    agent_graph.add_edge()
    return agent_graph.compile()
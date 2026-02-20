from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBot



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    
    def basic_chatbot_build_graoh(self):
        """Builds a basic chatbot using langgraph"""
        
        self.basic_chatbot_node = BasicChatBot(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def setup_graph(self, usecase: str):
        """Sets up graph basiced on use base"""

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graoh()
            graph = self.graph_builder.compile()
            return graph
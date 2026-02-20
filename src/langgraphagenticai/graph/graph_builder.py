from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBot
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from src.langgraphagenticai.nodes.basic_chatbot_with_tool_node import ChatbotwithToolNode
from langgraph.prebuilt import tools_condition


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
    
            

    def chatbot_with_tools_build_graph(self):
        """Builds a basic chatbot using tools"""

        tools = get_tools()
        tool_node = create_tool_node(tools)


        ##define the llm 
        llm = self.llm

        #define chatbot node
        obj_with_chatbot_wtih_node = ChatbotwithToolNode(llm)
        chatbot_node = obj_with_chatbot_wtih_node.create_chatbot(tools)



        #add nodes and graph 
        

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
        

    def basic_web_search_build_graph(self, usecase:str):
        """build basic web search chatbot"""

        if usecase == "Chatbot with Web":
            self.basic_chatbot_build_graoh()
            graph = self.graph_builder.compile()
            return graph
        
    def setup_graph(self, usecase: str):
        """Sets up graph basiced on use base"""
        self.graph_builder = StateGraph(State)
        
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graoh()
            graph = self.graph_builder.compile()
            return graph
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
            return self.graph_builder.compile()
# from src.langgraphagenticai.state.state import State


# class ChatbotwithToolNode:
#     """Basic chatbot tool implementation"""

#     def __init__(self, model):
#         self.llm = model
    
#     def process(self, state: State) -> dict:
#         """Process input state and give chat response"""

#         user_input = state.messages[-1] if state.messages else ""

#         llm_response = self.llm.invoke([{"role": "user", "content": user_input}])


#         tools_response = f"Tool integeation fro : {user_input}"

#         return {"messages": [llm_response + tools_response]}
    
    
#     def create_chatbot(self, tools):

#         """returns chatbot node information """

#         llm_with_tools = self.llm.bind_tools(tools)

#         def chatbot_node(state:State):

#             """Chatbot logic for processing the input state and returning a response"""

#             return {"messages": [llm_with_tools.invoke.state.messages]}
        
#         return chatbot_node

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.state.state import State


class ChatbotwithToolNode:

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:

        if not state.messages:
            return {"messages": []}

        # Invoke LLM properly
        llm_response = self.llm.invoke(state.messages)

        return {"messages": [llm_response]}

    def create_chatbot(self, tools):

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):

            response = llm_with_tools.invoke(state.messages)

            return {"messages": [response]}

        return chatbot_node
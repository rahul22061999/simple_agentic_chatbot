from src.langgraphagenticai.state.state import State


class BasicChatBot:
    """Basic chatbot logic implementation"""

    def __init__(self, model):
        self.llm = model
    
    def process(self, state: State) -> dict:
        """Process input state and give chat response"""

        return {"messages": self.llm.invoke(state.messages)}
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages
from typing import Annotated, List


class State(BaseModel):
    """Represents the structure of the state used in graph"""

    messages: Annotated[List, add_messages] 

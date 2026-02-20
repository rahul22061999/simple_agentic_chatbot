from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode


def get_tools():
    """Return the list of tools to build in chatbot"""

    tools = [TavilySearch(max_results =2)]
    return tools


def create_tool_node(tools):
    """creates and retuens a tool node for a graph"""


    return ToolNode(tools=tools)
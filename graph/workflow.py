from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver

from llm.Agent import Graph_Agent, StructuredNode
from graph.state import AgentState
from tools.ToolsCollection import tools

memory = InMemorySaver()

Builder = StateGraph(AgentState)

Builder.add_node("Graph_Agent", Graph_Agent)
Builder.add_node("tools", ToolNode(tools))
Builder.add_node("StructuredNode", StructuredNode)

Builder.add_edge(START, "Graph_Agent")

Builder.add_conditional_edges(
    "Graph_Agent",
    tools_condition,
    {
        "tools": "tools",
        "__end__": "StructuredNode"
    }
)

Builder.add_edge("tools", "Graph_Agent")

Builder.add_edge("StructuredNode", END)

FinalAgent = Builder.compile(
    checkpointer=memory
)
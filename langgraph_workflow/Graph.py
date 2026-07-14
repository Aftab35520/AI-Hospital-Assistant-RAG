from langgraph_workflow.Agent import llm_with_tools
from langgraph.graph import StateGraph,START,END
from langgraph_workflow.AgentState import AgentState
from langgraph_workflow.memory import memory
from langgraph.prebuilt import tools_condition,ToolNode
from tools.tools_collection import tools


graph=StateGraph(AgentState)
graph.add_node("llm_with_tools",llm_with_tools)
graph.add_node("tools",ToolNode(tools))
graph.add_edge(START,"llm_with_tools")
graph.add_conditional_edges(
    "llm_with_tools",
    tools_condition
)
graph.add_edge("tools","llm_with_tools")
graph=graph.compile(checkpointer=memory)




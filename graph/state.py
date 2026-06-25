from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages:Annotated[list,add_messages]
    patient_id:str
    structured_response: dict
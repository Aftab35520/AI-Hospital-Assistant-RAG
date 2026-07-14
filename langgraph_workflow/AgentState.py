
from typing import Annotated,TypedDict,Optional
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages:Annotated[list,add_messages]
    USERID:Optional[str]


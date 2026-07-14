

from langgraph_workflow.Graph import graph
def chatRoute(query):
    config={"configurable":{"thread_id":query["userId"]}}
    llm_response=graph.invoke({"messages":query["message"],"USERID":query["userId"]},config=config)
    return llm_response['messages'][-1].content

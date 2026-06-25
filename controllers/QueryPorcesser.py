from graph.workflow import FinalAgent

from langchain_core.messages import HumanMessage

def QueryProcesser(query,patient_id):
    config={'configurable':{'thread_id':patient_id}}
    
    response = FinalAgent.invoke(
    {
        "messages": [HumanMessage(content=query)],
        "patient_id": patient_id,
    },
    config=config,
)
    # return response["messages"][-1].content
    return response['structured_response']
  

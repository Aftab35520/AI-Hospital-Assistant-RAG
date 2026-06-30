from llm.model import Chat_Model
from graph.state import AgentState
from tools.ToolsCollection import tools
from langchain_core.messages import SystemMessage
from Schema.messageschema import ChatResponseFormat

Chat_Model_with_tools=Chat_Model.bind_tools(tools)
from datetime import datetime

now = datetime.now()

current_date = now.date()
current_time = now.time()

def Graph_Agent(state:AgentState):
    messages = [
     SystemMessage(
    content=f"""
# Hospital Assistant - System Prompt

## Role
You are a professional hospital assistant. Only help with:
- Finding doctors
- Booking appointments
- Hospital information

Always use available tools to retrieve data.

## Critical Rules
- Never invent, assume, or guess any information.
- Always retrieve doctor, patient, department, availability, and appointment data using tools.
- Never use placeholder values.
- Never provide medical diagnosis or treatment advice.
- If a request is unrelated to hospitals, reply:
  "I specialize in hospital-related assistance. Please ask about doctors, appointments, or hospital services."

## Doctor Search
- Recommend only doctors returned by tools.
- Maximum 3 doctors.
- Include:
  - Name
  - Specialization
  - Availability (if available)
  - Brief bio (if available)

If no doctors are found, offer to:
1. Search another specialization
2. Check another date
3. Suggest another department

## Appointment Booking

Required information:
- Doctor (from tool only)
- Appointment date (YYYY-MM-DD)
- Appointment time (HH:MM, 24-hour)
- Patient name

If multiple fields are missing, ask for all missing fields in one message.

Before booking, validate:
- Date format is YYYY-MM-DD
- Date is not in the past
- Date is within allowed booking range (3 months if applicable)
- Time format is HH:MM (24-hour)
- Time is between 08:00 and 20:00
- Doctor is available (check tool)
- All required fields are present

## Confirmation (Mandatory)

Before booking, show a summary and ask:

"Please confirm these details. Reply YES to confirm or NO to cancel."

Proceed only if the user replies:
YES, Y, CONFIRM, OK, SURE, or CORRECT.

If NO/CANCEL/STOP, cancel and ask whether they want to modify.

If unclear, ask again.

Never call the booking tool before explicit confirmation.

## Forbidden
Never:
- Book without confirmation
- Ask for patient ID (use existing state if available)
- Guess dates, times, doctors, departments, or availability
- Use placeholder values
- Skip validation
- Recommend more than 3 doctors
- Discuss non-hospital topics
- Make diagnoses or medical recommendations

## Principles
- Accuracy over assumptions
- Tool data only
- Validate before booking
- Keep responses clear, concise, and professional
- Ask for clarification whenever information is missing
"""
)
    ] + state["messages"]
    return {'messages':[Chat_Model_with_tools.invoke(messages)]}





FormatterLLM = Chat_Model.with_structured_output(
    ChatResponseFormat,
    method="json_mode"
)


def StructuredNode(state: AgentState):

    last_message = state["messages"][-1]

    structured_response = FormatterLLM.invoke(
        f"""
Convert the following hospital assistant response into the schema.

Schema:
- type: "text" or "selector"
- message: string
- selections: array


Rules:
- Use type="selector" when the user must choose from options.
- Use type="text" for normal replies.
- If doctor options, date options, or time slots are present,
  place them inside selections.
{{
  "type": "text" | "selector",
  "message": "string",
  "selections": []
}}
STRICT RULES:

1. Exactly one mode must be used.

TEXT MODE:
- type = "text"
- message contains the entire response
- selections MUST be []

SELECTOR MODE:
- type = "selector"
- message contains only the selection instruction
- selections contains ALL selectable options
- Do NOT put option details inside message
- write message about options in message


2. Never return both a detailed message and selections.
3. If selections is not empty, type MUST be "selector".
4. If type is "selector", all option data must be inside selections.
5. If type is "text", selections must be [].
6. Return only valid structured output.



Response:

{last_message.content}
"""
    )

    return {
        "structured_response": structured_response.model_dump()
    }
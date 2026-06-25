from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
Chat_Model=ChatGroq(
    groq_api_key=os.getenv("ApiKey"),
    model="llama-3.3-70b-versatile"
)




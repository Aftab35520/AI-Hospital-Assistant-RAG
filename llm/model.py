from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI

Chat_Model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("AZURE_API_KEY"),
    azure_deployment=os.getenv("AZURE_DEPLOYMENT"),
    api_version="2024-10-21",
  
    temperature=0
)
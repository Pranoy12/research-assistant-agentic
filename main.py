from tools import search_web, create_md_file
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

# Importing tools
tools = [
    search_web,
    create_md_file
]

# Configure LLM
GEMINI_INSTRUCTION = """
    You are a Research Assistant. 
    Your job is to search for 3 research papers on the topic given by the user and summarise them.
    Atlast write the summary into a .md file with each research paper title and its summary.
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)
# llm_with_tools = llm.bind_tools(tools)
agent_executor = create_agent(llm, tools) 

# Gettting User Input
user_query = input("You: ")
response = agent_executor.invoke({"messages": [("system", GEMINI_INSTRUCTION),("user", user_query)]})
print(response)

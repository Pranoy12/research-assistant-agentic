from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()

# Tool 1: Search
def search_web(search_str: str) -> object:
    """
    Searches the web on the given input search_str.
    Returns the TITLE and CONTENT of the search result as an object with structure {TITLE, CONTENT}.
    """
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Search the web
    response = tavily.search(query=search_str, search_depth="advanced")
    # print(response['results'][0]['content'])
    title = response['results'][0]['title']
    content = response['results'][0]['content']
    return({title, content})

# Tool 2: Writer
def create_md_file(title: str, content: str):
    """
    Creates a basic Markdown file with a title and content.
    """
    filename='summary.md'
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(content)

# # Usage
# create_md_file("Project Status", "This is a **bold** update.")

# res = search_web('AGENTIC AI')
# print(res)


import os

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import dotenv

dotenv.load_dotenv()
@tool
def search(query: str):
    """Call to surf the web."""
    # This is a placeholder, but don't tell the LLM that...
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


tools = [search]
model = ChatOpenAI(model="gpt-4o", openai_api_key=os.environ["OPENROUTER_API_KEY"], openai_api_base="https://openrouter.ai/api/v1")
checkpointer = MemorySaver()

app = create_react_agent(
    model,
    tools,
    checkpointer=checkpointer,
)

final_state_1 = app.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in egypt"}]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state_1["messages"][-1].content)

final_state_2 = app.invoke(
    {"messages": [{"role": "user", "content": "what about ny"}]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state_2["messages"][-1].content)

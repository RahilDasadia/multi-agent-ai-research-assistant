from app.llm.ollama_client import OllamaClient


class ToolSelector:

    def __init__(self):
        self.llm = OllamaClient(model="llama3")

    def decide_tool(self, query: str):

        prompt = f"""
You are an assistant that decides whether a tool should be used.

Available tools:

calculator → for math calculations
time → for current system time

User Query:
{query}

Respond ONLY like this:

TOOL: calculator
INPUT: 25*8

OR

TOOL: time
INPUT: none

OR

TOOL: NONE
INPUT: none
"""

        response = self.llm.generate(prompt)

        return response
from app.agents.base import BaseAgent
from app.agents.schemas import SharedState, AgentOutput

from app.llm.ollama_client import OllamaClient
from app.rag.retriever import Retriever
from app.tools.tool_manager import ToolManager


class ResearcherAgent(BaseAgent):

    retriever_loaded = False

    def __init__(self):

        super().__init__(
            name="Researcher",
            role="Information Gathering Specialist",
            description="Researches topics using LLM knowledge, document retrieval, and available tools."
        )

        self.llm = OllamaClient(model="tinyLlama")  # Use a smaller model for research to save resources

        self.retriever = Retriever()

        self.tools = ToolManager()

        # Load documents only once
        if not ResearcherAgent.retriever_loaded:
            try:
                self.retriever.ingest_documents()
                ResearcherAgent.retriever_loaded = True
            except Exception as e:
                print("RAG ingestion error:", e)

    def generate(self, state: SharedState) -> AgentOutput:

        task = state.original_task

        # ---------- TOOL CHECK ----------

        tool_result = self.tools.try_use_tool(task)

        if tool_result:
            return AgentOutput(
                agent=self.name,
                thought="Used tool to answer the query.",
                result=tool_result,
                confidence=0.99,
                recommended_next_agent="Writer",
                terminate=False
            )

        # ---------- RAG RETRIEVAL ----------

        retrieved_context = ""

        try:
            retrieved_context = self.retriever.retrieve(task)
        except Exception as e:
            print("RAG retrieval error:", e)

        # ---------- CONVERSATION HISTORY ----------

        history = "\n".join(state.conversation_history)

        # ---------- LLM PROMPT ----------

        prompt = f"""
You are a professional research assistant.

Conversation History:
{history}

User Query:
{task}

Relevant Knowledge From Documents:
{retrieved_context}

Instructions:
- Provide clear factual information
- Use bullet points
- Do not simulate conversation
- Do not write "AI:" or "User:"
- Only output the research findings
"""

        try:

            llm_response = self.llm.generate(prompt)

            # DEBUG: see actual LLM output
            print("LLM RESPONSE:", llm_response)

            return AgentOutput(
                agent=self.name,
                thought="Retrieved knowledge and generated research insights.",
                result=llm_response,
                confidence=0.92,
                recommended_next_agent="Analyst",
                terminate=False
            )

        except Exception as e:

            return AgentOutput(
                agent=self.name,
                thought="Error occurred during research.",
                result=str(e),
                confidence=0.0,
                recommended_next_agent=None,
                terminate=True
            )
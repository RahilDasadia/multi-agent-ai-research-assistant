from .base import BaseAgent
from .schemas import SharedState, AgentOutput
from app.llm.ollama_client import OllamaClient


class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analyst",
            role="Insight Extraction Specialist",
            description="Analyzes research findings and extracts structured insights."
        )
        self.llm = OllamaClient(model="llama3")

    def generate(self, state: SharedState) -> AgentOutput:
        if not state.intermediate_results:
            return AgentOutput(
                agent=self.name,
                thought="No research data available to analyze.",
                result="No research data available.",
                confidence=0.0,
                recommended_next_agent=None,
                terminate=True
            )

        research_content = state.intermediate_results[-1]

        prompt = f"""
You are a professional data analyst.

You have received the following research content:

{research_content}

Your job:
- Extract the most important insights
- Identify patterns or implications
- Remove redundancy
- Structure the output clearly
- Provide concise analytical commentary

Focus on analysis, not repeating raw research.
"""

        try:
            analysis_result = self.llm.generate(prompt)

            return AgentOutput(
                agent=self.name,
                thought="I analyzed the research content and extracted key insights.",
                result=analysis_result,
                confidence=0.92,
                recommended_next_agent="Writer",
                terminate=False
            )

        except Exception as e:
            return AgentOutput(
                agent=self.name,
                thought="An error occurred during analysis.",
                result=str(e),
                confidence=0.0,
                recommended_next_agent=None,
                terminate=True
            )
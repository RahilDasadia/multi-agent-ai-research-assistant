from .base import BaseAgent
from .schemas import SharedState, AgentOutput
from app.llm.ollama_client import OllamaClient


class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writer",
            role="Professional Report Generator",
            description="Transforms analytical insights into a polished professional report."
        )
        self.llm = OllamaClient(model="tinyLlama")  # Use a smaller model for writing to save resources

    def generate(self, state: SharedState) -> AgentOutput:
        if not state.intermediate_results:
            return AgentOutput(
                agent=self.name,
                thought="No analysis available to generate report.",
                result="No analysis available.",
                confidence=0.0,
                recommended_next_agent=None,
                terminate=True
            )

        analysis_content = state.intermediate_results[-1]

        prompt = f"""
You are a professional report writer.

You have received the following analytical insights:

{analysis_content}

Your task:
- Convert this into a polished, structured professional report
- Add a strong executive summary at the top
- Ensure logical flow
- Improve clarity and readability
- Use professional tone
- Keep it well formatted with headings

Produce a final comprehensive report.
"""

        try:
            final_report = self.llm.generate(prompt)

            return AgentOutput(
                agent=self.name,
                thought="I transformed the analytical insights into a polished professional report.",
                result=final_report,
                confidence=0.95,
                recommended_next_agent=None,
                terminate=True
            )

        except Exception as e:
            return AgentOutput(
                agent=self.name,
                thought="An error occurred during report generation.",
                result=str(e),
                confidence=0.0,
                recommended_next_agent=None,
                terminate=True
            )
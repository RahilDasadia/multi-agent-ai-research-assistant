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
Below is analytical content:

{analysis_content}

Rewrite it as a **clean professional report**.

Rules:
- DO NOT include "AI:" or "User:"
- DO NOT simulate conversation
- DO NOT include dialogue
- ONLY output the final report
- Start directly with the report

Structure:

Executive Summary

Key Insights

Detailed Explanation

Conclusion
"""

        try:
            final_report = self.llm.generate(prompt)
            final_report = final_report.replace("AI:", "").replace("User:", "")

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
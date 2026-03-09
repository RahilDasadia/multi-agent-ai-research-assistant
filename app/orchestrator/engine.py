from typing import Dict
from datetime import datetime

from app.agents.schemas import SharedState, AgentOutput
from app.agents.researcher import ResearcherAgent
from app.agents.analyst import AnalystAgent
from app.agents.writer import WriterAgent

from app.db.session import SessionLocal
from app.db import models


class Orchestrator:

    def __init__(self):
        self.agents: Dict[str, object] = {
            "Researcher": ResearcherAgent(),
            "Analyst": AnalystAgent(),
            "Writer": WriterAgent(),
        }

    def run(self, task: str):

        db = SessionLocal()

        # Create Task
        db_task = models.Task(original_task=task)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        # Create Run
        db_run = models.Run(task_id=db_task.id, status="running")
        db.add(db_run)
        db.commit()
        db.refresh(db_run)

        state = SharedState(
            original_task=task,
            conversation_history=[task]
        )

        current_agent_name = "Researcher"

        max_iterations = 10
        iteration = 0

        while iteration < max_iterations:

            iteration += 1

            agent = self.agents.get(current_agent_name)

            if not agent:
                break

            output: AgentOutput = agent.generate(state)

            # Save agent message to DB
            db_message = models.AgentMessage(
                run_id=db_run.id,
                agent_name=output.agent,
                thought=output.thought,
                result=output.result,
                confidence=output.confidence
            )

            db.add(db_message)
            db.commit()

            # Update shared state
            state.messages.append(output.result)
            state.conversation_history.append(output.result)
            state.intermediate_results.append(output.result)

            # Check termination
            if output.terminate:
                state.final_output = output.result

                db_run.status = "completed"
                db_run.finished_at = datetime.utcnow()

                db.commit()
                break

            # ---------- SMART AGENT ROUTING ----------

            # If next agent suggested is Analyst, check if task is complex
            if output.recommended_next_agent == "Analyst":

                complex_keywords = [
                    "compare",
                    "analysis",
                    "analyze",
                    "pros",
                    "cons",
                    "advantages",
                    "disadvantages",
                    "impact",
                    "difference"
                ]

                is_complex = any(word in task.lower() for word in complex_keywords)

                if is_complex:
                    current_agent_name = "Analyst"
                else:
                    # Skip Analyst → go directly to Writer
                    current_agent_name = "Writer"

            else:
                current_agent_name = output.recommended_next_agent

        db.close()

        return state.final_output
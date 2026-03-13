from typing import List, Optional
from pydantic import BaseModel


class AgentOutput(BaseModel):
    agent: str
    thought: str
    result: str
    confidence: float
    recommended_next_agent: Optional[str] = None
    terminate: bool = False


class SharedState(BaseModel):

    original_task: str

    messages: List[str] = []

    intermediate_results: List[str] = []

    conversation_history: List[str] = []

    final_output: Optional[str] = None
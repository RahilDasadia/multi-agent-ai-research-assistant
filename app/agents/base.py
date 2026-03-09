from abc import ABC, abstractmethod
from .schemas import SharedState, AgentOutput


class BaseAgent(ABC):
    def __init__(self, name: str, role: str, description: str):
        self.name = name
        self.role = role
        self.description = description

    @abstractmethod
    def generate(self, state: SharedState) -> AgentOutput:
        """
        Each agent must implement this method.
        It takes the shared state and returns structured AgentOutput.
        """
        pass
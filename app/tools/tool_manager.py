from app.tools.calculator import CalculatorTool
from app.tools.system_tool import SystemTool


class ToolManager:

    def __init__(self):

        self.calculator = CalculatorTool()
        self.system_tool = SystemTool()

    def use_tool(self, tool_name: str, input_value: str):

        if tool_name == "calculator":
            return self.calculator.calculate(input_value)

        if tool_name == "time":
            return self.system_tool.current_time()

        return "Tool not found"
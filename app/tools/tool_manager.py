class ToolManager:

    def try_use_tool(self, task: str):

        task = task.lower()

        # Calculator detection
        if any(op in task for op in ["+", "-", "*", "/"]):
            try:
                result = eval(task)
                return f"Calculation Result: {result}"
            except:
                return None

        # Time detection
        if "time" in task or "current time" in task:
            from datetime import datetime
            return f"Current system time: {datetime.now()}"

        return None
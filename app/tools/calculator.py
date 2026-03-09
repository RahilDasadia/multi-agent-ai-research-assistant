class CalculatorTool:

    def calculate(self, expression: str):

        try:
            result = eval(expression, {"__builtins__": {}})
            return str(result)

        except Exception:
            return "Invalid calculation"
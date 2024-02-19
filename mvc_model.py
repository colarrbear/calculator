class CalculatorModel:
    def __init__(self):
        self.current_expression = ""
        self.stack = []
        self.operator = {'+', '-', '*', '/', '^', '(', ')', '%'}

    def get_history(self):
        return self.stack

    def add_to_history(self, expression, result):
        self.stack.append((expression, result))
        print(self.stack)

    def clear(self):
        self.current_expression = ""
        self.stack = []

    def clear_expression(self):
        self.current_expression = ""

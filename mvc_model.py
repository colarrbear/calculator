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


    # def append_digit(self, digit):
    #     self.current_expression += digit
    #
    # def append_decimal(self):
    #     if '.' not in self.current_expression:
    #         self.current_expression += '.'

    # def append_operator(self, operator):
    #     if self.current_expression:
    #         self.stack.append(self.current_expression)
    #         self.current_expression = ""
    #         self.stack.append(operator)

    # def evaluate_expression(self):
    #     try:
    #         current = self.current_expression
    #         result = eval(current.replace('^', '**').replace('ln','math.log'))
    #         self.stack.append((self.current_expression, result))
    #         return str(result)
    #     except ZeroDivisionError:
    #         return "Error"
    #     except Exception as e:
    #         # print(f'Error: {e}')
    #         return "Error"

        # if not self.stack:
        #     print('No expression to evaluate')
        #     raise ValueError
        # operand2 = float(self.stack.pop())
        # operator = self.stack.pop()
        # operand1 = float(self.stack.pop())
        # result = self.operators[operator](operand1, operand2)
        # self.stack.append(str(result))
        # return result

    # def add(self, a, b):
    #     return a + b
    #
    # def subtract(self, a, b):
    #     return a - b
    #
    # def multiply(self, a, b):
    #     return a * b
    #
    # def divide(self, a, b):
    #     if b == 0:
    #         print('Division by zero')
    #         raise ValueError
    #     return a / b

    # def power(self, a, b):
    #     return a ** b

    def clear(self):
        self.current_expression = ""
        self.stack = []

    # def del_last_element(self):
    #     self.current_expression = self.current_expression[:-1]
    #     if self.current_expression == "":
    #         self.current_expression = "0"
    #     return self.current_expression

    def clear_expression(self):
        self.current_expression = ""

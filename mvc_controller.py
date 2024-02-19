from mvc_model import CalculatorModel
from mvc_view import CalculatorView
import math

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def handler_press(self, value):
        print('value:', value)
        if value == '=':
            result = self.model.evaluate_expression()
            if result != "Error":
                self.model.stack.append((self.model.current_expression, result))
                self.view.clear_display()
                self.view.update_display(result)
                self.model.clear()
            else:
                self.view.set_display_colour("red")
                self.view.bell()  # add sound
        elif value in ('(', ')'):
            self.handle_parentheses(value)
        elif value == 'mod':
            self.handle_modulus()
        elif value == 'DEL':
            self.handle_delete()
        elif value == 'CLR':
            self.handle_clear()
        elif value in ('exp', 'ln', 'log10', 'log2', 'sqrt'):
            self.handle_function(value)
        else:
            self.handle_digit_or_operator(value)
            # self.view.update_display(self.model.current_expression)

    def handle_parentheses(self, value):
        last_char = self.model.current_expression[-1] if self.model.current_expression else ''
        if value == '(':
            if not self.model.current_expression or last_char in ('+', '-', '*', '/', '^', '('):
                self.model.current_expression += '('
                self.view.update_display(value)
            elif last_char.isdigit() or last_char == ')':
                self.model.current_expression += '*' + value
                self.view.update_display('*' + value)
        elif value == ')':
            if last_char.isdigit() or last_char == ')':
                self.model.current_expression += value
                self.view.update_display(value)

    def handle_modulus(self):
        self.model.current_expression += '%'
        self.view.update_display('%')

    def handle_delete(self):
        self.model.current_expression = self.model.current_expression[:-1]
        self.view.clear_display()
        self.view.update_display(self.model.current_expression)

    def handle_clear(self):
        self.model.clear_expression()
        self.view.clear_display()

    # def handle_function(self, value):
    #     last_char = self.model.current_expression[-1] if self.model.current_expression else ''
    #
    #     if last_char.isdigit() or last_char == ')':
    #         self.model.current_expression += '*' + value + '('
    #     else:
    #         self.model.current_expression += value + '('
    #
    #     self.view.update_display(value + '(')

        # old
        # if self.model.current_expression.endswith(('+', '-', '*', '/', '^')):
        #     self.model.current_expression += value + '('
        # elif self.model.current_expression:
        #     self.model.current_expression += '*' + value + '('
        # else:
        #     self.model.current_expression += value + '('
        # self.view.update_display(value + '(')

    def handle_function(self, value):
        last_char = self.model.current_expression[-1] if self.model.current_expression else ''
        print('last char:', last_char)
        if last_char.isdigit() or last_char == ')':
            print(value)
            if value == 'exp':
                self.model.current_expression += '*' + 'math.exp' + '('
            elif value == 'ln':
                self.model.current_expression += 'math.log' + '('
                print('current expression:', self.model.current_expression)
            elif value == 'log10':
                self.model.current_expression += '*' + 'math.log10' + '('
            elif value == 'log2':
                self.model.current_expression += '*' + 'math.log2' + '('
            # elif value == 'sqrt':
            #     self.model.current_expression += '*' + 'math.sqrt' + '('
        else:
            if value == 'exp':
                self.model.current_expression += 'math.exp' + '('
            elif value == 'ln':
                self.model.current_expression += 'math.log' + '('
            elif value == 'log10':
                self.model.current_expression += 'math.log10' + '('
            elif value == 'log2':
                self.model.current_expression += 'math.log2' + '('
            elif value == 'sqrt':
                self.model.current_expression += 'math.sqrt' + '('

        self.view.update_display(value + '(')

    def handle_digit_or_operator(self, value):
        last_char = self.model.current_expression[
            -1] if self.model.current_expression else ''
        if value.isdigit():
            if last_char == ')':
                self.model.current_expression += '*' + value
                self.view.update_display('*' + value)
            else:
                self.model.current_expression += value
                self.view.update_display(value)
        elif value in ('+', '-', '*', '/'):
            if last_char.isdigit() or last_char == ')':
                self.model.current_expression += value
                self.view.update_display(value)
            elif last_char in ('+', '-', '*', '/', '^'):
                self.model.current_expression = self.model.current_expression[
                                                :-1] + value
                self.view.clear_display()
                self.view.update_display(value)
        else:
            if last_char.isdigit() or last_char == ')':
                self.model.current_expression += '*' + value
                self.view.update_display('*' + value)

    def run(self):
        self.view.mainloop()


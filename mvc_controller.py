from mvc_model import CalculatorModel
from mvc_view import CalculatorView
from math import *


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def handler_keypad_press(self, value):
        if value == '=':
            # print('2')
            # print(self.view.display.get(1.0, "end-1c"))
            result = self.evaluate_expression(self.view.display.get(1.0, "end-1c"))
            # print(result)
            if result != "Error":
                # self.model.stack.append((self.model.current_expression, result))
                # self.model.add_to_history('', '')
                self.view.clear_display()
                # print('value:', value)
                # self.model.add_to_history(self.model.current_expression, result)
                self.view.update_display(result)

                self.model.clear()
                # self.model.add_to_history(self.model.current_expression, value)
            else:
                # foreground need to be fix
                self.view.change_text_colour('red')
                # self.view.set_display_colour("red")
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

    def evaluate_expression(self, txt):
        try:
            # current = self.model.current_expression
            result = eval(txt.replace('^', '**').replace('mod', '%').replace('ln','log'))
            # print('result:', result)
            self.model.add_to_history(txt, result)
            return str(result)
        except ZeroDivisionError:
            # make the display red
            # print('Division by zero')
            return "Error"
        except Exception as e:
            # print(f'Error: {e}')
            return "Error"

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
        # print('last char:', last_char)
        if last_char.isdigit() or last_char == ')':
            # print(value)
            if value == 'exp':
                self.model.current_expression += '*' + 'math.exp' + '('
            elif value == 'ln':
                self.model.current_expression += 'math.log' + '('
                # print('current expression:', self.model.current_expression)
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
                self.model.current_expression += value
                self.view.update_display(value)

    def run(self):
        self.view.mainloop()

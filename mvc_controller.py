# class CalculatorController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#         # Bind view events to controller methods
#         self.view.keypad.bind('<Button-1>', self.handle_keypad_press)
#
#     def handle_keypad_press(self, event_or_key):
#         if isinstance(event_or_key, str):
#             key = event_or_key
#         else:
#             button = event_or_key.widget
#             key = button['text']
#
#         if key in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
#             self.model.append_digit(key)
#             self.view.display_text(self.model.current_expression)
#         elif key == '.':
#             self.model.append_decimal()
#             self.view.display_text(self.model.current_expression)
#         elif key in ('+', '-', '*', '/', '^'):
#             self.model.append_operator(key)
#             self.view.display_text(self.model.current_expression)
#         elif key == '=':
#             try:
#                 result = self.model.evaluate_expression()
#                 self.view.display_text(result)
#                 self.model.clear()  # Clear after successful evaluation
#             except ValueError as e:
#                 self.view.display_error(f"Error: {e}")
#         # else:
#     # Handle other keys (C, etc.)

import math
from mvc_model import CalculatorModel
from mvc_view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def on_button_click(self, value):
        if value == '=':
            result = self.model.evaluate_expression()
            if result != "Error":
                self.model.stack.append((self.model.current_expression, result))
            else:
                self.view.set_display_colour("red")
                return
            self.model.clear()
            self.view.update_display(result)
            if result != "Error":
                self.model.clear_expression()
        elif value == '()':
            last_char = self.model.current_expression[-1] if self.model.current_expression else ''
            if last_char in ('+', '-', '*', '/', '^', '(') or last_char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                self.model.current_expression += '('
                self.view.update_display(')')
            elif last_char == ')':
                self.model.current_expression += ')'
                self.view.update_display(')')
            else:
                self.model.current_expression += '('
                self.view.update_display('(')
        elif value == 'mod':
            self.model.current_expression += '%'
            self.view.update_display('%')
        elif value == 'DEL':
            self.model.current_expression = self.model.current_expression[:-1]
            self.model.clear()
            self.view.update_display(self.model.current_expression)
        elif value == 'CLR':
            self.model.clear_expression()
            self.model.clear()
        elif value in ('exp', 'ln', 'log10', 'log2', 'sqrt'):
            if self.model.current_expression.endswith(('+', '-', '*', '/', '^')):
                self.model.current_expression += value + '('
            elif self.model.current_expression:
                self.model.current_expression += '*' + value + '('
            else:
                self.model.current_expression += value + '('
            self.view.update_display(value + '(')
        else:
            if self.model.current_expression.endswith(')'):
                self.model.current_expression += '*' + value
            else:
                self.model.current_expression += value
            self.view.update_display(value)

    def run(self):
        self.view.mainloop()

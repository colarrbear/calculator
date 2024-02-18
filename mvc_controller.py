"""controller module for the calculator app"""


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind view events to controller methods
        self.view.keypad.bind('<Button-1>', self.handle_keypad_press)
        self.view.combobox_function.bind('<<ComboboxSelected>>', lambda event: self.handle_function_combobox)
        self.view.operator_pad.bind('<Button-1>', lambda event: self.handle_operator_button(event))

    # from mvc_view.py
    # def handle_keypad_press(self, event_or_key):
    #     if isinstance(event_or_key, str):
    #         key = event_or_key
    #     else:
    #         button = event_or_key.widget
    #         key = button['text']
    #
    #     value = key
    #
    #     if value == '=':
    #         try:
    #             expression = self.display.get('1.0', 'end-1c')
    #             result = eval(expression.replace("^", "**"))
    #             self.display.configure(state='normal')
    #             self.display.delete('1.0', tk.END)
    #             self.display.insert(tk.END, str(result), "right")
    #             self.display.configure(state='disabled')
    #         except Exception as e:
    #             print("Error", e)
    #     else:
    #         self.display.configure(state='normal')
    #         self.display.insert(tk.END, value, "right")
    #         self.display.configure(state='disabled')

    def handle_keypad_press(self, event_or_key):
        if isinstance(event_or_key, str):
            key = event_or_key
        else:
            button = event_or_key.widget
            key = button['text']

        try:
            if key in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                self.model.append_digit(key)
                # self.view.display_text(self.model.current_expression)
            # elif key == '.':
            #     self.model.append_decimal()
            #     # self.view.display_text(self.model.current_expression)
            # elif key in ('+', '-', '*', '/', '^'):
            #     self.model.append_operator(key)
            #     # self.view.display_text(self.model.current_expression)
            # elif key == '=':
            #     try:
            #         result = self.model.evaluate_expression()
            #         self.view.display_text(result)
            #         self.model.clear()  # Clear after successful evaluation
            #     except ValueError as e:
            #         self.view.display_error(f"Error: {e}")
            # elif key == 'CLR':
            #     self.model.clear()
                # self.view.display_text(self.model.current_expression)
            else:
                # self.view.display_error(f"Unknown key: {key}")
                # raise ValueError(f"Unknown key: {key}")
                raise ValueError(f"Invalid value: {key}")

            self.view.display_text(self.model.current_expression)
            # Handle other keys (C, etc.)

        except ValueError as e:
            self.view.display_error(f"Error: {e}")

    def handle_function_combobox(self):
        try:
            function = self.combobox_function.get()
            self.model.append_function(function)
            self.view.display_text(self.model.current_expression)
        except ValueError as e:
            self.view.display_error(f"Error: {e}")

    def handle_operator_button(self, event):
        button = event.widget
        key = button['text']

        try:
            if key in ('+', '-', '*', '/', '^'):
                self.model.append_operator(key)
            # elif key == '=':
            #     try:
            #         result = self.model.evaluate_expression()
            #         self.view.display_text(result)
            #         self.model.clear()  # Clear after successful evaluation
            #     except ValueError as e:
            #         self.view.display_error(f"Error: {e}")
            else:
                raise ValueError(f"Unknown operator: {key}")

            self.view.display_text(self.model.current_expression)

        except ValueError as e:
            self.view.display_error(f"Error: {e}")


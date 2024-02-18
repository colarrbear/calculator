# """ui for calculator"""
# import tkinter as tk
# from tkinter import ttk
# from keypad import Keypad
# from mvc_controller import CalculatorController
#
#
# class CalculatorUI(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Calculator')
#         self.display = None
#         self.keypad = None
#         self.init_components()
#
#     # def init_components(self):
#     #     self.display = tk.Text(self, height=2, state='disabled',
#     #                            font=('Sarabun', 16), padx=12, pady=12)
#     #     self.display.tag_configure("right", justify="right")
#     #     self.display.grid(row=0, column=0, columnspan=4, sticky='news')
#     #
#     #     self.keypad = Keypad(self,keynames=['7', '8', '9', '4', '5', '6', '1', '2','3', ' ', '0', '.'], columns=3)
#     #     # self.keypad = Keypad(self,keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
#     #     self.keypad.grid(row=1, column=0, sticky='news')
#     #
#     #     operators = self.make_operator_pad()
#     #     operators.grid(row=1, column=1, sticky='news')
#     #
#     #     self.rowconfigure(0, weight=1)  # row 0 is the display
#     #     # self.rowconfigure(1, weight=1)  # row 1 is the keypad
#     #     self.rowconfigure(1, weight=1)  # test
#     #     # self.rowconfigure(2, weight=0)  # row 2 is the operators
#     #
#     #     self.columnconfigure(0, weight=1)  # column 0 is the keypad
#     #     self.columnconfigure(1, weight=1)  # column 1 is the operators
#     #     # self.rowconfigure(1, weight=0)
#     #     # self.rowconfigure(2, weight=1)
#     #
#     #
#     #     # self.keypad.bind('<Button-1>', self.handle_keypad_press)
#     #     self.keypad.bind('<Button-1>', CalculatorController.handle_keypad_press)
#     #
#     #     # combobox = ttk.Combobox(frame_operators,values=['exp', 'ln', 'log base 10', 'log2','sqrt'])
#     #     # combobox.set('Select Function')
#     #     # combobox.grid(row=row, column=col, **options)
#     #     self.make_combobox_function()
#     #     self.rowconfigure(2, weight=1)
#     def init_components(self):
#         self.display = tk.Text(self, height=2, state='disabled',
#                                font=('Sarabun', 16), padx=12, pady=12)
#         self.display.tag_configure("right", justify="right")
#         self.display.grid(row=0, column=0, columnspan=4, sticky='news')
#
#         self.keypad = Keypad(self,
#                              keynames=['7', '8', '9', '4', '5', '6', '1', '2',
#                                        '3', ' ', '0', '.'], columns=3)
#         self.keypad.grid(row=1, column=0, sticky='news')
#
#         operator_pad = self.make_operator_pad()
#         operator_pad.grid(row=1, column=1, sticky='news')
#
#         command_pad = self.make_command_pad()
#         command_pad.grid(row=0, column=2, rowspan=2, sticky='news')
#
#         self.rowconfigure(0, weight=1)  # row 0 is the display
#         self.rowconfigure(1, weight=1)  # row 1 is the keypad
#         self.rowconfigure(2, weight=0)  # row 2 is the operators and commands
#
#         self.columnconfigure(0, weight=1)  # column 0 is the keypad
#         self.columnconfigure(1, weight=1)  # column 1 is the operators
#         self.columnconfigure(2, weight=1)  # column 2 is the commands
#
#         self.keypad.bind('<Button-1>', CalculatorController.handle_keypad_press)
#
#     def make_combobox_function(self):
#         functionvar = tk.StringVar()
#         function = ttk.Combobox(self, textvariable=functionvar)
#         function['values'] = ('exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan')
#         function.grid(row=1, column=0, sticky='news')
#
#     # def make_operator_pad(self) -> tk.Frame:
#     #     frame_operators = tk.Frame(self)
#     #     operator = ['*', '/', '+', '-', '^', '(', ')', 'mod', 'CLR', 'DEL', '=']
#     #     # options = {'sticky': 'NWES', 'padx': 1, 'pady': 1}
#     #     options = {'padx': 1, 'pady': 1}
#     #
#     #     num_col = 2
#     #     num_rows = len(operator) // num_col + 1
#     #
#     #     # self.rowconfigure(2, weight=0)
#     #
#     #     for i, key in enumerate(operator):
#     #         row = i % num_rows
#     #         col = i // num_rows
#     #
#     #         rowspan = 2 if key == '=' else 1
#     #
#     #         button = tk.Button(frame_operators, text=key, command=lambda
#     #             key=key: CalculatorController.handle_keypad_press(key, self))
#     #         button.grid(row=row, column=col, rowspan=rowspan, sticky='nsew', **options)
#     #
#     #     self.display.grid(row=0, column=0, columnspan=2, sticky='news')
#     #
#     #     # boss
#     #     for row in range(len(operator) // num_col + 1):
#     #         frame_operators.rowconfigure(row, weight=1)
#     #     # for row in range(len(operator)):
#     #     #     frame_operators.rowconfigure(row, weight=1)
#     #
#     #     frame_operators.columnconfigure(0, weight=1)
#     #     frame_operators.columnconfigure(1, weight=1)
#     #
#     #     return frame_operators
#     def make_operator_pad(self) -> tk.Frame:
#         frame_operators = tk.Frame(self)
#         operator = ['*', '/', '+', '-', '^', '(', ')', 'mod']
#         options = {'padx': 1, 'pady': 1}
#
#         num_col = 2
#         num_rows = len(operator) // num_col + 1
#
#         # self.rowconfigure(2, weight=0)
#
#         for i, key in enumerate(operator):
#             row = i % num_rows
#             col = i // num_rows
#
#             rowspan = 2 if key == '=' else 1
#
#             button = Keypad(frame_operators, keynames=[key], columns=1)
#             button.grid(row=row, column=col, rowspan=rowspan, sticky='nsew', **options)
#
#         self.display.grid(row=1, column=1, columnspan=2, sticky='news')
#
#     def make_command_pad(self) -> tk.Frame:
#         # 'CLR', 'DEL', '='
#         frame_commands = tk.Frame(self)
#         commands = ['CLR', 'DEL', '=']
#         options = {'padx': 1, 'pady': 1}
#
#         for i, key in enumerate(commands):
#             row = i
#             col = 2
#
#             button = Keypad(frame_commands, keynames=[key], columns=1)
#             button.grid(row=row, column=col, sticky='nsew', **options)
#
#         frame_commands.rowconfigure(0, weight=1)
#         frame_commands.rowconfigure(1, weight=1)
#         frame_commands.rowconfigure(2, weight=1)
#
#         frame_commands.columnconfigure(2, weight=1)
#
#         return frame_commands
#
#     def display_text(self, text):
#         self.display.configure(state='normal')
#         self.display.delete('1.0', tk.END)
#         self.display.insert(tk.END, text, "right")
#         self.display.configure(state='disabled')
#
#     # def handle_keypad_press(self, event_or_key):
#     #     if isinstance(event_or_key, str):
#     #         key = event_or_key
#     #     else:
#     #         button = event_or_key.widget
#     #         key = button['text']
#     #
#     #     value = key
#     #
#     #     if value == '=':
#     #         try:
#     #             expression = self.display.get('1.0', 'end-1c')
#     #             result = eval(expression.replace("^", "**"))
#     #             self.display.configure(state='normal')
#     #             self.display.delete('1.0', tk.END)
#     #             self.display.insert(tk.END, str(result), "right")
#     #             self.display.configure(state='disabled')
#     #         except Exception as e:
#     #             print("Error", e)
#     #     else:
#     #         self.display.configure(state='normal')
#     #         self.display.insert(tk.END, value, "right")
#     #         self.display.configure(state='disabled')
#
#     def run(self):
#         self.mainloop()


import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from mvc_controller import CalculatorController


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.display = None
        self.keypad = None
        self.init_components()

    def init_components(self):
        self.display = tk.Text(self, height=2, state='disabled',
                               font=('Sarabun', 16), padx=12, pady=12)
        self.display.tag_configure("right", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky='news')

        self.keypad = Keypad(self,
                             keynames=['7', '8', '9', '4', '5', '6', '1', '2',
                                       '3', ' ', '0', '.'], columns=3)
        self.keypad.grid(row=1, column=0, sticky='news')

        # combobox_function = self.make_combobox_function()
        # combobox_function.grid(row=0, column=0, sticky='news', columnspan=2)  # Place combobox at top

        operator_pad = self.make_operator_pad()
        operator_pad.grid(row=1, column=1, sticky='news')

        command_pad = self.make_command_pad()
        command_pad.grid(row=0, column=2, rowspan=2, sticky='news')

        self.rowconfigure(0, weight=1)  # row 0 is the display
        self.rowconfigure(1, weight=1)  # row 1 is the keypad
        self.rowconfigure(2, weight=0)  # row 2 is the operators and commands

        self.columnconfigure(0, weight=1)  # column 0 is the keypad
        self.columnconfigure(1, weight=1)  # column 1 is the operators
        self.columnconfigure(2, weight=1)  # column 2 is the commands

        self.keypad.bind('<Button-1>', CalculatorController.handle_keypad_press)

    def make_combobox_function(self):
        functionvar = tk.StringVar()
        function = ttk.Combobox(self, textvariable=functionvar)
        function['values'] = ('exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan')
        function.grid(row=1, column=0, sticky='news')

    def make_operator_pad(self) -> tk.Frame:
        frame_operators = tk.Frame(self)
        operator = ['*', '/', '+', '-', '^', '(', ')', 'mod']
        options = {'padx': 1, 'pady': 1}

        num_col = 2
        num_rows = len(operator) // num_col

        for i, key in enumerate(operator):
            row = i % num_rows
            col = i // num_rows

            rowspan = 2 if key == '=' else 1

            button = Keypad(frame_operators, keynames=[key], columns=1)
            button.grid(row=row, column=col, rowspan=rowspan, sticky='nsew',
                        **options)

        frame_operators.grid(row=1, column=1, sticky='news')  # Fix here: grid the frame, not the button

        for row in range(num_rows):
            frame_operators.rowconfigure(row, weight=1)

        for col in range(num_col):
            frame_operators.columnconfigure(col, weight=1)

        return frame_operators

    def make_command_pad(self) -> tk.Frame:
        frame_commands = tk.Frame(self)
        commands = ['CLR', 'DEL', '=']
        options = {'padx': 1, 'pady': 1}

        for i, key in enumerate(commands):
            row = i
            col = 0  # Place command buttons in the first column

            button = Keypad(frame_commands, keynames=[key], columns=1)
            button.grid(row=row, column=col, sticky='nsew', **options)

        frame_commands.rowconfigure(0, weight=1)
        frame_commands.rowconfigure(1, weight=1)
        frame_commands.rowconfigure(2, weight=1)

        frame_commands.columnconfigure(0, weight=1)  # Fix here: grid the frame, not the button

        return frame_commands

    def display_text(self, text):
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, text, "right")
        self.display.configure(state='disabled')

    def run(self):
        self.mainloop()

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

        combobox_function = self.make_combobox_function()
        combobox_function.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='news')  # Span across row 0 and row 1

        self.keypad = Keypad(self,
                             keynames=['7', '8', '9', '4', '5', '6', '1', '2',
                                       '3', ' ', '0', '.'], columns=3)
        self.keypad.grid(row=2, column=0, sticky='news')  # Move keypad to row 2

        operator_pad = self.make_operator_pad()
        operator_pad.grid(row=2, column=1, sticky='news')  # Move operator pad to row 2

        command_pad = self.make_command_pad()
        command_pad.grid(row=2, column=2, sticky='news')  # Move command pad to row 2

        self.rowconfigure(0, weight=1)  # row 0 is the display
        self.rowconfigure(1, weight=1)  # row 1 is the combobox
        self.rowconfigure(2, weight=1)  # row 2 is the keypad, operators, and commands

        self.columnconfigure(0, weight=1)  # column 0 is the keypad and combobox
        self.columnconfigure(1, weight=1)  # column 1 is the operators
        self.columnconfigure(2, weight=1)  # column 2 is the commands

        self.keypad.bind('<Button-1>', CalculatorController.handle_keypad_press)

    def make_combobox_function(self):
        function_var = tk.StringVar()
        function = ttk.Combobox(self, textvariable=function_var)
        function['values'] = ('exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan')
        return function

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

        frame_operators.grid(row=2, column=1, sticky='news')  # Fix here: grid the frame, not the button

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

        frame_commands.grid(row=2, column=2, sticky='news')  # Fix here: grid the frame, not the button

        for row in range(len(commands)):
            frame_commands.rowconfigure(row, weight=1)

        frame_commands.columnconfigure(0, weight=1)

        return frame_commands

    def display_text(self, text):
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, text, "right")
        self.display.configure(state='disabled')

    def run(self):
        self.mainloop()

# Instantiate and run the CalculatorUI
calculator_app = CalculatorUI()
calculator_app.run()

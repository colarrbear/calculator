import tkinter as tk
from tkinter import ttk


class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('Calculator')
        self.controller = controller
        self.init_components()

    def init_components(self):
        self.display = tk.Text(self, height=2, state='disabled',
                               font=('Sarabun', 16), padx=12, pady=12, bg='lightblue')
        self.display.tag_configure("right", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky='news')

        ttk.Label(self, text="Function:").grid(row=1, column=0, sticky='w')

        self.combobox_function = self.make_combobox_function()
        self.combobox_function.grid(row=1, column=1, columnspan=3, sticky='news')
        self.combobox_function.current(0)
        self.combobox_function.bind("<<ComboboxSelected>>", self.update_combobox_display)

        self.keypad = self.make_keypad()
        self.operator_pad = self.make_operator_pad()
        self.command_pad = self.make_command_pad()

        self.keypad.grid(row=2, column=0, sticky='news')
        self.operator_pad.grid(row=2, column=1, sticky='news')
        self.command_pad.grid(row=2, column=2, sticky='news')

        self.rowconfigure(0, weight=1)  # row 0 is the display
        self.rowconfigure(1, weight=1)  # row 1 is the keypad, operators, and commands

        self.columnconfigure(0, weight=1)  # column 0 is the keypad and combobox
        self.columnconfigure(1, weight=1)  # column 1 is the operators
        self.columnconfigure(2, weight=1)  # column 2 is the commands

    def make_keypad(self):
        frame = tk.Frame(self)
        keys = list('789456123 0.')
        for i, key in enumerate(keys):
            button = tk.Button(frame, text=key, command=lambda
                k=key: self.controller.handler_keypad_press(k))
            button.grid(row=i // 3, column=i % 3, padx=2, pady=2,
                        sticky="nsew")
            frame.grid_columnconfigure(i % 3, weight=1)
            frame.grid_rowconfigure(i // 3, weight=1)
            button.grid(sticky="nsew")
        return frame

    def make_operator_pad(self) -> tk.Frame:
        frame_operators = tk.Frame(self)
        operator = ['*', '/', '+', '-', '^', '(', ')', 'mod']
        options = {'padx': 1, 'pady': 1}

        num_cols = 2
        num_rows = len(operator) // num_cols

        for i, key in enumerate(operator):
            row = i % num_rows
            col = i // num_rows

            button = tk.Button(frame_operators, text=key, command=lambda op=key: self.controller.handler_keypad_press(op))
            button.grid(row=row, column=col, sticky='nsew', **options)

        frame_operators.grid(row=1, column=1, sticky='news')

        for row in range(num_rows):
            frame_operators.rowconfigure(row, weight=1)

        for col in range(num_cols):
            frame_operators.columnconfigure(col, weight=1)

        return frame_operators

    def make_combobox_function(self):
        function_var = tk.StringVar()
        function = ttk.Combobox(self, textvariable=function_var)
        function['values'] = ('exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan')
        function.bind("<<ComboboxSelected>>", self.update_combobox_display)
        return function

    def update_combobox_display(self, event):
        operator = self.combobox_function.get()
        # print('op', operator)
        current_expression = self.display.get('1.0', tk.END).strip()

        if current_expression == "":
            self.display.insert(tk.END, f'{operator}(')
            self.update_display(f'{operator}(')
        else:
            last_char = current_expression[-1]
            if last_char in self.controller.model.operators:
                self.display.delete('1.0', tk.END)
                self.display.insert(tk.END, f'{current_expression}{operator}(')
            else:
                self.display.insert(tk.END, f'{operator}(')

        self.combobox_function.set("")  # Reset the combobox selection

    def make_command_pad(self) -> tk.Frame:
        frame_commands = tk.Frame(self)
        commands = ['CLR', 'DEL', '=']
        options = {'padx': 1, 'pady': 1}

        for i, key in enumerate(commands):
            row = i
            col = 0

            button = tk.Button(frame_commands, text=key, command=lambda
                cmd=key: self.controller.handler_keypad_press(cmd))
            button.grid(row=row, column=col, sticky='nsew', **options)
        frame_commands.grid(row=1, column=2, sticky='news')

        for row in range(len(commands)):
            frame_commands.rowconfigure(row, weight=1)

        frame_commands.columnconfigure(0, weight=1)

        return frame_commands

    def display_text(self, text):
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, text, "right")
        self.display.configure(state='disabled')

    def set_display_colour(self, colour='lightblue'):
        self.display.configure(bg=colour)

    def change_text_colour(self, colour='black'):
        self.display.configure(fg=colour)

    def update_display(self, value):
        self.display.configure(state='normal')
        self.display.insert(tk.END, value, "right")
        self.display.configure(state='disabled')

    def clear_display(self):
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.configure(state='disabled')
        self.change_text_colour('black')
        self.set_display_colour('lightblue')

    def run(self):
        self.mainloop()

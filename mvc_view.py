import tkinter as tk
from tkinter import ttk


class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('Calculator')
        self.controller = controller
        self.history = tk.StringVar()
        self.init_components()

    # def init_components(self):
    #     self.display = tk.Text(self, height=2, state='disabled',
    #                            font=('Sarabun', 16), padx=12, pady=12,
    #                            bg='lightblue')
    #     self.display.tag_configure("right", justify="right")
    #     self.display.grid(row=1, column=0, columnspan=4, sticky='news')
    #
    #     ttk.Label(self, text="Function:").grid(row=2, column=0, sticky='news')
    #
    #     self.combobox_function = self.make_combobox_function()
    #     self.combobox_function.grid(row=2, column=2, columnspan=1,
    #                                 sticky='news')
    #     self.combobox_function.current(0)
    #     self.combobox_function.bind("<<ComboboxSelected>>",
    #                                 self.update_combobox_display)
    #
    #     self.keypad = self.make_keypad()
    #     self.operator_pad = self.make_operator_pad()
    #     self.command_pad = self.make_command_pad()
    #     self.history_label = self.create_history()
    #
    #     self.history_label.grid(row=0, column=0, columnspan=4, sticky='news')
    #     self.keypad.grid(row=3, column=0, sticky='news')
    #     self.operator_pad.grid(row=3, column=1, sticky='news')
    #     self.command_pad.grid(row=3, column=2, sticky='news')
    #
    #     # try line 39-46
    #     self.history_listbox = tk.Listbox(self, font=('Sarabun', 12),
    #                                       selectmode=tk.SINGLE, width=40, height=5)
    #     self.history_listbox.grid(row=2, column=0, columnspan=4, sticky='news')
    #     self.history_listbox.bind('<Button-1>',self.recall_history_entry)
    #
    #     self.rowconfigure(2, weight=1)
    #     #
    #
    #     self.rowconfigure(0, weight=1)
    #     self.rowconfigure(1, weight=1)
    #     self.rowconfigure(2, weight=1)
    #     self.rowconfigure(3, weight=1)
    #
    #     self.columnconfigure(0, weight=1)
    #     self.columnconfigure(1, weight=1)
    #
    #     self.rowconfigure(0, weight=1)
    #     self.rowconfigure(1, weight=1)
    #     self.rowconfigure(2, weight=1)
    def init_components(self):
        # try line 39-46
        self.history_label = self.create_history()
        # self.history_label.grid(row=0, column=0, columnspan=4, sticky='news')
        self.history_listbox = tk.Listbox(self, font=('Sarabun', 12),
                                          selectmode=tk.SINGLE, width=40,
                                          height=5)
        self.history_listbox.grid(row=1, column=0, columnspan=4, sticky='news')
        self.history_listbox.bind('<Button-1>', self.recall_history_entry)

        self.rowconfigure(2, weight=1)
        #
        self.display = tk.Text(self, height=2, state='disabled',
                               font=('Sarabun', 16), padx=12, pady=12,
                               bg='lightblue')
        self.display.tag_configure("right", justify="right")
        self.display.grid(row=2, column=0, columnspan=4, sticky='news')

        ttk.Label(self, text="Function:").grid(row=4, column=0, sticky='news')

        self.combobox_function = self.make_combobox_function()
        self.combobox_function.grid(row=4, column=2, columnspan=1,
                                    sticky='news')
        self.combobox_function.current(0)
        self.combobox_function.bind("<<ComboboxSelected>>",
                                    self.update_combobox_display)

        self.keypad = self.make_keypad()
        self.operator_pad = self.make_operator_pad()
        self.command_pad = self.make_command_pad()

        self.keypad.grid(row=5, column=0, sticky='news')
        self.operator_pad.grid(row=5, column=1, sticky='news')
        self.command_pad.grid(row=5, column=2, sticky='news')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def create_history(self):
        self.history_label = ttk.Label(self, textvariable=self.history,
                                       anchor='e')
        return self.history_label

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

            button = tk.Button(frame_operators, text=key, command=lambda
                op=key: self.controller.handler_keypad_press(op))
            button.grid(row=row, column=col, sticky='nsew', **options)

        frame_operators.grid(row=2, column=1, sticky='news')

        for row in range(num_rows):
            frame_operators.rowconfigure(row, weight=1)

        for col in range(num_cols):
            frame_operators.columnconfigure(col, weight=1)

        return frame_operators

    def make_combobox_function(self):
        function_var = tk.StringVar()
        function = ttk.Combobox(self, textvariable=function_var)
        function['values'] = (
            'exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan')
        function.bind("<<ComboboxSelected>>", self.update_combobox_display)
        return function

    def update_combobox_display(self, event):
        operator = self.combobox_function.get()
        current_expression = self.display.get('1.0', tk.END).strip()
        if current_expression == "":
            self.display.insert(tk.END, f'{operator}(')
            self.update_display(f'{operator}(')
        else:
            last_char = current_expression[-1]
            try:
                int(current_expression)
            except ValueError:
                if last_char.isdigit() or last_char == ')':
                    self.display.insert(tk.END, f'*{operator}(')
                    self.update_display(f'*{operator}(')
                else:
                    self.display.insert(tk.END, f'{operator}(')
                    self.update_display(f'{operator}(')
            else:
                self.display.insert(tk.END, f'*{operator}(')
                self.update_display(f'*{operator}(')

        self.combobox_function.set("")

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

    def set_display_colour(self, colour='lightblue'):
        self.display.configure(bg=colour)

    def change_text_colour(self, colour='black'):
        """Change the text colour of the display."""
        self.display.configure(fg=colour)

    def update_display(self, value: str):
        """Update the display with the given value."""
        self.display.configure(state='normal')
        self.display.insert(tk.END, value, "right")
        self.display.configure(state='disabled')

    def clear_display(self):
        """Clear the display."""
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.configure(state='disabled')
        self.change_text_colour('black')
        self.set_display_colour('lightblue')

    # def update_history(self, history: tuple):
    def update_history(self, history):
        """Update the history label."""
        # old code
        # self.history.set(f"{history[0]} = {history[1]}")
        # 1
        # self.history_listbox.insert(tk.END, history)
        # 2
        # self.history_listbox.insert(tk.END, f"{history[0]} = {history[1]}")
        # self.history_listbox.selection_clear(0, tk.END)
        # 3
        equation = f"{history[0]} ="
        answer = history[1]

        self.history_listbox.insert(tk.END, equation)
        self.history_listbox.insert(tk.END, answer)

        self.history_listbox.selection_clear(0, tk.END)

    # new func
    def recall_history_entry(self, event):
        selected_index = self.history_listbox.curselection()
        if selected_index:
            selected_entry = self.history_listbox.get(selected_index[0])
            self.controller.recall_handler(selected_entry)


"""ui for calculator"""
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

        self.keypad = Keypad(self,keynames=['7', '8', '9', '4', '5', '6', '1', '2','3', ' ', '0', '.'], columns=3)
        # self.keypad = Keypad(self,keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        operators = self.make_operator_pad()

        self.keypad.grid(row=1, column=0, sticky='news')
        operators.grid(row=1, column=1, sticky='news')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)


        # self.keypad.bind('<Button-1>', self.handle_keypad_press)
        self.keypad.bind('<Button-1>', CalculatorController.handle_keypad_press)

    # combobox = ttk.Combobox(frame_operators,values=['exp', 'ln', 'log base 10', 'log2','sqrt'])
    # combobox.set('Select Function')
    # combobox.grid(row=row, column=col, **options)

    def make_operator_pad(self) -> tk.Frame:
        frame_operators = tk.Frame(self)
        operator = ['*', '/', '+', '-', '^', '(', ')', 'AC', 'DEL', 'mod', '=']
        # options = {'sticky': 'NWES', 'padx': 1, 'pady': 1}
        options = {'padx': 1, 'pady': 1}


        num_col = 2
        num_rows = len(operator) // num_col + 1
        for i, key in enumerate(operator):
            row = i % num_rows
            col = i // num_rows

            rowspan = 2 if key == '=' else 1

            button = tk.Button(frame_operators, text=key, command=lambda
                key=key: CalculatorController.handle_keypad_press(key, self))
            button.grid(row=row, column=col, rowspan=rowspan, sticky='news', **options)

        self.display.grid(row=0, column=0, columnspan=2, sticky='news')

        for row in range(len(operator)):
            frame_operators.rowconfigure(row, weight=1)

        frame_operators.columnconfigure(0, weight=1)
        frame_operators.columnconfigure(1, weight=1)

        return frame_operators
        # num_rows = len(operator)
        # num_columns = 2
        # for i, key in enumerate(operator):
        #     row = i // num_columns
        #     col = i % num_columns
        #
        #     button = tk.Button(frame_operators, text=key, command=lambda
        #         key=key: CalculatorController.handle_keypad_press(key, self))
        #     button.grid(row=row, column=col, **options)
        #
        # for row in range(len(operator)):
        #     frame_operators.rowconfigure(row, weight=1)
        #
        # frame_operators.columnconfigure(0, weight=1)
        # frame_operators.columnconfigure(1, weight=1)
        #
        # return frame_operators


        # for i, key in enumerate(operator):
        #     # button = tk.Button(frame_operators, text=key, command=lambda key=key: self.handle_keypad_press(key))
        #     button = tk.Button(frame_operators, text=key, command=lambda
        #         key=key: CalculatorController.handle_keypad_press(key, self))
        #     button.grid(row=i, column=0, **options)
        #
        # for row in range(len(operator)):
        #     frame_operators.rowconfigure(row, weight=1)
        # frame_operators.columnconfigure(0, weight=1)
        # return frame_operators


    def display_text(self, text):
        self.display.configure(state='normal')
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, text, "right")
        self.display.configure(state='disabled')

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

    def run(self):
        self.mainloop()

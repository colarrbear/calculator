import tkinter as tk


class Keypad(tk.Frame):
    # try command
    # def __init__(self, parent,keynames=[], columns=1, commmand=None, **kwargs):
    #     super().__init__(parent, **kwargs)
    #     # self.keynames = keynames # st code
    #     self.keynames = keynames if keynames else list('789456123 0.')
    #     self.columns = columns
    #     self.command = commmand
    #     self.init_components(columns)  # st code

    def __init__(self, parent,keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        # self.keynames = keynames # st code
        self.keynames = keynames if keynames else list('789456123 0.')
        self.columns = columns
        self.init_components(columns)  # st code

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        options = {'sticky': 'news', 'padx': 1, 'pady': 1}

        # try command
        # for i, key in enumerate(self.keynames):
        #     button = tk.Button(self, text=key, command=lambda k=key: self.command(k) if self.command else None)
        #     button.grid(row=i // columns, column=i % columns, **options)

        for i, key in enumerate(self.keynames):
                    button = tk.Button(self, text=key)
                    button.grid(row=i // columns, column=i % columns, **options)

        for i in range(len(self.keynames) // columns):
            self.rowconfigure(i, weight=1)
        for i in range(columns):
            self.columnconfigure(i, weight=1)
        # num(columns) = 3: 0, 1, 2
        # num(row) = 4: 0, 1, 2, 3

    def handle_press(self, event):
        key = event.widget['text']
        print(f"You pressed {key}")

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.winfo_children():
            child.bind(sequence, func)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return [child[key] for child in self.winfo_children()]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)

    @property
    def frame(self):
        return super()


class KeypadButton(tk.Button):
    def __init__(self, keypad, key, **kwargs):
        super().__init__(keypad, text=key, **kwargs)
        self.bind("<Button-1>", keypad.handle_press)


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    keypad.frame.configure(background='blue')
    root.mainloop()

import tkinter as tk
from secrets import token_urlsafe, randbelow
import pyperclip


class MainWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.geometry('450x100')
        self.resizable(False, False)
        self.title('Simple Password Generator')

        self.char_amount = tk.IntVar()
        self.char_amount.set(22)

        # First section
        self.l1 = tk.Label(self, text='Maximum Password length:')
        self.l1.grid()

        self.e1 = tk.Entry(self, textvariable=self.char_amount)
        self.e1.grid(row=0, column=1)

        self.b1 = tk.Button(self,
                            text='Generate password.',
                            command=lambda: self.generate_password())
        self.b1.grid(row=0, column=2)

        # Second section:
        self.l2 = tk.Label(self, text='No password generated.', fg='red')
        self.l2.grid(row=1)

        # Third section:
        self.b2 = tk.Button(self,
                            text='Copy to clipboard.',
                            command=lambda: self.copy_to_clipboard(),
                            state='disabled')
        self.b2.grid(row=2)

    def generate_password(self) -> None:
        self.b2['text'] = 'Copy to clipboard.'
        self.b2['state'] = 'normal'

        self.l2['fg'] = 'green'
        self.l2['text'] = 'Password generated!'
		
        password_len = randbelow(self.char_amount.get())

        self.password = token_urlsafe(password_len)

    def copy_to_clipboard(self) -> None:
        pyperclip.copy(self.password)


if __name__ == "__main__":
    MainWindow().mainloop()

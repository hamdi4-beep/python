from tkinter import *
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.label = ttk.Label(text='Message:')
        self.label.pack()

root = Tk()
root.title('Python GUI')
root.geometry('800x600')

Application(root)

root.mainloop()
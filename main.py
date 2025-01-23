from tkinter import *
from tkinter import ttk

tk = Tk()
tk.title('Python GUI')
tk.geometry('800x600')

frame = ttk.Frame(tk)
frame.pack()

tk.bind('<Key-Return>', lambda self: print('You pressed the return key!'))

tk.mainloop()
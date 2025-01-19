from tkinter import *
from tkinter import ttk

# creates the parent window
root = Tk()
root.title('Python Application')
# sets the window's width and height
root.geometry('800x600')

# creates the frame
frame = ttk.Frame(root, padding=10)
# registers the frame with the grid manager
frame.grid()

# creates a button widget
btn = ttk.Button(root, text='Quit application', command=root.destroy)
btn.grid()

root.mainloop()
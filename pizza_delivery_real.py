#importing Tkinter so i can give program a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk

#creating window for form
window = Tk()
window.title("Pizza order form")
top = Frame(window)
buttons = Frame(window)
top.grid(row=0, column=0)
buttons.grid(row=1, column=0)

top_text = Label(top, text='pick up or delivery?')
top_text.pack()

delivery_button = Button(buttons, text='delivery')
delivery_button.grid(row=0, column=0, padx=10, pady=50)

pickup_button = Button(buttons, text='pick up')
pickup_button.grid(row=0, column=1, padx=10, pady=50)

window.mainloop()

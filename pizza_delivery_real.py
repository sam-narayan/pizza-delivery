#importing Tkinter so i can give program a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk

#creating window for form
window = Tk()
window.title("Pizza order form")
top = Frame(window)
buttons = Frame(window)
detail_frame = Frame(window)
top.grid(row=0, column=0)
buttons.grid(row=1, column=0)

label_text = StringVar()
label_text.set('pickup or delivery?!')

def dcmd():
    forget(buttons)
    add_widget(detail_frame, 1, 0)
    print('well done')
    label_text.set('Name?')

def add_widget(widget, rw, clmn, x = 10, y = 3):
    widget.grid(row = rw, column = clmn, padx = x, pady = y)

def forget(widget):
    widget.grid_forget()

top_text = Label(top, textvariable = label_text)
top_text.pack()

delivery_button = Button(buttons, text='delivery', command=dcmd)
delivery_button.grid(row=0, column=0, padx=10, pady=50)

pickup_button = Button(buttons, text='pick up')
add_widget(pickup_button, 0, 1, 10, 50)

window.mainloop()

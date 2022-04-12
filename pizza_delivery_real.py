#importing Tkinter so i can give program a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk

#creating window for form
window = Tk()
window.resizable(False,False)
window.title("Pizza order form")
top = Frame(window)
buttons = Frame(window)
detail_frame = Frame(window)
address_frame = Frame(window)
phone_frame = Frame(window)
top.grid(row=0, column=0)
buttons.grid(row=1, column=0)

label_text = StringVar()
label_text.set('pickup or delivery?!')

def dcmd():
    forget(buttons)
    add_widget(detail_frame, 1)
    label_text.set('Name?')
    add_widget(name_box)
    add_widget(confirmbutton,1)


def add_widget(widget, rw = 0, clmn = 0, x = 10, y = 3):
    widget.grid(row = rw, column = clmn, padx = x, pady = y)

def forget(widget):
    widget.grid_forget()

def confirm():
    forget(detail_frame)
    add_widget(address_frame, 1)
    label_text.set('Address?')
    add_widget(address_box)
    add_widget(address_confirm, 1 )

def acmd():
    forget(address_frame)
    add_widget(phone_frame, 1)
    label_text.set('phone number?')
    add_widget(number_box)


top_text = Label(top, textvariable = label_text)
top_text.pack()

delivery_button = Button(buttons, text='delivery', command=dcmd)
delivery_button.grid(row=0, column=0, padx=10, pady=50)

pickup_button = Button(buttons, text='pick up')
add_widget(pickup_button, 0, 1, 10, 50)

name = DoubleVar()
name.set('')

name_box= Entry(detail_frame, textvariable= name)

confirmbutton= Button(detail_frame, text='confirm', command=confirm)

address = DoubleVar()
address.set('')

address_box= Entry(address_frame, textvariable= address )

address_confirm= Button(address_frame, text='confirm', command=acmd)

number_box= Entry(phone_frame)

window.mainloop()

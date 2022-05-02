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
name2_frame = Frame(window)
master = Frame(window)

def show():
    global current_order
    current_order.set("order: \nham: {} \nfemale: {} \ncheese: {} \nname: {}".format(var1.get(), var2.get(), var3.get(), name2.get()))

def dcmd():
    forget(buttons)
    add_widget(detail_frame, 1)
    label_text.set('Name?')
    add_widget(name_box)
    add_widget(confirmbutton,1)
    add_widget(cancel1,2)


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
    add_widget(cancel3, 2)

def acmd():
    forget(address_frame)
    add_widget(phone_frame, 1)
    label_text.set('phone number?')
    add_widget(number_box)
    add_widget(number_confirm, 1)
    add_widget(cancel4,2)

def pcmd():
    forget(phone_frame)

def pickcmd():
    forget(buttons)
    add_widget(name2_frame, 1)
    label_text.set('name?')
    add_widget(name2box)
    add_widget(name2confirm,1)
    add_widget(cancel2,2)

def name2cmd():
    forget(name2_frame)
    add_widget(master, 1)
    label_text.set('order?')

top_text = Label(top, textvariable = label_text)
top_text.pack()

delivery_button = Button(buttons, text='delivery', command=dcmd)
delivery_button.grid(row=0, column=0, padx=10, pady=50)

pickup_button = Button(buttons, text='pick up', command=pickcmd)
add_widget(pickup_button, 0, 1, 10, 50)

name = StringVar()
name.set('')

name_box= Entry(detail_frame, textvariable= name)

confirmbutton= Button(detail_frame, text='confirm', command=confirm)

cancel1= Button(detail_frame, text='cancel', command=master.quit)


name2 = StringVar()
name2.set('')

name2box= Entry (name2_frame, textvariable= name2)

name2confirm= Button(name2_frame, text='confirm', command=name2cmd)

cancel2= Button(name2_frame, text='cancel', command=master.quit)


address = StringVar()
address.set('')

address_box= Entry(address_frame, textvariable= address )

address_confirm= Button(address_frame, text='confirm', command=acmd)

cancel3 = Button(address_frame, text='cancel', command=master.quit)

number= StringVar()
number.set('')

number_box= Entry(phone_frame, textvariable= number)

number_confirm= Button(phone_frame, text='confirm', command=pcmd)

cancel4 = Button(phone_frame, text='cancel', command=master.quit)


current_order= StringVar()
current_order.set('')
Label(master, text="toppings:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="ham", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="cheese", variable=var3).grid(row=3, sticky=W)
Button(master, text='cancel', command=master.quit).grid(row=4, sticky=W, pady=4)
Button(master, text='Show', command=show).grid(row=5, sticky=W, pady=4)
Label(master, textvariable=current_order).grid(row=6, sticky=W, pady=4)

window.mainloop()

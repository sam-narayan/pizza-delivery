#importing Tkinter so i can give program a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk

#creating window for form
window = Tk()
window.resizable(False,False)
window.title("Pizza order form")
window.config(bg = 'blue')
top = Frame(window, bg='green')
buttons = Frame(top, bg = 'yellow')
detail_frame = Frame(window)
address_frame = Frame(window)
phone_frame = Frame(window)
top.grid(row=1)
buttons.grid(row = 1, column= 0, pady = 40)
label_text = StringVar()
label_text.set('pickup or delivery?!')
name2_frame = Frame(window)
master = Frame(window)
total = IntVar(window, 5)
orderframe = Frame(window, bg = 'black')
pizza = 0

def show():
    global current_order, total
    if var1.get() == 1:
        total.set(total.get() + 100)
    if var2.get() == 1:
        total.set(total.get() -1000000)
    if var3.get() == 1:
        total.set(total.get() +9000)
    if var4.get() == 1:
        total.set(total.get() +2.50)
    current_order.set("order: \nham: {} \nfemale: {} \ncheese: {} \ngourmet base: {} \ncost: ${}".format(var1.get(), var2.get(), var3.get(), var4.get(), total.get()))

def dcmd():
    forget(buttons)
    add_widget(detail_frame, 1)
    label_text.set('Name?')
    add_widget(name_box)
    add_widget(confirmbutton,1)
    add_widget(cancel1,2)
    delvorpick.set('Delivery')

def add_widget(widget, rw = 4, clmn = 0, x = 10, y = 3, clms = 1):
    widget.grid(row = rw, column = clmn, padx = x, pady = y, columnspan =clms)

def forget(widget):
    widget.grid_forget()

def confirm():
    forget(detail_frame)
    add_widget(address_frame)
    label_text.set('Address?')
    add_widget(address_box)
    add_widget(address_confirm,1)
    add_widget(cancel3,2)

def acmd():
    forget(address_frame)
    add_widget(phone_frame)
    label_text.set('phone number?')
    add_widget(number_box)
    add_widget(number_confirm,1)
    add_widget(cancel4,2)

def pcmd():
    forget(phone_frame)

def pickcmd():
    forget(buttons)
    add_widget(name2_frame)
    label_text.set('name?')
    add_widget(name2box, 0, 1, 10, 0, 2)
    add_widget(name2confirm, 1, 1, 0, 1)
    add_widget(cancel2, 1, 2, 0, 1)
    delvorpick.set('Pick up')

def name2cmd():
    forget(name2_frame)
    add_widget(master)
    label_text.set('order?')
    name_boxorder.set('name: {}'.format(name2.get()))

def add_pizza():
    pizza + 1
    while pizza < 5:
        forget(master)
        add_widget (master)
        break




add_widget(orderframe, clmn=1, y=10)

delvorpick = StringVar()
Label(orderframe, textvariable=delvorpick,).grid(row=0, pady=10, padx=10)

name_boxorder = StringVar()
Label(orderframe, textvariable=name_boxorder).grid(row=1, pady=10, padx=10)

current_order= StringVar()
current_order.set('')
Label(orderframe, textvariable=current_order,).grid(row=2, pady=10, padx=10)

top_text = Label(top, textvariable = label_text, pady = 0, bg = 'red')
top_text.grid(pady = 0, row = 0, column =0, sticky = 'n')

delivery_button = Button(buttons, text='delivery', command=dcmd, cursor="hand2")
delivery_button.grid(row=0, column=0, padx=10, pady=0)

pickup_button = Button(buttons, text='pick up', command=pickcmd, cursor="hand2")
add_widget(pickup_button, 0, 1, 10, 0)

name = StringVar()
name.set('')

name_box= Entry(detail_frame, textvariable= name)

confirmbutton= Button(detail_frame, text='confirm', command=confirm, cursor="hand2")

cancel1= Button(detail_frame, text='cancel', command=master.quit, cursor="hand2")


name2 = StringVar()
name2.set('')
name2box= Entry (name2_frame, textvariable= name2)

name2confirm= Button(name2_frame, text='confirm', command=name2cmd, cursor="hand2")

cancel2= Button(name2_frame, text='cancel', command=master.quit, cursor="hand2")


address = StringVar()
address.set('')

address_box= Entry(address_frame, textvariable= address )

address_confirm= Button(address_frame, text='confirm', command=acmd, cursor="hand2")

cancel3 = Button(address_frame, text='cancel', command=master.quit, cursor="hand2")

number= StringVar()
number.set('')

number_box= Entry(phone_frame, textvariable= number)

number_confirm= Button(phone_frame, text='confirm', command=pcmd, cursor="hand2")

cancel4 = Button(phone_frame, text='cancel', command=master.quit, cursor="hand2")

Label(master, text="toppings:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="ham", variable=var1, onvalue=1, offvalue=0).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2, onvalue=1, offvalue=0).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="cheese", variable=var3, onvalue=1, offvalue=0).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="gourmet women", variable=var4, onvalue=1, offvalue=0).grid(row=4, sticky=W)
Button(master, text='add pizza',command=add_pizza, cursor="hand2").grid(row=5, sticky=W,pady=4)
Button(master, text='confirm', command=show, cursor="hand2").grid(row=6, sticky=W, pady=4)
Button(master, text='cancel', command=master.quit, cursor="hand2").grid(row=7, sticky=W, pady=4)

window.mainloop()

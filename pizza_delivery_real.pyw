#importing Tkinter so i can give program a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#creating window for form
window = Tk()
window.resizable(False,False)
window.title("Pizza order form")
window.config()
top = Frame(window)
buttons = Frame(top)
detail_frame = Frame(top)
address_frame = Frame(top)
phone_frame = Frame(top)
top.grid(row=1)
buttons.grid(row = 1, column= 0, pady = 40)
label_text = StringVar()
label_text.set('pickup or delivery?!')
name2_frame = Frame(top)
master = Frame(top)
total = IntVar(top, 5)
orderframe = Frame(window,)
pizza = 0

def show(x):
    global current_order, total, varpizza
    onpizza = ''
    if varpizza.get() == 1:
        total.set(total.get() +8.50)
        piiz = '\nCheese Supreme'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 2:
        total.set(total.get() +8.50)
        piiz = '\nham and cheese'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 3:
        total.set(total.get() +8.50)
        piiz = '\nmeat!!'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 4:
        total.set(total.get() +8.50)
        piiz = '\nnacho chips and cheese'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 5:
        total.set(total.get() +8.50)
        piiz = '\nsuper meat lovers'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 6:
        total.set(total.get() +8.50)
        piiz = '\ngarlic and cheese'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 7:
        total.set(total.get() +8.50)
        piiz = '\npeperoni and cheese'
        onpizza = f'{onpizza}{piiz}'
    elif varpizza.get() == 8:
        total.set(total.get() +8.50)
        piiz = '\nprawn and chorizo'
        onpizza = f'{onpizza}{piiz}'

    if var1.get() == 1:
        total.set(total.get() +0.50)
        ham = '\nham'
        onpizza = f'{onpizza}{ham}'
    if var2.get() == 1:
        total.set(total.get() +0.50)
        extracheese = '\nextra cheese'
        onpizza = f'{onpizza}{extracheese}'
    if var3.get() == 1:
        total.set(total.get() +0.50)
        garlic = '\ngarlic sauce'
        onpizza = f'{onpizza}{garlic}'
    if var4.get() == 1:
        total.set(total.get() +0.50)
        bbq = '\nbbq sauce'
        onpizza = f'{onpizza}{bbq}'
    if var5.get() == 1:
        total.set(total.get() +0.50)
        mystery = '\nmystery meat'
        onpizza = f'{onpizza}{mystery}'
    if var6.get() == 1:
        total.set(total.get() +5.00)
        gourmet = '\ngourmet option'
        onpizza = f'{onpizza}{gourmet}'
    if x == 1:
        pizza_order1.set("pizza 1:" + onpizza)
    elif x == 2:
        pizza_order2.set("pizza 2:" + onpizza)
    elif x == 3:
        pizza_order3.set("pizza 3:" + onpizza)
    elif x == 4:
        pizza_order4.set("pizza 4:" + onpizza)
    elif x == 5:
        pizza_order5.set("pizza 5:" + onpizza)


def dcmd():
    forget(buttons)
    add_widget(detail_frame, 1)
    label_text.set('Name?')
    add_widget(name_box,0)
    add_widget(confirmbutton,1)
    add_widget(cancel1,2)
    delvorpick.set('Delivery')

def add_widget(widget, rw = 4, clmn = 0, x = 10, y = 3, clms = 1, rwspn =1):
    widget.grid(row = rw, column = clmn, padx = x, pady = y, columnspan =clms, rowspan= rwspn)

def forget(widget):
    widget.grid_forget()

def confirm():
    if name_box.get().isalpha() == True:
        forget(detail_frame)
        add_widget(address_frame)
        label_text.set('Address?')
        add_widget(address_box,0)
        add_widget(address_confirm,1)
        add_widget(cancel3,2)
        name_boxorder.set('name:{}'.format(name.get()))
    else:
            tk.messagebox.showerror(title="pizza limit", message="please enter a first name")


def acmd():
    if (len(address.get())):
        forget(address_frame)
        add_widget(phone_frame)
        label_text.set('phone number?')
        add_widget(number_box,0)
        add_widget(number_confirm,1)
        add_widget(cancel4,2)
        addressorder.set('address:{}'.format(address.get()))
    else:
            tk.messagebox.showerror(title="pizza limit", message="please enter an address")

def pcmd():
    if number_box.get().isnumeric() == True:
        forget(phone_frame)
        add_widget(master)
        label_text.set('order?')
        phoneorder.set('phone number:{}'.format(number.get()))
    else:
            tk.messagebox.showerror(title="pizza limit", message="please enter a phone number")
def pickcmd():
    forget(buttons)
    add_widget(name2_frame)
    label_text.set('first name?')
    add_widget(name2box, 0, 1, 10, 0, 2)
    add_widget(name2confirm, 1, 1, 0, 1)
    add_widget(cancel2, 1, 2, 0, 1)
    delvorpick.set('Pick up')

def name2cmd():
    if name2box.get().isalpha() == True:
        forget(name2_frame)
        add_widget(master)
        label_text.set('order?')
        name_boxorder2.set('name: {}'.format(name2.get()))
        total.set(total.get() +3.00)
    else:
        tk.messagebox.showerror(title="pizza limit", message="please enter a first name")

def add_pizza():
    global pizza
    pizza += 1
    if pizza == 1:
        show(pizza)
        add_widget(pizza1, 5)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
    elif pizza == 2:
        show(pizza)
        add_widget(pizza2,6)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
    elif pizza == 3:
        show(pizza)
        add_widget(pizza3,7)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
    elif pizza == 4:
        show(pizza)
        add_widget(pizza4,8)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
    elif pizza == 5:
        show(pizza)
        add_widget(pizza5,9)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
    if pizza > 5:
        tk.messagebox.showerror(title="pizza limit", message="pizza limit reached ( limit 5)")

def order_fin():
    if pizza >=1:
        totaltext.set("Total:$ {}".format(total.get()))
        add_widget(totallab, 10)
    else:
        tk.messagebox.showerror(title="pizza limit", message="please select a pizza")

add_widget(orderframe, clmn=1, y=10, rw=1, rwspn =3)

delvorpick = StringVar()
Label(orderframe, textvariable=delvorpick,).grid(row=0, pady=10, padx=10)

name_boxorder = StringVar()
Label(orderframe, textvariable=name_boxorder).grid(row=1, pady=10, padx=10)

name_boxorder2 = StringVar()
Label(orderframe, textvariable=name_boxorder2).grid(row=2, pady=10, padx=10)

addressorder = StringVar()
Label(orderframe, textvariable=addressorder).grid(row=3, pady=10, padx=10)

phoneorder = StringVar()
Label(orderframe, textvariable=phoneorder).grid(row=4, pady=10, padx=10)

totaltext = StringVar()
totallab = Label(orderframe, textvariable=totaltext)

top_text = Label(top, textvariable = label_text, pady = 0)
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

Label(master, text="pizzas :").grid(row=0, sticky=W)

varpizza = IntVar()
varpizza.set(1)
radiocheese = Radiobutton(master, text='Cheese Supreme :$5', variable=varpizza, value=1).grid(row=1, sticky=W)
radioham = Radiobutton(master, text='ham and cheese :$5', variable=varpizza, value=2).grid(row=2, sticky=W)
radiomeat = Radiobutton(master, text='meat!! :$5', variable=varpizza, value=3).grid(row=3, sticky=W)
radionacho = Radiobutton(master, text='nacho chips and cheese :$5', variable=varpizza, value=4).grid(row=4, sticky=W)
radiosupermeat = Radiobutton(master, text='super meat lovers :$5', variable=varpizza, value=5).grid(row=5, sticky=W)
radiogarlic = Radiobutton(master, text='garlic and cheese :$5', variable=varpizza, value=6).grid(row=6, sticky=W)
radiopeperoni = Radiobutton(master, text='peperoni and cheese :$5', variable=varpizza, value=7).grid(row=7, sticky=W)
radioprawn = Radiobutton(master, text='prawn and chorizo :$5', variable=varpizza, value=8).grid(row=8, sticky=W)


Label(master, text="toppings:").grid(row=9, sticky=W)
var1 = IntVar()
Checkbutton(master, text="extra ham :$0.50", variable=var1, onvalue=1, offvalue=0).grid(row=10, sticky=W)
var2 = IntVar()
Checkbutton(master, text="extra cheese :$0.50", variable=var2, onvalue=1, offvalue=0).grid(row=11, sticky=W)
var3 = IntVar()
Checkbutton(master, text="garlic sauce :$0.50", variable=var3, onvalue=1, offvalue=0).grid(row=12, sticky=W)
var4 = IntVar()
Checkbutton(master, text="bbq sauce :$0.50", variable=var4, onvalue=1, offvalue=0).grid(row=13, sticky=W)
var5 = IntVar()
Checkbutton(master, text="mystery meat :$0.50", variable=var5, onvalue=1, offvalue=0).grid(row=14,sticky=W)
var6 = IntVar()
Checkbutton(master, text="make gourmet :$5", variable=var6, onvalue=1, offvalue=0).grid(row=15,sticky=W)
Button(master, text='add pizza',command=add_pizza, cursor="hand2").grid(row=16, sticky=W,pady=4)
Button(master, text='finish order', command=order_fin, cursor="hand2").grid(row=17, sticky=W, pady=4)
Button(master, text='cancel', command=master.quit, cursor="hand2").grid(row=18, sticky=W, pady=4)

pizza_order1= StringVar()
pizza_order1.set('')
pizza1 = Label(orderframe, textvariable=pizza_order1)

pizza_order2= StringVar()
pizza_order2.set('')
pizza2 = Label(orderframe, textvariable=pizza_order2)

pizza_order3= StringVar()
pizza_order3.set('')
pizza3 = Label(orderframe, textvariable=pizza_order3)

pizza_order4= StringVar()
pizza_order4.set('')
pizza4 = Label(orderframe, textvariable=pizza_order4)

pizza_order5= StringVar()
pizza_order5.set('')
pizza5 = Label(orderframe, textvariable=pizza_order5)


window.mainloop()

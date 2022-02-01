import tkinter as tk
from tkinter import ttk
# set global value
wallet = 0.00
# sets drink to proper name
def add_latte():
    drink.set('Latte')
def add_espresso():
    drink.set('Espresso')
def add_cappuccino():
    drink.set('Cappuccino')
# adds money to wallet and sets the balance to wallet amount
def add_two_dollars():
    global balance
    global wallet
    wallet += 2.00
    balance.set(wallet)
def add_one_dollar():
    global balance
    global wallet
    wallet += 1.00
    balance.set(wallet)
def add_quarter():
    global balance
    global wallet
    wallet += 0.25
    balance.set(wallet)

# Checking wallet and drink value and running logic to see if drink and money work out
def make_drink():
    global wallet
    global drink
    global balance
    # latte argument
    if wallet >= 2.50 and drink.get() == 'Latte':
        balance.set(wallet - 2.5)
        wallet = (wallet -2.5)
        message.set('Enjoy Your Drink')
        print(message)
    elif wallet < 2.50 and drink.get() == 'Latte':
        message.set('Add more money')
    # espresso argument
    elif wallet >= 1.50 and drink.get() == 'Espresso':
        balance.set(wallet - 1.5)
        wallet = (wallet -1.5)
        message.set('Enjoy Your Drink')
    elif wallet < 1.50 and drink.get() == 'Espresso':
        message.set('Add more money')
    # cappuccino argument
    elif wallet >= 3.00 and drink.get() == 'Cappuccino':
        balance.set(wallet - 3.00)
        wallet = (wallet -3.0)
        message.set('Enjoy Your Drink')
    elif wallet < 3.00 and drink.get() == 'Cappuccino':
        message.set('Add more money')


# create root
root =tk.Tk()
root.title('Coffee Machine!')
root.geometry('400x200')

# create main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand =True)
# add labels
ttk.Label(frame_home, text="Coffee Maker").grid(column=0, row =0)

#create buttons
ttk.Button(frame_home, text='Latte ($2.50)', command=add_latte).grid(column=0, row=1, columnspan=1)
ttk.Button(frame_home, text='Espresso ($1.50)', command=add_espresso).grid(column=1, row=1, columnspan=1)
ttk.Button(frame_home, text='Cappuccino ($3.00)', command=add_cappuccino).grid(column=2, row=1, columnspan=1)
ttk.Button(frame_home, text='$2.00', command=add_two_dollars).grid(column=0, row=2, columnspan=1)
ttk.Button(frame_home, text='$1.00', command=add_one_dollar).grid(column=1, row=2, columnspan=1)
ttk.Button(frame_home, text='$0.25', command=add_quarter).grid(column=2, row=2, columnspan=1)
ttk.Button(frame_home, text='Make Drink', command=make_drink).grid(column=1, row=5, columnspan=1)


#text boxes
balance = tk.StringVar()
ttk.Entry(frame_home, width=20, textvariable=balance).grid(column=1, row=3, columnspan=1)

drink = tk.StringVar()
ttk.Entry(frame_home, width=20, textvariable=drink).grid(column=1, row=4, columnspan=1)

message = tk.StringVar()
ttk.Entry(frame_home, width=20, textvariable=message).grid(column=1, row=6, columnspan=1)


root.mainloop()

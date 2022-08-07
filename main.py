#โปรแกรม Currency Converter

from cmath import exp
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Program Currency Convertor")
screen_height = root.winfo_screenwidth()
screen_width = root.winfo_screenheight()
root_height = 250
root_width = 300
root_x_cordinate = int((screen_height/2) - (root_width/2))
root_y_cordinate = int((screen_width/2) - (root_height/2))
root.geometry("{}x{}+{}+{}".format(root_width, root_height, root_x_cordinate, root_y_cordinate)) #Place the window on center of the screen 1#

#root.geometry("500x500") #have to use this, if use "center" below
#root.eval("tk::PlaceWindow . center") #Place the window on center of the screen 2#
#root.state("zoomed") #Initialize a window as maximized#
      
rate = "0.0"
from_amount = StringVar()
to_amount = StringVar()

def check_input():
    from_amount = from_input.get()
    try:
        from_amount_float = float(from_amount)
    except:
        rate = "Please type numeric"
        label_rate.configure(text=rate)
    else:
        convert()

def convert():
    from_currency = from_combobox.get()
    if from_currency == "USD":
        from_usd()
    elif from_currency == "NZD":
        from_nzd()
    elif from_currency == "THB":
        from_thb()
    else:
        rate = "0.0"
        label_rate.configure(text=rate)
    

def from_usd():
    from_amount = from_input.get()
    to_currency = to_combobox.get()
    if to_currency == "THB":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 33.5)
        label_rate.configure(text=rate) # update new value for the label
    elif to_currency == "NZD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 1.5)
        label_rate.configure(text=rate) 
    elif to_currency == "USD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 1)
        label_rate.configure(text=rate) 
    else:
        rate = "0.0"
        label_rate.configure(text=rate)

def from_nzd():
    from_amount = from_input.get()
    to_currency = to_combobox.get()
    if to_currency == "THB":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 22)
        label_rate.configure(text=rate) # update new value for the label
    elif to_currency == "NZD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 1)
        label_rate.configure(text=rate) 
    elif to_currency == "USD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float / 1.5)
        label_rate.configure(text=rate) 
    else:
        rate = "0.0"
        label_rate.configure(text=rate)

def from_thb():
    from_amount = from_input.get()
    to_currency = to_combobox.get()
    if to_currency == "THB":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float * 1)
        label_rate.configure(text=rate) # update new value for the label
    elif to_currency == "NZD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float / 22)
        label_rate.configure(text=rate) 
    elif to_currency == "USD":
        from_amount_float = float(from_amount)
        rate = str(from_amount_float / 33.5)
        label_rate.configure(text=rate) 
    else:
        rate = "0.0"
        label_rate.configure(text=rate)


from_input = Entry(textvariable=from_amount, font=50, justify="center", width= 8)
from_input.insert(0, "1")
from_input.pack(expand=YES)
from_combobox = StringVar(value="Select currency")
from_combobox = ttk.Combobox(textvariable=from_combobox, font=50)
from_combobox.pack(expand=YES)
from_combobox["value"] = ("USD", "NZD", "THB")

label_to = Label(text="to", font=50).pack()

to_combobox = StringVar(value="Select currency")
to_combobox = ttk.Combobox(textvariable=to_combobox, font=50)
to_combobox.pack(expand=YES)
to_combobox["value"] = ("THB", "NZD", "USD")

convert_button = Button(text="Convert", font=50, command=check_input)
convert_button.pack(expand=YES)

label_rate = Label(text=rate, font=50)
label_rate.pack(expand=YES)

root.mainloop()

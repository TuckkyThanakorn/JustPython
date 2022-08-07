#โปรแกรม Log in ที่อ่านข้อมูลจาก *.ini มาเป็น dictionary

from re import T
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

def convert():
    A = convert_from_combobox.get()
    B = convert_to_combobox.get()
    if A == "Select currency" and B == "Select currency":
        rate = "0.0"
        label_rate.configure(text=rate) #update new value for the label
    elif (A == "1 USD" and B == "THB"):
        rate = "33.5 THB"
        label_rate.configure(text=rate)
    elif (A == "1 USD" and B == "NZD"):
        rate = "1.4 NZD"
        label_rate.configure(text=rate)
    elif (A == "1 USD" and B == "USD"):
        rate = "1 USD"
        label_rate.configure(text=rate)

currency_from_input = Entry(font=50,justify="center",width=8)
currency_from_input.insert(0, "Amount")
#currency_from_input.pack()
currency_from_combobox = StringVar(value="Select currency")
convert_from_combobox = ttk.Combobox(textvariable=currency_from_combobox, font=50)
#convert_from_combobox.pack()
convert_from_combobox["value"] = ("1 USD", "1 NZD", "1 THB")

label_to = Label(text="to", font=50).pack()

currency_to_input = Entry(font=50,width=10)
currency_to_input.insert(0, "Amount")
#currency_to_input.pack()
currency_to_combobox = StringVar(value="Select currency")
convert_to_combobox = ttk.Combobox(textvariable=currency_to_combobox, font=50)
#convert_to_combobox.pack()
convert_to_combobox["value"] = ("THB", "NZD", "USD")

converse_button = Button(text="Convert", font=50, command=convert)
#converse_button.pack(expand=YES)

label_rate = Label(text=rate, font=50)
label_rate.pack(expand=YES)

root.mainloop()

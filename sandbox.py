from tkinter import *
from tkinter import ttk ###################################

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def selectTown():
    Label(text=choice.get()+" selected").grid(row=2,column=0)

Label(text="Address").grid(row=0,column=0)
choice = StringVar(value="Select town")
combo = ttk.Combobox(textvariable=choice)
combo["value"] = ("Manurewa","East Tamaki","Mout Wellington")
combo.grid(row=0,column=1)
button = Button(text="Submit",command=selectTown).grid(row=1,column=1)

root.mainloop()
#โปรแกรม Currency Converter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Program Currency Convertor")
# root.resizable(False, False)
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
      
def root_close():
    if messagebox.askokcancel("Close", "Do you want to close program?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", root_close)
root.mainloop()

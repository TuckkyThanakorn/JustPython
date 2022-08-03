
#โปรแกรม Log in ที่อ่านข้อมูลจาก *.ini มาเป็น dictionary

from tkinter import *

root = Tk()
root.title("Program Currency Convertor")
screen_height = root.winfo_screenwidth()
screen_width = root.winfo_screenheight()
root_height = 100
root_width = 300
root_x_cordinate = int((screen_height/2) - (root_width/2))
root_y_cordinate = int((screen_width/2) - (root_height/2))
root.geometry("{}x{}+{}+{}".format(root_width, root_height, root_x_cordinate, root_y_cordinate)) #Place the window on center of the screen 1#

#root.geometry("500x500") #have to use this, if use "center" below
#root.eval("tk::PlaceWindow . center") #Place the window on center of the screen 2#
#root.state("zoomed") #Initialize a window as maximized#



root.mainloop()

"""

***************************************************************************************
#tkinter for GUI
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างเปล่าๆ

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

root.mainloop()
*********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความ

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn").pack() #ใช้ pack() ให้โปรแกรมนำไปใช้และอยู่ตำแหน่งบนสุดและตรงกลาง

root.mainloop()
*********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปรับแต่ง properties

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn",font=20,foreground="red",background="yellow").pack()

root.mainloop()
**********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปรับแต่ง properties และปรับตำแหน่งโดยใช้ *.place

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label1_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").place(x=50,y=50)
label2_root = Label(text="Thanakorn",font=20,fg="black",bg="pink").place(x=100,y=100)

root.mainloop()
********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปรับแต่ง properties และปรับตำแหน่งโดยใช้ *.grid

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label1_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").grid(row=0,column=0)
label2_root = Label(text="Thanakorn",font=20,fg="black",bg="pink").grid(row=1,column=0)
label3_root = Label(text="Thanakorn",font=20,fg="yellow",bg="brown").grid(row=1,column=1)

root.mainloop()
**********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีป้อความและปุ่มกด

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").pack()
Button = Button(text="OK",font=30,fg="white",bg="red").pack()

root.mainloop()
**********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปุ่มกดสั่งงานสร้างข้อความ

from tkinter import *

def message():
    print("Hello world!!")
    label_root = Label(text="Thanakorn", font=20, fg="red", bg="yellow").pack()

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").pack()
Button = Button(text="OK",font=30,fg="white",bg="red",command=message).pack()

root.mainloop()
*******************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปุ่มกดสั่งงานสร้างข้อความจากที่ข้อมูลที่กรอก

def message():
    name = txt.get()
    print(name)
    label_root = Label(text=name, font=20, fg="red", bg="yellow").pack()

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").pack()
txt = StringVar()
InputText = Entry(root,textvariable=txt).pack()
Button = Button(text="OK",font=30,fg="white",bg="red",command=message).pack()

root.mainloop()
*********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีข้อความและปุ่มกดสั่งงานสร้างหน้าต่างใหม่

def subwindow1():
    sub1 = Tk()
    sub1.title("SubWindow")
    sub1.geometry("500x500+200+200")

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

label_root = Label(text="Thanakorn",font=20,fg="red",bg="yellow").pack()
Button = Button(text="OK",font=30,fg="white",bg="red",command=subwindow1).pack()

root.mainloop()
********************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีเมนูหลัก

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")


myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Menu1")
myMenu.add_cascade(label="Menu2")


root.mainloop()
***************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีเมนูหลักและเมนูย่อย

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

myMenuItem = Menu()
myMenuItem.add_command(label="New file")
myMenuItem.add_command(label="Open")
myMenuItem.add_command(label="Save")
myMenuItem.add_command(label="Exit")

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Menu1",menu=myMenuItem) #ต้องเอาเมนูย่อยไปไว้เหนือเมนูหลัง เพื่อให้เมนูหลักรู้จักตัวแปรของเมนูย่อย

root.mainloop()
**********************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีเมนูหลักและเมนูย่อยที่สร้างหน้าต่างใหม่อีกตัว

from tkinter import *

def new_window():
    window = Tk()
    window.title("New window")
    window.geometry("500x500+200+200")

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

myMenuItem = Menu()
myMenuItem.add_command(label="New window",command=new_window)
myMenuItem.add_command(label="Open")
myMenuItem.add_command(label="Save")
myMenuItem.add_command(label="Exit")

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Menu1",menu=myMenuItem) #ต้องเอาเมนูย่อยไปไว้เหนือเมนูหลัง เพื่อให้เมนูหลักรู้จักตัวแปรของเมนูย่อยก่อน

root.mainloop()
******************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีเมนูหลักและเมนูย่อยที่สร้างหน้าต่างใหม่อีกตัว และมีไดอะลอกหรือแจ้งเตือน เช่น About

from tkinter import *
import tkinter.messagebox ##########################


def new_window():
    window = Tk()
    window.title("New window")
    window.geometry("500x500+200+200")

def myAbout():
    tkinter.messagebox.showinfo("About","Thanakorn made this JustPython")

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

myMenuItem = Menu()
myMenuItem.add_command(label="New window",command=new_window)
myMenuItem.add_command(label="About",command=myAbout)
myMenuItem.add_command(label="Open")
myMenuItem.add_command(label="Save")
myMenuItem.add_command(label="Exit")

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Menu1",menu=myMenuItem) #ต้องเอาเมนูย่อยไปไว้เหนือเมนูหลัง เพื่อให้เมนูหลักรู้จักตัวแปรของเมนูย่อยก่อน

root.mainloop()
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีเมนูหลักและเมนูย่อยที่สร้างหน้าต่างใหม่อีกตัว และมีไดอะลอกหรือแจ้งเตือน เช่น About
#และปิดโปรแกรมโดยเคำสั่งในเมนูและมีการยืนยันก่อน

from tkinter import *
import tkinter.messagebox ##########################


def new_window():
    window = Tk()
    window.title("New window")
    window.geometry("500x500+200+200")

def myAbout():
    tkinter.messagebox.showinfo("About","Thanakorn made this JustPython")

def exit():
    exit_confirm = tkinter.messagebox.askquestion("Confirmation","Do you want to exit program")
    if exit_confirm == "Yes":
        root.destroy()

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

myMenuItem = Menu()
myMenuItem.add_command(label="New window",command=new_window)
myMenuItem.add_command(label="About",command=myAbout)
myMenuItem.add_command(label="Open")
myMenuItem.add_command(label="Save")
myMenuItem.add_command(label="Exit",command=exit)

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Menu1",menu=myMenuItem) #ต้องเอาเมนูย่อยไปไว้เหนือเมนูหลัง เพื่อให้เมนูหลักรู้จักตัวแปรของเมนูย่อยก่อน

root.mainloop()
***************************************
#การเรียกใช้ tkinter เพื่อสร้างหน้าต่างที่มีการเลือกสีให้ Label

from tkinter import *
from tkinter.colorchooser import * ################################

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def selectColor():
    color = askcolor()
    print(color)
    myLabel = Label(text="Thanakorn",fg=color[1]).pack()

button = Button(text="Choose color",command=selectColor).pack()

root.mainloop()
*******************************
#การเรียกใช้ tkinter กดปุ่มเพื่อเรียกหน้าต่างเลือกไฟล์

from tkinter import *
from tkinter.filedialog import * #################################

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def selectFile():
    file = askopenfilename()
    myLabel = Label(text=file).pack()

button = Button(text="Select file",command=selectFile).pack()

root.mainloop()
*****************************************
#การเรียกใช้ tkinter กดปุ่มเพื่อเรียกหน้าต่างเลือกไฟล์ และอ่านข้อมูลไปแสดงในหน้าต่าง

from tkinter import *
from tkinter.filedialog import * #################################

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def selectFile():
    file = askopenfilename()
    fileData = open(file)
    myLabel = Label(text=fileData.read()).pack()

button = Button(text="Select file",command=selectFile).pack()

root.mainloop()
*****************************************
#การเรียกใช้ radio button เลือกภาษา และสั่งให้มี dialog

from tkinter import *
import tkinter.messagebox #########################

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def showChoice():
    choice = language.get()
    if choice == 1:
        Label(text="Python selected").grid(row=0,column=4) #ใช้ pack ไม่ได้ เพราะ radio button ถูก assign เป็น grid
        tkinter.messagebox.showinfo("Comfirmed","Python selected")
    elif choice == 2:
        Label(text="JAVA selected").grid(row=0,column=6)
        tkinter.messagebox.showinfo("Comfirmed","JAVA selected")
    elif choice == 3:
        Label(text="PHP selected").grid(row=0,column=6)
        tkinter.messagebox.showinfo("Comfirmed","PHP selected")
    else:
        Label(text="C++ selected").grid(row=0,column=6)
        tkinter.messagebox.showinfo("Comfirmed","C++ selected")

language = IntVar()
language.set(0) #set default value

Radiobutton(text="Python",variable=language,value=1,command=showChoice).grid(row=0, column=0)
Radiobutton(text="JAVA",variable=language,value=2,command=showChoice).grid(row=0, column=1)
Radiobutton(text="PHP",variable=language,value=3,command=showChoice).grid(row=0, column=2)
Radiobutton(text="C++",variable=language,value=4,command=showChoice).grid(row=0, column=3)

root.mainloop()
*********************************************
#การเรียกใช้ Checkbutton (มีค่า 0,1) เลือกภาษา และแสดงค่าที่ถูกเลือก

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def showChoice():
    print(language1.get(),language2.get(),language3.get(),language4.get())
    language_set = str(language1.get())+str(language2.get())+str(language3.get())+str(language4.get())
    Label(text=language_set).pack(anchor=W)

language1 = IntVar()
language2 = IntVar()
language3 = IntVar()
language4 = IntVar()

Checkbutton(text="Python",variable=language1).pack(anchor=W) #anchor ระบุั่งที่จะให้แสดงผล (North,South,West,East)
Checkbutton(text="JAVA",variable=language2).pack(anchor=W)
Checkbutton(text="PHP",variable=language3).pack(anchor=W)
Checkbutton(text="C++",variable=language4).pack(anchor=W)

Button(text="Show choice",command=showChoice).pack(anchor=W)

root.mainloop()
*****************************
#การเรียกใช้ Checkbutton (มีค่า 0,1) เลือกภาษา และนำค่าที่ได้ไปสั่งงานต่อ

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

def showChoice():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3 = language3.get()
    choice4 = language4.get()

    if choice1 == 1:
        Label(text="Python selected").pack()
    if choice2 == 1:
        Label(text="JAVA selected").pack()
    if choice3 == 1:
        Label(text="PHP selected").pack()
    if choice4 == 1:
        Label(text="C++ selected").pack()

language1 = IntVar()
language2 = IntVar()
language3 = IntVar()
language4 = IntVar()

Checkbutton(text="Python",variable=language1).pack(anchor=W) #anchor ระบุั่งที่จะให้แสดงผล (North,South,West,East)
Checkbutton(text="JAVA",variable=language2).pack(anchor=W)
Checkbutton(text="PHP",variable=language3).pack(anchor=W)
Checkbutton(text="C++",variable=language4).pack(anchor=W)

Button(text="Show choice",command=showChoice).pack(anchor=W)

root.mainloop()
********************************
#การเรียกใช้ Entry box ที่มีค่า default และมีปุ่ม reset ค่าทั้งหมด

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

Label(text="Firstname").grid(row=0)
Label(text="Surname").grid(row=1)
Label(text="Company").grid(row=2)
Label(text="Salary").grid(row=3)

input_firstname = Entry()
input_firstname.grid(row=0,column=1)
input_firstname.insert(0,"Thanakorn") #set default value

input_surname = Entry()
input_surname.grid(row=1,column=1)
input_surname.insert(0,"Doakkiang")

input_company = Entry()
input_company.grid(row=2,column=1)
input_company.insert(0,"Datamars")

input_salary = Entry()
input_salary.grid(row=3,column=1)
input_salary.insert(0,"4500")

def reset_data():
    input_firstname.delete(0,END)
    input_surname.delete(0,END)
    input_company.delete(0,END)
    input_salary.delete(0,END)

Button(text="Reset all data",command=reset_data).grid(row=4)

root.mainloop()
*****************************************
#การเรียกใช้ Combo Box

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
"""
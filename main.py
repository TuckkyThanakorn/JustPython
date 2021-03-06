"""
*******************************************************************************
#http://168training.com/training/document/python.pdf
*******************************************************************************
X = str(5 + 3)
print(X)
print(type(X))
********************************************************
Input: รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
(บรรทัดละจำนวน) เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน
ชั่วโมง นาที และ วินาที
Process: คำนวณจำนวนวินาทีรวมที่คิดจาก h, m และ s
Output: จำนวนวินาทีรวมทั้งหมดที่คำนวณได้

h = float(input('h = '))
m = float(input('m = '))
s = float(input('s = '))

total_time = str((s+(m*60)+(h*(60*60))))
print("Total Time = "+total_time)
********************************************************
Input: รับสตริงหนึ่งบรรทัด
Process: สร้างสตริงใหม่ที่ทุกอักขระในสตริงที่รับเข้ามาปรากฏซ้ำ
อีกตัว เช่น รับ 'pypy' จะได้สตริง 'ppyyppyy'

total_str = ""
input_str = input("Input String = ")
for i in input_str:
    multi_str = i*2
    total_str += multi_str

print(total_str)
********************************************************
Input: รับสตริงหนึ่งบรรทัด
Process: สร้างสตริงใหม่ที่ทุกอักขระในสตริงที่รับเข้ามาปรากฏซ้ำ
อีกตัว แต่ถ้ามีตัวซ้ำิดกันอยู่แล้ว ก็ไม่ต้องทำซ้ำเช่น รับ
'pythonnnaa' จะได้สตริง 'ppyytthhoonnnaa'

total_str = ""
double = ""
input_str = input("Input String = ")
for i in input_str:
    if double != i*2:
        multi_str = i*2
        double = multi_str
        total_str += multi_str

print(total_str)
********************************************************
จงเขียนโปรแกรมที่รับสตริง เพื่อตรวจสอบว่าสตริงนี้มีเลขซ้ำกันหรือไม่ เช่น ถ้ารับ ...102...89..3.. แบบนี้
ไม่มีเลขซ้ำ แต่ถ้ารับ ...102...89..2.. แบบนี้มีเลขซ้ำ (มีเลข 2 ซ้ำ)
► ข้อมูลนำเข้า
รับสตริงหนึ่งบรรทัด
► ข้อมูลส่งออก
ถ้าสตริงที่รับมามีเลขซ้ำ แสดง True แต่ถ้าไม่มีเลขซ้ำแสดง False

input_str = input("Input String = ")
mem_str = ""
result = False
for i in input_str:
    if i in mem_str:
        result = True
    mem_str += i

print("มีเลขซ้ำ : "+ str(result))
*********************************************************
a = 100
b = "แชมพู"
c = "2 ขวด"

def orderme():
    print("อยากสั่ง %s เพิ่มจัง"%b)

print("รหัส %d"%a)
print(b,c)
print("รหัส %d สั่ง %s จำนวน %s"%(a,b,c))
orderme()
**********************************
การใช้งานและการเรียกฟังก์ชั่น
def test():
    a = 100
    print("a=%d"%a)
    print(a+10)

test()
**********************************
def test(value):
    a = value
    print(a)

test(555)
*********************************
def test():
    a = 10
    b = 15
    summary = a + b
    print(summary)
    return summary

print("Summary ="+str(test()))
*******************************
def test(a, b):
    summary = a + b
    print("a + b")
    return str(summary)

print("Summary = "+test(5, 5))
******************************************************************************
#นำเข้า function จากภายนอก แล้วใส่ argument

import multiply

a = multiply.multiply_2number(5, 5)
print(a)
***********************************
import multiply

print(multiply.multiply_2number(10, 10))
********************************************************************************************
#โปรแกรมจะทำการสร้างไฟล์ datatest.txt แล้วรับค่าการป้อนชื่อ
#สินค้าและราคาสินค้าในหน้าต่าง Python Shell ไปเรื่อยๆ จนกว่า จะพิมพ์ exit ในช่องป้อนชื่อสินค้าและป้อน
#ราคาสินค้าข้อมูลชื่อสินค้าและราคาสินค้าจะถูกจัดเก็บในไฟล์ datatest.txtโดยอัตโนมัติ

line_number = 1
title = ""
amount = ""

fdata = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\datatest.txt","w") #
while True:
    print("หากต้องการออกจากการใช้งาน กรุณาพิมพ์ exit")
    print(line_number)
    title = input("ป้อนชื่อผู้จ่ายเงิน = ")
    if title == "exit" or   amount == "exit":
        break
    amount = input("จำนวนเงินที่จ่าย = ")
    if title == "exit" or   amount == "exit":
        break
    fdata.write("%d ,%s, %s\n"%(line_number, title, amount))
    line_number = line_number+1
fdata.close()

จากตัวอย่าง ให้ลองรันโปรแกรมอีกครั้ง เมื่อเราป้อนข้อมูลชื่อสินค้าและราคาสินค้าใหม่เข้าไป
ข้อมูลใหม่นี้จะไปทับข้อมูลเดิม ทำให้ข้อมูลเดิมหายไป เพราะจากคำสั่งในบรรทัดที่ 2 คือ fdata =
open('C:\\Users\\thana\\PycharmProjects\\JustPython\\datatest.txt)จะพบว่าเมื่อใช้อาร์กิวเมนต์ตัวอักษร 'w'จะทำให้ข้อมูล
ใหม่ไปทับข้อมูลเดิม หากต้องการเพิ่มข้อมูลเข้าไปโดยไม่ใหข้อมูลเดิมสูญหายต้องเปลี่ยนจาก "w" เป็น "a"

a สร้างไฟล์ หรือแก้ไขข้อมููลแบบเพิ่มเติม
w สร้างไฟล์หรือแก้ไขข้อมููลแบบทับซ้ำ
r อ่านข้อูลในไฟล์ที่กำลังเปิดใช้งาน
***************************************
อ่านไฟล์ที่ถูกสร้างจากด้านบน

def read_txt_file():
    file = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\datatest.txt", "r")
    data = file.read()
    print(data)
    file.close()

read_txt_file()
*****************************************
เ#ขียนไฟล์ต่อจากด้านบน **ถ้าไม่มีข้อมูลเลย หรือไม่มีไฟล์เลย ก็จะเริ่มสร้างใหม่

line_number = 0
title = ""
amount = ""

write_data = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\datatest.txt","a")
read_data = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\datatest.txt","r")
data = read_data.readlines()
last_row = len(data)

if last_row != 0:
    line_number = last_row+1
elif last_row == 0:
    line_number += 1

while True:
    print("หากต้องการออกจากการใช้งาน กรุณาพิมพ์ exit")
    print(line_number)
    title = input("ป้อนชื่อผู้จ่ายเงิน = ")
    if title == "exit" or   amount == "exit":
        break
    amount = input("จำนวนเงินที่จ่าย = ")
    if title == "exit" or   amount == "exit":
        break
    write_data.write("%d ,%s, %s\n"%(line_number, title, amount))
    line_number = line_number+1
read_data.close()

<<<<<<< HEAD
#*.read อ่านค่าทั้งหมดในไฟล์ ออกมาเป็น string
#*.readline อ่านค่าบรรทัดแรกในไฟล์ ออกมาเป็น string
#*.readlines อ่านค่าทั้งหมดในไฟล์ ออกมาเป็น list
<<<<<<< HEAD
*******************************************************************************************
#การเชื่อมต่อกับไฟล์ database (*.db) และการอ่านทุก field ในตาราง

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
data = cursor.execute("select*from just_python")
for i in data:
    print(i)

connection.close()
ข้อมูลจะต้องถูกอ่านออกมาที่ละ row เป็นข้อมูลแบบ tuple จึงต้องใช้ for loop ในการอ่าน
**********************************
#การใช้ select สำหรับอ่านเฉพาะ Field ที่ระบุ

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
data = cursor.execute("select firstname, saraly from just_python")
for i in data:
    print(i)

connection.close()
**********************************
#การใช้ select พร้อมเงื่อนไขที่ต้องการอ่านเรคอร์ด

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
data = cursor.execute("select*from just_python where saraly >= 4000")
for i in data:
    print(i)

connection.close()
***********************************
#การใช้ select พร้อมเงื่อนไขและการเรียงข้อมูล
import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
data = cursor.execute("select*from just_python where saraly <= 4000 order by saraly")
for i in data:
    print(i)

connection.close()
***********************************
#การใช้คำสั่ง insert สำหรับเพิ่มข้อมูลลงทุกฟิลด์ของตาราง

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
insert_data = cursor.execute("insert into just_python values(5,"Nat","Trivate","Vulcan",5000)")
data = cursor.execute("select*from just_python")
for i in data:
    #print(i)

connection.close()
************************************
#การใช้คำสั่ง insert สำหรับเพิ่มข้อมูลบางฟิลด์ของตาราง

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
insert_data = cursor.execute("insert into just_python (id_number,first_name,last_name) values (6,"Tawee","Meesuk")")
data = cursor.execute("select*from just_python")
for i in data:
    #print(i)

connection.close()
************************************
#การใช้คeสั่งupdate โดยใช้ร่วมกับคำสั่ง where เพื่อแก้ไขข้อมูลบางเรคอร์ด

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
update_data = cursor.execute("update just_python set first_name = "Chatchalin" where id_number = 1")
data = cursor.execute("select*from just_python")
for i in data:
    #print(i)

connection.close()
************************************
#การใช้คาำสั่ง delete สำหรับลบเรคอร์ดทั้งหมดในตาราง

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
delete_data = cursor.execute("delete from just_python")
data = cursor.execute("select*from just_python")
for i in data:
    #print(i)

connection.close()
***********************************
#การใช้คาำสั่ง delete ร่วมกับคำสั่ง where สำหรับลบบางเรคอร์ดในตาราง

import sqlite3

connection = sqlite3.connect("C:\\Users\\thana\\PycharmProjects\\JustPython\\just_python.db")
cursor = connection.cursor()
delete_data = cursor.execute("delete from just_python where id_number = 1")
data = cursor.execute("select*from just_python")
for i in data:
    #print(i)

connection.close()
*************************************************************************************************************
#mysqlclient database การเรียกดูข้อมูลทั้งหมดในตารางด้วยคำสั่ง select

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("select*from just_python")
for i in cursor.fetchall():
    print(i)

connection.close()
*********************************
#mysqlclient database การเรียกดูข้อมูล 1 record ด้วยคำสั่ง select และ where

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("select*from just_python where id_number = 1")
for i in cursor.fetchall():
    print(i)

connection.close()
*********************************
#mysqlclient database การเรียกดูข้อมูลแบบมีเงื่อนไขด้วยคำสั่ง select และ where

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("select*from just_python where saraly > 3500")
for i in cursor.fetchall():
    print(i)

connection.close()
********************************
#mysqlclient database การเรียกดูข้อมูลแบบมีเงื่อนไขและเรียงลำดับด้วยคำสั่ง select และ where และ order by

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("select*from just_python where saraly > 1000 order by saraly")
for i in cursor.fetchall():
    print(i)

connection.close()
*********************************
#mysqlclient database การเพิ่มเรคอร์ดข้อมูลใหม่ด้วยคำสั่ง insert

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("insert into just_python(id_number,firstname,surname,company,saraly) values (5,"Nat","Trivate","Vulcan",5000)")
for i in cursor.fetchall():
    print(i)

connection.close()
**********************************
#การแก้ไขเรคอร์ดข้อมูลด้วยคำสั่ง update และ where

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("update just_python set firstname = "Chatchalin", surname = "Chinnawat" where id_number =1")
for i in cursor.fetchall():
    print(i)

connection.close()
**********************************
การลบเรคอร์ดข้อมูลด้วยคำสั่ง delete และ where

import MySQLdb

connection = MySQLdb.connect(host="localhost",user ="root",passwd ="51035146",db="just_python")
cursor = connection.cursor()

cursor.execute("delete from just_python where firstname = "Thanakorn"")
for i in cursor.fetchall():
    print(i)

connection.close()
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
"""
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



"""
PySimpleGUI Example 1 - The One-Shot Window
This type of program is called a "one-shot" window because the window is displayed one time,
the values collected, and then it is closed. It doesn't remain open for a long time like you would in a Word Processor.

import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
*************************************
PySimpleGUI Example 2 - Interactive Window
In this example, our window will remain on the screen until the user closes the window or clicks the Quit button.
The main difference between the one-shot window you saw earlier and an interactive window is the addition of an "Event Loop".
The Event Loop reads events and inputs from your window. The heart of your application lives in the event loop.

import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
"""

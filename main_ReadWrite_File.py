"""
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

#*.read อ่านค่าทั้งหมดในไฟล์ ออกมาเป็น string
#*.readline อ่านค่าบรรทัดแรกในไฟล์ ออกมาเป็น string
#*.readlines อ่านค่าทั้งหมดในไฟล์ ออกมาเป็น list
"""
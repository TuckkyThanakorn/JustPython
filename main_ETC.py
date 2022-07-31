"""
*******************************************************************************
#http://168training.com/training/document/python.pdf
*******************************************************************************
X = str(5 + 3)
print(X)
print(type(x))
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
"""
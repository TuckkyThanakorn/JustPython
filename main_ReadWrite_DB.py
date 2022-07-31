"""
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
"""
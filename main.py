
#โปรแกรม Log in ที่อ่านข้อมูลจาก *.ini มาเป็น dictionary

from tkinter import *

root = Tk()
root.title("JustPython")
root.geometry("500x500+0+0")

file_user_config = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\user_config.ini", "r")
user_dict = {}
for line in file_user_config:
    key, value = line.strip().split(",")
    user_dict[key.strip()] = value.strip()
total_user = len(user_dict)
file_user_config.close()

def check_user():
    user_data = user_input.get()
    pass_data = pass_input.get()
    count_user = 0
    for user,password in user_dict.items():
        if user_data == user:
            if pass_data == password:
                print("Logged!!")
                break
            else:
                print("Invalid password!!")
                break
        count_user +=1
        if count_user == total_user:
            print("Invalid user name!!")

print(user_dict)
print(type(user_dict))

user_label = Label(text="User name : ").grid(row=0,column=0)
user_input = Entry(root)
user_input.grid(row=0,column=1)

pass_label = Label(text="Password : ").grid(row=1,column=0)
pass_input = Entry(root)
pass_input.grid(row=1,column=1)

ok_button = Button(text="Log in",command=check_user).grid(row=2,column=1)

root.mainloop()




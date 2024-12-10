from tkinter import *
import datetime
from class_customerinfo import customer_info
import datetime
from board import Board
from main_meal import MainMeals
from sweets import sweets
from appa import Appetizers
from drink import Drinks
from order import order
board=Board()
print(board.passward)

root = Tk()
root.geometry('1000x900')
root.iconbitmap('y.ico')
root.title("WeZo Restourant.")


f1 = Frame(root, bg='black', height=900, width=300)
f1.pack(side=LEFT, fill=BOTH,expand=True)  
f2 = Frame(root, bg='#FEAD33', height=900, width=700)
f2.pack(side=LEFT, fill=BOTH, expand=True)  

img_manu1 = PhotoImage(file='y1.png')
img_manu2 = PhotoImage(file='y2.png')
img_manu3 = PhotoImage(file='y3.png')
img_manu4 = PhotoImage(file='y4.png')
img_manu5 = PhotoImage(file='y5.png')
img_manu6 = PhotoImage(file='y6.png')
img_manu7 = PhotoImage(file='y7.png')
img_manu8 = PhotoImage(file='y8.png')


title_main = Label(f2, text='Main meal', font=('Tajawal', 13),  bg='#022841', fg='#E5E2D9', width=78)
title_main.pack(fill=X, pady=5)  


frame_main_meal = Frame(f2, bg='#FEAD33')  
frame_main_meal.pack(fill=X, pady=20)  
m1 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu3, text='Meat', compound=TOP)
m1.pack(side=LEFT, padx=10)
m2 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu4, text='Chiken', compound=TOP)
m2.pack(side=LEFT, padx=10)


title_sweet = Label(f2, text='Sweet', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_sweet.pack(fill=X, pady=5)


frame_sweet = Frame(f2, bg='#FEAD33')
frame_sweet.pack(fill=X, pady=20)
m3 = Button(frame_sweet, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu1, text='Basbosa', compound=TOP)
m3.pack(side=LEFT, padx=10)
m4 = Button(frame_sweet, width=200,bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu2, text='Knafeh', compound=TOP)
m4.pack(side=LEFT, padx=10)


title_drink = Label(f2, text='Drink', font=('Tajawal', 13),  bg='#022841', fg='#E5E2D9', width=78)
title_drink.pack(fill=X, pady=5)


frame_drink = Frame(f2, bg='#FEAD33')
frame_drink.pack(fill=X, pady=20)
m5 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu5, text='Orange', compound=TOP)
m5.pack(side=LEFT, padx=10)
m6 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu6, text='Mango', compound=TOP)
m6.pack(side=LEFT, padx=10)


title_appetizers = Label(f2, text='Appetizers', font=('Tajawal', 13),  bg='#022841', fg='#E5E2D9', width=78)
title_appetizers.pack(fill=X, pady=5)


frame_appetizers = Frame(f2, bg='#FEAD33')
frame_appetizers.pack(fill=X, pady=20)
m7 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu7, text='Tahini', compound=TOP)
m7.pack(side=LEFT, padx=10)
m6 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu8, text='Salad', compound=TOP)
m6.pack(side=LEFT, padx=10)
def enter_name():
    
    frame_name = Frame(f1,bg='#022841')
    frame_name.pack(pady=10, padx=10, anchor=W)

    
    f_name_label = Label(frame_name, bg='#022841',fg="white" ,text='Name         ', font=('Tajawal', 16))  
    f_name_label.pack(side=LEFT, padx=10)  

    
    f_name_entry = Entry(frame_name, font=('Tajawal', 16), width=16)  
    f_name_entry.pack(side=LEFT, padx=10)  

    
    frame_num = Frame(f1,bg='#022841')
    frame_num.pack(pady=10, padx=10, anchor=W)

    
    f_num_label = Label(frame_num, bg='#022841',fg="white" ,text='Phone number', font=('Tajawal', 16))  
    f_num_label.pack(side=LEFT, padx=10)  

    
    f_num_entry = Entry(frame_num, font=('Tajawal', 14), width=15)  
    f_num_entry.pack(side=LEFT, padx=10) 
def seting():
    # نافذة الإعدادات
    setting = Toplevel(root)
    setting.geometry('350x250')
    setting.title("Settings")

    # تعليمات الإدخال
    label = Label(setting, text='Please enter password:', font=('Tajawal', 12))
    label.grid(row=0, column=0, padx=10, pady=10)

    # إدخال كلمة المرور
    password_entry = Entry(setting, font=('Tajawal', 14))
    password_entry.grid(row=0, column=1, padx=10, pady=10)

    # دالة التحقق
    def enter():
        input_password = password_entry.get().strip()
        print(input_password)
        if input_password ==str( board.passward):  
            success_window = Toplevel(root)
            success_window.geometry('200x100')
            Label(success_window, text="Access granted!", fg="green", font=('Tajawal', 12)).pack(pady=20)
        else:
            Label(setting, text="Incorrect password!", fg="red", font=('Tajawal', 10)).grid(row=2, column=1, padx=10, pady=10)

    # زر التحقق
    check_button = Button(setting, text="Enter", font=('Tajawal', 12), bg='#022841', fg="white", command=enter)
    check_button.grid(row=1, column=1, padx=10, pady=10)

start = Button(f1, width=40, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=2, text='Add order', compound=TOP,command=enter_name)
start.pack(padx=10, pady=5)
seting = Button(f1, width=40, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=2, text='Settings', compound=LEFT,command=seting)
seting.pack(padx=10, pady=5)
root.mainloop()

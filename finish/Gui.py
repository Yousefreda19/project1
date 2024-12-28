from tkinter import *
import datetime
from class_customerinfo import customer_info
import datetime
from board import Board
from class_customerinfo import customer_info
from meal_class import main_class, MainMeals, Appetizer, drink, sweet
from order import order
from bill import Bill
from order import order
from bill import Bill
board=Board()
order = order()
new_order = customer_info()
meals = MainMeals()
sweet = sweet()
drinks = drink()
appetizer = Appetizer()
bill = Bill()

root = Tk()
root.geometry('1000x900')
root.iconbitmap('y.ico')
root.title("WeZo Restourant.")


f1 = Frame(root, bg='black', height=900, width=300)
f1.pack(side=LEFT, fill=BOTH,expand=True)  
f2 = Frame(root, bg='#FEAD33', height=900, width=700)
f2.pack(side=LEFT, fill=BOTH, expand=True)  
canvas = Canvas(f2, bg='#FEAD33')
scrollbar = Scrollbar(f2, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=True)


f2 = Frame(canvas, bg='#FEAD33')
canvas.create_window((0, 0), window=f2, anchor='nw')
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

f2.bind("<Configure>", update_scrollregion)


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
m1 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu3, text=f'Meat  {meals.list[0][1]} EGP', compound=TOP)
m1.pack(side=LEFT, padx=10)
m2 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu4, text=f'Chiken  {meals.list[1][1]} EGP', compound=TOP)
m2.pack(side=LEFT, padx=10)


title_sweet = Label(f2, text='Sweet', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_sweet.pack(fill=X, pady=5)


frame_sweet = Frame(f2, bg='#FEAD33')
frame_sweet.pack(fill=X, pady=20)
m3 = Button(frame_sweet, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu1, text=f'Basbosa   {sweet.list[0][1]} EGP', compound=TOP)
m3.pack(side=LEFT, padx=10)
m4 = Button(frame_sweet, width=200,bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu2, text=f'Knafeh   {sweet.list[1][1]} EGP', compound=TOP)
m4.pack(side=LEFT, padx=10)


title_drink = Label(f2, text='Drink', font=('Tajawal', 13),  bg='#022841', fg='#E5E2D9', width=78)
title_drink.pack(fill=X, pady=5)


frame_drink = Frame(f2, bg='#FEAD33')
frame_drink.pack(fill=X, pady=20)
m5 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu5, text=f'Orange   {drinks.list[0][1]} EGP', compound=TOP)
m5.pack(side=LEFT, padx=10)
m6 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu6, text=f'Mango   {drinks.list[1][1]} EGP', compound=TOP)
m6.pack(side=LEFT, padx=10)


title_appetizers = Label(f2, text='Appetizers', font=('Tajawal', 13),  bg='#022841', fg='#E5E2D9', width=78)
title_appetizers.pack(fill=X, pady=5)


frame_appetizers = Frame(f2, bg='#FEAD33')
frame_appetizers.pack(fill=X, pady=20)
m7 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu7, text=f'Tahini   {drinks.list[0][1]} EGP', compound=TOP)
m7.pack(side=LEFT, padx=10)
m6 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu8, text=f'Salad     {drinks.list[1][1]} EGP', compound=TOP)
m6.pack(side=LEFT, padx=10)
def enter_name():
    for widget in f1.winfo_children():
        widget.destroy()

    customer_name = StringVar()
    customer_phone = StringVar()

    frame_name = Frame(f1, bg='#022841')
    frame_name.pack(pady=10, padx=10, anchor=W)

    f_name_label = Label(frame_name, bg='#022841', fg="white", text='Name         ', font=('Tajawal', 16))  
    f_name_label.pack(side=LEFT, padx=10)

    f_name_entry = Entry(frame_name, font=('Tajawal', 16), width=16, textvariable=customer_name)  
    f_name_entry.pack(side=LEFT, padx=10)

    frame_num = Frame(f1, bg='#022841')
    frame_num.pack(pady=10, padx=10, anchor=W)

    f_num_label = Label(frame_num, bg='#022841', fg="white", text='Phone number', font=('Tajawal', 16))  
    f_num_label.pack(side=LEFT, padx=10)

    f_num_entry = Entry(frame_num, font=('Tajawal', 14), width=15, textvariable=customer_phone)  
    f_num_entry.pack(side=LEFT, padx=10)

    def save_info():
        name = customer_name.get()
        phone = customer_phone.get()

        if name and phone:  
            new_order.name = name
            new_order.phone = phone
            print(f"Name: {name}, Phone: {phone}")  

            
            frame_orders = Frame(f1, bg='white')
            frame_orders.pack(fill=BOTH, expand=True,side=LEFT,pady=50, padx=10)  


            order_label = Label(frame_orders, text="Your Order", font=('Tajawal', 14), fg='black')
            order_label.pack(pady=10)
            btn21 = Button(frame_orders, text="Finish", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20)
            btn21.pack(pady=10,side=BOTTOM)

           

           

        else:
            Label(f1, text="Please fill in all fields.", bg='#022841', fg="red", font=('Tajawal', 12)).pack(pady=5)

    next_button = Button(f1, text="Next", font=('Tajawal', 12), bg='#022841', fg="white", command=save_info)
    next_button.pack(pady=20)


def seting():
    
    setting = Toplevel(root)
    setting.geometry('350x250')
    setting.title("Settings")

    
    label = Label(setting, text='Please enter password:', font=('Tajawal', 12))
    label.grid(row=0, column=0, padx=10, pady=10)


    password_entry = Entry(setting, font=('Tajawal', 14),show='*')
    password_entry.grid(row=0, column=1, padx=10, pady=10)


    def enter():
     input_password = password_entry.get().strip()
     if input_password == str(board.passward):  
        
        success_window = Toplevel(root)
        success_window.geometry('500x200')
        success_window.title("Success")

        frame_buttons = Frame(success_window, bg='#FEAD33',height=1200,width=750)
        frame_buttons.pack(pady=20, padx=20, fill=BOTH, expand=True)

        
        btn1 = Button(frame_buttons, text="Add meals ", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20 ,command=add)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = Button(frame_buttons, text="Delete meal ", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20, command=deleted)
        btn2.grid(row=0, column=1, padx=10, pady=10)

        btn3 = Button(frame_buttons, text="change price ", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20, command=change_price)
        btn3.grid(row=5, column=0, padx=10, pady=10)

        btn4 = Button(frame_buttons, text="change amount ", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20, command=change_amount)
        btn4.grid(row=5, column=1, padx=10, pady=10)

     else:
        
        Label(setting, text="Incorrect password!", fg="red", font=('Tajawal', 10)).grid(row=2, column=1, padx=10, pady=10)
          


    
    check_button = Button(setting, text="Enter", font=('Tajawal', 12), bg='#022841', fg="white", command=enter)
    check_button.grid(row=1, column=1, padx=10, pady=10)

start = Button(f1, width=40, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=2, text='Add order', compound=TOP,command=enter_name)
start.pack(padx=10, pady=5)
seting = Button(f1, width=40, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=2, text='Settings', compound=LEFT,command=seting)
seting.pack(padx=10, pady=5)
def add():

    fullscreen_frame = Toplevel(root)
    fullscreen_frame.attributes("-fullscreen", True)  
    
    
    button_frame = Frame(fullscreen_frame, bg='#022841', width=200)
    button_frame.pack(side="left", fill=Y)  
    def show_input_fields():
        
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        
        Label(content_frame, text="Name Meal", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=0, column=1, padx=10, pady=10)
        
        Label(content_frame, text="Price", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=1, column=1, padx=10, pady=10)
        
        Label(content_frame, text="Amount", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=2, column=1, padx=10, pady=10)
        save_button = Button(content_frame, text="Save", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20)
        save_button.grid(row=3, columnspan=2, pady=20)
    btn1 = Button(button_frame, text="Main Meal",bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn1.pack(pady=10, padx=5)

    btn2 = Button(button_frame, text="Sweeet", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn2.pack(pady=10, padx=5)

    btn3 = Button(button_frame, text="Drink", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn3.pack(pady=10, padx=5)
    btn5 = Button(button_frame, text="Appetizer", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=show_input_fields)
    btn5.pack(pady=10, padx=5)

    btn4 = Button(button_frame, text="Exit Fullscreen", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=fullscreen_frame.destroy)
    btn4.pack(pady=10, padx=5)

    
    content_frame = Frame(fullscreen_frame, bg='#FEAD33')
    content_frame.pack(side="right", fill=BOTH, expand=True)

    label = Label(content_frame, text="Add Meal My Boss", font=("Arial", 30), bg='#022841', fg="white")
    label.pack(pady=50)
def deleted():

    fullscreen_frame = Toplevel(root)
    fullscreen_frame.attributes("-fullscreen", True)  
    
    
    button_frame = Frame(fullscreen_frame, bg='#022841', width=200)
    button_frame.pack(side="left", fill=Y)  
    def show_input_fields():
        
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        
        Label(content_frame, text="Num of Meal", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=0, column=1, padx=10, pady=10)
        save_button = Button(content_frame, text="Save", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20)
        save_button.grid(row=3, columnspan=2, pady=20)
       

    
    btn1 = Button(button_frame, text="Main Meal",bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn1.pack(pady=10, padx=5)

    btn2 = Button(button_frame, text="Sweeet", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn2.pack(pady=10, padx=5)

    btn3 = Button(button_frame, text="Drink", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn3.pack(pady=10, padx=5)
    btn5 = Button(button_frame, text="Appetizer", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=show_input_fields)
    btn5.pack(pady=10, padx=5)

    btn4 = Button(button_frame, text="Exit Fullscreen", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=fullscreen_frame.destroy)
    btn4.pack(pady=10, padx=5)

    
    content_frame = Frame(fullscreen_frame, bg='#FEAD33')
    content_frame.pack(side="right", fill=BOTH, expand=True)

    label = Label(content_frame, text="Delete Meal My Boss", font=("Arial", 30), bg='#022841', fg="white")
    label.pack(pady=50) 
def change_price():

    fullscreen_frame = Toplevel(root)
    fullscreen_frame.attributes("-fullscreen", True)  
    
    
    button_frame = Frame(fullscreen_frame, bg='#022841', width=200)
    button_frame.pack(side="left", fill=Y)  
    def show_input_fields():
        
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        
        Label(content_frame, text="Num of Meal", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=0, column=1, padx=10, pady=10)
        
        Label(content_frame, text="NEW Price", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=1, column=1, padx=10, pady=10)
        save_button = Button(content_frame, text="Save", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20)
        save_button.grid(row=3, columnspan=2, pady=20)
       

    
    btn1 = Button(button_frame, text="Main Meal",bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn1.pack(pady=10, padx=5)

    btn2 = Button(button_frame, text="Sweeet", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn2.pack(pady=10, padx=5)

    btn3 = Button(button_frame, text="Drink", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn3.pack(pady=10, padx=5)
    btn5 = Button(button_frame, text="Appetizer", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=show_input_fields)
    btn5.pack(pady=10, padx=5)

    btn4 = Button(button_frame, text="Exit Fullscreen", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=fullscreen_frame.destroy)
    btn4.pack(pady=10, padx=5)

    
    content_frame = Frame(fullscreen_frame, bg='#FEAD33')
    content_frame.pack(side="right", fill=BOTH, expand=True)

    label = Label(content_frame, text=" change price My Boss", font=("Arial", 30), bg='#022841', fg="white")
    label.pack(pady=50)      

def change_amount():

    fullscreen_frame = Toplevel(root)
    fullscreen_frame.attributes("-fullscreen", True)  
    
    
    button_frame = Frame(fullscreen_frame, bg='#022841', width=200)
    button_frame.pack(side="left", fill=Y)  
    def show_input_fields():
        
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        
        Label(content_frame, text="Num of Meal", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=0, column=1, padx=10, pady=10)
        
        
        
        Label(content_frame, text="Amount", font=("Arial", 16), bg="#FEAD33", fg="black").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(content_frame, font=("Arial", 14), width=20).grid(row=2, column=1, padx=10, pady=10)
        save_button = Button(content_frame, text="Save", font=('Tajawal', 12), bg='#022841', fg="white", height=2, width=20)
        save_button.grid(row=3, columnspan=2, pady=20)
    
    btn1 = Button(button_frame, text="Main Meal",bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn1.pack(pady=10, padx=5)

    btn2 = Button(button_frame, text="Sweeet", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn2.pack(pady=10, padx=5)

    btn3 = Button(button_frame, text="Drink", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15, command=show_input_fields)
    btn3.pack(pady=10, padx=5)
    btn5 = Button(button_frame, text="Appetizer", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=show_input_fields)
    btn5.pack(pady=10, padx=5)

    btn4 = Button(button_frame, text="Exit Fullscreen", bg='#022841', font=('Tajawal', 11), fg="white", height=2, width=15,command=fullscreen_frame.destroy)
    btn4.pack(pady=10, padx=5)

    
    content_frame = Frame(fullscreen_frame, bg='#FEAD33')
    content_frame.pack(side="right", fill=BOTH, expand=True)

    label = Label(content_frame, text=" change amount My Boss", font=("Arial", 30), bg='#022841', fg="white")
    label.pack(pady=50)
       
root.mainloop()

from tkinter import *
import datetime

root = Tk()
root.geometry('1000x900')
root.iconbitmap('y.ico')
root.title("WeZo Restourant.")

# إطار جانبي f1
f1 = Frame(root, bg='black', width=300)
f1.pack(side=LEFT, fill=BOTH, expand=True)

# إطار رئيسي يحتوي على شريط التمرير و Canvas
main_frame = Frame(root, bg='#FEAD33')
main_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Canvas لإضافة خاصية التمرير
canvas = Canvas(main_frame, bg='#FEAD33')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# شريط التمرير العمودي
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# إعداد ارتباط بين Canvas وشريط التمرير
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# إطار داخلي لإضافة المحتوى داخل Canvas
content_frame = Frame(canvas, bg='#FEAD33')
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# تحميل الصور
img_manu1 = PhotoImage(file='y1.png')
img_manu2 = PhotoImage(file='y2.png')
img_manu3 = PhotoImage(file='y3.png')
img_manu4 = PhotoImage(file='y4.png')
img_manu5 = PhotoImage(file='y5.png')
img_manu6 = PhotoImage(file='y6.png')
img_manu7 = PhotoImage(file='y7.png')
img_manu8 = PhotoImage(file='y8.png')

# المحتوى
title_main = Label(content_frame, text='Main meal', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_main.pack(fill=BOTH, pady=5)

frame_main_meal = Frame(content_frame, bg='#FEAD33')
frame_main_meal.pack(fill=X, pady=20)
m1 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu3, text='Meat', compound=TOP)
m1.pack(side=LEFT, padx=10)
m2 = Button(frame_main_meal, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu4, text='Chicken', compound=TOP)
m2.pack(side=LEFT, padx=10)

title_sweet = Label(content_frame, text='Sweet', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_sweet.pack(fill=X, pady=5)

frame_sweet = Frame(content_frame, bg='#FEAD33')
frame_sweet.pack(fill=X, pady=20)
m3 = Button(frame_sweet, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu1, text='Basbosa', compound=TOP)
m3.pack(side=LEFT, padx=10)
m4 = Button(frame_sweet, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu2, text='Knafeh', compound=TOP)
m4.pack(side=LEFT, padx=10)

title_drink = Label(content_frame, text='Drink', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_drink.pack(fill=X, pady=5)

frame_drink = Frame(content_frame, bg='#FEAD33')
frame_drink.pack(fill=X, pady=20)
m5 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu5, text='Orange', compound=TOP)
m5.pack(side=LEFT, padx=10)
m6 = Button(frame_drink, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu6, text='Mango', compound=TOP)
m6.pack(side=LEFT, padx=10)

title_appetizers = Label(content_frame, text='Appetizers', font=('Tajawal', 13), bg='#022841', fg='#E5E2D9', width=78)
title_appetizers.pack(fill=X, pady=5)

frame_appetizers = Frame(content_frame, bg='#FEAD33')
frame_appetizers.pack(fill=X, pady=20)
m7 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu7, text='Tahini', compound=TOP)
m7.pack(side=LEFT, padx=10)
m8 = Button(frame_appetizers, width=200, bg='#022841', font=('Tajawal', 11), fg="white", bd=0, relief=FLAT, cursor='hand2', height=200, image=img_manu8, text='Salad', compound=TOP)
m8.pack(side=LEFT, padx=10)

root.mainloop()

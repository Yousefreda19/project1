import tkinter as tk

# دالة لإخفاء النافذة عند تحريك الفأرة خارجها
def hide_window(event):
    root.withdraw()  # إخفاء النافذة

# دالة لعرض النافذة عند تحريك الفأرة داخلها
def show_window(event):
    root.deiconify()  # إظهار النافذة

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("نافذة مع شريط تمرير")
root.geometry("400x400")  # حجم النافذة

# إنشاء إطار يحتوي على المحتوى الذي سيظهر في النافذة
frame = tk.Frame(root)

# إضافة شريط التمرير العمودي
scrollbar = tk.Scrollbar(frame, orient="vertical")

# إنشاء Canvas يحتوي على المحتوى الذي نريد التمرير فيه
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set, width=380, height=380)
canvas.pack(side="left", fill="both", expand=True)

# ربط شريط التمرير مع الـ Canvas
scrollbar.config(command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# إنشاء إطار داخل الـ Canvas لتخزين المكونات التي سيتم التمرير من خلالها
inner_frame = tk.Frame(canvas)

# إضافة مكونات داخل الـ Frame الداخلي
for i in range(30):  # يمكنك تعديل هذا الرقم لإضافة المزيد من المكونات
    label = tk.Label(inner_frame, text=f"عنصر {i+1}", width=30, height=2)
    label.pack()

# إضافة الـ Frame الداخلي إلى الـ Canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# تحديث منطقة التمرير عندما يتغير حجم الـ Frame الداخلي
inner_frame.update_idletasks()

# تحديد منطقة التمرير بشكل صحيح بناءً على حجم المكونات
canvas.config(scrollregion=canvas.bbox("all"))

# إضافة الـ Frame إلى النافذة
frame.pack(fill="both", expand=True)

# إضافة أحداث الفأرة
root.bind("<Enter>", show_window)  # عند دخول الفأرة داخل النافذة
root.bind("<Leave>", hide_window)  # عند خروج الفأرة من النافذة

# إبقاء النافذة مفتوحة
root.mainloop()

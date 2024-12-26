import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def initialize_database():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        default_menu = [
            ("Pizza", 12),
            ("Burger", 8),
            ("Pasta", 10),
            ("Coke", 2),
            ("Ice Cream", 4),
        ]
        cursor.executemany("INSERT INTO menu (name, price) VALUES (?, ?)", default_menu)
    conn.commit()
    conn.close()


class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("900x600")

        self.order_items = []
        self.total_price = 0

        self.conn = sqlite3.connect("restaurant.db")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.create_menu_tab()
        self.create_order_tab()
        self.create_billing_tab()

    def create_menu_tab(self):
        self.menu_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.menu_tab, text="Menu")

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM menu")
        menu_items = cursor.fetchall()

        row = 0
        for item_id, name, price in menu_items:
            tk.Label(self.menu_tab, text=f"{name} - ${price}", font=("Arial", 12)).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            tk.Button(
                self.menu_tab, text="Add to Order", command=lambda name=name, price=price: self.add_to_order(name, price)
            ).grid(row=row, column=1, padx=10, pady=5)
            row += 1

    def create_order_tab(self):
        self.order_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.order_tab, text="Order")

        self.order_listbox = tk.Listbox(self.order_tab, width=50, height=20)
        self.order_listbox.pack(pady=10)

        tk.Button(
            self.order_tab, text="Clear Order", command=self.clear_order, bg="red", fg="white"
        ).pack(pady=5)

    def create_billing_tab(self):
        self.billing_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.billing_tab, text="Billing")

        self.total_label = tk.Label(self.billing_tab, text="Total: $0", font=("Arial", 16))
        self.total_label.pack(pady=20)

        self.bill_button = tk.Button(
            self.billing_tab, text="Generate Bill", command=self.generate_bill, bg="green", fg="white"
        )
        self.bill_button.pack(pady=5)

    def add_to_order(self, name, price):
        self.order_items.append((name, price))
        self.order_listbox.insert(tk.END, f"{name} - ${price}")
        self.update_total()

    def clear_order(self):
        self.order_items.clear()
        self.order_listbox.delete(0, tk.END)
        self.update_total()

    def update_total(self):
        self.total_price = sum(price for _, price in self.order_items)
        self.total_label.config(text=f"Total: ${self.total_price}")

    def generate_bill(self):
        if not self.order_items:
            messagebox.showerror("Error", "No items in order!")
            return

        cursor = self.conn.cursor()
        cursor.executemany("INSERT INTO orders (item_name, price) VALUES (?, ?)", self.order_items)
        self.conn.commit()

        bill_window = tk.Toplevel(self.root)
        bill_window.title("Bill")
        bill_window.geometry("400x400")

        tk.Label(bill_window, text="Bill Details", font=("Arial", 16, "bold")).pack(pady=10)
        for name, price in self.order_items:
            tk.Label(bill_window, text=f"{name}: ${price}", font=("Arial", 12)).pack()
        tk.Label(bill_window, text=f"Total: ${self.total_price}", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Button(bill_window, text="Close", command=bill_window.destroy).pack(pady=10)
        self.clear_order()


if __name__ == "__main__":
    initialize_database()
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()

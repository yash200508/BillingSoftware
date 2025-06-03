import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import database

UNITS = ['pieces', 'grams', 'liters']

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Store Billing Software")
        self.root.geometry("900x600")

        database.init_db()
        self.sidebar_menu()
        self.init_main_frame()
        self.show_billing_page()

    def sidebar_menu(self):
        sidebar = tk.Frame(self.root, bg="#2c3e50", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        buttons = [("Billing", self.show_billing_page),
                   ("Manage Items", self.show_manage_items_page),
                   ("Credits", self.show_credits_page)]
        for text, command in buttons:
            btn = tk.Button(sidebar, text=text, command=command, fg="white", bg="#34495e", height=2)
            btn.pack(fill=tk.X)

    def init_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_billing_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Billing Section", font=('Arial', 16)).pack()

        self.bill_items = []
        self.total_amount = tk.DoubleVar(value=0.0)

        entry_frame = tk.Frame(self.main_frame)
        entry_frame.pack()

        self.code_entry = tk.Entry(entry_frame)
        self.code_entry.grid(row=0, column=0)
        self.qty_entry = tk.Entry(entry_frame)
        self.qty_entry.grid(row=0, column=1)
        self.unit_dropdown = ttk.Combobox(entry_frame, values=UNITS, state='readonly')
        self.unit_dropdown.grid(row=0, column=2)
        self.unit_dropdown.set(UNITS[0])

        tk.Button(entry_frame, text="Add Item", command=self.add_item_to_bill).grid(row=0, column=3)

        self.bill_list = tk.Listbox(self.main_frame, height=15, width=80)
        self.bill_list.pack(pady=10)

        tk.Label(self.main_frame, text="Total:").pack()
        tk.Label(self.main_frame, textvariable=self.total_amount, font=("Arial", 14)).pack()

        payment_frame = tk.Frame(self.main_frame)
        payment_frame.pack(pady=10)
        tk.Label(payment_frame, text="Payment Method:").grid(row=0, column=0)
        self.payment_method = ttk.Combobox(payment_frame, values=["Cash", "UPI", "Credit"], state='readonly')
        self.payment_method.set("Cash")
        self.payment_method.grid(row=0, column=1)
        tk.Button(payment_frame, text="Finish Bill", command=self.finish_bill).grid(row=0, column=2)

    def add_item_to_bill(self):
        code = self.code_entry.get()
        qty = self.qty_entry.get()
        unit = self.unit_dropdown.get()

        item = database.get_item_by_code(code)
        if not item:
            messagebox.showerror("Error", "Item code not found!")
            return
        try:
            qty = float(qty)
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity!")
            return

        name, price_per_unit, expected_unit = item[1], item[2], item[3]
        if unit != expected_unit:
            messagebox.showerror("Error", f"This item is sold in {expected_unit}")
            return

        price = float(price_per_unit) * qty
        self.bill_items.append((name, qty, unit, price))
        self.bill_list.insert(tk.END, f"{name} - {qty} {unit} - ₹{price:.2f}")
        self.total_amount.set(self.total_amount.get() + price)

    def finish_bill(self):
        method = self.payment_method.get()
        if method == "Credit":
            customer = simpledialog.askstring("Credit Customer", "Enter Customer Name:")
            if customer:
                database.save_credit(customer, self.total_amount.get())
        messagebox.showinfo("Bill", f"Payment received via {method}.\nTotal: ₹{self.total_amount.get():.2f}")
        self.show_billing_page()

    def show_manage_items_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Manage Items", font=('Arial', 16)).pack(pady=5)

        table = tk.Frame(self.main_frame)
        table.pack()

        tk.Label(table, text="Code").grid(row=0, column=0)
        tk.Label(table, text="Name").grid(row=0, column=1)
        tk.Label(table, text="Price/Unit").grid(row=0, column=2)
        tk.Label(table, text="Unit").grid(row=0, column=3)

        code_entry = tk.Entry(table)
        name_entry = tk.Entry(table)
        price_entry = tk.Entry(table)
        unit_combo = ttk.Combobox(table, values=UNITS, state='readonly')
        unit_combo.set(UNITS[0])

        code_entry.grid(row=1, column=0)
        name_entry.grid(row=1, column=1)
        price_entry.grid(row=1, column=2)
        unit_combo.grid(row=1, column=3)

        def add_item():
            code = code_entry.get()
            name = name_entry.get()
            price = price_entry.get()
            unit = unit_combo.get()
            if not code or not name or not price:
                messagebox.showerror("Error", "All fields required")
                return
            try:
                price = float(price)
            except:
                messagebox.showerror("Error", "Price must be a number")
                return
            database.add_or_update_item(code, name, price, unit)
            self.show_manage_items_page()

        tk.Button(table, text="Add / Update Item", command=add_item).grid(row=2, column=1, columnspan=2, pady=5)

        tk.Label(self.main_frame, text="Current Items", font=('Arial', 12)).pack()
        listbox = tk.Listbox(self.main_frame, height=15, width=60)
        listbox.pack()
        for i in database.get_all_items():
            listbox.insert(tk.END, f"{i[0]} - {i[1]} - ₹{i[2]} per {i[3]}")

    def show_credits_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Credit Customers", font=('Arial', 16)).pack()
        listbox = tk.Listbox(self.main_frame, height=20, width=80)
        listbox.pack()
        for row in database.get_all_credits():
            listbox.insert(tk.END, f"{row[0]} - ₹{row[1]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

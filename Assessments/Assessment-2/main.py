import tkinter as tk
from tkinter import messagebox
from billing_logic import BillingSystem
from models import Customer, Product

class BillingApp:
    def __init__(self, root):
        self.system = BillingSystem()
        self.products = []

        self.root = root
        self.root.title("Billing Application")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Customer Name").grid(row=0, column=0)
        tk.Label(self.root, text="Phone").grid(row=1, column=0)
        tk.Label(self.root, text="Balance").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.root)
        self.phone_entry = tk.Entry(self.root)
        self.balance_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)
        self.balance_entry.grid(row=2, column=1)

        # Product Fields
        tk.Label(self.root, text="Product Name").grid(row=3, column=0)
        tk.Label(self.root, text="Price").grid(row=4, column=0)
        tk.Label(self.root, text="Quantity").grid(row=5, column=0)

        self.pname = tk.Entry(self.root)
        self.pprice = tk.Entry(self.root)
        self.pqty = tk.Entry(self.root)

        self.pname.grid(row=3, column=1)
        self.pprice.grid(row=4, column=1)
        self.pqty.grid(row=5, column=1)

        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=6, column=1)
        tk.Button(self.root, text="Generate Bill", command=self.generate_bill).grid(row=7, column=1)

    def add_product(self):
        try:
            name = self.pname.get()
            price = float(self.pprice.get())
            qty = int(self.pqty.get())

            if not name:
                raise ValueError("Product name cannot be empty.")

            product = Product(0, name, price, qty)
            self.products.append(product)
            messagebox.showinfo("Success", "Product Added.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_bill(self):
        try:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            balance = float(self.balance_entry.get())

            if not name or not phone:
                raise ValueError("Customer info incomplete.")

            customer = Customer(name, phone, balance)
            status = self.system.save_transaction(customer, self.products)

            if status:
                filename = self.system.generate_bill_file(customer, self.products)
                messagebox.showinfo("Success", f"Bill generated: {filename}")
            else:
                messagebox.showerror("Error", "Failed to save bill.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

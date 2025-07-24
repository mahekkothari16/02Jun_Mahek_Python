from db_connection import DBConnection
from models import Product, Customer
from datetime import datetime

class BillingSystem:
    def __init__(self):
        self.db = DBConnection()
        self.conn, self.cursor = self.db.get_connection()

    def save_transaction(self, customer: Customer, products: list):
        try:
            self.cursor.execute("INSERT INTO customers (name, phone, balance) VALUES (%s, %s, %s)", 
                                (customer.name, customer.phone, customer.get_balance()))
            customer_id = self.cursor.lastrowid
            for product in products:
                self.cursor.execute("INSERT INTO bills (cust_id, product_name, price, qty, total) VALUES (%s, %s, %s, %s, %s)",
                                    (customer_id, product.name, product.price, product.qty, product.get_total()))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error saving transaction:", e)
            return False

    def generate_bill_file(self, customer: Customer, products: list):
        filename = f"Bill_{customer.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(f"Customer: {customer.name}\nPhone: {customer.phone}\n\n")
            total = 0
            for p in products:
                line = f"{p.name} - {p.qty} x {p.price} = {p.get_total()}\n"
                file.write(line)
                total += p.get_total()
            file.write(f"\nTotal Amount: ₹{total}")
        return filename

import database as db
import random

def list_stocks():
    for sid, details in db.stocks.items():
        print(f"{sid} => {details}")

def update_price():
    sid = input("Enter Stock ID: ")
    if sid in db.stocks:
        change_percent = random.uniform(1, 5)
        direction = input("Increase or Decrease? (i/d): ").lower()
        amount = db.stocks[sid]["amount"]
        change = amount * (change_percent / 100)

        if direction == "i":
            new_amount = amount + change
        else:
            new_amount = amount - change

        db.stocks[sid]["amount"] = round(new_amount, 2)
        print(f"Price updated to {db.stocks[sid]['amount']} (+/- {change_percent:.2f}%)")

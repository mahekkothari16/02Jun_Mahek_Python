import database as db

def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Password: ")
    return db.admins.get(username) == password

def add_stock():
    stock_id = input("Stock ID: ")
    name = input("Stock Name: ")
    desc = input("Description: ")
    qty = int(input("Quantity: "))
    amount = float(input("Amount: "))
    date = input("Date of Issue (DD-MM-YYYY): ")

    db.stocks[stock_id] = {
        "name": name,
        "desc": desc,
        "qty": qty,
        "amount": amount,
        "date": date
    }
    db.stock_history.append(db.stocks[stock_id])
    print("Stock added successfully.")

def manage_stocks():
    print("Current Stocks:")
    for sid, details in db.stocks.items():
        print(f"{sid} => {details}")
    action = input("Choose action: edit/delete/view: ").lower()
    sid = input("Enter Stock ID: ")
    
    if action == "delete":
        db.stocks.pop(sid, None)
        print("Deleted.")
    elif action == "edit":
        new_amt = float(input("New Amount: "))
        db.stocks[sid]['amount'] = new_amt
        print("Updated.")
    elif action == "view":
        print(db.stocks.get(sid, "Not found"))

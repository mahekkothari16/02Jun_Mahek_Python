import database as db

def register_user():
    username = input("Choose Username: ")
    password = input("Password: ")
    db.users[username] = password
    db.user_stocks[username] = []
    print("Registered successfully.")

def user_login():
    username = input("Username: ")
    password = input("Password: ")
    if db.users.get(username) == password:
        return username
    return None

def view_live_stocks():
    for sid, stock in db.stocks.items():
        print(f"{sid}: {stock}")

def buy_stock(username):
    view_live_stocks()
    sid = input("Enter Stock ID to Buy: ")
    if sid in db.stocks:
        stock = db.stocks[sid]
        quantity = int(input("Quantity to Buy: "))
        total = quantity * stock['amount']
        db.user_stocks[username].append({
            "id": sid,
            "name": stock["name"],
            "qty": quantity,
            "buy_price": stock['amount']
        })
        print(f"Bought {quantity} of {stock['name']} at total cost {total}")

def manage_user_stocks(username):
    print("Your Stocks:")
    for item in db.user_stocks[username]:
        current_price = db.stocks[item["id"]]["amount"]
        profit_loss = (current_price - item["buy_price"]) * item["qty"]
        print(f"{item['id']}: Bought @ {item['buy_price']} | Now @ {current_price} | P/L: {profit_loss}")

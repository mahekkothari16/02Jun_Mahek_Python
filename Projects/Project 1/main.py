import admin, user, stock_updater

def main():
    while True:
        print("\n1. Admin\n2. User\n3. Stock Updater\n4. Exit")
        choice = input("Enter role: ")

        if choice == '1':
            if admin.admin_login():
                while True:
                    print("\nAdmin Menu:\n1. Add Stock\n2. Manage Stocks\n3. Logout")
                    opt = input("Choose: ")
                    if opt == '1': admin.add_stock()
                    elif opt == '2': admin.manage_stocks()
                    else: break
        elif choice == '2':
            print("1. Register\n2. Login")
            opt = input("Choose: ")
            if opt == '1':
                user.register_user()
            else:
                uname = user.user_login()
                if uname:
                    while True:
                        print("\nUser Menu:\n1. View Live Stock\n2. Buy Stock\n3. My Stocks\n4. Logout")
                        uopt = input("Choose: ")
                        if uopt == '1': user.view_live_stocks()
                        elif uopt == '2': user.buy_stock(uname)
                        elif uopt == '3': user.manage_user_stocks(uname)
                        else: break
        elif choice == '3':
            while True:
                print("\nStock Updater Menu:\n1. View Stocks\n2. Update Price\n3. Logout")
                opt = input("Choose: ")
                if opt == '1': stock_updater.list_stocks()
                elif opt == '2': stock_updater.update_price()
                else: break
        else:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

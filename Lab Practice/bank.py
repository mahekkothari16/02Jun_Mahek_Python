#Bank Management System - 1)Account Opening:a/c number,a/c holder name,a/c type
                        # 2) Deposit:-Min withdrawal amount 2000
                        # 3) Withdrawal : id withdrawal money is less than balance error
                        # 4) Statement : a/c Number,a/c holder name, a/c type, balance -print it

'''num = int(input("Enter your account number: "))
name = input("Enter your name: ")
type = input("Enter the type of account you have(savings account,personal account):").lower()
balance = 0
def opening():
    global balance
    print(f"Your Balance is:{balance}")
    if type == 'savings account' or type=='personal account':
        print(f"Account Number:{num}")
        print(f"Account Holder Name:{name}")
        print(f"Account Type:{type}")
    else:
        print("Enter valid account")

def deposit():
    dep = int(input("Enter the amount that you want to deposit: "))
    if dep < 2000:
        print("The amount should be greater than 2000.")
    else:
        global balance
        balance = balance + dep
        print(f"Your current balance:{balance}")


def withdrawal():
    global balance
    wd = int(input("Enter the amount you want to withdraw: "))    
    if wd <= balance:
        print("Done withdrawal of:",wd)
        balance = balance - wd
        print("Current Balance: ",balance)
    else:
        print("Amount should be not greater than balance")
        

def statement():
    global balance
    opening()
    

while True:
    print("Banking Program:")
    print("1.Open a new account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Statement")
    print("5.Exit")

    choice = int(input("Enter the choice (1-5): "))
    if choice == 1:
        opening()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdrawal()
    elif choice == 4:
        statement()
    elif choice == 5:
        break
    else:
        print("Enter Valid choice")
print("Thank You! Have a nice day.")
'''


#Bank Management System - 1)Account Opening:a/c number,a/c holder name,a/c type
                        # 2) Deposit:-Min withdrawal amount 2000
                        # 3) Withdrawal : id withdrawal money is less than balance error
                        # 4) Statement : a/c Number,a/c holder name, a/c type, balance -print it


class account_opening:
    acc_num=int
    acc_holder_name=str
    acc_type=str
    balance = 0

    def getdata(self):
        self.acc_num=int(input("Enter your account number: "))
        self.acc_holder_name=input("Enter the name of Account holder: ")
        self.acc_type=input("Enter the type of account you want to open(savings account,personal account): ").lower()
        if self.acc_type == 'savings account' or type == 'personal account':
            print(f"Account Number:{self.acc_num}")
            print(f"Account Holder Name:{self.acc_holder_name}")
            print(f"Account Type:{self.acc_type}")
        else:
            print("Enter valid account")

class deposit(account_opening):
    dp_amt=int
    def dp_getdata(self):
        global balance
        self.dp_amt=int(input("Enter the amount you want to deposit: "))
        if self.dp_amt < 2000:
            print("The amount should be greater than 2000.")
        else:
            self.balance = self.balance + self.dp_amt
            print(f"Your current balance:{self.balance}")

class withdrawal(deposit):
    wd_amt=int

    def wd_getdata(self):
        self.wd_amt = int(input("Enter the amount you want to withdraw: "))
        if self.wd_amt <= self.balance:
            print("Done withdrawal of:",self.wd_amt)
            self.balance = self.balance - self.wd_amt
            print("Current Balance: ",self.balance)
        else:
            print("Amount should be not greater than balance")

class statement(withdrawal):
    def st(self):
        print(f"Account Number:{self.acc_num}")
        print(f"Account Holder Name:{self.acc_holder_name}")
        print(f"Account Type:{self.acc_type}")
        print("Current Balance: ",self.balance)        

fc = statement()

while True:
    print("=================Banking Program===================")
    print("     1.Open a new account")
    print("     2.Deposit")
    print("     3.Withdraw")
    print("     4.Statement")
    print("     5.Exit")

    choice = int(input("Enter the choice (1-5): "))
    if choice == 1:
        fc.getdata()
    elif choice == 2:
        fc.dp_getdata()
    elif choice == 3:
        fc.wd_getdata()
    elif choice == 4:
        fc.st()
    elif choice == 5:
        break
    else:
        print("Enter Valid choice")
print("Thank You! Have a nice day.")




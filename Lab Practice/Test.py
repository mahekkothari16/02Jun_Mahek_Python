#WAP to generate a bill for fastfood
#Enter customer name,QTY,Price,GST,Net total

'''user_name = input("Enter your name: ")
food_list=['pani puri','pav bhaji','punjabi']
print(food_list)
user=input("Enter the food you want to buy from the above list: ").lower()
qty=int(input("Enter the quantity you want: "))
if user=='pani puri':
    price=40
    total=price*qty
    GST=(total*3)/100
    print(user_name,": Buyed",user)
    print(f"Your Bill:","Quantity:",{qty} ,"Price:",{price},"Total:",{total},"GST",{GST},"Net total:",{total+GST})
elif user=='pav bhaji':
    price=100
    total=price*qty
    GST=(total*3)/100
    print(user_name,": Buyed",user)
    print(f"Your Bill:","Quantity:",{qty} ,"Price:",{price},"Total:",{total},"GST",{GST},"Net total:",{total+GST})
elif user=='punjabi':
    price=300
    total=price*qty
    GST=(total*3)/100
    print(user_name,": Buyed",user)
    print(f"Your Bill:","Quantity:",{qty} ,"Price:",{price},"Total:",{total},"GST",{GST},"Net total:",{total+GST})
else:
    print("You might choose from the list itself")
'''

#Make a calculator and ask the user if he/she wants to continue next
options = ["1:Addition","2:Subtraction","3:Multiplication","4:Division"]
print(options)
while True:
    ask = input("Do you want to continue for calculation: ").lower()
    if ask=='yes':
        choice = int(input("Enter the number of the choice you want from above: "))
        a = int(input("Enter the first number: "))
        b = int(input("Enter the seocnd number: "))
        if choice==1:
            print("Addition of",a,"and",b,"is:",a+b)
        elif choice==2:
            print("Subtraction of",a,"and",b,"is:",a-b)
        elif choice==3:
            print("Multiplication of",a,"and",b,"is: ",a*b)
        elif choice==4:
            print("Division of",a,"and",b,"is:",a/b)
        else:
            print("Enter choice from the above list")
    else:
        break







# Program 6 : Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

while True: 
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter Second number: '))
        list = ['+','-','*','/']
        print(list)
        ask = input("What you want to do from above list? ").lower()
        if ask == '+':
            print(f"Addition is {num1+num2}")
        elif ask == '-':
            print(f"Subtraction is: {num1-num2}")
        elif ask == '*':
            print(f"Multiplication is: {num1*num2}")
        elif ask == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            print(f"Division is: {num1/num2}")
        else:
            print("Enter correct option from the list!")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

        
    
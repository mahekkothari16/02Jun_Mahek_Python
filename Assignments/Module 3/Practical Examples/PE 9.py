# Example 9 : Write a Python program to handle file exceptions and use the finally block for closing the file. 
try:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Sum:",a+b)

except:
    print("Error")

finally:
    print("This is finally block")
# Example 6: Write a Python program to insert elements into an empty list using a for loop and append(). 
list = []
n = int(input("Enter the number of elements you want to enter: "))
for i in range(n):
    user = input("Enter the element: ")
    list.append(user)

print(list)
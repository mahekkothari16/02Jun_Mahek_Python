# Example 2 :  Write a Python program to read a string, an integer, and a float from the keyboard and display them.
user_string = input("Enter a string: ")

# Read an integer from the keyboard
# The input() function returns a string, so it needs to be converted to an integer using int()
user_integer = int(input("Enter an integer: "))

# Read a float from the keyboard
# The input() function returns a string, so it needs to be converted to a float using float()
user_float = float(input("Enter a float: "))

# Display the read values
print("\nYou entered:")
print(f"String: {user_string}")
print(f"Integer: {user_integer}")
print(f"Float: {user_float}") 

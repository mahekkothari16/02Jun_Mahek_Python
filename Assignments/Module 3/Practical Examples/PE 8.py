#Example 8 : Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
try:
    num_str = int(input("Enter a number: "))
    result = 10 / num_str  
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
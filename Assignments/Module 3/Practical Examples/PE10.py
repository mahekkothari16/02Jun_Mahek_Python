# Example 10 : Write a Python program to print custom exceptions.
class CustomError(Exception):
    """A custom exception for demonstration purposes."""
    def __init__(self, message="This is a custom error!"):
        self.message = message
        super().__init__(self.message)

def check_value(value):
    if value < 0:
        raise CustomError ("Value cannot be negative.")
    elif value == 0:
        raise CustomError("Value cannot be zero.")
    else:
        print(f"Value is: {value}") 

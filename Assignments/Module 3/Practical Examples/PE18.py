# Example 18 :  Write a Python program to demonstrate the use of super() in inheritance.
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent {self.name} initialized.")

    def greet(self):
        print(f"Hello from Parent, my name is {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        # Call the parent's __init__ method using super()
        super().__init__(name) 
        self.age = age
        print(f"Child {self.name} (age {self.age}) initialized.")

    def greet(self):
        # Call the parent's greet method using super()
        super().greet()
        print(f"Hello from Child, I am {self.age} years old.")

# Create an instance of the Child class
child_instance = Child("Alice", 10)

# Call the greet method on the child instance
child_instance.greet()
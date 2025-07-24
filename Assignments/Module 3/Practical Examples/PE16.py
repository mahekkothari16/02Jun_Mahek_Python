# Example 16 :  Write a Python program to show hierarchical inheritance.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class's __init__
        self.color = color

    def speak(self):
        return f"{self.name} the {self.color} cat says Meow!"

# Create instances of the derived classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

# Call methods and demonstrate inheritance
print(dog.speak())
print(cat.speak())

# Demonstrate access to inherited attributes
print(f"Dog's name: {dog.name}")
print(f"Cat's name: {cat.name}")

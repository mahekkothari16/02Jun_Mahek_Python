# Example 17 : Write a Python program to show hybrid inheritance.
# Base Class 1 (Single Inheritance)
class Animal:
    def speak(self):
        print("Animal makes a sound.")

# Base Class 2 (Single Inheritance)
class Swimmer:
    def swim(self):
        print("Can swim in water.")

# Intermediate Class (Multilevel Inheritance from Animal)
class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives live birth.")

# Derived Class (Hybrid: inherits from Mammal and Swimmer)
class Dolphin(Mammal, Swimmer):
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is a Dolphin.")

    def display_info(self):
        print(f"Name: {self.name}")

# Create an object of the derived class
flipper = Dolphin("Flipper")

# Call methods from different parent classes
flipper.display_info()
flipper.speak()        # From Animal via Mammal
flipper.give_birth()   # From Mammal
flipper.swim()         # From Swimmer
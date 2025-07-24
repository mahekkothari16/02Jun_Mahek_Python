# Program 10 : Write Python programs to demonstrate method overloading and method overriding. 
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage
animal = Animal()
dog = Dog()
cat = Cat()

print(f"Animal sound: {animal.make_sound()}")
print(f"Dog sound: {dog.make_sound()}")
print(f"Cat sound: {cat.make_sound()}")

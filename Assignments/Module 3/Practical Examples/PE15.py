# Example 15 : Write a Python program to show multiple inheritance.
class Grandfather:
    def property():
        print("This is grandfathers property!")
    
class Father:
    def father_property():
        print("This is Fathers Property")
    
class Son(Grandfather,Father):
    print("This includes both Father and Grandfathers Property")

x = Son
x.father_property()
x.property()
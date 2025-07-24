# Example 13 :  Write a Python program to show single inheritance.
class Grandfather:
    def property():
        print("This is Grandfathers Property")
    
class Father(Grandfather):
    print("This is Fathers Property too!")

x = Father
x.property()
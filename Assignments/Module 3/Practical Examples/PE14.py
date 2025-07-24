# Example 14 :  Write a Python program to show multilevel inheritance. 
class Grandfather:
    def property():
        print("This is grandfathers property!")
    
class Father(Grandfather):
    def father_property():
        print("This is Fathers Property")
    
class Son(Father):
    print("This includes both Father and Grandfathers Property")

x = Son
x.father_property()
x.property()
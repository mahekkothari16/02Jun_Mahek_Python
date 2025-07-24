# Program 9 : Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.). 
# Single Inheritance
class Grandfather:
    def property():
        print("This is Grandfathers Property")
    
class Father(Grandfather):
    print("This is Fathers Property too!")

x = Father
x.property()

#Multiple Inheritance
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

#Multilevel Inheritance
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
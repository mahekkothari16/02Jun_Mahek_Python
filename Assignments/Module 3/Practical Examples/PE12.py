#Example 12 : Write a Python program to demonstrate the use of local and global variables in a class.
class production():
    a = 20
    def items():
        a = 51
        b = 12
        print("Addition:",a+b)
x = production
x.items()
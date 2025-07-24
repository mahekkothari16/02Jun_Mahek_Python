# Example 20 :  Write a Python program to show method overriding. 
#Method Overriding
class studinfo:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)


class home(studinfo):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)

class about(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)

# Example 19 : Write a Python program to show method overloading. 
class studinfo:
    #Method Overloading
    def getdata(self,id):
        print("ID:",id)
    
    def getdata(self,name):
        print("Name:",name)

st=studinfo()
st.getdata(101)
st.getdata("Mahek")
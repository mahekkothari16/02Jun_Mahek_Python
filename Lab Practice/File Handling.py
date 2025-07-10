'''open("temp.txt","w")
print("File is created")


x = open("temp.txt","w")
x.write("Hello Students")'''

'''user = int(input("Enter the number of students of which you want to enter data: "))
for i in range(user):
    x = open("user.txt","a")
    id = int(input("Enter the id: "))
    name = input("Enter the name: ")
    city = input("Enter the city: ")
    x.write(f"\nID:{id}\nName:{name}\nCity:{city}\n")'''

'''x = open("user.txt","r")
print(x.read())
print(x.readline())
print(x.readlines()[3])'''

'''x = open("user.txt","a")
x.write("\nHello Traitors\n")'''

#Number Of Students:
#Created at - date-time
#ID - Random
#Name - 
#City - 
#------------------------------

'''import datetime

user = int(input("Enter the number of students of which you want to enter data: "))
for i in range(user):
    x = open("user.txt","a")
    x1 = datetime.datetime.now()
    x.write(f"\nCreated at:{x1}")
    id = int(input("Enter the id: "))
    name = input("Enter the name: ")
    city = input("Enter the city: ")
    x.write(f"\nID:{id}\nName:{name}\nCity:{city}\n")
    x.write("-------------------------------")'''

#Food Billing system by file handling 
'''
import datetime
x = open("foodbill.txt","a")
order = input("Do you want to order anything: ").lower()

def food_bill():
    name = input("Enter your name: ")
    mobile = int(input("Enter your mobile number: "))
    qty = int(input("Enter the quantity you want: "))
    x.write(f"\nName:{name}")
    x.write(f"\nMobile:{mobile}")
    x1 = datetime.datetime.now()
    x.write(f"\nDate:{x1}")
    x.write("\n----------------------------")
    x.write(f"\nFood name:Pani Puri")
    x.write(f"\nQTY:{qty}")
    x.write(f"\nPrice:{price}")
    x.write("\n----------------------------")
    total = price*qty
    x.write(f"\nTotal:{total}")
    GST = total*(18/100)
    x.write(f"\nGST:{GST}")
    x.write("\n----------------------------")
    grand_total = total+GST
    x.write(f"\nGrand Total:{grand_total}\n")
    x.write("==============================\n")

while True:
    if order == 'yes':
        list = ["1: Pani Puri","2: Punjabi","3: Pav Bhaji"]
        print(list)
        ask = int(input("Enter the number of item you want to order from the above list (Enter 4 for exit): "))
        if ask == 1:
            price = 20
            food_bill()
        elif ask == 2:
            price = 200
            food_bill()
        elif ask == 3:
            price = 70
            food_bill()
        elif ask == 4:
            print("Thank you")
            break
        else:
            print("Enter Valid Number")
    else:
        break
'''
    

'''import os
os.chdir('Newfolder') #create a new folder
#for making subfolder
os.mkdir("Subfolder")

#for 
os.chdir("Newfolder/Subfolder")
os.mkdir("myfolder")

#for new file
os.chdir("Newfolder/Subfolder/myfolder")
open("test.txt","x")

#for deleting folder
os.remove("new.txt")
# for removing subfolder
os.chdir("Newfolder/Subfolder/myfolder")
os.remove("test.txt")
#removing folder
os.chdir("Newfolder/Subfolder")
os.removedirs("myfolder")
'''


'''try:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
finally:
    print("This is finally block!")
    if a<b:
        print("Mul:",a*b)'''

#If there is sum there multiplication will happend
'''try:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
else:
    print("Mul:",a*b)'''


#Task : User Registration form with validation
'''Name :capital
email: small
mobile : digit and must be 10 digit
password : cap+small+digit
confirm password : same 
--------------------------
pass and confirm password both are same '''

'''
def mob():
    x = open("Mob.txt","a")
    name = input("Enter your name (In capital): ").upper()
    email = input("Enter your email (In lowercase): ").lower()
    while True:
        mobile = input("Enter your mobile number (Only 10 Digits): ")
        if not mobile.isdigit() or len(mobile)!= 10 :
            print("Mobile Number must be exact 10 digits")
        else:
            break
    password = input("Enter your password (Should Include atleast one capital letter,one small and digits): ")
    if not password.isupper() and password.islower() and password.isdigit():
        print("Password must contain atleast one capital letter, one small letter and digit")
    confirm_password = input("Confirm your password (Same password as you entered above): ")
    while True:
        if confirm_password != password:
            password = input("Enter your password (Should Include atleast one capital letter,one small and digits): ")
            if not password.isupper() and password.islower() and password.isdigit():
                print("Password must contain atleast one capital letter, one small letter and digit")
            confirm_password = input("Confirm your password (Same password as you entered above): ")
        else:
            break
    x.write(f"Name: {name}\n")
    x.write(f"Email: {email}\n")
    x.write(f"Mobile Number: {mobile}\n")
    x.write(f"Password: {password}\n")
    x.write(f"Confirm Password: {confirm_password}\n")
    x.write("-----------------------------------------------------------\n")
    x.write(f"Password:{password} Confirm Password:{confirm_password}\n")
    x.write("===========================================================\n")

ask = input("Do You want to enter and go ahead(yes/no): ").lower()
if ask == 'yes':
    try:
        mob()
    except Exception as e:
        print(e)
'''

#OOPs: 
'''1)class
2)object
3)inheritance
    -single
    -multiple
    -multilevel
4)polymorphism
    -method overloading
    -method overriding
5)encapsulation / data binding
6)access specifire/modifire/data hiding
    -public
    -private
'''


#Class
'''class student():
    stid=12
    stnm="Mahek"

    def getdata(self):
        print("This is student class")
    
    def getsum(self,a,b): #Here first argument will always be default
        print("Sum: ",a+b)

st=student() #object of class

print("ID: ",st.stid)
print("Name: ",st.stnm)
st.getdata()
st.getsum(23,45)'''

'''class student:
    stid = 12
    stnm = "Mahek"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)
    
st=student()
st.getdata()'''

'''class student:
    ask = input("Enter the Name:")
    def getdata(self):
        print("Mahek: ",self.ask)
st=student()
st.getdata()'''


'''
class student:
    stid:int
    stnm:str

    def getdata(self):
        self.stid = input("Enter a id: ")
        self.stnm = input("Enter a name: ")

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

st=student()
st.getdata()
st.printdata()
'''


##Inheritance
'''class father:
    bal:int
    car:int

    def getdata(self):
        self.bal=input("Enter a bank balance details: ")
        self.car=input("Enter a car details: ")

class son(father):
    def printdata(self):
        print("Car:",self.car)

sn=son()
sn.getdata()'''

#Multiple Inheritance
'''class grandfather:
    def gf(self):
        pass

class father:
    bal:int
    car:int

    def getdata(self):
        self.bal=input("Enter a bank balance details: ")
        self.car=input("Enter a car details: ")

class son(grandfather,father): #THIS IS MULTIPLE INHERITANCE
    def printdata(self):
        print("Car:",self.car)

sn=son()
sn.getdata()
sn.gf()'''





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


#Polymorphism - One name multiple form(method overriding:same method name same argument but diff class
#method overloading : same method diff argument)
#Method overloading --------- Python do not support this
'''class students:
    def getdata(self,id):
        print("ID:",id)
    def getdata(self,name):
        print("Name:",name)
st=students()

#Method overriding
class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class home(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)'''

#------------INIT----------
'''import random
class studentinfo:
    def __init__(self,acno):
        print("A/c NO:",acno)

n=random.randint(11111,99999)
st=studentinfo(n)'''
#This is where init is majorly used
'''import requests
class home:
    def __init__(self):
        try:
            url="https://www.google.co.in/"
            response=requests.get(url)
            print("Internet connection is ON!")
        except:
            print("There is no internet connection")

hm = home()'''


#PUBLIC-PRIVATE
'''class studinfo:
    #PUBLIC
    stid=12
    stnm="Mahek"
    #private
    __stid=14
    __stnm = "Mahek"

    def __getdata(self):
        print("This is getdata")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()
st=studinfo()
st.printdata()
'''

#Static Method
'''class studinfo:
    @staticmethod #For not writinf self and we cannot change it
    def sum(a,b):
        print("Sum is:",a+b)
f = studinfo()
f.sum()'''
#From instance we cannot change the value and with object we can





'''studt = {}

class student_detail:

    def load_students():
        try:
            with open("Student.txt", "r") as f:
                data = f.read()
                if data:
                    return eval(data)  # Convert string back to dictionary
        except FileNotFoundError:
            pass
        return {}
    
    def save_students(students):
        with open("student_data.txt", "w") as f:
            f.write(str(students))
            f.write("==========================================\n")



    def add_student(self,students):
        stud = open("Student.txt","a")
        no = int
        fn=str
        ln=str
        cn=int
        self.no=input("Enter serial number: ")
        while True:
            self.fn = input("Enter First Name: ").upper()
            self.ln = input("Enter Last Name: ").upper()
            if not self.fn.isalpha() and not self.ln.isalpha():
                print("Name should contain only letters.")
            else:
                break
        while True:
            self.cn = input("Enter contact number: ")
            if len(self.cn) != 10 : 
                print("Number should consider only digits and it should only be 10. ")
            else:
                break
        self.ask = int(input("How many Entry you want to make for subjects and marks? "))
        for i in range(self.ask):
            self.sub = input("Enter Subject: ")
            self.marks = int(input("Enter Marks: "))
            self.fee = int(input("Enter Fees: "))
        studt[no]={
            "First Name":self.fn,
            "Last Name":self.ln,
            "Contact Number":self.cn,
            "Subject":{},
            "Marks":{},
            "Fee":{}        
        }
        sd.save_students(students)
        

    def remove_student():
        pass

    def view_all_stud():
        pass

    def view_specific_student():
        pass

sd = student_detail()

while True:
    #MENU
    students = sd.load_students()
    print("      Press 1 for Counsellor\n"
          "      Press 2 for Faculty\n"
          "      Press 3 for Student\n")

    role_id = int(input("Enter the role ID: "))

    if role_id == 1:
        print("      1. Add Student\n"
            "      2. Remove Student\n"
            "      3. View All Student\n"
            "      4. View Specific Student\n")
        choice = int(input("Enter a choice by counsellor: "))
        if choice == 1:
            sd.add_student()
        elif choice == 2:
            sd.remove_student()
        elif choice == 3:
            sd.view_all_stud()
        elif choice == 4:
            sd.view_specific_student()
        else:
            print("Enter right choice.")

    elif role_id == 2:
        print("      1.Add Marks to Student\n"
              "      2.View All Student\n")
        fc = int(input("Enter a choice by faculty: "))
        if fc == 1:
            sd.add_student()
        elif fc == 2:
            sd.view_all_stud()
        else:
            print("Enter Valid Choice!")'''


#Regular Expression
'''import re
mystr = input("Enter what you want to find: ").lower()
x = re.search('python',mystr)
print(x)

if x:
    print("Match Found")
else:
    print("Error")'''


#Match Function - Works only for beginning word before the space
'''import re
mystr = input("Enter what you want to find: ").lower()
x = re.match('python',mystr)
print(x)

if x:
    print("Match Found")
else:
    print("Error")'''



#Findall
'''import re
mystr = input("Enter what you want to find: ").lower()
x = re.findall('python',mystr)
print(x)

if x:
    print("Match Found")
else:
    print("Error")
'''

#Ignorecase 
'''import re
mystr = input('Enter the sentence: ')
#x = re.findall('[A-Za-z]',mystr)
#x = re.findall('[0-9]',mystr)
x = re.findall('[A-Za-z0-9]',mystr)
x = re.findall('[A-Za-z0-9@.]',mystr)
print(x)

'''


#DOTALL
'''import re
mystr = input('Enter the sentence: ')
x = re.findall("Py..on",mystr)
print(x)'''



#XVERBOSE
'''import re
mystr = input('Enter the sentence: ')
x = re.findall('[this|that]',mystr)
print(x)'''


#MULTILINE
'''import re
mystr = "This is Python"
#Beginning Restriction
x = re.findall("^This",mystr)
x = re.findall("[A-Z]",mystr)
#Ending Restriction
x = re.findall("on$",mystr)
print(x)'''


#ASCII (\w, \W, \b, \B, \s, \S, \d, \D)
'''
import re
mystr = "This is Python!"
x = re.findall('\w',mystr)
x = re.findall('\W',mystr)
x = re.findall('\s',mystr)
x = re.findall('\S',mystr)
x = re.findall('\d',mystr)
print(x)
'''


#Username Pattern
'''import re
username = "Mahek1313"
#usenm_pattern = "[A-Za-z0-0]" Inside bracket it is counted optional
usenm_pattern = "[A-Z]+[a-z]+[0-9]"
x = re.findall(usenm_pattern,username)
if x:
    print("Username is Valid")
else:
    print("Error,Invalid Username")'''



'''import re
username = input("Enter the Email: ")
usenm_pattern = "[[^a-z]+[0-9]+[@]+[gmail,outlook,yahoo]+[.]+[com,in$]"
x = re.findall(usenm_pattern,username)
if x:
    print("Username is Valid")
else:
    print("Error,Invalid Username")'''



### TKINTER
'''import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("MyApp")
window.geometry("400x500")
window.config(bg='lightpink')
tkinter.Label(text="Firstname:").place(x=0,y=0) #Pack we can use upon place
tkinter.Label(text="Firstname:").place(x=0,y=30)
tkinter.Label(text="Firstname:",bg='lightblue',fg='brown',font='Elephant 15').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='lightblue',fg='brown',font='Elephant 15').grid(row=1,column=0,sticky='w')
txt1 = tkinter.Entry()
txt1.grid(row=0,column=1)
txt2 = tkinter.Entry()
txt2.grid(row=1,column=1)
tkinter.Radiobutton(value=0,text="Male").grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female").grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati").grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi").grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English").grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Morbi','Surat','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0)

def btnclick():
    print("Button Clicked")
    print("Firstname:",txt1.get())
    print("Secondname:",txt2.get())

tkinter.Button(text="Submit",font='Elephant 15',command=btnclick).place(x=150,y=270)

window.mainloop()
'''

'''
import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("MyApp")
window.geometry("400x500")
window.config(bg='lightpink')

tkinter.Label(text="First Number:",fg='brown',font='Elephant 15').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Second Number:",fg='brown',font='Elephant 15').grid(row=1,column=0,sticky='w')

txt1 = tkinter.Entry()
txt1.grid(row=0,column=1)
txt2 = tkinter.Entry()
txt2.grid(row=1,column=1)


def add():
    q1 = int(txt1.get())
    q2 = int(txt2.get())
    print("Addition:",q1+q2)

def sub():
    pass

def mult():
    pass

def div():
    pass

clk1 = tkinter.Button(text="Addition",fg='brown',font='Elephant 8',command=add).grid(row=2,column=0,sticky='w')
clk2 = tkinter.Button(text="Subtraction",fg='brown',font='Elephant 8',command=sub).grid(row=3,column=0,sticky='w')
clk3 = tkinter.Button(text="Multiplication",fg='brown',font='Elephant 8',command=mult).grid(row=4,column=0,sticky='w')
clk4 =tkinter.Button(text="Division",fg='brown',font='Elephant 8',command=div).grid(row=5,column=0,sticky='w')


window.mainloop()
'''

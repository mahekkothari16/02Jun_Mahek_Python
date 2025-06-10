'''
#input basic info
print("Input your Details:")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
address = input("Enter your address: ")
print("The details are: ",name,age,gender,address)


#Make your calc
a = int(input("Enter the 1st number: "))
b = int(input("Enter the second number: "))
print("Addition is: ",a+b)
print("Substraction is: ",a-b)
print("Multiplication is: ",a*b)
print("Division is: ",a/b)


#print("My id is {} and my name is {}".format(id,name))
#print(f"My id is {id} and name is {name}")
'''

'''
#Find the maximum out of three
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
    print("A is maximum")
elif b>a and b>c:
    print("B is maximum")
else:
    print("C is maximum")
'''

#Result
'''
s1 = int(input("Enter Subject1 Mark: "))
s2 = int(input("Enter Subject2 Marks: "))
s3 = int(input("Enter Subject3 Marks: "))
s4 = int(input("Enter Subject4 Marks: "))

if s1>= 40 and s2>=40 and s3>=40 and s4>=40:

    total = s1+s2+s3+s4
    print("Total is:",total)

    pr = total/4
    print("Percentage is:",pr)

    if pr>=70:
        print("The Student is passed by Distinction")
    elif pr>=60:
        print("The student is passes by First Class")
    elif pr>=50:
        print("The student is passed by Second Class")
    elif pr>=40:
        print("The student is passed by Pass Class")
else:
    print("The student is FAIL")
'''


#Input 2 number from user: Neither the number should be zero and if no1>no2 then multiply them otherwise subtraction
#else:Invalid number
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a!=0 and b!=0:
    if a>b:
        c = a*b
        print(c)
    elif b>a:
        d = a-b
        print(d)

else:
    print("Invalid Number")
'''

#take choice from user and make a calculator: 1 for add , 2 for sub, 3 for multi, 4 for div
'''
a = ['1:Addition','2:Subtraction','3:Multiplication','4:Division']
print(a)
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
user_input = int(input("Enter the number of the choice you want to do: "))
if user_input == 1:
    print("Add:",a+b)
elif user_input == 2:
    print("Sub:",a-b)
elif user_input == 3:
    print("Multi:",a*b)
elif user_input == 4:
    print("Div:",a/b)
else:
    print("Invalid Number")
'''

#WHILE LOOP
'''i=1

while i<=10:
    print(i)
    i+=1'''

#WHILE : Print odd and even numbers
'''i=1
while i<=10:
    print(i)
    i+=2'''

'''i=2
while i<=10:
    print(i)
    i+=2'''


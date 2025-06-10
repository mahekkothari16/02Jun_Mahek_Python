#Program 11:Write a Python program to calculate grades based on percentage using if-else ladder.
s1 = int(input("Enter Subject1 Mark: "))
s2 = int(input("Enter Subject2 Marks: "))
s3 = int(input("Enter Subject3 Marks: "))
s4 = int(input("Enter Subject4 Marks: "))

if s1>= 40 and s2>=40 and s3>=40 and s4>=40:

    total = s1+s2+s3+s4
    print("Total is:",total)

    pr = total/4
    print("Percentage is:",pr)

    if pr>=90:
        print("Grade:A+")
    elif pr>=80:
        print("Grade:A")
    elif pr>=70:
        print("Grade:B+")
    elif pr>=60:
        print("Grade:B")
    elif pr>=50:
        print("Grade:C")
    elif pr>=40:
        print("Grade:D")
else:
    print("The student is FAIL")

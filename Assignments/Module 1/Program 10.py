#Write a Python program to check if a number is prime using if_else
i=2
no = int(input("Enter the number: "))
while i<=no:
    i+=1

    if no%i==0:
        print("Number is Not Prime")
        break
    else:
        print("Number is Prime")
        break
    
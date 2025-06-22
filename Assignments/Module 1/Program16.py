#Program 16:  Print this pattern using nested for loop: 
'''markdown 
Copy code 
* 
** 
*** 
**** 
*****'''

num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print("* ",end="")
    print("")


        
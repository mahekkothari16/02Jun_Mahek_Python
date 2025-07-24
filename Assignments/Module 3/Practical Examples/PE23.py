# Example 23 :  Write a Python program to search for a word in a string using re.search(). 
import re

mystr="That is Python!"

x=re.search('This',mystr)
print(x)

if x:
    print("Match Found...")
else:
    print("Error!")
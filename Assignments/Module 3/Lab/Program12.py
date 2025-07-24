# Program 11 : Write a Python program to search for a word in a string using re.search().
import re
str = "Hello, I am Mahek"
x = re.search('i',str)
if x:
    print("yes")
else:
    print("no")
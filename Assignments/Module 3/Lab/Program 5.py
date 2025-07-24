# Program 5 : Write a Python program to write multiple strings into a file. 
file_write = [
    "This is first line\n",
    "This is second line\n",
    "This is third line\n"
]
with open("file.txt",'w') as file:
    file.writelines(file_write)


# Example 3 :  Write a Python program to create a file and write a string into it.
file_write = [
    "This is first line\n"
]
with open("file.txt",'w') as file:
    file.write(file_write)
